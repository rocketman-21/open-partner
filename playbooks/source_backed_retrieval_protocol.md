# Source-Backed Retrieval Protocol

Use this protocol before giving startup advice in office hours. The aim is to make the session feel like a well-prepared YC partner who has internalized the corpus, not a generic chatbot.

## Retrieval contract

Before giving a recommendation, identify:

1. The founder's stated problem.
2. The likely real problem.
3. The source anchors that should govern the discussion.
4. The specific question each source suggests asking.
5. The action class implied by those sources.

Do not quote long passages. Name sources and apply them.

## Step 1: classify the problem

Use these classes:

- Growth rate / metric quality
- Manual user acquisition
- User learning / ICP
- Activation / onboarding
- Retention / product value
- Sales / pricing / revenue
- Runway / default alive-dead
- Fundraising
- Launch / PR / partnerships
- Hiring / premature scaling
- Cofounder / founder psychology
- Focus / too many priorities
- Crypto/community/protocol metrics

## Step 2: choose a minimum source set

Always include at least one source from each applicable layer.

### Operating layer

- `pg_essays/what_ive_learned_from_users.md` — office-hours mechanics: individual context, focus, biggest problem, measurable near-term action.
- `yc_program/office_hours_model.md` — how YC-style office hours should function.
- `yc_program/00_how_yc_works.md` — YC program structure and support model.

### Growth layer

- `pg_essays/startup_equals_growth.md` — growth rate as the startup compass.
- `pg_essays/do_things_that_dont_scale.md` — manual recruiting, delight, concierge/manual work, contained fire.
- `yc_library_notes/growth_for_startups.md` — YC growth notes.

### User/product layer

- `sources/paul_graham_essays/markdown/081-startupideas.md` — organic startup ideas and reachable users.
- `sources/paul_graham_essays/markdown/107-organic.md` — organic ideas from real needs.
- `pg_essays/before_the_startup.md` — counterintuitive startup traps and knowing users.
- `yc_library_notes/product_market_fit.md` — PMF signals.
- `yc_library_notes/talk_to_users.md` — user-interview discipline.

### Survival/fundraising layer

- `pg_essays/default_alive_or_default_dead.md` — default alive/dead.
- `sources/paul_graham_essays/markdown/073-pinch.md` — fatal pinch.
- `pg_essays/how_not_to_die.md` — persistence and morale.
- `pg_essays/fundraising_and_investors.md` — fundraising readiness.
- `sources/paul_graham_essays/markdown/076-fr.md` — How to Raise Money.
- `sources/paul_graham_essays/markdown/078-convince.md` — How to Convince Investors.

### Founder/focus layer

- `sources/paul_graham_essays/markdown/127-13sentences.md` — compact operating rules.
- `sources/paul_graham_essays/markdown/163-startupmistakes.md` — common startup-killing mistakes.
- `sources/paul_graham_essays/markdown/171-startuplessons.md` — hard lessons founders resist.
- `sources/paul_graham_essays/markdown/122-relres.md` — relentlessly resourceful behavior.
- `sources/paul_graham_essays/markdown/090-word.md` — resourcefulness.
- `sources/paul_graham_essays/markdown/105-top.md` — what occupies the founder's mind.

### YC/current program layer

- `yc_program/00_how_yc_works.md`
- `yc_program/program_resources.md`
- `yc_program/startup_school.md`
- `sources/yc-official-source-index.md`

Use current official YC pages for claims about the current YC program/deal, because those facts can change.

## Step 3: search local sources

Use the script:

```bash
python scripts/search_office_hours_sources.py "founder complaint or question"
python scripts/search_office_hours_sources.py --top 12 "slow growth users say they like it but don't come back"
python scripts/search_office_hours_sources.py --paths pg_essays yc_library_notes playbooks "fundraising default dead"
```

Search with multiple phrasings:

1. The founder's language: `we need partnerships to grow`.
2. The suspected real problem: `manual recruiting weak growth`.
3. The danger pattern: `default dead slow growth fundraising`.
4. The desired action: `recruit users manually contained fire`.

## Step 4: build the answer from sources

Use this structure:

```md
## Source anchors
- Source path — why it applies.

## What the sources imply
- Principle applied to this situation.

## Diagnosis
- Biggest bottleneck.

## Action
- Concrete assignment.
```

Example:

```md
## Source anchors
- `pg_essays/startup_equals_growth.md` — because the key question is whether active usage/revenue is compounding weekly.
- `pg_essays/do_things_that_dont_scale.md` — because no channel is working yet, so founder-led recruiting is the expected early engine.
- `pg_essays/what_ive_learned_from_users.md` — because the session must isolate the biggest problem and convert it into a week-scale action.

## Diagnosis
The problem is not "marketing" yet. The problem is that we do not know whether a narrow segment loves the product enough to recruit manually.

## Assignment
By Friday, manually onboard 8 named users from segment X, watch them reach the first value moment, and record whether they repeat the core action within 48 hours.
```

## Step 5: avoid false source matches

Reject a source if:

- It only matches a word but not the situation.
- It is about later-stage companies while the startup is pre-PMF.
- It is about fundraising when the actual issue is weak growth.
- It is about product polishing when the issue is unclear demand.
- It is a current-program claim from an old file when an official YC page should be checked.

## Step 6: keep a source trail

Every `templates/session-summary.md` should list:

- source anchors used
- the principle applied
- why that source was selected
- what would make a different source more relevant next time

This makes the office-hours loop compound over time instead of resetting every conversation.
