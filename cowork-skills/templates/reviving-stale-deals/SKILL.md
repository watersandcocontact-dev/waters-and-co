---
name: reviving-stale-deals
description: Scans Gmail sent mail and Google Calendar for prospects who have gone quiet past a threshold and drafts personalized re-engagement emails as Gmail drafts. Use when asked to revive stale deals, chase non-responders, or prep follow-ups. Drafts only — never sends.
---

# Reviving Stale Deals

## When to use
Trigger on: stale deals, dead deals, no-reply prospects, re-engagement, follow-up sweep.

## Inputs
- Gmail sent folder (last 90 days) + relevant threads
- Google Calendar (past meetings = deal context; find last real interaction)

## Workflow
- [ ] 1. Identify threads I sent with no reply in 30/45/60/90 days
- [ ] 2. For each, one-sentence summary of what stalled + last real touch date
- [ ] 3. Classify: revive / archive / escalate
- [ ] 4. For "revive," draft ONE re-engagement email per the copy rules below (see `reference/templates.md`)
- [ ] 5. Save as Gmail DRAFT only. Never send.
- [ ] 6. Output a review table: contact / days quiet / stall reason / angle used / draft link

## Copy rules
- No "just checking in." Every draft needs a specific new angle.
- Reference concrete past context (their words, the meeting, the original objection).
- One CTA only. Plain text. Under ~100 words unless context demands more.
- Quote only from the actual thread; if a detail is unknown, leave a [BRACKET] for the human to fill in — never invent specifics.
- Match message type to how quiet they are — see `reference/templates.md` for the 4-touch sequence.

## Boundaries
- Never send, delete, or mark read. Human approves every send.
- Archive non-responders after the full sequence (~4-5 touches) — continuing to email harms deliverability.
