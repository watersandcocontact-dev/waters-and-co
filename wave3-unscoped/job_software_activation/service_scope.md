# Job-Software Activation — Service Scope

Turning on the automations a trade business is **already paying for and not
using**: automated quote follow-up, booking confirmations and reminders,
"on my way" texts, and automatic invoice chasing inside ServiceM8. The
software is not the product — the configuration is. Sold to the same
trades/SME base as GBP, ReviewGen and MissedCall, in the same
setup-plus-optional-management shape those lines already use.

**Scored 33/35 on 2026-08-10** (see `opportunity_scan/candidates_log.md`) —
the highest total any candidate has scored. No licence, registration or
qualification is required to deliver it; it sits in the same
low-regulatory class as Crypto Literacy and AI Tools for Business, not the
held NDIS/Deceased-Estate/Airbnb lines.

## The open question the Owner needs to settle first

**This may be a productised package under an existing line rather than a
new line.** `AIToolsBusiness` ("set up the tools an SME won't set up
itself") and `AIImplementation` ("$990–4,000 implementation projects for
SMEs") already describe this shape. Three defensible options:

1. **Own line** (`JobSoftware` key) — cleanest to market and to sell cold,
   because the pitch is concrete and vendor-named ("we set up your
   ServiceM8") rather than abstract.
2. **A named package under `AIImplementation`** — the Tier-1 $990–1,490
   band already brackets the full-setup price below, and no new hub
   plumbing is needed. This is the precedent-following option.
3. **A `task_type` split** (`switch-on` / `full-setup`) wherever it lands,
   mirroring the 2026-08-06 Downsizing `coordination`/`labour` split.

**Recommendation: option 2, a named package under `AIImplementation`.**
The 2026-08-09 AI Search Visibility scan reached the same conclusion for
GBP for the same reason — a new key is only worth it when the delivery
work is genuinely different, and here it is not: scoping a business's
workflow, configuring a tool, training the staff and handing over a plan
is exactly what AIImplementation already is. What *is* new and worth
carrying across is the vendor-named pitch, not a new business line.
Flagging rather than deciding. Nothing has been wired into
`ops-hub/app/config.py` either way.

## What's actually delivered

- **Workflow scoping session** — how jobs currently arrive, get quoted,
  get booked, get invoiced, and where they leak. Usually 45–60 minutes.
- **Quote follow-up automation** — the automatic email/SMS that goes out
  when a quote sits unaccepted. This is the single highest-value switch
  for most trades and the one almost nobody turns on.
- **Booking confirmations and reminders** — sent to the customer ahead of
  the job; the no-show/forgotten-appointment fix.
- **"On my way" / ETA texts** — triggered from the job card, the
  complaint-prevention automation.
- **Automatic invoice follow-up** — polite payment chasing on outstanding
  invoices, without the awkward phone call.
- **Templates that sound like the business** — job types, quote and
  invoice templates, and the actual wording of every automated message.
  Default vendor wording is generic; rewriting it is most of the value.
- **Accounting integration connected** (Xero/MYOB/QuickBooks) — connection
  and mapping only, see boundaries below.
- **Staff training + a one-page written handover** — so it survives the
  Owner walking away, same deliverable discipline as every other line.

## Client base and channel reuse

Reuse scores 5 and it is not a stretch:

- **The base is already there.** Every GBP, ReviewGen and MissedCall
  client is a trade business with a job pipeline; so is essentially all of
  the 120-lead cold campaign currently scheduled to send. This is a warm
  follow-on conversation, not a cold sell.
- **The pitch is the same pitch.** MissedCall is "you're losing jobs to
  calls you don't answer." This is "you're losing jobs to quotes you don't
  follow up." Same customer, same problem shape, same objection handling.
- **The delivery shape already exists** — fixed setup fee plus optional
  monthly management is exactly GBP and MissedCall's structure, including
  the `setup`/`management` task-type split already in the hub.
- **No new website segment needed** — belongs under the existing Small
  Business Support / AI Systems for Business segments.

## Market evidence (checked 2026-08-10, all figures fetched live)

The market is **real, priced, contested at the top, and — unusually —
subsidised by the software vendor itself.**

| Who | What | Price found |
|---|---|---|
| **ServiceM8** (the platform, AU) | Free (30 jobs/mo, 1 user), Starter, Growing, Premium, Premium Plus | **$0 / $29 / $79 / $149 / $349 per month**, SMS overage 10c |
| **ServiceM8 Setup & Training Rebate** | Client pays a certified Partner for setup/training, sends ServiceM8 the receipt, gets a **matching account credit up to $2,000**, applied at 50% of plan base price per month until exhausted | vendor-funded |
| **ServiceM8 Partner program** | Self-paced training + certification, partner-directory listing, $500 referral bonuses, **up to 20% ongoing revenue share** | no joining fee stated |
| **Growth Local** (certified AU partner) — Starter Pack | Account setup, ≤3 users, 1 quote/invoice template, 5 job categories, 1 enquiry form, 60min training, 14 days support | **$1,250 setup + $197/mo** |
| **Growth Local** — Growth Pack | ≤10 users, 15 job categories, accounting integration, 3 enquiry forms, 3 add-ons, 2 training sessions | **$1,870 setup + $297/mo** |
| Other AU partners (Maximum Efficiency, WorkM8 Consulting et al.) | Certified setup/training/automation | rates not published — partners set their own |
| Adjacent AU tradie automation (LUNA Systems, TradieAus) | Monthly automation subscriptions | **$26–$349/mo** |

**What the shape of that table means.** Every automation in the delivered
list above is bundled into *every* ServiceM8 plan, including the free one.
Nothing is being resold. The gap is entirely the configuration layer —
and the evidence that the gap is real, rather than assumed, is that
**ServiceM8 will pay up to $2,000 of a client's setup bill to get it
closed**. A vendor does not subsidise a service that its customers are
managing on their own.

The contest is at the top of the price range: $1,250–1,870 setup puts the
incumbents out of reach of a one-to-three-person crew, which is precisely
the segment this business already talks to. That is where the room is, and
it is why market gap was scored 3 rather than 5 — occupied, but not at
this end.

**The honest differentiator is the warm base and the price point, not
novelty.** Growth Local has to buy every customer cold and price a
dedicated account manager into $297/mo. Selling an activation to someone
who already pays for GBP has neither cost.

## Boundaries (don't cross these)

- **Get certified before selling it.** The rebate that makes this an easy
  yes for the client is explicitly a *Partner* rebate — pitching it
  without holding partner certification would be selling a benefit that
  cannot be delivered. Certification is self-paced and no joining fee is
  stated on the partner page, but *no stated fee is not the same as
  confirmed free* — verify before quoting anyone.
- **These are transactional messages to the client's own customers, and
  they must stay that way.** Quote follow-ups, booking reminders and
  invoice notices go to people who asked for a quote or booked a job.
  Turning any of it into promotional or list-based messaging puts the
  client on the wrong side of the Spam Act 2003 consent and
  unsubscribe rules — the same discipline applied to the business's own
  cold-email compliance work on 2026-08-09. If a client asks for
  marketing blasts, that is a different conversation with different rules.
- **Connect the accounting integration; do not operate it.** Mapping
  ServiceM8 to Xero/MYOB is configuration. Reconciling, coding
  transactions or touching a BAS is the Bookkeeping line's boundary and
  the TPB line — do not drift across it because the integration screen
  happens to be open.
- **Never hold the client's ServiceM8 billing or payment details.** Set up
  under their own account and their own card, same rule as every other
  line.
- **Don't promise a conversion-rate number.** "Automated follow-up
  recovers jobs you'd otherwise lose" is a mechanism, not a measured
  outcome for this client. Sell the switch-on, not a percentage — the
  same discipline as the AI Search Visibility line's no-rankings rule.

## What's out of scope

- Migrating historical job/customer data from another system — real work,
  quoted separately, not bundled into an activation fee
- Ongoing bookkeeping, invoicing or debtor management for the client
- Custom app/API development against the ServiceM8 developer platform
- Other platforms (Tradify, simPRO, AroFlo, Fergus). **Only ServiceM8 was
  researched for this draft** — the same model very likely applies to
  Tradify, but that is an assumption and is deliberately not claimed here.
  Extend only after a real ServiceM8 delivery.

## Status

**DRAFT 2026-08-10 — not validated by delivery, not wired into the hub.**
Competitor and vendor figures are live-fetched, but no partner
certification has been completed, no client has been quoted, and nothing
has been delivered. Deliberately NOT added to `ops-hub/app/config.py`
BUSINESS_LINES, `PRICING.md`, or the public website — settle the
own-line-vs-AIImplementation-package question above first, and complete
the partner certification before anything is offered to a client.
