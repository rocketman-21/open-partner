# Growth Ledger

`growth.md` is the append-only record of the weekly growth rate — the number
PG asks for first and the compass for every session. Like `sessions/`, the
convention ships and the contents don't: everything here except this README is
gitignored.

## The rules

- **One best real metric.** Revenue first, active usage second, retained core
  action if neither is ready. Changing the metric is allowed but gets its own
  row and a note saying why — no silent re-basing.
- **At least one row per week.** More often is better; the weekly growth column
  always compares against the entry closest to 7 days prior.
- **The partner writes it.** During office hours, the growth question
  ("what is the current weekly growth rate of the best real metric?") is
  answered by appending a row to `growth.md` — not just discussed. The founder
  can also append rows between sessions whenever there's a fresh number.
- **No row, no narrative.** If the number isn't known, the row says UNKNOWN —
  and finding it usually becomes the session's action item.

## Format (`growth.md`)

```markdown
| Date | Metric | Value | Weekly growth | Notes |
|---|---|---:|---:|---|
| 2026-06-10 | Revenue (MRR) | $1,200 | +8% | first paid annual plan |
```

5–7% a week is good. 10% a week is exceptional. 1% a week means you haven't
figured out what you're doing yet. (`growth.md` exists so you can't avoid
knowing which one you are.)
