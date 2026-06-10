# PG/YC Source-Backed Office-Hours Workflow

This is the canonical live workflow for a 30-60 minute recurring mock YC office-hours session.

The goal is not to brainstorm everything. The goal is to find the biggest obstacle to growth or survival, apply the right PG/YC source anchors, and leave with a measurable action.

## Non-negotiables

- Do not impersonate Paul Graham. Use PG/YC source-backed reasoning.
- Do not give generic startup advice before collecting facts.
- Do not let the session become a feature review, fundraising therapy, pitch polish, or market-size discussion unless that is the real bottleneck.
- Do not end without a written commitment.
- Do not produce more than two actions unless the session is explicitly a planning session rather than office hours.

## Inputs

The founder should bring:

- `templates/oh_prep.md`
- `templates/weekly-metrics.md`
- the latest summary in `sessions/` (the session ledger — read it FIRST, every time)
- user notes, sales notes, support tickets, or product analytics
- list of exact users/prospects contacted since last session

## The 30-minute agenda

### 0-5 minutes: commitment and fact review

Open the latest `sessions/` summary and score every commitment BEFORE any narrative
is allowed — the founder explains after the scoreboard exists, not instead of it:

| Commitment | Score |
|---|---|
| ... | DONE / PARTIAL / NOT DONE |

Rules:
- A commitment scored NOT DONE twice in a row does not get re-assigned — it gets
  SHRUNK until it cannot fail (e.g. "launch the challenge" becomes "send one text
  before this session ends, while I watch").
- Work done INSTEAD of the commitment — however excellent — scores the commitment
  NOT DONE. Quality of the substitute is discussed only after the score is recorded.

Then ask:

1. What did you commit to last session?
2. Did you do it? If not, why not?
3. What changed materially?
4. What did users do or teach you?
5. What is the current weekly growth rate of the best real metric?
6. How much runway do you have, and are you default alive or dead?

Write a fact table:

| Fact | Current | Previous | Change | Confidence |
|---|---:|---:|---:|---|
| Revenue |  |  |  |  |
| Active users/accounts |  |  |  |  |
| Retained core action |  |  |  |  |
| Activation |  |  |  |  |
| User conversations |  |  |  |  |
| Burn/runway |  |  |  |  |

### 5-8 minutes: source routing

Pick 3-7 sources using `sources/pg_yc_office_hours_source_matrix.md` and `office_hours_corpus_map.md`.

Minimum default set for a launched startup:

- `pg_essays/startup_equals_growth.md`
- `pg_essays/do_things_that_dont_scale.md`
- `pg_essays/what_ive_learned_from_users.md`

Add survival sources if runway matters:

- `pg_essays/default_alive_or_default_dead.md`
- `sources/paul_graham_essays/markdown/073-pinch.md`

Add idea/ICP sources if users are vague:

- `sources/paul_graham_essays/markdown/081-startupideas.md`
- `sources/paul_graham_essays/markdown/107-organic.md`
- `pg_essays/before_the_startup.md`

Add fundraising sources only if fundraising is truly the next constraint:

- `pg_essays/fundraising_and_investors.md`
- `sources/paul_graham_essays/markdown/076-fr.md`
- `sources/paul_graham_essays/markdown/078-convince.md`

### 8-18 minutes: bottleneck diagnosis

Use this tree in order. Stop at the highest unresolved gate.

#### Gate 1: Survival

- Are we default alive or default dead?
- Is runway short enough that survival constrains the next action?
- Are we assuming fundraising will save us without growth evidence?

If survival is the bottleneck, the action is usually: increase revenue quickly, decrease burn, narrow scope, or run a focused fundraising process with a fallback date.

#### Gate 2: Real user demand

- Who exactly wants this?
- What are they already doing instead?
- What have they done that costs them time, money, reputation, or effort?
- Would they be upset if the product disappeared?
- Have they paid, returned, referred, integrated, or depended on it?

If demand is weak, the action is usually: talk to a narrower user segment, watch real usage, manually solve the problem, or ask for money.

#### Gate 3: Product value / activation

- Can a user reach value without founder handholding?
- If not, where do they fail?
- Is the first value moment obvious and fast?
- What happened in the last 5 observed onboarding attempts?

If activation is weak, the action is usually: remove steps, concierge onboarding, rewrite onboarding around the user's words, or instrument the key drop-off.

#### Gate 4: Retention

- Who keeps using it?
- How often do they repeat the core action?
- What do retained users have in common?
- What do churned users have in common?

If retention is weak, the action is usually: interview retained users, cut non-retained segments, improve the repeated value loop, or narrow ICP.

#### Gate 5: Growth / distribution

- Are happy users growing week over week?
- What channel produced the last 10 real users or customers?
- What manual recruiting did the founders do?
- Is there a contained-fire segment where density can be achieved quickly?

If growth is weak but users are happy, the action is usually: manual recruiting sprint, narrow segment launch, founder-led sales, referral ask, or community/customer wedge.

#### Gate 6: Focus / founder behavior

- Are the founders spending most time on the bottleneck?
- What are they doing that feels productive but avoids the scary thing?
- What would be obvious to do if survival depended on this week?

If focus is weak, the action is usually: stop-list, calendar rewrite, one metric, one owner, one deadline.

### 18-25 minutes: design the action

Every assignment must fit this shape:

```md
Hypothesis:
Source anchors:
Target users/accounts:
Action:
Owner:
Deadline:
Metric:
Expected result:
Failure signal:
Fallback if it fails:
What we are explicitly not doing:
```

Good actions:

- “Founder will manually onboard 10 named users from segment X by Friday and watch each reach the first value moment.”
- “Founder will ask 5 current users for paid conversion and record objections verbatim.”
- “Founder will cut onboarding from 7 steps to 3 and measure activation for the next 20 signups.”
- “Founder will run 20 outbound messages to a narrow ICP, not a general launch.”

Two enforcement patterns for founders who build instead of asking:

- **Launch test**: before accepting any build-flavored action, ask "could a text
  message launch this today?" If yes, the message IS the action.
- **Reward gating**: tie the technical action the founder WANTS to the founder
  action they are avoiding ("you don't get to merge the PR until the three
  kickoff texts are sent"). The build becomes the reward, not the escape.

Bad actions:

- “Improve growth.”
- “Work on marketing.”
- “Talk to users” without named users or questions.
- “Explore partnerships.”
- “Build features users requested” without knowing whether they affect activation, retention, or revenue.

### 25-30 minutes: close

Write `sessions/YYYY-MM-DD-<company>.md` from `templates/session-summary.md` before
the session ends — an unwritten summary means the next session starts blind and
the accountability loop dies. Then end with:

- The biggest problem.
- The source anchors used.
- One or two commitments.
- The metric to review next session.
- The tempting work to ignore.
- The first question for the next office hours.

## The 60-minute agenda

Use the same structure, but spend additional time on raw evidence:

| Time | Focus |
|---:|---|
| 0-10 | Previous commitment, facts, metrics, runway. |
| 10-15 | Source routing. |
| 15-30 | Deep user evidence review: actual quotes, behavior, sales notes, analytics. |
| 30-42 | Bottleneck diagnosis and counter-diagnosis. |
| 42-52 | Action design and scope cuts. |
| 52-60 | Commitment, stop-list, next session setup. |

## Counter-diagnosis habit

Before accepting the founder's proposed problem, force at least one alternative:

| Founder says | Counter-diagnosis to test |
|---|---|
| We need more awareness | Maybe the product is not loved enough, or the ICP is too broad. |
| We need funding | Maybe investors are correctly reading weak growth or unclear demand. |
| We need more features | Maybe activation is broken, or users do not care enough. |
| We need a partnership | Maybe you are avoiding manual sales. |
| We need to hire | Maybe founders are avoiding the work only founders can do. |
| Community is excited | Maybe social enthusiasm is not retained product behavior. |
| I'll launch right after I finish X | X is usually avoidance. Apply the launch test: could a text message launch this today? If yes, the launch comes first and X waits. |
| We needed the infrastructure first | Maybe one of the launches needed it — the others never did. Launch the unblocked ones today; build only for the blocked one. |

## Source-backed session output template

```md
# Office Hours Summary

Date:
Company:
Session length:

## Source anchors used
- Source:
  - Why used:
  - Applied principle:

## Facts
- Metric snapshot:
- User evidence:
- Revenue/pipeline:
- Runway/default alive-dead:
- What changed:
- What is unknown:

## Diagnosis
Biggest problem:
Why this is the bottleneck:
Why the founder's stated problem is/was incomplete:
What we are ignoring for now:

## Assignment
Action 1:
- Owner:
- Deadline:
- Target users/accounts:
- Expected result:
- Failure signal:
- Metric:

Action 2, if truly needed:
- Owner:
- Deadline:
- Target users/accounts:
- Expected result:
- Failure signal:
- Metric:

## Stop-list until next session
-

## Next session starts with
-
```
