# PG/YC Office-Hours Source Matrix

Use this as the router for source-backed office hours. It maps founder complaints to the highest-yield Paul Graham / YC materials, the principle to apply, and the concrete questions/actions to force.

The point is not to cite everything. It is to retrieve the few sources that make the diagnosis sharper.

## Default source stack

For most launched startups, start with:

1. `pg_essays/what_ive_learned_from_users.md` — office-hours method: identify the most important problem, solve at week-scale, measure results.
2. `pg_essays/startup_equals_growth.md` — growth as the startup compass.
3. `pg_essays/do_things_that_dont_scale.md` — manual recruiting, delight, concierge work, contained fire.
4. `yc_program/office_hours_model.md` — YC-style one-on-one and group office-hour mechanics.
5. `templates/weekly-metrics.md` — current metric truth.

Then add sources based on the bottleneck.

## Problem-to-source router

| Founder complaint / signal | Likely real issue | Primary sources | Questions to ask | Likely assignment |
|---|---|---|---|---|
| “We need more users.” | Passive acquisition, weak ICP, or weak product love. | `pg_essays/do_things_that_dont_scale.md`; `pg_essays/startup_equals_growth.md`; `yc_library_notes/first_customers.md`; `case_studies/stripe_collison_installation.md` | Who are the last 10 users? How did each arrive? Who did a founder personally recruit? What is weekly growth? | Manual recruiting sprint with named targets and activation observation. |
| “Users like it, but growth is flat.” | Interest is not demand, or users are not retained. | `pg_essays/startup_equals_growth.md`; `yc_library_notes/product_market_fit.md`; `yc_library_notes/analytics_and_metrics.md`; `templates/weekly-metrics.md` | What behavior proves they like it? What is retention? What is the core repeated action? | Define real metric, inspect retained users, talk to churned users. |
| “We need a launch.” | Avoiding manual acquisition; confusing publicity with traction. | `pg_essays/do_things_that_dont_scale.md`; `sources/paul_graham_essays/markdown/127-13sentences.md`; `yc_library_notes/first_customers.md`; `checklists/pre_launch_checklist.md` | What do we need from launch besides attention? Who is the initial core of users? | Launch only as a way to recruit a narrow initial user set; no broad PR-first launch. |
| “We need partnerships.” | Hoping someone else will provide distribution. | `pg_essays/do_things_that_dont_scale.md`; `sources/paul_graham_essays/markdown/069-corpdev.md`; `playbooks/growth_diagnostic.md` | What can the founders do directly this week? Which partner action is under our control? | Replace partnership work with founder-led sales/recruiting unless a specific customer contract is imminent. |
| “We need to hire to grow.” | Premature scaling, founders avoiding sales/product/user work. | `pg_essays/default_alive_or_default_dead.md`; `sources/paul_graham_essays/markdown/163-startupmistakes.md`; `pg_essays/how_to_start_a_startup.md` | What repeatable work exists? Which bottleneck can only founders solve? What happens to burn? | Do founder work manually first; hire only after repeatable bottleneck is proven. |
| “We need funding.” | Could be real, but often weak company performance. | `pg_essays/default_alive_or_default_dead.md`; `sources/paul_graham_essays/markdown/073-pinch.md`; `pg_essays/fundraising_and_investors.md`; `sources/paul_graham_essays/markdown/076-fr.md` | Are we default alive? What metric would make investors lean in? What is plan B if no raise? | Run default-alive calculation; set fundraising process and survival fallback date. |
| “Investors don’t get it.” | Pitch unclear or growth/product evidence insufficient. | `sources/paul_graham_essays/markdown/078-convince.md`; `sources/paul_graham_essays/markdown/165-investors.md`; `yc_program/application_interview.md` | Do users get it? Does growth make it obvious? What is the single sentence? | Rewrite pitch around user pull and metric; test on 5 smart outsiders. |
| “We have lots of ideas.” | Lack of focus; no single growth bottleneck. | `pg_essays/what_ive_learned_from_users.md`; `pg_essays/startup_equals_growth.md`; `sources/paul_graham_essays/markdown/105-top.md`; `rubrics/problem_priority_matrix.md` | Which idea most affects this week's growth/survival? What are we avoiding? | Choose one bottleneck and one action; create explicit stop-list. |
| “The product needs more features.” | Maybe activation/value issue; maybe lack of demand. | `pg_essays/do_things_that_dont_scale.md`; `sources/paul_graham_essays/markdown/171-startuplessons.md`; `yc_library_notes/mvp.md`; `yc_library_notes/product_market_fit.md` | Which user failed because of which missing feature? How many? Would they pay if it existed? | Concierge/manual workaround before building; build only if it changes activation/retention/revenue. |
| “People say it’s interesting.” | Polite interest, not demand. | `yc_library_notes/talk_to_users.md`; `sources/paul_graham_essays/markdown/081-startupideas.md`; `pg_essays/before_the_startup.md` | What did they do after saying this? Did they pay, return, refer, or ask urgently? | Ask for commitment: payment, intro, migration, repeated use, or next meeting. |
| “Our ICP is everyone.” | No initial wedge. | `sources/paul_graham_essays/markdown/081-startupideas.md`; `sources/paul_graham_essays/markdown/107-organic.md`; `pg_essays/do_things_that_dont_scale.md`; `case_studies/facebook_contained_fire.md` | Which subset can reach critical mass fastest? Who is most desperate? | Choose contained-fire segment and recruit it manually. |
| “Activation is low.” | First value moment unclear, too much friction, wrong user. | `yc_library_notes/mvp.md`; `yc_library_notes/analytics_and_metrics.md`; `playbooks/user_learning_pipeline.md`; `templates/user_interview_script.md` | Where exactly do users drop? Have we watched them? What is the first value moment? | Watch 5 users onboard; remove or concierge the top failure step. |
| “Retention is low.” | Product not valuable enough or wrong segment. | `yc_library_notes/product_market_fit.md`; `pg_essays/do_things_that_dont_scale.md`; `sources/paul_graham_essays/markdown/171-startuplessons.md` | Who retained? Who churned? What changed in their workflow? | Interview retained/churned users; narrow to the retained segment; fix repeated-value loop. |
| “Sales calls go well but deals stall.” | Buyer pain/urgency/pricing not proven. | `yc_library_notes/first_customers.md`; `yc_library_notes/talk_to_users.md`; `pg_essays/fundraising_and_investors.md` | Who owns budget? What event creates urgency? What would they pay now? | Ask for paid pilot with deadline; collect verbatim objections. |
| “We’re demoralized.” | Slow progress, bad focus, or near-death drift. | `pg_essays/how_not_to_die.md`; `sources/paul_graham_essays/markdown/122-relres.md`; `sources/paul_graham_essays/markdown/090-word.md`; `rubrics/founder_diagnostics.md` | Is this morale or lack of evidence? What action would produce evidence fastest? | Small win sprint: users contacted, revenue asked, activation fixed, or burn reduced. |
| “Cofounder tension.” | Alignment/focus/ownership issue. | `rubrics/founder_diagnostics.md`; `yc_library_notes/cofounders_and_team.md`; `pg_essays/before_the_startup.md` | Is the conflict about facts, goals, trust, or work allocation? | Write responsibilities and one-week commitments; resolve or escalate quickly. |
| “We’re default dead / low runway.” | Survival first. | `pg_essays/default_alive_or_default_dead.md`; `sources/paul_graham_essays/markdown/073-pinch.md`; `pg_essays/how_not_to_die.md`; `templates/fundraising-readiness.md` | What must happen before cash runs out? What expenses can drop? What revenue can close? | 7-14 day survival plan: revenue, burn cut, fundraising fallback, scope reduction. |
| “We want to apply to YC.” | Need clarity, user learning, momentum. | `yc_program/application_interview.md`; `yc_program/00_how_yc_works.md`; `pg_essays/what_ive_learned_from_users.md`; `pg_essays/startup_equals_growth.md` | What have you learned from users? What changed last week? Why this team? | Application/interview drill using real user evidence and metric trend. |

## High-priority Paul Graham essays for office hours

| Essay | Local path | Best used for |
|---|---|---|
| What I've Learned from Users | `sources/paul_graham_essays/markdown/019-users.md` | YC office-hours mechanics; recurring startup problems; focus and near-term action. |
| Do Things that Don't Scale | `sources/paul_graham_essays/markdown/079-ds.md` | Manual recruiting, delight, concierge work, contained fire, avoiding big-launch thinking. |
| Startup = Growth | `sources/paul_graham_essays/markdown/083-growth.md` | Weekly growth rate, metric choice, growth as decision compass. |
| How to Get Startup Ideas | `sources/paul_graham_essays/markdown/081-startupideas.md` | Organic ideas, founder-user fit, reachable early users. |
| Organic Startup Ideas | `sources/paul_graham_essays/markdown/107-organic.md` | Ideas that emerge from real need rather than brainstorming. |
| Before the Startup | `sources/paul_graham_essays/markdown/075-before.md` | Counterintuitive traps, knowing users, avoiding startup theater. |
| How to Start a Startup | `sources/paul_graham_essays/markdown/193-start.md` | Fundamentals, users, frugality, persistence. |
| Startups in 13 Sentences | `sources/paul_graham_essays/markdown/127-13sentences.md` | Compact operating checklist. |
| Default Alive or Default Dead? | `sources/paul_graham_essays/markdown/063-aord.md` | Runway, burn, fundraising dependence, hiring restraint. |
| The Fatal Pinch | `sources/paul_graham_essays/markdown/073-pinch.md` | Slow growth + high burn + hope of fundraising. |
| Ramen Profitable | `sources/paul_graham_essays/markdown/116-ramenprofitable.md` | Survival, optionality, low burn. |
| How Not to Die | `sources/paul_graham_essays/markdown/151-die.md` | Persistence, morale, not drifting into failure. |
| The 18 Mistakes That Kill Startups | `sources/paul_graham_essays/markdown/163-startupmistakes.md` | Failure modes and startup-killing patterns. |
| The Hardest Lessons for Startups to Learn | `sources/paul_graham_essays/markdown/171-startuplessons.md` | Counterintuitive lessons founders resist. |
| What We Look for in Founders | `sources/paul_graham_essays/markdown/098-founders.md` | Founder qualities, resilience, clarity. |
| Relentlessly Resourceful | `sources/paul_graham_essays/markdown/122-relres.md` | Founder behavior under constraints. |
| A Word to the Resourceful | `sources/paul_graham_essays/markdown/090-word.md` | Resourcefulness as YC-style selection/operation. |
| Schlep Blindness | `sources/paul_graham_essays/markdown/091-schlep.md` | Painful but valuable work founders avoid. |
| The Airbnbs | `sources/paul_graham_essays/markdown/037-airbnbs.md` | Listening, persistence, manual marketplace work. |
| Subject: Airbnb | `sources/paul_graham_essays/markdown/095-airbnb.md` | Founder persistence and early traction narrative. |
| How to Raise Money | `sources/paul_graham_essays/markdown/076-fr.md` | Fundraising process and investor dynamics. |
| How to Convince Investors | `sources/paul_graham_essays/markdown/078-convince.md` | Investor persuasion and clarity. |
| A Fundraising Survival Guide | `sources/paul_graham_essays/markdown/134-fundraising.md` | Fundraising without letting it consume the company. |
| How to Present to Investors | `sources/paul_graham_essays/markdown/165-investors.md` | Pitching effectively. |
| Don't Talk to Corp Dev | `sources/paul_graham_essays/markdown/069-corpdev.md` | Avoiding acquisition/partnership distraction. |
| The Top Idea in Your Mind | `sources/paul_graham_essays/markdown/105-top.md` | Founder focus and cognitive priority. |
| Founder Mode | `sources/paul_graham_essays/markdown/008-foundermode.md` | Founder-led intensity, especially post-PMF or scaling. |

## YC official/current sources

Use official YC pages for current program mechanics because these facts can change.

| Source | Local note | Best used for |
|---|---|---|
| YC: What Happens at YC | `yc_program/00_how_yc_works.md` | Batch structure, office hours, groups/sections, Demo Day, first customers, community. |
| YC Standard Deal | `yc_program/program_resources.md` | Current funding/deal mechanics. |
| Startup School | `yc_program/startup_school.md` | Curriculum, accountability, cofounder matching, weekly updates. |
| YC Library | `sources/yc_library_seed_index.md` | Expanding topic notes and source coverage. |

## How to use this matrix during a live session

1. Copy the founder's exact complaint.
2. Pick the closest row.
3. Add one row for the suspected underlying problem.
4. Pull the primary sources.
5. Ask the questions before giving advice.
6. Convert the principle into a deadline-bound assignment.
7. Record the selected sources in `templates/session-summary.md`.
