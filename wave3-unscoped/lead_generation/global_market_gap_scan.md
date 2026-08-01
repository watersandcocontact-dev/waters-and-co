# Global Market-Gap Scan — 2026-08-01

Open-ended scan for genuinely new business lines (not already in the
18-21-line portfolio) against a strict filter: must-have pain (not
nice-to-have), remote-deliverable to an English-speaking market, mostly
automatable via Claude Code (so delivery cost stays low), and a real,
quotable pricing gap between cheap DIY and expensive incumbents. Ranked
strongest to weakest evidence — none of these are wired into anything
yet, all need a real scoping pass before being treated as a live line.

## 1. Merchant chargeback / payment-dispute defense — STRONG

**Pain:** E-commerce merchants losing chargeback disputes even with good
evidence, compounding losses (product + refund + chargeback fee) — one
documented Shopify case: $1,465 lost on a single transaction, funds
frozen up to 3 months during disputes. [Shopify Community thread](https://community.shopify.com/t/why-are-we-losing-all-chargeback-disputes-even-with-good-customer-service/187858)

**Pricing gap:** DIY template kits $7-49/case (fine for simple one-offs,
useless for evidence-heavy disputes or volume); the AI-native leader
Chargeflow charges 25% of every dollar *recovered*, uncapped — brutal on
high-value chargebacks. A flat-fee-per-case ($75-150/dispute) or monthly
retainer for volume sits cleanly between the two.

**Why Claude Code fits:** Pure document assembly — pull order records,
shipping confirmations, chat logs, match against Visa/Mastercard reason
codes, draft a compliant rebuttal packet. No physical presence, no
licensing.

## 2. US multi-state sales-tax nexus monitoring & registration — STRONG

**Pain:** Post-Wayfair economic-nexus thresholds keep shifting under
sellers' feet (Utah dropped its 200-transaction threshold July 2025,
Illinois follows January 2026) while states ramp up audit programs — real
and growing financial exposure for small online sellers, not background
noise.

**Pricing gap:** Self-serve calculators are cheap (TaxJar Starter $39/mo,
Anrok Starter $100/mo) but only calculate/remit — they don't flag *when*
a seller crosses a new state's threshold or handle registration
paperwork. Full-service nexus consultants exist but are quote-only,
opaque, and priced for mid-market firms, not a solo Shopify seller.

**Why Claude Code fits:** Ingest a seller's sales-by-state CSV monthly,
flag new threshold breaches against a maintained rules table, auto-draft
the state registration forms. A genuine "watch and alert + paperwork"
niche between the DIY calculator and the enterprise consultant.

## 3. Google/Meta ad account suspension & reinstatement appeals — STRONG

**Pain:** Acute and urgent. Documented case: a wrongful Google Ads
suspension cost a client $100,000+ in lost revenue over 7 days. Meta
suspensions reportedly spiking, with no disclosed reason and the
automated appeal bot routinely going nowhere.

**Pricing gap:** Fiverr gigs sit around $30 (low-quality, generic);
dedicated agencies charge $197 (audit) up to $997 (complex reinstatement)
or a flat $799. Undercutting the $500-800 agency tier while being far
more thorough than a $30 gig is a real, specific gap.

**Why Claude Code fits:** Text-pattern-matching against known ad-platform
policies plus precise, policy-citing appeal drafting — Chris does final
human review before submission.

## 4. US medical bill / EOB error advocacy — MODERATE (narrower, US-only)

**Pain:** Well-documented — up to 80% of medical bills reviewed contain
at least one error or overcharge.

**Pricing gap:** Contingency advocates charge 20-35% of savings (GoodBill
20% capped at $1,000; Resolve $249-499 deposit + 10-25% success fee).

**Caveat:** This niche already has well-funded AI-native competitors
(GoodBill, Resolve, mediloop) actively closing the exact gap this filter
looks for — narrower room for a solo operator than the top 3. Single-
market only (Australia's Medicare doesn't generate this problem). Worth
testing only with a differentiated angle (flat-fee review instead of
contingency, or a bill type/insurer the incumbents ignore) — not a
priority pick.

## 5. SME government/corporate RFP compliance-matrix + first-draft service — SPECULATIVE (weakest fit)

**Pain:** Real and government-acknowledged (the Obama-era RFP-EZ
initiative existed because small businesses found bidding "too
complicated, too expensive" to bother with). Producing a compliant
proposal reportedly costs 0.5-2% of the contract's value in labor.

**Pricing gap:** Full proposal agencies charge $3,000-20,000+/bid;
freelance writers bill $75-200/hr. Nothing exists for a small business
that just wants a compliant response to a modest local-government
tender.

**Why this is the weakest fit:** Claude Code can automate the mechanical
half (requirements → compliance matrix, boilerplate sections) but the
win-theme narrative and pricing strategy that actually wins bids still
leans on human judgment and business-specific facts supplied per client —
closer to "AI-accelerated expert service" than "AI does the heavy
lifting." Pilot only as a narrowly-scoped "compliance matrix + first
draft" product, not a full win-the-bid service.

## Bottom line

Chargeback defense, tax-nexus monitoring, and ad-account reinstatement
have the cleanest evidence on all four filter criteria. None have a
service_scope.md or pricing_sheet.md yet — that's the next step if any
get picked up, following the same pattern as `ai_implementation/`.
