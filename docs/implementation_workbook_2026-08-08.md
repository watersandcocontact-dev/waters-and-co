# Waters & Co — Implementation Workbook

Companion to `docs/deep_research_growth_seo_ai_blueprint_2026-08-07.md`. That
document is the strategy; this one is the concrete build record — what's
actually live on the `ai-practices-rebuild` branch as of 2026-08-08, what's
deliberately deferred and why, and the decisions the Owner supplied that
made the rebuild possible.

## 1. Owner decisions locked in (blueprint §13)

| # | Decision | Answer | Where it landed |
|---|---|---|---|
| 1 | Legal entity | Waters & Co, ABN 85 928 697 823 | Privacy + Terms only (not schema, not footer — confirmed not an SEO/GBP ranking factor, so no reason to publish it more widely) |
| 2 | Service area | Doubleview, WA 6018 · north-of-river Perth in person · Australia-wide/worldwide remote | Footer, About, structured data `areaServed` |
| 3 | Support hours | Normal weekday trading hours, after-hours by arrangement | About page |
| 4 | Insurance | None — deliberate, scope stays outside advice/funds/binding-decision territory | How We Work + Terms, framed as a scope statement, not a gap |
| 5 | Bookkeeping/other qualifications | None held; TPB/BAS status unconfirmed | Bookkeeping copy already excludes BAS lodgement (referred out) — unchanged, correct as-is |
| 6 | Property/pension/financial qualifications | None | Existing service copy already stays in preparation/administration territory, not advice — unchanged, correct as-is |
| 7 | Primary Google Business Profile category | See §2 below | Not a website change — set directly in the GBP dashboard |
| 8 | Testimonials | Will come with clients, Owner will organise | No fabricated testimonials added anywhere — evidence sections left empty/omitted until real ones exist |
| 9 | Ad budget | $0 for now | No paid channel work done or recommended as active; blueprint §6.1/§11 paid-search step explicitly not actioned |

## 2. Google Business Profile category recommendation

**Primary category: "Internet Marketing Service"** — the closest fixed
Google category match to the #1-priority acquisition service (GBP
management for other businesses), and the practice the blueprint identifies
as the flagship acquisition/recurring engine.

**Suggested secondary categories:** "Business Management Consultant"
(covers the AI Solutions and Personal Digital Support breadth without
diluting the primary category) and "Marketing Consultant".

**Caveat, stated plainly:** Google's category picker is a live, autocomplete
list that isn't reliably scrapable from outside the dashboard, and it can
change. This is a strong directional recommendation, not a guaranteed exact
string match — confirm the closest available option directly in the GBP
dashboard when setting the primary category, rather than assuming this
exact label is selectable.

## 3. What's built vs. what's deferred

### Built (this branch, not yet merged/deployed)

- Full 4-practice information architecture replacing the 5-segment one,
  with every one of the 16 services kept and re-homed per the blueprint's
  own §5.1 sitemap
- SEO-friendly nested URLs (`/<practice>/<service>/`) for all 16 services
- **Every old URL 301-redirects** to its new home (5 old segment URLs, 16
  old service URLs) — nothing that was already live/indexed/bookmarked
  breaks. The old contact-form POST route 307-redirects (the only redirect
  status that preserves the method and form body)
- Schema.org JSON-LD updated to the new URL scheme; breadcrumbs now reflect
  the 3-level hierarchy (Home → Practice → Service)
- Offer-ladder package names (blueprint §3.3) tagged onto the 6 services
  they map to — see `PRICING.md`'s 2026-08-08 update
- The 5 priority service pages named in blueprint §11 (GBP, AI Tools for
  Business, AI Missed-Call Reception, AI Implementation for SMEs, Review
  Management) upgraded with the blueprint §5.2 template: who it's for / who
  it isn't for, real process steps, FAQs. The template renders these
  sections conditionally, so the other 11 services are unaffected and
  unchanged
- Four new pages: About, How We Work, Privacy Policy, Terms — previously
  the site had none of these
- Privacy Policy includes the OAIC-guided AI-use disclosure (verified live
  against oaic.gov.au before writing it, not assumed)

### Deliberately deferred (not built this pass)

- **The 21 content-cluster articles (blueprint §5.3).** The blueprint's own
  stated principle is "publish fewer, stronger pages... after confirming
  demand in keyword tools" — and there's no Search Console or Keyword
  Planner access available to validate demand before writing them. Writing
  21 speculative articles without that validation would be exactly the
  scaled-content-without-evidence pattern the blueprint (and Google's own
  guidance, §2.2) warns against. Full title list kept below as a ready
  backlog once keyword data exists.
- **Content pages for the other 11 (non-priority) services.** Same
  reasoning — the blueprint names five specific pages to upgrade first;
  the rest wait for evidence they're worth the same investment.
- **Paid acquisition setup** (Google Search test, Meta) — $0 budget
  confirmed, nothing built or spent.
- **CRM field additions** — see §5 below; most of what the blueprint asks
  for already exists in the hub.

## 4. Content calendar backlog (blueprint §5.3, unpublished)

Kept in priority order, grouped by practice, for whenever keyword-tool
access exists to validate before writing:

**Local Business Growth**
1. Google Business Profile management cost in Perth
2. Why a service business is not appearing in Google Maps
3. Google Business Profile cleanup checklist for tradies
4. How to ask every customer for an honest review without review gating
5. What to do with a negative Google review
6. Missed-call text-back versus AI receptionist for a small business

**AI Solutions**
7. Which small-business task should you automate first?
8. AI automation cost for an Australian small business
9. Five signs a workflow is ready for automation
10. AI tool setup versus a custom automation
11. What data should never go into a public AI tool?
12. A human-approval checklist for small-business AI

**Personal Digital Support**
13. What to prepare before an Age Pension claim
14. What a Centrelink paperwork helper can and cannot do
15. In-home technology help for seniors in Perth: what to expect
16. A family digital account inventory checklist
17. How to prepare photos for professional digitisation

**Specialist Projects**
18. How WA property valuation objections work and why deadlines matter
19. What belongs in an evidence-backed valuation objection
20. Podcast repurposing: what ten useful clips should include
21. Grant finder versus grant writer: the difference

## 5. CRM / measurement fields (blueprint §9.1)

Checked `ops-hub/app/db.py`'s actual `leads` schema against the blueprint's
minimum data set rather than assuming a gap:

| Blueprint wants | Already in the hub | Gap |
|---|---|---|
| First-touch source and campaign | `source` (manual/webhook/referral/import) + `expansion_spend.campaign_tag` for UTM-style attribution | None — already built |
| Landing page and service | `business_line`, `source_url` | None |
| Revenue, cost, hours, contribution | `estimated_value`, `time_estimate_hours`, `time_entries` table, computed `$/hr` | None |
| Repeat purchase / referral | `referred_by_lead_id` (per DECISIONS.md's 2026-08-01 audit entry) | None |
| **Qualified/unqualified + reason** | Not a distinct field — currently folded into `notes` free text | **Real gap** — worth a dedicated `qualified` + `disqualify_reason` field if this becomes a reporting need |
| **Response time** | Not tracked — no timestamp captured for first reply | **Real gap** — would need a `first_response_at` timestamp set when a lead's status first leaves "New" |

Two genuine additions if/when this becomes a priority; everything else the
blueprint asks for is already there.

## 6. Compliance checklist before this goes live

- [ ] Owner to register the ABN-linked business name with ASIC if not
      already done (flagged since the 2026-08-06 deployment prep, still
      outstanding per this repo's history)
- [ ] Confirm the ABN (85 928 697 823) is correct — checksum validated
      locally (passes the official mod-89 test), but a live ABN Lookup
      registry check wasn't completable this session (the lookup site
      blocked the request) — worth a manual glance before go-live
- [ ] Have an Australian lawyer or qualified compliance adviser review the
      new Privacy Policy and Terms pages — both are honest, scoped
      drafts, not a substitute for legal review (same caveat the blueprint
      itself states in §8)
- [ ] Confirm bookkeeping's actual TPB/BAS status before any client work
      that could be read as a BAS service — current site copy already
      excludes BAS lodgement and refers it out, which is correct either
      way
- [ ] Decide whether to add the two CRM fields in §5 above

## 7. Agent workflows (blueprint §7) — current reality check

The blueprint's 8-agent model is a target state, not a from-scratch build.
What's already functionally live in this repo today, mapped to the
blueprint's table:

- **Lead triage** — live today: `website/webapp/draft_email.py` generates
  a service-matched draft reply on every submission, attached to the lead
  for the Owner to review and send (the "Owner sends/quotes" gate the
  blueprint specifies is already how this works — nothing sends itself)
- **Reporting and retention** — partially live: the hub's `$/hr`-sorted
  Daily Queue and `expansion_spend` outcome tracking cover the reporting
  half; no automated renewal/referral prompt exists yet
- **Demand intelligence, research/content brief, proposal builder, delivery
  coordinator, quality/compliance** — not built; genuinely new work, and
  the blueprint's own approval-gate design (no autonomous publish/quote/
  spend) should hold for any of these when they are built

## 8. What's NOT in this workbook

Google Ads Keyword Planner volumes, Search Console data, real CRM
conversion numbers, customer interviews, and legal review — same
limitations the blueprint itself names in its §16. This workbook doesn't
manufacture those; it records what was decided and built without them, and
flags exactly where they'd change the plan once available.
