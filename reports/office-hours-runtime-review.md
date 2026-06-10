# Office-Hours Runtime Review

Date: 2026-05-12

This review compares the corpus against the important Paul Graham startup essays and YC program materials needed to run recurring mock office hours.

## Verdict

The corpus had good summaries and many source files, but the runtime layer was too generic. It needed stronger instructions for:

- source-routing before advice;
- weekly growth as the first-class operating metric;
- root-cause bottleneck diagnosis;
- default alive/dead survival gating;
- resisting launch, fundraising, hiring, partnerships, and community vanity metrics as avoidance patterns;
- ending with one or two measurable founder-owned actions.

The patch adds that runtime layer.

## Essential PG/YC ideas that must shape every session

### 1. YC office hours are individualized diagnosis, not generic curriculum

`What I've Learned from Users` explains that startup problems recur, but advising cannot be fully automated because each startup needs specific context. The mock system therefore needs a company memory, prior commitments, source anchors, and a diagnosis tailored to the current bottleneck.

Files now enforcing this:

- `prompts/pg_yc_office_hours_master_prompt.md`
- `playbooks/pg_yc_office_hours_workflow.md`
- `templates/session-summary.md`

### 2. Growth is the compass

`Startup = Growth` is the core operating frame for launched startups. The office-hours loop must ask for weekly growth in revenue, active usage, retained core action, or the best available real proxy. It must reject absolute user counts and vanity metrics when they obscure the rate.

Files now enforcing this:

- `README.md`
- `playbooks/growth_diagnostic.md`
- `templates/oh_prep.md`
- `checklists/weekly_growth_review.md`

### 3. Early growth usually requires manual founder effort

`Do Things that Don't Scale` is the default source when growth is weak. The workflow should assume the founders may need to recruit users manually, delight early users, act as concierge, do work by hand, or focus on a narrow contained-fire market.

Files now enforcing this:

- `sources/pg_yc_office_hours_source_matrix.md`
- `office_hours_corpus_map.md`
- `playbooks/pg_yc_office_hours_workflow.md`
- `scripts/search_office_hours_sources.py`

### 4. The biggest problem wins

`What I've Learned from Users` says YC's essence is finding which problem matters most, making a week-scale plan, and measuring the result. The workflow now explicitly challenges the founder's stated diagnosis and chooses one priority.

Files now enforcing this:

- `playbooks/session_protocol.md`
- `playbooks/pg_yc_office_hours_workflow.md`
- `templates/session-summary.md`
- `rubrics/problem_priority_matrix.md`

### 5. Survival gates ambition

`Default Alive or Default Dead?` and `The Fatal Pinch` should override normal growth/product discussion when burn and runway are dangerous. The new prompt and workflow add a survival gate before product/growth strategy.

Files now enforcing this:

- `prompts/pg_yc_office_hours_master_prompt.md`
- `playbooks/session_protocol.md`
- `playbooks/source_backed_retrieval_protocol.md`
- `sources/pg_yc_office_hours_source_matrix.md`

### 6. Funding, hiring, partnerships, and launch are often avoidance patterns

Many PG/YC essays warn that founders can focus on impressive-looking work instead of making something users want and growing. The new source matrix routes these topics to counter-diagnoses first.

Files now enforcing this:

- `office_hours_corpus_map.md`
- `sources/pg_yc_office_hours_source_matrix.md`
- `checklists/office_hours_preflight.md`

### 7. For crypto/protocol startups, retained behavior beats hype

The corpus already had a web3 adaptation file. The patch integrates it into the source matrix and README so community/token/social excitement is translated into retained usage, paid activity, economic throughput, or durable protocol dependency.

Files now enforcing this:

- `README.md`
- `office_hours_corpus_map.md`
- `sources/pg_yc_office_hours_source_matrix.md`
- `scripts/search_office_hours_sources.py`

## Important PG essays covered by the routing matrix

- `What I've Learned from Users`
- `Do Things that Don't Scale`
- `Startup = Growth`
- `How to Get Startup Ideas`
- `Organic Startup Ideas`
- `Before the Startup`
- `How to Start a Startup`
- `Startups in 13 Sentences`
- `Default Alive or Default Dead?`
- `The Fatal Pinch`
- `Ramen Profitable`
- `How Not to Die`
- `The 18 Mistakes That Kill Startups`
- `The Hardest Lessons for Startups to Learn`
- `What We Look for in Founders`
- `Relentlessly Resourceful`
- `A Word to the Resourceful`
- `Schlep Blindness`
- `The Airbnbs`
- `Subject: Airbnb`
- `How to Raise Money`
- `How to Convince Investors`
- `A Fundraising Survival Guide`
- `How to Present to Investors`
- `Don't Talk to Corp Dev`
- `The Top Idea in Your Mind`
- `Founder Mode`

## What changed in the patch

- Rewrote `README.md` as a usage-focused office-hours operating guide.
- Added a high-fidelity master prompt for source-backed PG/YC office hours.
- Added a canonical 30/60 minute workflow.
- Added a source-backed retrieval protocol.
- Added a detailed source matrix mapping founder complaints to PG/YC sources, questions, and assignments.
- Upgraded prep/session templates to force metrics, prior commitments, source anchors, diagnosis, stop-list, and measurable assignments.
- Upgraded growth diagnostics and checklists.
- Added a local search script to retrieve relevant sources from the corpus during sessions.
- Added compatibility wrappers for older mock-office-hours playbooks.
