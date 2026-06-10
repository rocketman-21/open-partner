# Copyright and Refresh Policy

## What this corpus stores

- Source URLs
- Short summaries
- Diagnostic frameworks
- Session templates
- Paraphrased advice
- A manifest for future ingestion

## What this corpus avoids

- Full copyrighted essays
- Full YC library transcripts
- Long verbatim excerpts
- Bulk republishing of pages that are not ours

## How to refresh

1. Use `scripts/build_pg_manifest.py` locally to parse Paul Graham's essay index.
2. Add new source URLs to `sources/source_manifest.json`.
3. Summarize in your own words.
4. Keep direct quotes short and rare.
5. Prefer action-oriented notes over archival text.

## Why this matters

The goal is not to clone PG/YC's archive. The goal is to internalize the advice well enough to simulate the discipline of YC office hours: focus, speed, weekly measurable progress, user learning, and honest diagnosis.
