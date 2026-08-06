# PRICING.md — Rate Card & $/hr Reference (drives the Daily Queue sort)

**Source:** pasted by the user on 2026-07-30. These are planning estimates
based on typical Australian small-service pricing, not quotes — adjust as
real client data comes in. The hub recalculates actual $/hr per lead
automatically once real time-tracking data exists (see `ops-hub/app/config.py`
`RATE_CARD` and `models.py` `dollar_per_hour()`), falling back to these
defaults until then.

**Reconciliation note:** where this table's numbers differ from the more
detailed pricing sheets already built for GBP and MissedCall
(`wave1/gbp/pricing_sheet.md`, `wave1/missedcall/pricing_sheet.md`), the
pricing sheets remain the authoritative *client-facing quote* (per your "keep
ur pricing" instruction) — e.g. MissedCall setup is quoted at $300-600 in the
pricing sheet, not the $100-300 implied here. This table's **$/hr figures**
still drive queue sorting either way, since they're closer to your actual
time cost either way and that's what this table is for.

**Update 2026-07-30:** ReviewGen and LandTax now have their own pricing
sheets too (`wave1/reviewgen/pricing_sheet.md`, `wave1/landtax/pricing_sheet.md`),
built from real AU competitor research (`docs/competitor_pricing_research.md`)
rather than this table's rough estimates — those are now the authoritative
client-facing quotes for those two lines, same status as GBP/MissedCall.

**Update 2026-08-01 — CONFIRMED for the website:** re-ran competitor checks
(`docs/competitor_pricing_research.md`'s "Re-verification — 2026-08-01"
section) for the 4 business lines actually live on the public website — GBP,
ReviewGen, MissedCall, LandTax. All four hold as-is and are now marked
**Status: CONFIRMED 2026-08-01** in their own pricing sheets; the numbers in
`website/webapp/config.py` already match them exactly. One market move
found and logged (Starworks reputation-management SaaS repriced down to
$49-135/mo) — didn't change our price, but does sharpen how ReviewGen needs
to be pitched (managed service vs. self-serve tool, not price alone). The
other 17 business lines below are priced for internal queue-sorting only —
none are on the website yet.

**Business-line scope note:** rows 1, 3, 5, 8, 9, 10, 11 map to the 8
businesses already fully built (Wave 1 + Wave 2 prep). Rows 2 (land tax,
already built) plus rows 7, 12–19 introduce **9 businesses with no prior
build spec** — see DECISIONS.md's 2026-07-30 entry. They're wired into the
hub's schema/rate-card/queue now so they can receive leads and be ranked, but
none of their service-delivery assets (audit tools, templates, state
research, etc., the way GBP/LandTax/etc. got) have been built — that's a
separate, much larger task if/when you want to actually launch them.

**Update 2026-08-06 — real competitor research for the 12 lines that had no
sourced pricing (only rough planning estimates or, for 8 of them, an
explicitly-marked "draft/assumption" `pricing_sheet.md`):** ran real web
research (not memory) for Bookkeeping, Concession, GrantFinder, Pension,
TechConcierge, VideoRepurpose, Downsizing, LostSuper, CryptoLiteracy,
AIToolsBusiness, DigitalLegacy, and PhotoDigitisation. Nine now hold
sourced, confirmed numbers (marked `Status: CONFIRMED 2026-08-06` in their
own pricing sheets). Two structural findings, not just price changes:
**Concession/rebate navigation has no viable standalone paid market** — no
AU competitor found, and it's covered by free government/charity channels —
re-classified as a free bundled add-on, not sold on its own. **Senior
downsizing genuinely splits into two different services** — coordination-only
(no physical labour, $45-65/hr) vs hands-on labour ($50-80/hr, unchanged) —
different liability/insurance profile, not just a price tier, so it's now
`Downsizing` with a `coordination`/`labour` task-type split in the hub,
matching the GBP/MissedCall pattern. AIToolsBusiness's existing bands were
checked and confirmed unchanged. Also added `AIImplementation`,
`RealEstateLeads` (validated 2026-08-01, added to the website 2026-08-06),
`DigitalLegacy`, and `PhotoDigitisation` as full rows for the first time.
Full sourcing for every figure is in DECISIONS.md's 2026-08-06 entry and each
line's own `pricing_sheet.md`.

## Full table (2026-08-06 update — see note above)

| Rank | Business | Hub `business_line` key | Typical price per job/case | Time per job | Est. $/hr |
|---|---|---|---|---|---|
| 1 | Review generation (ongoing) | `ReviewGen` | $50–100/mo per client | ~15 min/mo active work | **$200–400/hr** |
| 2 | Land tax/rates objection | `LandTax` | $175–525/case (25–50% of ~$500–1,500 saving) | ~60–75 min/case | **$140–420/hr** |
| 3 | AI missed-call (monthly mgmt) | `MissedCall` (task type: management) | $100–200/mo per client | ~20–30 min/mo | **$200–400/hr** |
| 4 | AI missed-call (setup, one-off) | `MissedCall` (task type: setup) | $100–300/client | ~2–3 hrs | **$40–100/hr** |
| 5 | GBP/GEO (monthly mgmt) | `GBP` (task type: management) | $100–200/mo per client | ~40 min/mo | **$150–300/hr** |
| 6 | GBP/GEO (one-off cleanup) | `GBP` (task type: setup) | $150–300/client | ~2–3 hrs | **$60–100/hr** |
| 7 | Lost super/TPD navigation (referral fee) | `LostSuper` | Free to client (ATO search); $200–800/referred case, model confirmed 2026-08-06 but **exact $/case still unconfirmed** — needs a real partner agreement (Claimsplus is the natural first call) | ~30–45 min | **$270–1,000+/hr** (high but infrequent, and unconfirmed) |
| 8 | Concession/rebate navigation | `Concession` | **Re-classified 2026-08-06: not a viable standalone paid line** — two search passes found zero AU businesses charging for this; covered by free channels (Service NSW, financial counsellors) and several rebates now auto-renew once a concession card is on file. Fold into Tech Concierge/Downsizing visits as a free value-add. | ~15–20 min if bundled | **$0–25/visit if ever charged at all — do not sell standalone** |
| 9 | Bookkeeping (monthly retainer) | `Bookkeeping` | **CONFIRMED 2026-08-06**: $149–179/mo micro (0–25 txns), $299–449/mo small (25–100 txns) — undercuts Advancr's $249/mo entry tier | ~2–3 hrs/mo | **$60–95/hr** |
| 10 | SME grant-finder (flat report) | `GrantFinder` | **CONFIRMED 2026-08-06**: $79–99 flat (sweet spot $89) for a curated shortlist + eligibility pre-check — was priced as a $300–1,000+ success fee, real market is a one-off flat report undercutting The Grants Hub ($313–486/yr) and GrantHelper ($149/yr) | ~1–2 hrs | **$45–90/hr** |
| 11 | Age Pension/Centrelink assistance | `Pension` | **CONFIRMED 2026-08-06**: $349 flat (new claim), $249 flat (ARO review), disclosed up front — undercuts My Age Pension's $660+ package and beats their $132/hr-with-$396-minimum-even-if-ineligible clause | ~1.5–2 hrs | **$125–235/hr** |
| 12 | Deceased-estate admin | `DeceasedEstate` *(new, unscoped)* | $50–80/hr or $500–1,500/estate flat | ~5–7 hrs/wk/active estate | **$50–80/hr** |
| 13 | Senior tech concierge | `TechConcierge` | **CONFIRMED 2026-08-06**: $70–85/hr in-person, $55–65/hr remote — verified against My Senior IT (~$100/hr-equiv), Geeks2U ($158–198/hr), IT 4 Retirees ($162/hr+$73/hr travel) | ~1 hr | **$55–85/hr** |
| 14 | Grant writing (nonprofit) | `GrantWriting` *(new, unscoped)* | $500–2,000/grant | ~3–4 hrs total | **$130–500/hr** (lumpy, needs portfolio first) |
| 15 | NDIS plan navigation | `NDISNav` *(new, unscoped)* | $60–90/hr typical, or capped fee | ~7–9 hrs/wk ongoing | **$60–90/hr** |
| 16 | NDIS provider compliance/audit-prep | `NDISCompliance` *(new, unscoped)* | $70–120/hr or $1,500–3,000/audit package | ~4–6 hrs/audit cycle | **$70–120/hr** |
| 17 | Video/podcast repurposing | `VideoRepurpose` | **CONFIRMED 2026-08-06 (medium confidence)**: $249/episode for a 10-clip package, $199/episode on a 4-episode/mo subscription — undercuts agency retainers ($800–3,000+/mo); On Replay's real current price couldn't be verified (site blocked automated access), so treat this figure as reasonable, not fully pinned down | ~5–7 hrs/episode | **$28–50/hr** |
| 18 | Senior downsizing — coordination only | `Downsizing` (task type: coordination) | **Split into two tiers 2026-08-06** — no physical labour, liaising with removalists/cleaners/charities/agents only: $45–65/hr, or $400–1,200 packaged flat quote (vendor costs pass through to client) | ~2–4 hrs/job | **$45–65/hr** |
| 18b | Senior downsizing — hands-on labour | `Downsizing` (task type: labour) | **$80/hr flat (set 2026-08-06, Owner's call)** — was a $50-80/hr range; real AU competitor pricing for this specific split is genuinely unpublished (Care to Move, Home Moving Planners, We Move It are all quote-only) | ~4–6 hrs/job day | **$80/hr** |
| 19 | Airbnb co-hosting | `AirbnbCohost` *(new, unscoped)* | 10–25% of nightly revenue | ~5–7 hrs/wk/listing (with automation) | **$30–60/hr equivalent** |
| 20 | Crypto IT/Literacy (live session) | `CryptoLiteracy` (task type: session) | **CONFIRMED 2026-08-06**: $85/hr 1:1, $59/head or $349 flat (private group up to 8) — verified against AusBlock ($150/hr), Superprof generalist tutors ($29–45/hr avg) | ~1 hr | **$85–90/hr** |
| 21 | Crypto IT/Literacy (pre-recorded course) | `CryptoLiteracy` (task type: course) | built once, sold repeatedly | n/a — near-zero marginal delivery | **$300/hr equivalent** |
| 22 | AI Tools for Business | `AIToolsBusiness` | **CONFIRMED 2026-08-06, unchanged**: $200–350 basic / $400–600 standard one-off, $80–150/mo optional support — real Fiverr gigs ($10–95) and AU AI-consultant rates ($150–450/hr) both support the existing bands as-is | varies | **$85/hr** |
| 23 | Odd Jobs / gig marketplace | `OddJobs` | per-job, highly variable (Airtasker/Marketplace-style) | varies | **$50/hr** (rough default — override per-lead with the real quoted price/time) |
| 24 | AI Implementation for SMEs | `AIImplementation` | $990–1,490 single automation build, $2,500–4,000 multi-step system, $150–250/mo optional retainer — validated 2026-08-01, live on the website | ~3–8 hrs/client | **$225/hr** |
| 25 | AI Lead-Response — Real Estate Agents | `RealEstateLeads` | $129–199/mo flat, managed service — validated 2026-08-01 "GO WITH CAVEATS", US/UK/Canada remote-deliverable, live on the website | ~20–30 min/mo | **$390/hr** |
| 26 | Digital Legacy / Account Organiser | `DigitalLegacy` | **CONFIRMED 2026-08-06**: $120–150 Starter (~1.5hr), $250–320 Full inventory (~3hr), $80–100 Annual refresh (~1hr) — genuinely thin market, only one direct AU competitor found (Digital Care Services Australia) and even they don't publish a price | ~1–3 hrs | **$80–107/hr** |
| 27 | Photo & Memory Digitisation Concierge | `PhotoDigitisation` | **CONFIRMED 2026-08-06**: NOT a per-photo pricing menu — bulk scanning is commoditised (25–70c/photo, $24–35/tape across 7+ national bureaus); charge a coordination/curation fee on top of the bureau's pass-through cost | varies | **~$55/hr coordination fee** |
| — | General Enquiry (website catch-all) | `GeneralEnquiry` | n/a — not a priced service, a triage bucket for unclassified website enquiries | n/a | **$0/hr by design** — reclassify to a real business line once triaged |

*(27 numbered rows + 1 unnumbered (+ an 18b split), 25 distinct hub business lines. Rows 3/4 both MissedCall, 5/6 both GBP, 18/18b both Downsizing, 20/21 both CryptoLiteracy — split by task type since the sub-modes have very different $/hr. Rows 20-23 added 2026-08-01; rows 24-27 added 2026-08-06 alongside the real-competitor-research pass on rows 7-11, 13, 17, 18/18b, 20, 22 — see the update note above and DECISIONS.md for full sourcing.)*

## How the hub uses this

- `ops-hub/app/config.py` `RATE_CARD` stores a default $/hr per business line
  (and per task-type for GBP/MissedCall) taken as the midpoint of the range
  above.
- Every lead gets a computed `$/hr`: **actual hours logged** (once you start
  time-tracking a case) > **your own per-lead estimate override** > **this
  rate card's default** — in that priority order. See `models.py:dollar_per_hour()`.
- The Daily Queue (hub home page) sorts today's actionable items by this
  computed $/hr, highest first, full stop.
- Re-rank weekly once real client data exists — these are starting
  estimates, not fixed. Nothing about the sort order is hardcoded to this
  table; it's just today's default.
