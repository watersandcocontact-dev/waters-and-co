---
name: waters-co-stale-lead-revival
description: Drafts re-engagement emails for Waters & Co leads that have gone quiet (open status, no update in 30+ days). Use when asked to revive stale leads or chase quiet prospects. Drafts only — never sends.
---

# Waters & Co — Stale Lead Revival

## When to use
Trigger on: stale leads, quiet prospects, chase leads, revive deals.

## Input (manual hand-off required)
Cowork can't reach the local ops-hub database directly (it runs on claude.ai, the hub
runs on your machine — same reason scheduled tasks can't touch it either, see
`docs/monitoring.md`). Paste in the relevant rows from `/all` filtered to open leads
(anything not Won/Lost), sorted by `updated_at` oldest-first — or export via
`/tax/export`-style copy if that's easier. Each row needs at minimum: name, business
line, status, next_action, notes, contact_email, updated_at.

## Workflow
- [ ] 1. From the pasted data, identify leads with no update in 30/45/60+ days
- [ ] 2. For each, read `notes` and `next_action` for the actual stall reason —
      don't guess
- [ ] 3. Draft ONE revival email per lead, referencing the SPECIFIC business line and
      whatever was last discussed (from `notes`) — never "just checking in"
- [ ] 4. Match the touch to how quiet they are (see the general
      `templates/reviving-stale-deals/reference/templates.md` for the 4-touch sequence)
- [ ] 5. Save as Gmail DRAFT only
- [ ] 6. Output a table: lead name / business line / days quiet / angle used / draft link

## Copy rules
- Reference the real service (GBP, Land Tax, Missed-Call, etc.) and whatever's in
  `notes` — a generic template defeats the purpose of pasting real data in.
- If `notes` is empty/unhelpful, say so and skip drafting a specific-context email
  rather than inventing one — flag it back to Chris to fill in next_action/notes first.
- One CTA. Plain text. Under 100 words unless the context genuinely needs more.

## Boundaries
- Never send. Never revive a lead currently `On Hold` intentionally (check status is
  actually "gone quiet," not deliberately paused) before drafting.
