---
name: waters-co-referral-thank-you
description: Drafts a thank-you email to a Waters & Co client whose referral just converted, telling them about the earned discount. Use when a referral bonus becomes pending. Drafts only — never sends.
---

# Waters & Co — Referral Thank-You

## When to use
Trigger on: referral converted, new referral bonus, thank a referrer.

## Input (manual hand-off required)
Paste in the relevant row(s) from the referrer's "Referral & loyalty" box on their
lead page in ops-hub: referrer name, who they referred, which month the bonus
applies to (note if it rolled forward from the conversion month — see below).

## Workflow
- [ ] 1. Draft a short thank-you referencing WHO they referred by name (not "your
      referral") and confirming the bonus
- [ ] 2. If `applies_to_month` differs from the conversion month (i.e. it rolled
      forward because they already had a bonus that month — see
      `ops-hub/app/models.py` `_sync_referral_bonuses` for why), say so plainly:
      "since you've already got one lined up for [earlier month], this one's queued
      for [later month]" — don't hide the rollover, it's a real cap, not a mistake
- [ ] 3. Save as Gmail DRAFT only — Chris applies the actual discount manually when
      creating the client's next payment request

## Copy rules
- Genuine and specific — name the referred client, name the % (50% off, one month,
  per the current `REFERRAL_ONE_TIME_BONUS_PCT` in `app/config.py`).
- Short. This is a thank-you, not a sales email.

## Boundaries
- Never send. Never promise a dollar amount — the % applies to whatever their next
  invoice ends up being, which isn't fixed yet.
