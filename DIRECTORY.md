# Directory

## Root

- `README.md` — how to run source-backed PG/YC office hours.
- `research_report.md` — consolidated research report on YC/PG startup advice and how to emulate office hours.
- `office_hours_corpus_map.md` — fast router from founder complaint to likely real issue and source anchors.
- `INDEX.md` — supplemental imported-corpus index.

## Core office-hours runtime

Use these first for weekly sessions:

- `prompts/pg_yc_office_hours_master_prompt.md` — highest-fidelity source-backed office-hours prompt.
- `playbooks/pg_yc_office_hours_workflow.md` — canonical 30/60 minute session workflow.
- `playbooks/source_backed_retrieval_protocol.md` — source-selection and local-search protocol.
- `sources/pg_yc_office_hours_source_matrix.md` — problem-to-source router covering important PG/YC materials.
- `templates/oh_prep.md` — founder prep before every session.
- `templates/session-summary.md` — source-backed session notes and commitments.
- `templates/weekly-metrics.md` — weekly metric snapshot.
- `scripts/search_office_hours_sources.py` — local source search and routing helper.

## `sources/`

- `pg_yc_office_hours_source_matrix.md` — main source router for office hours.
- `source_manifest.json` — machine-readable source list.
- `official_sources.md` — source links grouped by topic.
- `pg_diagnostic_index.md` — named PG tests/heuristics indexed by bottleneck gate; a routing map into the full essays, which must be read whole (incompressibility rule).
- `pg_essay_catalog_startup_relevant.md` — startup-relevant PG essay index, with priority tags.
- `paul-graham-startup-core-reading.md` — startup-core reading order and local paths.
- `paul-graham-local-corpus.md` — local PG corpus notes.
- `paul-graham-essay-index.md` — local PG essay index.
- `yc_library_seed_index.md` — YC Startup Library seed index for expanding the corpus.
- `yc-official-source-index.md` — official YC source index.
- `startup-school-video-index.md` — Startup School curriculum index.
- `copyright_and_refresh_policy.md` — how to refresh ethically.
- `paul_graham_essays/` — local private source corpus, if present.

## `pg_essays/`

- `00_pg_startup_doctrine.md` — compact synthesis of PG startup advice.
- `do_things_that_dont_scale.md` — unscalable acquisition and feedback-loop playbook.
- `startup_equals_growth.md` — growth as the defining property of startups.
- `what_ive_learned_from_users.md` — synthesis on how YC helps founders through focus, diagnosis, and action loops.
- `default_alive_or_default_dead.md` — runway/default-alive diagnostic.
- `how_not_to_die.md` — morale, contact cadence, and survival.
- `how_to_start_a_startup.md` — people, users, frugality, and startup fundamentals.
- `startups_in_13_sentences.md` — 13 rules converted into checks.
- `before_the_startup.md` — counterintuitive startup traps and preparation.
- `fundraising_and_investors.md` — fundraising doctrine and investor readiness.

## `yc_program/`

- `00_how_yc_works.md` — current YC program model and value stack.
- `office_hours_model.md` — office-hours mechanics to emulate.
- `program_resources.md` — funding, Demo Day, Bookface, alumni, first customers, launch support.
- `startup_school.md` — Startup School curriculum and how to adapt it.
- `application_interview.md` — what YC looks for and how to pressure-test clarity.

## `playbooks/`

- `pg_yc_office_hours_workflow.md` — primary 30/60 minute source-backed office-hours workflow.
- `source_backed_retrieval_protocol.md` — how to route, search, and apply sources before advice.
- `session_protocol.md` — concise live checklist.
- `weekly_update_template.md` — weekly cadence and accountability loop.
- `growth_diagnostic.md` — growth metric and bottleneck diagnosis.
- `user_learning_pipeline.md` — talking to users, extracting insight, turning it into product/growth work.
- `do_things_that_dont_scale_sprints.md` — experiment menu.
- `fundraising_readiness.md` — when to fundraise and how to know.
- `question-bank.md` — tactical questions for office hours.
- `every-few-days-cadence.md` — high-frequency cadence.

## `rubrics/`

- `company_snapshot_schema.md` — info needed to simulate a YC partner.
- `problem_priority_matrix.md` — kill-risk vs leverage vs time-to-feedback.
- `pmf_rubric.md` — product-market fit signals.
- `founder_diagnostics.md` — cofounder, execution, motivation, and focus checks.
- `metrics_quality_rubric.md` — metric quality checks.
- `launch_rubric.md` — launch discipline.
- `fundraising_story_rubric.md` — fundraising narrative quality.

## `templates/`

- `oh_prep.md` — prep before every office-hours session.
- `session-summary.md` — source-backed session summary and assignments.
- `weekly-metrics.md` — weekly metrics snapshot.
- `metrics_dashboard.md` — dashboard template.
- `user-learning-log.md` — user evidence log.
- `user_interview_script.md` — tactical script for user calls.
- `experiment_card.md` / `growth-experiment.md` — action design templates.
- `problem-priority-triage.md` — bottleneck triage.
- `decision_log_template.md` — decision log.
- `investor_update.md` — concise investor/advisor update.
- `fundraising-readiness.md` — fundraising readiness checklist.
- `launch-hn-prep.md` — launch prep.



## `scripts/`

- `search_office_hours_sources.py` — dependency-free local source search and routing helper.
- `build_pg_manifest.py` — local script to parse PG's essay index and build a manifest.
- `build_pg_index.py` — local PG index builder.
- `build_local_pg_corpus_index.py` — local corpus index builder.
- `pull_paul_graham_essays.py` — private local source puller.
- `sync_sources_README.md` — how to refresh source maps.

## `case_studies/`

- `airbnb_unscalable.md` — manual marketplace work and founder persistence.
- `stripe_collison_installation.md` — collapsing interest into activation.
- `wufoo_delight.md` — unusually attentive early customer service.
- `facebook_contained_fire.md` — narrow initial market density.
- `yc_batch_sharding.md` — why individualized context matters.
- `viaweb_manual_operations.md` — doing user work manually before automation.

## `yc_library_notes/`

- `core_yc_startup_advice.md` — essential YC principles.
- `mvp.md` — MVP design and traps.
- `talk_to_users.md` — user interview discipline.
- `first_customers.md` — founder-led sales and early customers.
- `growth_for_startups.md` — growth hierarchy and bottlenecks.
- `product_market_fit.md` — PMF signals and false positives.
- `analytics_and_metrics.md` — metric quality and dashboarding.
- `fundraising_legal_safes.md` — financing mechanics without over-optimizing.
- `cofounders_and_team.md` — cofounder/team checks.

## `prompts/`

- `pg_yc_office_hours_master_prompt.md` — primary source-backed prompt.
- `mock_yc_partner_prompt.md` — shorter reusable mock YC partner prompt.
- `office_hours_kickoff_prompt.md` — prompt to begin a new loop.
- `user_update_prompt.md` — prompt for recurring updates.

## `checklists/`

- `pre_launch_checklist.md` — launch as learning, not publicity.
- `office_hours_preflight.md` — what to prepare before each session.
- `fake_progress_checklist.md` — detects startup theater.
- `fundraising_preflight.md` — checks whether fundraising is sane.
- `weekly_growth_review.md` — recurring growth review.

## `reports/`

- `recreate-yc-office-hours.md` — report on recreating YC-style office hours.
- `paul-graham-startup-theme-map.md` — PG essay theme map.
- `yc-how-it-works.md` — YC mechanics report.
- `yc-founder-support-map.md` — YC support model.
- `yc-advice-taxonomy.md` — advice taxonomy.
- `advice-by-problem.md` — problem-oriented advice map.

## `ops/`

- `12_week_mock_yc_batch.md` — 12-week mock batch plan.
- `decision_log.md` — running decision log.
- `knowledge_base_maintenance.md` — corpus maintenance guidance.

## sessions

Session ledger: one dated summary per office-hours session (`YYYY-MM-DD-<company>.md`).
Read the latest entry first and score its commitments; write a new entry before each
session ends. See `sessions/README.md`.

