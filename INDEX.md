# Supplemental Index

Last updated: 2026-05-12

The office-hours runtime is now the canonical layer for this directory. Use these first:

1. `README.md`
2. `prompts/pg_yc_office_hours_master_prompt.md`
3. `playbooks/pg_yc_office_hours_workflow.md`
4. `playbooks/source_backed_retrieval_protocol.md`
5. `sources/pg_yc_office_hours_source_matrix.md`
6. `office_hours_corpus_map.md`
7. `templates/oh_prep.md`
8. `templates/session-summary.md`
9. `scripts/search_office_hours_sources.py`

## Runtime principle

A session should not start with advice. It should start with facts, source routing, bottleneck diagnosis, then one or two measurable assignments. The local corpus should be searched based on what the founder is actually saying.

## Imported Senior Corpus

The zip import contains these primary sections:

- `pg_essays/` — PG startup doctrine summaries and applied notes.
- `yc_program/` — YC program mechanics and resources.
- `playbooks/` — office-hours, growth, user-learning, fundraising, and unscalable sprint playbooks.
- `rubrics/` — company snapshot, problem priority, PMF, founder, metrics, launch, and fundraising rubrics.
- `templates/` — prep, notes, user interview, metrics, investor update, decision log, and experiment templates.
- `case_studies/` — Airbnb, Stripe, Wufoo, Facebook, YC sharding, and Viaweb examples.
- `yc_library_notes/` — YC library notes by topic.
- `prompts/` — reusable mock YC partner prompts.
- `checklists/` — preflight and review checklists.
- `ops/` — 12-week mock batch, decision log, and maintenance guidance.
- `sources/` — official source maps, source manifest, YC library seed index, and refresh policy.

## Local Supplemental Artifacts

These are supplemental navigation and source metadata:

- `sources/paul-graham-essay-index.md`
- `sources/paul-graham-local-corpus.md`
- `sources/paul-graham-startup-core-reading.md`
- `sources/startup-school-video-index.md`
- `sources/yc-official-source-index.md`
- `reports/paul-graham-startup-theme-map.md`
- `reports/recreate-yc-office-hours.md`
- `reports/yc-how-it-works.md`
- `reports/yc-founder-support-map.md`
- `reports/yc-advice-taxonomy.md`
- `reports/advice-by-problem.md`

## Authorized Local Source Copies

The local folder may contain a private PG source corpus under:

- `sources/paul_graham_essays/`

Use it as raw source material when needed. Prefer the runtime files above for daily office-hours flow because they route sources into diagnosis and action.

## Recommended recurring loop

1. Fill `templates/oh_prep.md`.
2. Run `python scripts/search_office_hours_sources.py "<the current issue>"`.
3. Start the session with `prompts/pg_yc_office_hours_master_prompt.md`.
4. Use `playbooks/pg_yc_office_hours_workflow.md`.
5. Save the output in `templates/session-summary.md`.
6. Review the assignment first in the next session.
