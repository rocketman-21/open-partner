# Growth Diagnostic

Use this when growth is unclear, flat, noisy, or based on vanity metrics.

## 1. Pick the real metric

Best metrics, in order:

1. Revenue or paid commitments.
2. Active paying customers/accounts.
3. Retained active users/accounts.
4. Repeated core action.
5. Activation to first value moment.
6. Qualified pipeline, only if sales cycle is long and pipeline quality is strict.

Weak metrics:

- Waitlist size.
- Discord/Twitter followers.
- Token price or speculative volume.
- Press mentions.
- Raw signups without activation.
- One-time usage without retention.
- “Interested” users.

## 2. Calculate weekly growth

```text
weekly_growth = (current_week_metric - previous_week_metric) / previous_week_metric
```

Ask:

- What is the numerator?
- What is the denominator?
- Does this metric represent real user value?
- Can it be gamed?
- Is churn hidden?
- Is the segment narrow enough that growth means something?

## 3. Diagnose the growth bottleneck

| Bottleneck | Signal | Question | Action |
|---|---|---|---|
| No clear ICP | Users are heterogeneous; no one is desperate. | Who is most excited and why? | Narrow segment; interview/recruit only that group. |
| Acquisition | Happy users exist, but few new users arrive. | What produced the last 10 users? | Manual recruiting sprint. |
| Activation | Users sign up but do not reach value. | Where do they drop before first value? | Watch 5 onboardings; remove/concierge blockers. |
| Retention | Users try but do not return. | Who repeats the core action? | Interview retained/churned users; fix repeated-value loop. |
| Monetization | Usage exists but no payment. | Who has budget and urgency? | Ask for paid pilot or conversion. |
| Sales cycle | Prospects like it but deals stall. | What event forces a purchase now? | Define urgency, buyer, next step, close date. |
| Metric quality | Numbers move but behavior is weak. | Would this matter if the dashboard vanished? | Replace vanity metric with behavior/revenue. |
| Founder focus | Lots of work, little movement. | What scary work is being avoided? | Stop-list + one assignment. |

## 4. Apply PG/YC source anchors

- `pg_essays/startup_equals_growth.md` — growth is the compass; know weekly growth rate.
- `pg_essays/do_things_that_dont_scale.md` — early growth usually begins with manual founder effort.
- `pg_essays/what_ive_learned_from_users.md` — isolate the most important problem and create a week-scale measurable action.
- `yc_library_notes/analytics_and_metrics.md` — avoid vanity metrics.
- `yc_library_notes/product_market_fit.md` — distinguish growth from durable user pull.

## 5. The growth session questions

Ask in order:

1. What is the best real metric right now?
2. What was it last week and this week?
3. What created the increase or decrease?
4. Which users/accounts drove the movement?
5. Which user segment is most retained or most urgent?
6. What manual founder action could increase this metric before next session?
7. What are we tempted to do that would not move this metric?

## 6. Growth assignment examples

### Manual recruiting

```md
Hypothesis: Segment X has urgent need Y and will activate if personally onboarded.
Action: Founder manually recruits and onboards 10 named users from segment X.
Metric: Number activated + number repeating core action within 72 hours.
Failure signal: Fewer than 3 activate, or activated users do not repeat.
```

### Activation repair

```md
Hypothesis: Users want the product but fail before first value.
Action: Watch 5 new users onboard without coaching; fix the top blocker.
Metric: Activation rate for next 20 signups.
Failure signal: Same drop-off persists after fix.
```

### Retention repair

```md
Hypothesis: Retained users share a narrower job-to-be-done than our stated ICP.
Action: Interview 5 retained and 5 churned users; rewrite ICP and product promise.
Metric: Repeat core action in target segment.
Failure signal: No consistent difference between retained and churned users.
```

### Revenue conversion

```md
Hypothesis: Current active users have enough value to pay.
Action: Ask 5 active users for paid conversion or paid pilot by a specific date.
Metric: Paid commitments and objections.
Failure signal: No one agrees and objections indicate weak value, not pricing friction.
```
