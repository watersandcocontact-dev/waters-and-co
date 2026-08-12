# Cold campaign — hard bounce log

Dead addresses discovered after send, recorded by the `campaign-reply-watch`
scheduled task (see `PROGRESS.md` section on that task). These are **hard**
bounces (550 / address not found) — do not re-send to them, and treat the
contact as needing a fresh address before the lead is worth anything.

Cross-reference: `master_send_schedule_2026-08-10.md` (the send schedule),
`tailored_emails_master.md` (the drafted copy).

| Date found | # in schedule | Address | Business | Bounce reason | Subject sent |
|---|---|---|---|---|---|
| 2026-08-11 | 14 | admin@wollongongchiro.com.au | Wollongong Chiropractic | 550 5.1.1 address not found | Your "Ask Dr Browne" page |
| 2026-08-11 | 48 | office@canberrasbestgroup.com.au | Canberra's Best Group (plastering) | 550 5.1.1 address not found | Quick one for Canberra's Best Group |

## Running tally

- Batch sent Tue 2026-08-11 07:30 AWST (QLD/NSW/ACT/VIC/TAS, 76 leads): **2 hard bounces so far.**
- These are on top of the 11 addresses excluded as invalid *before* sending
  (2026-08-10 verification pass).

## What to do with a bounced lead

1. Leave it here — don't delete the row from the send schedule; the schedule is
   the record of what was attempted.
2. If the business is still a genuine fit, re-source a contact address (website
   contact form, GBP listing, phone) before drafting anything new.
3. If no valid address surfaces, drop the lead rather than guessing at
   addresses — guessed addresses hurt sender reputation and are exactly what
   produced these bounces.
