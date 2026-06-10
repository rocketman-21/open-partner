#!/usr/bin/env python3
"""Build metadata/navigation files for the local Paul Graham corpus.

This reads the user-supplied local essay files and writes only metadata,
tags, counts, and source paths. It does not quote or duplicate essay bodies.
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "sources" / "paul_graham_essays" / "manifest.json"
LOCAL_INDEX_OUT = ROOT / "sources" / "paul-graham-local-corpus.md"
STARTUP_READING_OUT = ROOT / "sources" / "paul-graham-startup-core-reading.md"
THEME_OUT = ROOT / "reports" / "paul-graham-startup-theme-map.md"


CORE_SLUGS: dict[str, tuple[str, str]] = {
    "users.html": ("office-hours", "Office-hours mechanics, user learning, focus, partner diagnosis."),
    "ds.html": ("users", "Manual recruiting, early user delight, concierge and Wizard-of-Oz work."),
    "growth.html": ("growth", "Startup definition, weekly growth, growth as the operating compass."),
    "startupideas.html": ("ideas", "Organic ideas, founder insight, reachable early users."),
    "getideas.html": ("ideas", "How to get new ideas and notice overlooked opportunities."),
    "before.html": ("ideas", "Preparation before starting; how founders become idea-ready."),
    "aord.html": ("runway", "Default alive/dead, runway, burn, and survival discipline."),
    "pinch.html": ("runway", "Fatal pinch: slow growth plus insufficient time to fix it."),
    "ramenprofitable.html": ("runway", "Low burn, survival, and optionality."),
    "fr.html": ("fundraising", "Fundraising process, investor psychology, and momentum."),
    "convince.html": ("fundraising", "Investor persuasion and credibility."),
    "fundraising.html": ("fundraising", "Fundraising survival and distraction control."),
    "hiresfund.html": ("fundraising", "High-resolution fundraising and closing investors independently."),
    "startupmistakes.html": ("failure-modes", "Common startup-killing mistakes."),
    "die.html": ("failure-modes", "How not to die as a startup."),
    "startuplessons.html": ("failure-modes", "Hard lessons startup founders repeatedly learn."),
    "13sentences.html": ("operating-rules", "Compact startup operating rules."),
    "whyyc.html": ("yc", "Why YC exists and what founders need."),
    "ycstart.html": ("yc", "How YC started."),
    "ycombinator.html": ("yc", "YC as a new venture model."),
    "founders.html": ("founders", "What YC looks for in founders."),
    "relres.html": ("founders", "Relentlessly resourceful founder behavior."),
    "airbnbs.html": ("case-studies", "Airbnb as example of user focus, persistence, and listening."),
    "airbnb.html": ("case-studies", "Airbnb fundraising/user story."),
    "corpdev.html": ("focus", "Avoiding corporate-development distraction."),
    "hubs.html": ("community", "Why startup hubs and peer density work."),
    "startuphubs.html": ("community", "Why founders should move to startup hubs."),
    "foundersatwork.html": ("founders", "Learning from founder stories."),
    "investors.html": ("fundraising", "How to present to investors."),
    "startupfunding.html": ("fundraising", "Startup funding basics."),
    "superangels.html": ("fundraising", "Funding landscape shifts."),
    "future.html": ("fundraising", "Future of startup funding."),
    "herd.html": ("fundraising", "Investor herd dynamics."),
    "swan.html": ("investing", "Black swan farming and startup selection."),
}

KEYWORDS: dict[str, list[str]] = {
    "users": ["user", "users", "customer", "customers"],
    "growth": ["growth", "grow", "growing"],
    "fundraising": ["fundraising", "investor", "investors", "raise money", "demo day"],
    "yc": ["y combinator", "yc", "office hours"],
    "launch": ["launch", "launched", "shipping", "ship"],
    "founders": ["founder", "founders", "cofounder", "cofounders"],
    "sales": ["sales", "sell", "selling", "revenue"],
    "runway": ["runway", "burn", "profitable", "default alive", "default dead"],
}


def load_manifest() -> dict:
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def word_count(path: Path) -> int:
    text = path.read_text(encoding="utf-8", errors="replace")
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'_-]*", text))


def keyword_counts(path: Path) -> Counter[str]:
    text = path.read_text(encoding="utf-8", errors="replace").lower()
    counts: Counter[str] = Counter()
    for label, needles in KEYWORDS.items():
        for needle in needles:
            counts[label] += text.count(needle)
    return counts


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def render_local_index(manifest: dict, rows: list[dict]) -> str:
    lines = [
        "# Paul Graham Local Corpus",
        "",
        "Metadata index for the local authorized PG essay corpus.",
        "",
        f"- Source index: {manifest['source_index']}",
        f"- Source index bytes: {manifest['source_index_bytes']}",
        f"- Discovered essays: {manifest['discovered_essay_count']}",
        f"- Pulled essays: {manifest['pulled_essay_count']}",
        f"- Failures: {manifest['failed_essay_count']}",
        f"- Started: {manifest['started_at']}",
        f"- Finished: {manifest['finished_at']}",
        "",
        "## Files",
        "",
        "| # | Title | Original | Local Markdown | Local HTML | Words | Tags |",
        "| ---: | --- | --- | --- | --- | ---: | --- |",
    ]
    for row in rows:
        tags = ", ".join(row["tags"])
        lines.append(
            f"| {row['position']} | {row['title']} | {row['url']} | "
            f"`{row['markdown_file']}` | `{row['html_file']}` | {row['words']} | {tags} |"
        )
    lines.append("")
    return "\n".join(lines)


def render_startup_reading(rows: list[dict]) -> str:
    core_rows = [row for row in rows if row["href"] in CORE_SLUGS]
    by_tag: dict[str, list[dict]] = defaultdict(list)
    for row in core_rows:
        by_tag[row["primary_tag"]].append(row)

    lines = [
        "# Paul Graham Startup-Core Reading Set",
        "",
        "A practical route through the local PG corpus for YC-style office hours.",
        "",
        "## Reading Order",
        "",
    ]
    order = [
        "office-hours",
        "users",
        "growth",
        "ideas",
        "runway",
        "fundraising",
        "failure-modes",
        "operating-rules",
        "founders",
        "yc",
        "community",
        "case-studies",
        "focus",
        "investing",
    ]
    for tag in order:
        items = by_tag.get(tag, [])
        if not items:
            continue
        lines.extend([f"## {tag.replace('-', ' ').title()}", ""])
        for row in items:
            lines.append(f"- [{row['title']}]({row['url']})")
            lines.append(f"  - Local Markdown: `{row['markdown_file']}`")
            lines.append(f"  - Local HTML: `{row['html_file']}`")
            lines.append(f"  - Office-hours use: {row['reason']}")
            lines.append(f"  - Words: {row['words']}")
        lines.append("")
    return "\n".join(lines)


def render_theme_map(rows: list[dict], keyword_totals: Counter[str], top_by_theme: dict[str, list[dict]]) -> str:
    lines = [
        "# PG Startup Theme Map",
        "",
        "Generated metadata from the local authorized PG corpus. Counts are rough keyword counts over local Markdown files and are meant for navigation, not scholarship.",
        "",
        "## Corpus Totals",
        "",
        f"- Essays indexed: {len(rows)}",
        f"- Total words: {sum(row['words'] for row in rows):,}",
        "",
        "## Theme Keyword Totals",
        "",
        "| Theme | Approximate hits |",
        "| --- | ---: |",
    ]
    for theme, count in keyword_totals.most_common():
        lines.append(f"| {theme} | {count} |")

    lines.extend(["", "## Top Essays By Theme", ""])
    for theme in KEYWORDS:
        lines.extend([f"### {theme.title()}", ""])
        for row in top_by_theme[theme][:10]:
            hits = row["keyword_counts"][theme]
            if hits <= 0:
                continue
            lines.append(f"- {row['title']} - {hits} hits - `{row['markdown_file']}`")
        lines.append("")

    lines.extend(
        [
            "## Practical Use",
            "",
            "- Use `users`, `growth`, `fundraising`, `runway`, and `yc` for office-hours prep.",
            "- Use `launch` and `sales` when preparing a user acquisition push.",
            "- Use `founders` when the problem smells like motivation, team dynamics, or founder-market fit.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    manifest = load_manifest()
    rows: list[dict] = []
    keyword_totals: Counter[str] = Counter()

    for essay in manifest["essays"]:
        markdown_path = ROOT / "sources" / "paul_graham_essays" / essay["markdown_file"]
        html_path = ROOT / "sources" / "paul_graham_essays" / essay["html_file"]
        tags: list[str] = []
        reason = ""
        primary_tag = ""
        if essay["href"] in CORE_SLUGS:
            primary_tag, reason = CORE_SLUGS[essay["href"]]
            tags.append(primary_tag)
        counts = keyword_counts(markdown_path)
        keyword_totals.update(counts)
        for theme, count in counts.most_common():
            if count >= 5 and theme not in tags:
                tags.append(theme)
        rows.append(
            {
                "position": essay["position"],
                "title": essay["title"],
                "href": essay["href"],
                "url": essay["url"],
                "markdown_file": rel(markdown_path),
                "html_file": rel(html_path),
                "words": word_count(markdown_path),
                "tags": tags[:6],
                "primary_tag": primary_tag,
                "reason": reason,
                "keyword_counts": counts,
            }
        )

    top_by_theme = {
        theme: sorted(rows, key=lambda row: row["keyword_counts"][theme], reverse=True)
        for theme in KEYWORDS
    }

    LOCAL_INDEX_OUT.write_text(render_local_index(manifest, rows), encoding="utf-8")
    STARTUP_READING_OUT.write_text(render_startup_reading(rows), encoding="utf-8")
    THEME_OUT.write_text(render_theme_map(rows, keyword_totals, top_by_theme), encoding="utf-8")
    print(f"Wrote {rel(LOCAL_INDEX_OUT)}, {rel(STARTUP_READING_OUT)}, {rel(THEME_OUT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

