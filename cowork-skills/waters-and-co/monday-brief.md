---
name: waters-co-monday-brief
description: Produces a one-page ranked briefing from the Waters & Co ops-hub's Daily Queue, deadlines, and pending referral bonuses. Use when asked for a Monday brief or weekly kickoff. Read-only.
---

# Waters & Co — Monday Brief

## When to use
Trigger on: Monday brief, weekly kickoff, what's on today, morning briefing.

## Input (manual hand-off required)
Paste in:
1. The Daily Queue (`/` on the hub) — today's actionable items, already $/hr sorted
2. The deadline alert banner (overdue / due-14 / due-30) from the same page
3. The `/referrals` dashboard — any pending bonuses or margin-floor flags
4. (Optional) the `/expansion` page if budget phase is on

## Workflow
- [ ] 1. Take the Daily Queue as already correctly ranked — don't re-rank it,
      just surface the top 3-5
- [ ] 2. Pull anything overdue or due within 14 days from the deadline banner —
      these outrank everything else regardless of $/hr
- [ ] 3. Note any pending referral bonuses that need applying to an upcoming invoice,
      and any margin-floor flags that need a decision
- [ ] 4. If expansion data was pasted, note anything past its evaluation window
      needing a keep/adjust/kill call
- [ ] 5. Synthesize into ONE page: ranked list, one line each, terse

## Output format
No preamble. Format:
```
TODAY'S TOP MOVES
1. [Lead name] ([business line]) — [next_action] — $[x]/hr
2. ...

DEADLINES
- [Lead name]: due [date] ([overdue/N days])

NEEDS A DECISION
- [whatever needs Chris's call — margin flag, expansion spend, etc.]
```

## Boundaries
- Read-only. Never drafts or sends anything — this is a summary, not an action skill.
