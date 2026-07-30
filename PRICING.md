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

**Business-line scope note:** rows 1, 3, 5, 8, 9, 10, 11 map to the 8
businesses already fully built (Wave 1 + Wave 2 prep). Rows 2 (land tax,
already built) plus rows 7, 12–19 introduce **9 businesses with no prior
build spec** — see DECISIONS.md's 2026-07-30 entry. They're wired into the
hub's schema/rate-card/queue now so they can receive leads and be ranked, but
none of their service-delivery assets (audit tools, templates, state
research, etc., the way GBP/LandTax/etc. got) have been built — that's a
separate, much larger task if/when you want to actually launch them.

## Full table (as provided, highest $/hr first)

| Rank | Business | Hub `business_line` key | Typical price per job/case | Time per job | Est. $/hr |
|---|---|---|---|---|---|
| 1 | Review generation (ongoing) | `ReviewGen` | $50–100/mo per client | ~15 min/mo active work | **$200–400/hr** |
| 2 | Land tax/rates objection | `LandTax` | $175–525/case (25–50% of ~$500–1,500 saving) | ~60–75 min/case | **$140–420/hr** |
| 3 | AI missed-call (monthly mgmt) | `MissedCall` (task type: management) | $100–200/mo per client | ~20–30 min/mo | **$200–400/hr** |
| 4 | AI missed-call (setup, one-off) | `MissedCall` (task type: setup) | $100–300/client | ~2–3 hrs | **$40–100/hr** |
| 5 | GBP/GEO (monthly mgmt) | `GBP` (task type: management) | $100–200/mo per client | ~40 min/mo | **$150–300/hr** |
| 6 | GBP/GEO (one-off cleanup) | `GBP` (task type: setup) | $150–300/client | ~2–3 hrs | **$60–100/hr** |
| 7 | Lost super/TPD navigation (referral fee) | `LostSuper` *(new, unscoped)* | $200–800/referred case | ~30–45 min | **$270–1,000+/hr** (high but infrequent) |
| 8 | Concession/rebate navigation | `Concession` | $80–200/case | ~40–60 min | **$80–200/hr** |
| 9 | Bookkeeping (monthly retainer) | `Bookkeeping` | $150–400/mo per client | ~2–3 hrs/mo | **$60–130/hr** |
| 10 | SME grant-finder (success fee or flat) | `GrantFinder` | $300–1,000+/won grant | ~1.5–2 hrs | **$150–500/hr** (lumpy, cyclical) |
| 11 | Age Pension/Centrelink assistance | `Pension` | $150–400/case | ~1.5–2 hrs | **$75–200/hr** |
| 12 | Deceased-estate admin | `DeceasedEstate` *(new, unscoped)* | $50–80/hr or $500–1,500/estate flat | ~5–7 hrs/wk/active estate | **$50–80/hr** |
| 13 | Senior tech concierge | `TechConcierge` *(new, unscoped)* | $60–100/session | ~1 hr | **$60–100/hr** |
| 14 | Grant writing (nonprofit) | `GrantWriting` *(new, unscoped)* | $500–2,000/grant | ~3–4 hrs total | **$130–500/hr** (lumpy, needs portfolio first) |
| 15 | NDIS plan navigation | `NDISNav` *(new, unscoped)* | $60–90/hr typical, or capped fee | ~7–9 hrs/wk ongoing | **$60–90/hr** |
| 16 | NDIS provider compliance/audit-prep | `NDISCompliance` *(new, unscoped)* | $70–120/hr or $1,500–3,000/audit package | ~4–6 hrs/audit cycle | **$70–120/hr** |
| 17 | Video/podcast repurposing | `VideoRepurpose` *(new, unscoped)* | $300–800/episode | ~5–7 hrs/episode | **$45–115/hr** |
| 18 | Senior downsizing/cleanout | `Downsizing` *(new, unscoped)* | $50–80/hr or project flat fee | ~4–6 hrs/job day | **$50–80/hr** |
| 19 | Airbnb co-hosting | `AirbnbCohost` *(new, unscoped)* | 10–25% of nightly revenue | ~5–7 hrs/wk/listing (with automation) | **$30–60/hr equivalent** |

*(19 rows, 17 distinct businesses — rows 3/4 are both MissedCall, rows 5/6 are both GBP, split by task type since setup and ongoing management have very different $/hr.)*

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
