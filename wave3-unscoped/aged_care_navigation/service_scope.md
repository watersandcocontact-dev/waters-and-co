# Aged Care Navigation (My Aged Care / Support at Home) — Service Scope

Getting an older person **into** the aged care system correctly and quickly:
registering with My Aged Care, preparing them for the assessment that decides
their priority category, and lodging the paperwork. Delivered in-home,
reusing the Tech Concierge / Downsizing / Pension client base and the
existing in-home booking flow.

**This is paperwork-and-preparation, not placement and not advice.** Two
things it is deliberately *not*, and the reasons are structural, not
cosmetic — see Boundaries:

1. **Not residential placement broking.** That is what the Perth incumbents
   sell, and several of them are on the current referral-partner list.
2. **Not aged care financial advice.** RAD vs DAP, means-tested fees, whether
   to sell or rent the family home — that is AFSL territory, the same
   boundary the Pension and Crypto Literacy lines already hold.

**Recommended shape: a scope extension / `task_type` on the existing
Pension line, not a new business line.** Reasoning in the Channel conflict
section — this is the single most important thing on this page and it is a
call for the Owner to confirm either way. Nothing has been wired into
`ops-hub/app/config.py`.

## What's actually delivered

- **My Aged Care registration** — creating the record, getting the referral
  code, making sure the online account actually works and the family can
  get back into it
- **Assessment preparation** — the highest-value hour in the whole service.
  A single assessment conversation sets the **priority category (Urgent /
  High / Standard)** and which service types get approved. Families
  routinely under-describe need on the day ("I'm managing fine, dear"), and
  the assessor can only record what they're told. Deliverable is a written,
  plain-English prompt sheet: a worked list of what the person actually
  struggles with — showering, stairs, meals, medication, driving, falls in
  the last 12 months — in the assessor's own terms, ready to hand over
- **Support-person attendance** — being in the room (or on the call) during
  the assessment so nothing gets skipped or minimised, and taking notes
- **Application and paperwork lodgement** — the forms, the supporting
  documents, the follow-up calls to My Aged Care when nothing happens
- **Provider shortlist** — once funding is assigned, a comparison of
  Support at Home providers actually taking clients in the person's suburb,
  with published pricing side by side. Comparison only, no commission, no
  preferred provider
- **Written handover pack** — what was lodged, what happens next, what the
  expected wait looks like, who to chase and when

## Client base and channel reuse

Same seniors and same adult children already booking Tech Concierge and
Downsizing, and the same Services-Australia-paperwork shape the Pension
line already runs. The trigger event is nearly always a fall, a hospital
discharge, or a partner's death — which is precisely the moment a
Downsizing enquiry also arrives. Same in-home visit, same booking flow,
same lead form, same buyer (the adult child, aged roughly 50-65, who pays).

## Market evidence (checked 2026-08-12)

**The backlog is the demand signal, and it is very large.** Figures below
are from aged-care industry press reporting on departmental data, gathered
via search — **secondary sources, not primary releases fetched directly.
Re-verify against health.gov.au / the GEN Aged Care Data site before any
of these numbers goes in front of a client.**

| Figure | Reported value |
|---|---|
| Waiting for Support at Home (30 Jun 2026) | **106,977**, up 13% |
| Waiting for an aged care assessment (31 Mar 2026) | **98,606** |
| Average wait for an initial assessment | **27 days** (up from 22) |
| Average application → services starting | **~306 days** |
| Entering system → accessing home support | **245 days** (up from 118 in 2023-24) |

Context: the Aged Care Act 2024 and the Support at Home program commenced
**1 November 2025**, and the transition itself is what produced the surge
in complaints and delays. That recency is the "why now" — and also why
criterion #5 (learnable) scored 4 and not 5: the rules genuinely moved
nine months ago and are still settling.

**The market is contested, not empty** — same finding shape as the AI
Search Visibility row:

- **ApplyWise** (national) sells the *identical* slice at **$595** — "help
  navigating My Aged Care and applying for a Home Care Package" — plus
  **$1,795+** for full residential placement. Direct proof people pay for
  exactly this. (Note their copy still says "Home Care Package," the
  pre-November-2025 program name — a possible staleness signal, worth a
  look before treating their offer as current.)
- **Free, provider-commission-funded services exist** (CareAbout, Aged Care
  Decisions and similar): the aged care home pays a referral fee, so the
  family pays nothing. Structurally these monetise **residential
  placement** — they have no revenue model for the home-care/assessment
  stage, which is exactly where the 100,000-person backlog sits. That gap
  is the wedge, and it is the reason the market-gap criterion scored 3
  rather than 1.
- **Perth fee-for-service consultants already operating**: RELACS
  (Stirling — fee-for-service, explicitly "no commissions or referral fees
  from care providers" in their own copy), Simpatica (Perth/Mandurah/South
  West), Care Match Solutions, All About Aged Care.
- Broad AU range for a full private consultant engagement: **$2,000-$4,000**,
  with some fixed offers around **$550-$595**.

## Channel conflict — read before building anything

**As of 2026-08-12 there are 18 outreach emails sitting as unsent Gmail
drafts, scheduled to go out the morning of 2026-08-13, to aged-care
financial advisers and placement consultants — including RELACS in
Stirling, Perth.** Every one of them positions Waters & Co as the
*complementary* partner: "paperwork and process only, no financial or
investment advice — a clean complementary handoff once your strategy work
is done." See `wave3-unscoped/lead_generation/offers/pension_referral_partners_batch2_2026-08-12.md`
and the 2026-08-12 entries in `DECISIONS.md`.

Standing up an aged care navigation **line** would make Waters & Co a
competitor to the firms being pitched as partners tomorrow morning. RELACS
in particular is a Perth placement consultant — a direct competitor if this
launched as a placement/advisory offer.

This does **not** kill the opportunity. It defines it:

- **Compatible** — assessment prep, My Aged Care registration, application
  lodgement, chasing. This is *literally what the referral emails already
  promise to do*. Delivering it strengthens the partner pitch rather than
  contradicting it, and gives the partners something concrete to hand off.
- **Incompatible** — residential placement broking, RAD negotiation,
  means-tested-fee strategy, "which home should Mum go into." Doing any of
  these turns 18 prospective partners into 18 competitors, and the referral
  flow that makes the Pension line work stops before it starts.

The referral then runs **both ways**: they hand us the paperwork, we hand
them the money questions we're not allowed to answer anyway.

## Boundaries (don't cross these)

- **No financial product advice.** RAD vs DAP, means-tested care fees,
  whether to keep/rent/sell the home, funeral bonds, income-stream
  structuring — all out. Point at the government's own fee estimator and
  refer to an accredited aged care financial adviser. Same boundary as
  Pension, Crypto Literacy and Lost Super.
- **Never promise to shorten the queue.** The reported average is ~306 days
  application-to-service and nothing a private consultant does changes the
  national waitlist. What preparation genuinely affects is the **priority
  category and the approved service types** — say that, and only that. A
  "we'll get you seen faster" claim is both false and the fastest way to a
  complaint.
- **The family stays the My Aged Care representative.** Prepare them, sit
  with them, take the notes — don't take over the formal representative
  role for a fee. Same shape as the Digital Legacy "never take custody of
  credentials" rule.
- **No commissions, ever, from any provider.** The moment a provider pays
  us, the shortlist stops being a comparison and the partner pitch becomes
  dishonest. Client-paid only.
- **Not a registered aged care provider and doesn't need to be** — checked
  2026-08-12: registration under the Aged Care Act 2024 attaches to
  entities *delivering Commonwealth-funded aged care services and receiving
  the subsidy*. We deliver no care and receive no subsidy. Corroborated by
  the fact that ApplyWise, RELACS, Simpatica and others operate this way
  openly. **This rests on secondary/summary sources, not a fetched primary
  regulator page** — the ACQSC and health.gov.au pages both failed to load
  during this scan (DNS/timeout, not a block). Confirm directly against
  agedcarequality.gov.au before the first paying client.
- **No clinical or care judgements.** We are not assessing anyone's health,
  capacity, or safety. Describing what a family reports is in scope;
  forming a view on whether someone can still live alone is not.
- **If the person has died and an estate process is underway** — that's the
  held Deceased-Estate Admin territory. Hand off, don't blur.

## What's out of scope

- Residential aged care placement, facility tours, RAD negotiation (see
  Channel conflict — this is the partners' business, not ours)
- Delivering any actual care, personal support, or domestic assistance
- Acting as an ongoing case manager or care coordinator after lodgement
- Appeals against a care-needs assessment outcome (different from a
  Centrelink ARO review — do not assume the Pension line's review process
  transfers here without checking it)
