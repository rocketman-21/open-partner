#!/usr/bin/env python3
"""Search and route the YC / Paul Graham office-hours corpus.

This is intentionally lightweight and dependency-free. It searches markdown files
in the corpus, boosts the sources that are most useful for YC-style office
hours, and prints short snippets plus routing hints.

Examples:
    python scripts/search_office_hours_sources.py "we need more users"
    python scripts/search_office_hours_sources.py --top 12 "default dead slow growth fundraising"
    python scripts/search_office_hours_sources.py --paths pg_essays yc_library_notes playbooks "activation low users don't come back"
"""

from __future__ import annotations

import argparse
import math
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "from",
    "has", "have", "how", "i", "if", "in", "is", "it", "its", "me", "more",
    "need", "of", "on", "or", "our", "that", "the", "this", "to", "we", "what",
    "when", "with", "you", "your", "users", "startup", "startups",
}

# Curated routing hints. These are not replacements for search; they are a fast
# way to choose likely source anchors before reading.
ROUTES: list[tuple[set[str], list[str], str]] = [
    (
        {"growth", "flat", "stalled", "metric", "weekly", "users", "revenue"},
        [
            "pg_essays/startup_equals_growth.md",
            "pg_essays/do_things_that_dont_scale.md",
            "pg_essays/what_ive_learned_from_users.md",
            "playbooks/growth_diagnostic.md",
        ],
        "Growth/metric issue: use weekly growth as the compass, then identify the bottleneck.",
    ),
    (
        {"manual", "recruit", "sales", "first", "customers", "acquire", "outbound"},
        [
            "pg_essays/do_things_that_dont_scale.md",
            "yc_library_notes/first_customers.md",
            "case_studies/stripe_collison_installation.md",
            "case_studies/airbnb_unscalable.md",
        ],
        "Manual acquisition issue: founder-led recruiting is likely the first action.",
    ),
    (
        {"retention", "churn", "return", "repeat", "come", "back"},
        [
            "yc_library_notes/product_market_fit.md",
            "yc_library_notes/analytics_and_metrics.md",
            "playbooks/user_learning_pipeline.md",
            "playbooks/growth_diagnostic.md",
        ],
        "Retention issue: inspect repeated behavior and compare retained vs churned users.",
    ),
    (
        {"activation", "onboarding", "signup", "drop", "funnel", "value"},
        [
            "yc_library_notes/mvp.md",
            "yc_library_notes/analytics_and_metrics.md",
            "templates/user_interview_script.md",
            "playbooks/growth_diagnostic.md",
        ],
        "Activation issue: watch users reach or fail to reach the first value moment.",
    ),
    (
        {"fundraise", "fundraising", "investor", "investors", "raise", "money", "runway"},
        [
            "pg_essays/default_alive_or_default_dead.md",
            "pg_essays/fundraising_and_investors.md",
            "sources/paul_graham_essays/markdown/073-pinch.md",
            "sources/paul_graham_essays/markdown/076-fr.md",
            "sources/paul_graham_essays/markdown/078-convince.md",
        ],
        "Fundraising/runway issue: check default alive/dead and whether growth makes the raise obvious.",
    ),
    (
        {"default", "dead", "alive", "burn", "cash", "runway", "pinch"},
        [
            "pg_essays/default_alive_or_default_dead.md",
            "sources/paul_graham_essays/markdown/073-pinch.md",
            "templates/fundraising-readiness.md",
            "templates/weekly-metrics.md",
        ],
        "Survival issue: runway gates ambition; create a survival plan before strategy.",
    ),
    (
        {"launch", "press", "pr", "producthunt", "hacker", "news", "announcement"},
        [
            "pg_essays/do_things_that_dont_scale.md",
            "checklists/pre_launch_checklist.md",
            "yc_library_notes/first_customers.md",
            "sources/paul_graham_essays/markdown/127-13sentences.md",
        ],
        "Launch issue: launch is only useful if it recruits a core of users or creates learning.",
    ),
    (
        {"partnership", "partnerships", "corp", "enterprise", "distribution"},
        [
            "pg_essays/do_things_that_dont_scale.md",
            "sources/paul_graham_essays/markdown/069-corpdev.md",
            "playbooks/growth_diagnostic.md",
        ],
        "Partnership issue: test whether this is distribution avoidance.",
    ),
    (
        {"hire", "hiring", "team", "employee", "recruiting"},
        [
            "pg_essays/default_alive_or_default_dead.md",
            "sources/paul_graham_essays/markdown/163-startupmistakes.md",
            "yc_library_notes/cofounders_and_team.md",
            "rubrics/founder_diagnostics.md",
        ],
        "Hiring/team issue: check if repeatable work exists and whether burn increases risk.",
    ),
    (
        {"idea", "ideas", "icp", "customer", "segment", "market", "wedge"},
        [
            "sources/paul_graham_essays/markdown/081-startupideas.md",
            "sources/paul_graham_essays/markdown/107-organic.md",
            "pg_essays/before_the_startup.md",
            "case_studies/facebook_contained_fire.md",
        ],
        "Idea/ICP issue: find the narrow user segment with urgent reachable demand.",
    ),
    (
        {"web3", "crypto", "token", "community", "discord", "dao", "protocol"},
        [
            "web3_protocol_notes/yc_style_for_protocol_startups.md",
            "pg_essays/startup_equals_growth.md",
            "pg_essays/do_things_that_dont_scale.md",
            "yc_library_notes/analytics_and_metrics.md",
        ],
        "Protocol/community issue: translate excitement into retained behavior, revenue, or dependency.",
    ),
    (
        {"focus", "distracted", "priorities", "too", "many", "decide", "decision"},
        [
            "pg_essays/what_ive_learned_from_users.md",
            "pg_essays/startup_equals_growth.md",
            "sources/paul_graham_essays/markdown/105-top.md",
            "rubrics/problem_priority_matrix.md",
        ],
        "Focus issue: identify the one bottleneck that matters this cycle.",
    ),
]

CORE_BOOSTS = {
    "pg_essays/what_ive_learned_from_users.md": 8.0,
    "pg_essays/startup_equals_growth.md": 8.0,
    "pg_essays/do_things_that_dont_scale.md": 8.0,
    "sources/pg_yc_office_hours_source_matrix.md": 7.0,
    "office_hours_corpus_map.md": 6.0,
    "playbooks/pg_yc_office_hours_workflow.md": 6.0,
    "playbooks/source_backed_retrieval_protocol.md": 6.0,
    "playbooks/growth_diagnostic.md": 5.0,
    "pg_essays/default_alive_or_default_dead.md": 5.0,
    "pg_essays/how_not_to_die.md": 4.0,
}

@dataclass
class Result:
    path: Path
    score: float
    title: str
    snippet: str


def tokenize(text: str) -> list[str]:
    terms = re.findall(r"[a-zA-Z0-9][a-zA-Z0-9_'-]{1,}", text.lower())
    return [t.strip("'-") for t in terms if t.strip("'-") and t not in STOPWORDS]


def corpus_root() -> Path:
    # script is yc/scripts/search_office_hours_sources.py
    return Path(__file__).resolve().parents[1]


def iter_markdown(root: Path, paths: Iterable[str]) -> Iterable[Path]:
    for rel in paths:
        p = root / rel
        if p.is_file() and p.suffix.lower() == ".md":
            yield p
        elif p.is_dir():
            yield from p.rglob("*.md")


def title_for(text: str, path: Path) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            return stripped.lstrip("#").strip()
    return path.stem.replace("_", " ").replace("-", " ").title()


def snippet_for(text: str, terms: set[str], width: int = 360) -> str:
    lowered = text.lower()
    positions = [lowered.find(t) for t in terms if lowered.find(t) >= 0]
    if not positions:
        start = 0
    else:
        start = max(0, min(positions) - width // 3)
    raw = re.sub(r"\s+", " ", text[start : start + width]).strip()
    return raw + ("..." if start + width < len(text) else "")


def score_doc(text: str, rel_path: str, query_terms: list[str]) -> float:
    if not query_terms:
        return 0.0
    text_terms = tokenize(text)
    if not text_terms:
        return 0.0
    counts: dict[str, int] = {}
    for t in text_terms:
        counts[t] = counts.get(t, 0) + 1
    score = 0.0
    unique_query = set(query_terms)
    for term in unique_query:
        tf = counts.get(term, 0)
        if tf:
            score += math.log1p(tf) * 3
    # phrase-ish boost for terms appearing close in text
    lower = text.lower()
    for term in unique_query:
        if term in lower:
            score += 1
    # curated boost
    score += CORE_BOOSTS.get(rel_path, 0.0)
    # startup source directories are generally more relevant for this tool
    if rel_path.startswith("pg_essays/"):
        score += 2.0
    if rel_path.startswith("yc_library_notes/"):
        score += 1.5
    if rel_path.startswith("playbooks/"):
        score += 1.0
    if rel_path.startswith("sources/paul_graham_essays/markdown/"):
        score += 0.75
    return score


def routing_hints(query_terms: set[str]) -> list[tuple[str, list[str]]]:
    hints: list[tuple[str, list[str]]] = []
    for keys, sources, reason in ROUTES:
        if keys & query_terms:
            hints.append((reason, sources))
    return hints


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Search YC/PG office-hours sources")
    parser.add_argument("query", nargs="+", help="Founder complaint, problem, or decision")
    parser.add_argument("--top", type=int, default=8, help="Number of search results to show")
    parser.add_argument(
        "--paths",
        nargs="*",
        default=[
            "README.md",
            "office_hours_corpus_map.md",
            "sources/pg_yc_office_hours_source_matrix.md",
            "pg_essays",
            "yc_program",
            "yc_library_notes",
            "playbooks",
            "rubrics",
            "templates",
            "case_studies",
            "web3_protocol_notes",
            "sources/paul_graham_essays/markdown",
        ],
        help="Relative files/directories to search from corpus root",
    )
    args = parser.parse_args(argv)

    root = corpus_root()
    query = " ".join(args.query)
    terms = tokenize(query)
    term_set = set(terms)

    print("# Routing hints")
    hints = routing_hints(term_set)
    if hints:
        seen: set[str] = set()
        for reason, sources in hints[:6]:
            print(f"\n- {reason}")
            for src in sources:
                if src not in seen:
                    print(f"  - {src}")
                    seen.add(src)
    else:
        print("- No explicit route matched. Start with source matrix + growth/users/default sources.")
        print("  - sources/pg_yc_office_hours_source_matrix.md")
        print("  - pg_essays/what_ive_learned_from_users.md")
        print("  - pg_essays/startup_equals_growth.md")
        print("  - pg_essays/do_things_that_dont_scale.md")

    results: list[Result] = []
    for path in iter_markdown(root, args.paths):
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        rel = str(path.relative_to(root))
        score = score_doc(text, rel, terms)
        if score <= 0:
            continue
        results.append(
            Result(
                path=path.relative_to(root),
                score=score,
                title=title_for(text, path),
                snippet=snippet_for(text, term_set),
            )
        )

    results.sort(key=lambda r: r.score, reverse=True)

    print("\n# Search results")
    for i, result in enumerate(results[: args.top], start=1):
        print(f"\n## {i}. {result.title}")
        print(f"Path: `{result.path}`")
        print(f"Score: {result.score:.2f}")
        print(f"Snippet: {result.snippet}")

    print("\n# Office-hours reminder")
    print("Use the sources to ask better questions. End with one or two measurable actions, not a reading list.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
