---
name: invoice-chase
description: Reads overdue/pending invoices, ranks them, and drafts a payment reminder per customer calibrated to their payment history and how overdue they are. Use when asked to chase invoices, follow up on payments, or prep reminder emails. Drafts only — never sends.
---

# Invoice Chase

## When to use
Trigger on: overdue invoices, chase payments, payment reminders, who hasn't paid.

## Workflow
- [ ] 1. Pull pending/overdue payments (source varies by project — see project-specific version)
- [ ] 2. Rank by amount + days overdue
- [ ] 3. For each, check the customer's own payment history — reliably-on-time payers get a
      friendly nudge, repeat-late payers get a firmer (but still professional) tone
- [ ] 4. Draft one reminder per overdue customer, matched to the escalation stage:
      3-5 days before due (friendly heads-up) -> due date (reminder) -> 7/14/30/60 days
      overdue (progressively firmer, still warm — most late payment is forgetfulness,
      not bad faith)
- [ ] 5. Include: invoice reference, amount, due date, and a payment link if one exists
- [ ] 6. Save as Gmail DRAFT only. Never send.
- [ ] 7. Output a ranked review table: customer / amount / days overdue / tone used / draft link

## Copy rules
- Warm until it genuinely can't be — don't escalate tone prematurely or use accusatory language.
- Make paying effortless — the payment link/reference front and center, not buried.
- One ask per email.

## Boundaries
- Never send. Never chase a payment that's already been marked paid — verify current status
  immediately before drafting, not from a stale snapshot.
