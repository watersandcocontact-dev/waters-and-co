---
name: monday-brief
description: Produces a one-page ranked "what needs you today" briefing by reading connected data sources — pipeline, deadlines, cash. Use when asked for a Monday brief, weekly kickoff, or "what should I focus on." Read-only.
---

# Monday Brief

## When to use
Trigger on: Monday brief, weekly kickoff, what's on today, morning briefing.

## Workflow
- [ ] 1. Pull today's/this week's actionable items, ranked by whatever the project's own
      priority metric is (e.g. $/hr, deal size, urgency)
- [ ] 2. Pull anything with a deadline in the next 14/30 days
- [ ] 3. Pull any pending financial items (invoices due, budget status)
- [ ] 4. Synthesize into ONE page: top 3-5 things to act on today, ranked, one line each
- [ ] 5. Note anything that needs a decision only the human can make — flag, don't guess

## Output format
Terse. A ranked list, not a report. Each line: what it is, why it matters (one clause), link
to act on it. No preamble, no "I hope this finds you well."

## Boundaries
- Read-only — this skill never drafts, sends, or changes anything. Safe to schedule
  fairly early since there's no send-risk, but still verify the first few runs.
