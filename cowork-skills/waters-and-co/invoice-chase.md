---
name: waters-co-invoice-chase
description: Drafts payment reminder emails for Waters & Co clients with pending Stripe payment requests, calibrated to how overdue they are. Use when asked to chase payments or follow up on invoices. Drafts only — never sends.
---

# Waters & Co — Invoice Chase

## When to use
Trigger on: chase payments, overdue invoices, who hasn't paid, payment reminders.

## Input (manual hand-off required)
Same limitation as stale-lead-revival — Cowork can't reach the local hub directly.
Paste in each lead's Payments table (visible on the lead's detail page in ops-hub):
description, amount, status, requested date, and the lead's name/contact_email.
Only `pending` rows matter here — `paid` ones need no action.

## Workflow
- [ ] 1. From the pasted data, find `pending` payment requests and how many days old
      each is (today's date minus the "Requested" date)
- [ ] 2. Rank by amount x days-pending
- [ ] 3. Draft one reminder per pending payment: reference the actual description
      (e.g. "Deposit — 50%", "Final balance") and business line, include the amount,
      and — since these are Stripe Checkout links, not attached invoices — ask Chris
      to note whether the original Checkout link is still valid or needs regenerating
      (Stripe Checkout Sessions expire; check before assuming the old link still works)
- [ ] 4. Tone matched to days pending: under 7 days = friendly nudge, 7-14 = clear
      reminder, 14+ = firmer but still professional (most non-payment is an overlooked
      email, not bad faith)
- [ ] 5. Save as Gmail DRAFT only
- [ ] 6. Output a ranked table: lead / description / amount / days pending / draft link

## Copy rules
- Warm until it can't be. One ask. Make paying effortless — the amount and what it's
  for should be obvious in the first two sentences.
- Don't reference "invoice #" language — these are Stripe Checkout payment requests,
  call them that.

## Boundaries
- Never send. Double-check the payment hasn't already flipped to `paid` since the
  data was pasted (webhook confirmation can lag slightly) before drafting — ask Chris
  to re-check the live page if the paste is more than a day old.
