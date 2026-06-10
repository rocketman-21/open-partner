#!/usr/bin/env python3
'''Build a metadata manifest from Paul Graham's public essay index.

Default behavior is metadata-only: title + URL. It intentionally does not save
full essay text. This keeps the corpus useful without redistributing copyrighted
content.

Usage:
  python scripts/build_pg_manifest.py --output sources/pg_manifest.json --markdown sources/pg_manifest.md
'''

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass, asdict
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

INDEX_URL = "https://paulgraham.com/articles.html"

@dataclass
class Essay:
    title: str
    url: str
    slug: str


def clean_title(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def fetch_index(url: str = INDEX_URL) -> list[Essay]:
    r = requests.get(url, timeout=20)
    r.raise_for_status()
    # PG pages may use legacy encodings; requests usually guesses well, but
    # this fallback avoids occasional unicode failures.
    if not r.encoding:
        r.encoding = "latin-1"
    soup = BeautifulSoup(r.text, "lxml")
    essays: list[Essay] = []
    seen: set[str] = set()
    for a in soup.find_all("a"):
        title = clean_title(a.get_text(" "))
        href = a.get("href")
        if not title or not href:
            continue
        if href.startswith("#") or "rss" in href.lower():
            continue
        abs_url = urljoin(url, href)
        if not abs_url.startswith("https://paulgraham.com/") and not abs_url.startswith("http://paulgraham.com/"):
            # keep external book chapters/translations out of the core PG essay manifest
            continue
        slug = abs_url.rsplit("/", 1)[-1]
        key = abs_url.lower()
        if key in seen:
            continue
        seen.add(key)
        essays.append(Essay(title=title, url=abs_url, slug=slug))
    return essays


def write_markdown(essays: list[Essay], path: Path) -> None:
    lines = ["# Paul Graham Essay Manifest", "", f"Source: {INDEX_URL}", "", "| # | Title | URL | Slug |", "|---:|---|---|---|"]
    for i, e in enumerate(essays, 1):
        lines.append(f"| {i} | {e.title} | {e.url} | {e.slug} |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, default=Path("sources/pg_manifest.json"))
    ap.add_argument("--markdown", type=Path, default=Path("sources/pg_manifest.md"))
    args = ap.parse_args()

    essays = fetch_index()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.markdown.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps([asdict(e) for e in essays], indent=2), encoding="utf-8")
    write_markdown(essays, args.markdown)
    print(f"Wrote {len(essays)} essays to {args.output} and {args.markdown}")


if __name__ == "__main__":
    main()
