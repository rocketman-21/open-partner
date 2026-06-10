# open-partner

**An open-source YC-style partner — office hours, accountability, and the source corpus.**

YC's real product was never the money. It's the method: a partner across the table who asks what you committed to, scores whether you did it, finds the one problem that matters this week, and sends you away with an action small enough that you can't hide from it. That method is mostly conversation + corpus + cadence — which means it can be a repo.

Point your AI agent (Claude Code, Codex, anything that reads markdown) at this directory and run office hours:

1. **Read first:** `playbooks/pg_yc_office_hours_workflow.md` — the canonical 30/60-minute session.
2. **The skill:** `.agents/skills/office-hours/` — drop-in agent skill with startup + builder modes.
3. **The ledger:** `sessions/` — one summary per session; every session starts by scoring the last one's commitments. This is the part that makes it work; without the ledger it's just chatting.
4. **The corpus:** `sources/` + `pg_essays/` — Paul Graham's essays and YC-method notes, routed per problem by `office_hours_corpus_map.md`.

Not affiliated with Y Combinator. By default the agent **roleplays Paul Graham** — first person, his voice, grounded in his essays and YC's operating model: direct, source-routed, allergic to fake progress. Ask for a neutral partner if you'd rather skip the persona.

---

This repository is not a generic startup wiki. It is an operating system for a weekly or every-few-days conversation that should feel like a sharp YC partner session: facts first, growth as the compass, the biggest obstacle surfaced fast, and one or two concrete founder-owned actions before the next session.

By default it speaks as Paul Graham: direct, source-routed, allergic to fake progress, and willing to say when the real problem is users, growth, product, focus, runway, or founder behavior. Ask for a neutral partner to drop the persona.

## The doctrine in one page

1. **Growth is the compass.** For a launched startup, the first serious question is: what is the weekly growth rate of the best available real metric? Revenue is best; active usage is next-best if monetization is not ready.
2. **User behavior beats founder narrative.** Office hours should ask what users actually did, paid for, returned to, complained about, or built into their workflow.
3. **The biggest problem wins.** Most startups have many problems, but only one or two matter this week. The session exists to identify the thing that constrains growth or survival most.
4. **Manual work is not a hack; it is the early engine.** Recruiting users manually, acting like a concierge, doing the work by hand, and delighting early users are often the shortest path to product truth.
5. **One week is the default action horizon.** The output is not a strategy memo. It is a measurable action with a deadline short enough to review next session.
6. **Survival gates ambition.** If runway/default-alive status is dangerous, the session switches from ambition to survival: revenue sooner, burn lower, fundraising less magical.
7. **Avoid startup theater.** Big launches, partnerships, fundraising gossip, hiring, community vanity metrics, and roadmaps are suspect until tied to real usage, revenue, or learning.

## How to run a session

Clone the repo, open your agent inside it, and say:

```
office hours
```

That's the whole interface. The agent reads `AGENTS.md`, loads the office-hours
skill, opens the latest `sessions/` entry, scores your previous commitments, and
runs the 30/60-minute workflow — asking you the prep questions conversationally
and writing the session summary itself. You never fill in a template by hand;
you just answer questions and bring facts (metrics, user quotes, what actually
happened since last time).

First session ever? Say `office hours` anyway — the partner interviews you to
build the company snapshot first.

Everything below this point is the machinery the agent uses (and reference for
running it manually if you ever want to).

## Source-backed retrieval flow

Every serious answer should route to sources before advice. The retrieval flow is:

1. Classify the issue: growth, users, activation, retention, sales, pricing, runway, fundraising, idea quality, cofounders, focus, launch, community/token metrics, or morale.
2. Open `sources/pg_yc_office_hours_source_matrix.md` and choose 3-7 source anchors.
3. Search local material with:

```bash
python scripts/search_office_hours_sources.py "we need more users but signups are flat"
python scripts/search_office_hours_sources.py "default dead slow revenue growth fundraising"
python scripts/search_office_hours_sources.py "web3 community excited but product usage weak"
```

4. In the office-hours answer, name the source anchors used and explain how they affect the recommendation.
5. Avoid long quotations. The goal is to apply the ideas, not recite essays.

## Fast article router

| Problem in the session | Start with these sources |
|---|---|
| Need more users / passive growth | `Do Things that Don't Scale`, `Startup = Growth`, `How to Get Startup Ideas`, `The Airbnbs` |
| Unclear ICP / weak user pull | `What I've Learned from Users`, `How to Get Startup Ideas`, `Organic Startup Ideas`, `Before the Startup` |
| Users try but do not come back | `Do Things that Don't Scale`, `The Hardest Lessons for Startups to Learn`, YC notes on PMF/metrics |
| Launch/press obsession | `Do Things that Don't Scale`, `Startups in 13 Sentences`, YC launch notes |
| Fundraising anxiety | `Default Alive or Default Dead?`, `The Fatal Pinch`, `How to Raise Money`, `How to Convince Investors` |
| Hiring as a growth plan | `Default Alive or Default Dead?`, `The 18 Mistakes That Kill Startups`, `How to Start a Startup` |
| Too many possible directions | `What I've Learned from Users`, `Startup = Growth`, `The Top Idea in Your Mind` |
| Founder psychology / morale | `How Not to Die`, `Relentlessly Resourceful`, `A Word to the Resourceful`, `Founder Mode` |

## 30-minute office-hours shape

| Time | What happens |
|---:|---|
| 0-5 | Facts: metrics, users, revenue, runway, what changed. |
| 5-10 | Source routing: choose the relevant PG/YC anchors. |
| 10-20 | Diagnose the true bottleneck; challenge the founder's stated problem. |
| 20-27 | Design one or two actions due in 2-7 days. |
| 27-30 | Commitments, metric, owner, next session's first question. |

## 60-minute office-hours shape

| Time | What happens |
|---:|---|
| 0-10 | Review last commitments and current facts. |
| 10-20 | Source routing and problem classification. |
| 20-35 | Root-cause diagnosis and uncomfortable questions. |
| 35-50 | Experiment/action design, including who exactly will be contacted or what exactly will ship. |
| 50-60 | Close with commitments, metric, failure signal, and what not to work on. |

## Directory map

See `DIRECTORY.md` for the file-by-file guide and `INDEX.md` for the supplemental imported corpus index.

The core files for daily use are:

- `prompts/pg_yc_office_hours_master_prompt.md`
- `playbooks/pg_yc_office_hours_workflow.md`
- `playbooks/source_backed_retrieval_protocol.md`
- `sources/pg_yc_office_hours_source_matrix.md`
- `office_hours_corpus_map.md`
- `templates/oh_prep.md`
- `templates/session-summary.md`
- `scripts/search_office_hours_sources.py`
