#!/usr/bin/env python3
"""Download Paul Graham essays from paulgraham.com.

The script reads the public essay index, discovers essay pages, and writes a
manifest plus one file per essay. It uses only the Python standard library.
"""

from __future__ import annotations

import argparse
import json
import re
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen


BASE_URL = "https://paulgraham.com/"
INDEX_URL = urljoin(BASE_URL, "articles.html")
USER_AGENT = "pg-essay-puller/1.0"

NON_ESSAY_PAGES = {
    "antispam.html",
    "arc.html",
    "articles.html",
    "bel.html",
    "bio.html",
    "books.html",
    "faq.html",
    "index.html",
    "kedrosky.html",
    "lisp.html",
    "quo.html",
    "raq.html",
    "rss.html",
}


@dataclass(frozen=True)
class EssayLink:
    title: str
    url: str
    href: str


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[EssayLink] = []
        self._current_href: str | None = None
        self._current_text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "a":
            return
        attr_map = dict(attrs)
        href = attr_map.get("href")
        if href:
            self._current_href = href.strip()
            self._current_text = []

    def handle_data(self, data: str) -> None:
        if self._current_href is not None:
            self._current_text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() != "a" or self._current_href is None:
            return
        title = normalize_inline_text("".join(self._current_text))
        if title:
            self.links.append(
                EssayLink(
                    title=title,
                    url=urljoin(BASE_URL, self._current_href),
                    href=self._current_href,
                )
            )
        self._current_href = None
        self._current_text = []


class EssayTextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.title = ""
        self.body_text = ""
        self._in_title = False
        self._in_body = False
        self._ignored_depth = 0
        self._title_parts: list[str] = []
        self._body_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        if tag == "title":
            self._in_title = True
        if tag == "body":
            self._in_body = True
        if tag in {"script", "style", "map"}:
            self._ignored_depth += 1
        if self._in_body and tag in {"br", "p", "tr", "table", "div", "hr"}:
            self._append_break()

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag == "title":
            self._in_title = False
            self.title = normalize_inline_text("".join(self._title_parts))
        if tag == "body":
            self._in_body = False
        if tag in {"script", "style", "map"} and self._ignored_depth:
            self._ignored_depth -= 1
        if self._in_body and tag in {"p", "tr", "table", "div", "font"}:
            self._append_break()

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self._title_parts.append(data)
        if not self._in_body or self._ignored_depth:
            return
        text = normalize_inline_text(data)
        if text:
            self._append_text(text)

    def close(self) -> None:
        super().close()
        self.body_text = normalize_block_text("".join(self._body_parts))

    def _append_text(self, text: str) -> None:
        if not self._body_parts or self._body_parts[-1].endswith((" ", "\n")):
            self._body_parts.append(text)
        else:
            self._body_parts.append(" " + text)

    def _append_break(self) -> None:
        if self._body_parts:
            self._body_parts.append("\n")


def normalize_inline_text(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def normalize_block_text(value: str) -> str:
    value = re.sub(r"[ \t]*\n[ \t]*", "\n", value)
    value = re.sub(r"\n{3,}", "\n\n", value)
    return value.strip()


def fetch_text(url: str, timeout: float) -> tuple[str, int, str]:
    request = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(request, timeout=timeout) as response:
        raw = response.read()
        charset = response.headers.get_content_charset() or "utf-8"
        final_url = response.geturl()
    try:
        text = raw.decode(charset)
    except UnicodeDecodeError:
        text = raw.decode("windows-1252", errors="replace")
    return text, len(raw), final_url


def extract_index_links(index_html: str) -> list[EssayLink]:
    list_html = isolate_essay_list(index_html)
    parser = LinkParser()
    parser.feed(list_html)
    parser.close()

    seen_urls: set[str] = set()
    essay_links: list[EssayLink] = []
    for link in parser.links:
        if not is_essay_url(link.url):
            continue
        if link.url in seen_urls:
            continue
        seen_urls.add(link.url)
        essay_links.append(link)
    return essay_links


def isolate_essay_list(index_html: str) -> str:
    start = index_html.find("the-reddits-2.gif")
    if start == -1:
        return index_html
    end = index_html.find('<a href="rss.html">RSS</a> feed', start)
    if end == -1:
        return index_html[start:]
    return index_html[start:end]


def is_essay_url(url: str) -> bool:
    parsed = urlparse(url)
    if parsed.netloc and parsed.netloc.lower() != "paulgraham.com":
        return False
    path = parsed.path.lstrip("/")
    filename = Path(path).name
    return path.endswith(".html") and filename not in NON_ESSAY_PAGES


def parse_essay(html: str) -> tuple[str, str]:
    parser = EssayTextParser()
    parser.feed(html)
    parser.close()
    return parser.title, parser.body_text


def markdown_for(title: str, source_url: str, fetched_at: str, body_text: str) -> str:
    return f"# {title}\n\nSource: {source_url}\nFetched: {fetched_at}\n\n{body_text}\n"


def safe_stem(href: str, fallback: str) -> str:
    stem = Path(urlparse(href).path).stem or fallback
    stem = re.sub(r"[^a-zA-Z0-9._-]+", "-", stem).strip("-._")
    return stem or fallback


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def iter_limited(items: Iterable[EssayLink], limit: int | None) -> Iterable[EssayLink]:
    for index, item in enumerate(items):
        if limit is not None and index >= limit:
            break
        yield item


def pull_essays(args: argparse.Namespace) -> int:
    output_dir = args.output
    markdown_dir = output_dir / "markdown"
    html_dir = output_dir / "html"

    index_html, index_bytes, index_final_url = fetch_text(args.index_url, args.timeout)
    essay_links = extract_index_links(index_html)
    selected_links = list(iter_limited(essay_links, args.limit))

    output_dir.mkdir(parents=True, exist_ok=True)
    write_text(output_dir / "articles.html", index_html)

    pulled = []
    failures = []
    started_at = utc_now()

    for position, link in enumerate(selected_links, start=1):
        stem = safe_stem(link.href, f"essay-{position}")
        fetched_at = utc_now()
        try:
            html, byte_count, final_url = fetch_text(link.url, args.timeout)
            parsed_title, body_text = parse_essay(html)
            title = parsed_title or link.title

            html_path = html_dir / f"{position:03d}-{stem}.html"
            markdown_path = markdown_dir / f"{position:03d}-{stem}.md"

            if args.format in {"html", "both"}:
                write_text(html_path, html)
            if args.format in {"markdown", "both"}:
                write_text(
                    markdown_path,
                    markdown_for(title, final_url, fetched_at, body_text),
                )

            pulled.append(
                {
                    "position": position,
                    "title": title,
                    "index_title": link.title,
                    "url": final_url,
                    "href": link.href,
                    "html_file": str(html_path.relative_to(output_dir))
                    if args.format in {"html", "both"}
                    else None,
                    "markdown_file": str(markdown_path.relative_to(output_dir))
                    if args.format in {"markdown", "both"}
                    else None,
                    "bytes": byte_count,
                    "text_chars": len(body_text),
                    "fetched_at": fetched_at,
                }
            )
            print(f"[{position}/{len(selected_links)}] {title}")
        except (HTTPError, URLError, TimeoutError, OSError) as exc:
            failures.append(
                {
                    "position": position,
                    "title": link.title,
                    "url": link.url,
                    "error": f"{type(exc).__name__}: {exc}",
                }
            )
            print(f"[{position}/{len(selected_links)}] FAILED {link.url}: {exc}")
            if args.fail_fast:
                break

        if position < len(selected_links) and args.delay > 0:
            time.sleep(args.delay)

    manifest = {
        "started_at": started_at,
        "finished_at": utc_now(),
        "source_index": index_final_url,
        "source_index_bytes": index_bytes,
        "discovered_essay_count": len(essay_links),
        "requested_essay_count": len(selected_links),
        "pulled_essay_count": len(pulled),
        "failed_essay_count": len(failures),
        "format": args.format,
        "essays": pulled,
        "failures": failures,
    }
    write_text(output_dir / "manifest.json", json.dumps(manifest, indent=2) + "\n")

    print(
        f"Done: pulled {len(pulled)} of {len(selected_links)} essays "
        f"into {output_dir}"
    )
    return 1 if failures else 0


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Pull Paul Graham essays from paulgraham.com."
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("sources/paul_graham_essays"),
        help="Directory for manifest and essay files.",
    )
    parser.add_argument(
        "--format",
        choices=("markdown", "html", "both"),
        default="both",
        help="Output format to write for each essay.",
    )
    parser.add_argument(
        "--index-url",
        default=INDEX_URL,
        help="Essay index URL to crawl.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Limit the number of essays to pull. Useful for testing.",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.2,
        help="Seconds to wait between essay requests.",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=30.0,
        help="HTTP timeout in seconds.",
    )
    parser.add_argument(
        "--fail-fast",
        action="store_true",
        help="Stop at the first failed essay download.",
    )
    return parser.parse_args()


def main() -> int:
    return pull_essays(parse_args())


if __name__ == "__main__":
    raise SystemExit(main())
