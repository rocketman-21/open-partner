#!/usr/bin/env python3
"""Build the Paul Graham essay URL index without downloading essay bodies.

This script intentionally fetches only the official index page and extracts
essay titles/links. It does not save full essay text.
"""

from __future__ import annotations

import html
import re
import sys
import urllib.request
from pathlib import Path
from urllib.parse import urljoin


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "sources" / "paul-graham-essay-index.md"
SOURCE_URL = "https://www.paulgraham.com/articles.html"

STARTUP_CORE_SLUGS = {
    "users.html": "office-hours mechanics, user learning, partner advice",
    "ds.html": "manual recruiting, early user delight, concierge work",
    "growth.html": "startup definition, weekly growth as compass",
    "startupideas.html": "organic ideas, founder insight, schlep blindness",
    "before.html": "pre-startup preparation and idea search",
    "aord.html": "default alive/default dead, runway discipline",
    "pinch.html": "fatal pinch, growth/runway danger",
    "fr.html": "fundraising process and investor psychology",
    "convince.html": "investor persuasion and fundraising narrative",
    "fundraising.html": "fundraising survival rules",
    "13sentences.html": "compact startup operating rules",
    "die.html": "how not to die",
    "startupmistakes.html": "startup failure modes",
    "startuplessons.html": "hardest startup lessons",
    "whyyc.html": "why YC exists and what founders need",
    "ycstart.html": "how YC started",
    "ycombinator.html": "YC as a new venture model",
    "founders.html": "what YC looks for in founders",
    "relres.html": "resourcefulness as founder trait",
    "airbnbs.html": "Airbnb example and founder behavior",
    "airbnb.html": "Airbnb fundraising/user story",
    "ramenprofitable.html": "default survival through low burn",
    "hiresfund.html": "high resolution fundraising",
    "hubs.html": "startup hubs and peer effects",
    "startuphubs.html": "why startup hubs matter",
    "corpdev.html": "avoid distracting corporate development paths",
}

NON_ESSAY_SLUGS = {
    "articles.html",
    "rss.html",
}


def fetch(url: str) -> str:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "yc-research-corpus/1.0 (+metadata-only)",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        raw = response.read()
    return raw.decode("utf-8", errors="replace")


def parse_articles(markup: str) -> list[tuple[str, str]]:
    pairs: list[tuple[str, str]] = []
    seen: set[str] = set()
    for href, title in re.findall(r'<a href="([^"]+)">([^<]+)</a>', markup):
        if not href.endswith(".html") or href in NON_ESSAY_SLUGS:
            continue
        clean_title = re.sub(r"\s+", " ", html.unescape(title)).strip()
        clean_href = html.unescape(href).strip()
        if not clean_title or clean_href in seen:
            continue
        seen.add(clean_href)
        pairs.append((clean_title, clean_href))
    return pairs


def render(pairs: list[tuple[str, str]]) -> str:
    startup_core = [
        (title, href, STARTUP_CORE_SLUGS[href])
        for title, href in pairs
        if href in STARTUP_CORE_SLUGS
    ]

    lines: list[str] = [
        "# Paul Graham Essay Index",
        "",
        "Generated from the official Paul Graham article index.",
        "",
        f"- Source: {SOURCE_URL}",
        "- Generated: 2026-05-12",
        "- Scope: metadata and URLs only. Full essay text is not stored here.",
        "",
        "## Startup-Core Reading Set",
        "",
        "| Essay | URL | Office-hours use |",
        "| --- | --- | --- |",
    ]

    for title, href, use in startup_core:
        url = urljoin(SOURCE_URL, href)
        lines.append(f"| {title} | {url} | {use} |")

    lines.extend(
        [
            "",
            "## Full Official Essay URL Inventory",
            "",
            "This is a title/link inventory, not a full-text archive.",
            "",
        ]
    )

    for index, (title, href) in enumerate(pairs, start=1):
        lines.append(f"{index}. [{title}]({urljoin(SOURCE_URL, href)})")

    lines.append("")
    return "\n".join(lines)


def main() -> int:
    markup = fetch(SOURCE_URL)
    pairs = parse_articles(markup)
    if len(pairs) < 100:
        print(f"Refusing to write suspiciously small PG index: {len(pairs)} links", file=sys.stderr)
        return 1
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(render(pairs), encoding="utf-8")
    print(f"Wrote {OUT.relative_to(ROOT)} with {len(pairs)} essay links")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
