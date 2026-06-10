# CLAUDE.md

Read `AGENTS.md` — it is the operating contract for this repository.

Short version: when the user says "office hours" (or anything close), load the
skill at `.claude/skills/office-hours/SKILL.md`, score the latest `sessions/`
entry's commitments first, run the workflow in
`playbooks/pg_yc_office_hours_workflow.md`, and write the session summary
yourself before ending. The founder never fills a template by hand.
