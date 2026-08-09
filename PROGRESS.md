# PROGRESS.md — live status

Last updated: 2026-08-06 — **25 business lines, ops hub with daily queue/expansion budget/tax tracking/Stripe payments/referral & loyalty program/httpSMS, public website (now 9 segments/17 services — every line with real pricing is now public). 12 lines re-priced today from real sourced 2026 competitor research (was internal guesses before). Full-state audit run 2026-08-01, 3 real bugs found and fixed (see DECISIONS.md); one real incident that day too — a database deletion mistake during Stripe testing, also logged in DECISIONS.md, not hidden.**

## Legend
✅ done · 🔶 partial · ⛔ blocked (needs you)

---

## The three systems, at a glance

1. **Ops hub** (`ops-hub/`, port 5000) — internal, password-gated, your daily driver. Daily Queue, all 25 business lines, expansion budget tracking, tax tracking.
2. **Public website** (`website/`, port 5050) — Waters & Co branded, public-facing, no auth. Writes leads straight into the hub's database.
3. **Standing docs & research** — `wave1/`, `wave2/`, `wave3-unscoped/`, `docs/`, `PRICING.md` — the actual content behind every business line.

Both apps need to be running for the website's contact form to work (it imports the hub's code directly). Run both:
```bash
cd ops-hub && python3 run.py &
cd website && python3 run.py &
```

---

## A. Central ops hub — ✅ complete, actively used

- ✅ **Daily Queue** (`/`, home page) — every open, actionable case across all 25 lines, sorted highest $/hr first, no other order
- ✅ Per-line separated views (`/lines` → `/line/<key>`)
- ✅ "All Cases" full list + filters (`/all`)
- ✅ Lead form with dynamic per-line fields, task-type rates (setup/management for GBP & MissedCall, session/course for Crypto Literacy), time tracking, done/left-for-you/source-link
- ✅ Intake webhook — built, inactive until you set `INTAKE_WEBHOOK_ENABLED`/`INTAKE_WEBHOOK_SECRET`
- ✅ Deadline alerts (14/30/60 day + overdue, state-aware for land tax — NT 30 days, others 60)
- ✅ Password gate (`HUB_PASSWORD`) + **Tailscale remote access live**: `http://m-hp.tail28a65e.ts.net:5000` from your phone
- ✅ Local monitoring script (`new_case_check.py`, cron-able) — cloud auto-monitoring isn't possible, see `docs/monitoring.md`
- ✅ **Expansion budget tracking** (`/expansion`) — spend logging, per-type evaluation windows, cost-per-outcome, keep/adjust/kill flags. Phase 1 = $0, `BUDGET_PHASE` in `app/config.py` is a code-level switch you flip yourself
- ✅ **Tax tracking** (`/tax`, export at `/tax/export`) — day-job pay periods, deductible expenses (day job + any business), no-receipt cap tracking, combined income position, day-job-vs-business $/hr comparison with a mortgage-serviceability flag. Not tax advice — organisation and flagging only. Currently a single, exactly-confirmed entry (your real 19 July payslip, cross-checked against the actual PDF) as the FY26-27 starting point — log each new payslip as it lands.
- ✅ **Stripe payments** (`app/payments.py`) — per-lead payment requests (deposit, final balance, etc., a lead can have several over its life), Stripe Checkout Sessions, signature-verified webhook confirms "paid" (never the client-side redirect). Currently **test-mode only** — `ops-hub/.stripe_env` auto-loaded by `launch_hub.sh` alongside a `stripe listen` forwarder (also auto-started, pidfile-guarded). Live-mode activation status on the real account (`acct_1TzJCBRq9KZRjLbM`) unconfirmed — see ROADMAP.md Phase 0.
- ✅ **SMS module** (`app/sms.py`) — native texting via a self-hosted httpSMS instance and the work phone's real SIM, ready but inactive (`HTTPSMS_ENABLED`). Outbound `send_sms()` reusable across every business line, rate-limited locally. Inbound webhook matches replies to existing leads by phone number and appends to notes, or creates a new GeneralEnquiry lead if no match. Tested end-to-end against a throwaway DB copy — one real bug found and fixed (phone-match tiebreak). Self-hosting httpSMS itself (Docker + a paired Android phone) is yours to do — see `docs/httpsms_setup.md`.
- ✅ **Referral & loyalty program** (`/referrals` + a box on each lead's page) — one-time 50% referral bonus (repeatable per converted referral), ongoing referrer-retention discount capped at 10%/mo, loyalty discount for repeat customers, a stacked top tier for both, a margin-floor guardrail flag. Advisory only — computes/recommends, never auto-applies to a Stripe payment amount. Contingency/fixed-external-rate lines (LandTax, NDISNav, NDISCompliance) excluded from eligibility. Discount-rate numbers were judgement calls where the spec only fixed the caps — see DECISIONS.md, worth reviewing.

## B. The 25 business lines

**Fully built (service scope + pricing, ready to pitch) — all 17 now live on the public website:**
GBP/Local SEO, Review Generation, AI Missed-Call Reception, Land Tax Objection (all 8 states), Senior Tech Concierge, Video/Podcast Repurposing, Senior Downsizing (now split coordination/labour), Lost Super/TPD Navigation (free-to-client + referral model), Crypto IT/Literacy (investment-advice guardrail baked in), AI Tools for Business, AI Implementation for SMEs ($990-4,000), AI Lead-Response for Real Estate Agents ($129-199/mo, US/UK/Canada), Bookkeeping non-BAS ($149-449/mo), SME Grant-Finder ($79-99 flat), Age Pension/Centrelink Assistance ($249-349 flat), **Digital Legacy / Account Organiser** (2026-08-06, new — $120-320 tiered), **Photo & Memory Digitisation Concierge** (2026-08-06, new — coordination fee over bureau pass-through cost).

**Deliberately NOT on the website — re-classified 2026-08-06:**
- Energy/Concession Navigation — no viable AU paid market found (covered by free government/charity channels); folded into Tech Concierge/Downsizing visits as a free value-add instead.

**Lightweight, no dedicated marketing:**
General Enquiry (website catch-all), Odd Jobs/Gig Marketplace (one-off Airtasker-style pickups).

**Deliberately held — regulatory complexity, need your explicit sign-off first:**
- ⛔ Airbnb Co-Hosting — likely needs a real estate licence in most states incl. WA (prosecution precedent in QLD/VIC). Talk to a property lawyer, not more docs.
- ⛔ Deceased-Estate Admin, NDIS Plan Navigation, NDIS Provider Compliance — real regulatory frameworks, need a scope/qualifications conversation before building client-facing material.
- ⛔ Grant Writing (Nonprofit) — your own pricing note says it needs a portfolio first, not viable cold.

## C. Public website (Waters & Co) — ✅ built, 🔶 not publicly hosted

- ✅ Landing page (hover/tap reveals 9 segments) → segment pages → service pages with real pricing → contact form. **2026-08-06 (first pass): added AI Implementation for SMEs and AI Lead-Response for Real Estate Agents.** **2026-08-06 (second pass, same day): researched and added the remaining 11 lines that only had internal guesses** — Bookkeeping, SME Grant-Finder, Age Pension/Centrelink, Senior Tech Concierge, Crypto IT/Literacy, AI Tools for Business, Digital Legacy, Senior Downsizing (split into coordination/labour tiers), Photo & Memory Digitisation, Lost Super Navigation, Video/Podcast Repurposing — every one backed by real 2026 competitor research, not estimates (see `DECISIONS.md`). Energy/Concession Navigation researched and deliberately **not** added — no viable AU paid market exists for it. Every business line with real pricing is now public; only the 5 regulatory-held lines (NDIS x2, Deceased-Estate, Grant Writing, Airbnb) and the always-internal ones (GeneralEnquiry, OddJobs) remain off the site. Malachite/gold branding finished and applied site-wide (background image + separate crisp text layer, `website/static/img/hero-background.jpg` + `wordmark-gold.png`).
- ✅ Contact form writes straight into the hub's lead database, tagged by service, with a template-based draft reply attached (no AI call, no cost) for you to review and send
- ✅ No phone number anywhere — every page pushes to the contact form
- ✅ Branding: dark slate green + gold, **Fraunces** for display type (switched from Cormorant after comparing 16+ fonts), Jost for labels
- ✅ **LIVE at [watersandco.info](https://watersandco.info)** (2026-08-07) — real domain, real HTTPS, real deploy. Hosted on Render (free tier, `render.yaml` Blueprint), talking to this hub over a Tailscale-Funnel-exposed webhook (`HUB_MODE=remote`, only `/webhook/website-lead` is public — the dashboard/login stay private on the tailnet). DNS via Cloudflare. Verified end-to-end with 3 real test submissions all the way through to real hub lead records (#7-9, test data, Owner to delete). Full setup trail in `docs/website_deployment.md` and DECISIONS.md's 2026-08-07 entry.

## D. Opportunity scanning & competitive monitoring — ✅ built, running

- ✅ Scoring rubric (`wave3-unscoped/opportunity_scan/scoring_rubric.md`) — 7 factors, infrastructure-reuse weighted highest, folds in every criterion you gave (learnable-via-self-research, low-cost, simple model, "can't be bothered doing it themselves")
- ✅ Gig-marketplace scanning process (Airtasker/Marketplace/etc.) — separate, lighter-weight lane for one-off jobs that don't need a dedicated business line
- ✅ **Daily scheduled task live** (`daily-opportunity-scan`, 9:08am daily) — researches 1-2 candidates, scores them, logs to `candidates_log.md`, drafts assets for anything scoring 25+ with no regulatory complexity, but never wires a new line into the live hub without your confirmation
- ✅ **Global expansion research** (`wave3-unscoped/lead_generation/global_expansion_research.md`, 2026-08-01) — US/UK/Canada/NZ/Ireland demand for the 8 location-independent lines. Real live budgeted Upwork jobs found for Video Repurposing (strongest signal) and GBP/MissedCall; a real US competitor already sells AI reception to HVAC shops. Timezone is a genuine constraint (Perth's early afternoon is dead for every English-speaking market). Priority order given in the doc.
- ✅ **Launch lead research** (`wave3-unscoped/lead_generation/launch_leads_and_contacts.md`, 2026-08-01) — ranked easiest-to-hardest: 4 warm contacts with a specific documented hook, 22 verified weak-Google-profile trade prospects (12 new + the existing 10), referral-partner targets for LandTax/Downsizing/LostSuper, real named advertising channels per line. Nothing contacted yet — desk research only, re-verify before sending.
- ✅ **Cowork skill templates** (`cowork-skills/`) — 5 general + 4 Waters & Co-specific (stale-lead-revival, invoice-chase, monday-brief, referral-thank-you), wired to the real hub data model. Inactive until you connect Gmail+Calendar to Claude Cowork yourself.
- ✅ **Scan run 2026-08-01** — first automated run. Two candidates scored and drafted (neither wired into the live hub — awaiting your confirmation): **Digital Legacy / Account Organiser** (33/35, `wave3-unscoped/digital_legacy/`) and **Photo & Memory Digitisation Concierge** (31/35, `wave3-unscoped/photo_digitisation/`). Both are deliberate bolt-ons to an existing client visit (Tech Concierge / Downsizing) rather than standalone lines. The photo one scored a low 3/5 on market gap on purpose — Perth's scanning market is crowded, so it's scoped as a sorting/coordination layer, not a scan bureau, and its pricing sheet says to stop if the first few upsells don't convert.
- ✅ Local-cron fallback script documented as backup (`run_daily_scan.sh`), not currently needed
- ✅ **Competitive monitoring, monthly** (`monthly-competitive-monitor` scheduled task, 1st of the month) — re-checks competitor pricing/reviews for 3-4 business lines per run against `docs/competitive_analysis_full_portfolio.md` (deep, 18-business, sourced complaint quotes — added 2026-08-01) and the older `docs/competitor_pricing_research.md` (GBP-focused). Logs findings (including "nothing changed") to `wave3-unscoped/competitive_monitoring/monitoring_log.md`. Recommends pricing changes, never applies them — same "flag, don't file" pattern as expansion-spend evaluation. **Needs the same one-time "Run now" approval click as the opportunity scan before its automatic runs will go hands-off.**

## E. Pricing & research foundations

- ✅ `PRICING.md` — full rate table for all 25 lines, 12 re-priced 2026-08-06 from real sourced competitor research
- ✅ **`ml_training_log/`** (started 2026-08-07) — structured JSONL process log, forward-only, complementing the hub's own DB (outcomes) and the prose DECISIONS.md/PROGRESS.md (narrative) with the *reasoning* side (what was searched, why a lead was accepted/rejected, pricing logic) — for future ML training on how the business actually operates.
- ✅ Competitor pricing research (`docs/competitor_pricing_research.md`)
- ✅ ATO tax figures verified for FY2026-27 (`wave3-unscoped/tax_tracking/ato_figures_verification.md`) — 9/11 confirmed, one correction made (super carry-forward expiry), one flagged unconfirmed (WFH rate)

---

## Audit note (2026-07-31)

Ran a full end-to-end pass after today's additions: all 21 business line views, all core hub routes, the expansion and tax modules, and the complete website→hub pipeline (contact form → lead creation → draft email, checked for the `None`-rendering bug that was fixed earlier in the build — confirmed still clean). Zero regressions found. Both apps confirmed running and reachable (hub via Tailscale, website locally).

---

## Things only you can do (the real punch list)

1. **Pick and sign up for an AI phone/reception platform** (`wave1/missedcall/platform_research.md`) and give me the API key to activate the webhook.
2. **Pick and sign up for a review-automation tool** (`wave1/reviewgen/tool_research.md` — NiceJob recommended).
3. **Confirm Stripe's live-mode activation status** (Gmail's already done) — see `ROADMAP.md` Phase 0 / accounts table.
4. **Pick accounting software (Xero or QBO)** for bookkeeping — clients invite you in, you generally don't pay.
5. **Review every draft template before client use** — none are legally vetted.
6. **If serious about Airbnb co-hosting: talk to a property/real estate lawyer first.**
7. **Decide if/when to pursue the 5 still-held lines** — each needs a scope/qualifications conversation.
8. **Click "Run now" on the `daily-opportunity-scan` scheduled task once**, in the Scheduled sidebar section — pre-approves the tools it needs so future automatic runs don't stall on a permission prompt.
9. **Log your day-job pay periods and business expenses as they happen** — the tax module is only as useful as what's actually entered; it currently has the two recovered entries (see DECISIONS.md 2026-08-01 RECOVERY entry) plus whatever you add going forward.
10. **Flip `BUDGET_PHASE` to "on" in `ops-hub/app/config.py`** when you're actually ready to spend on expansion — it's a code-level switch, not automatic.
11. **Read `ROADMAP.md`** — the full plan of attack, phase by phase, updated today.
12. **If you want the intake webhook or ongoing (non-`stripe listen`) Stripe webhooks actually live**, sign up for Twilio (and/or confirm a stable public URL plan) yourself — account creation isn't something I can do. The code for both is already built and ready the moment you hand me credentials/a URL.
13. **If you want a GitHub backup of this repo**, create an empty repo yourself and give me the URL — I'll wire up the remote and push, but can't create the account.
14. **Review the referral/loyalty discount-rate assumptions** (5%/referral retention increment, 10% loyalty base, 20% stacked tier, 50%-of-rate-card margin floor) — my judgement calls, documented in DECISIONS.md 2026-08-01, change `app/config.py`'s `REFERRAL_*`/`LOYALTY_*`/`DISCOUNT_*` constants if you want different numbers.
15. **Click "Run now" once on `monthly-competitive-monitor`** too, same reason as the opportunity scan (pre-approves its tools).
16. **Decide whether the two 2026-08-01 scan candidates become real business lines** — Digital Legacy (33/35) and Photo Digitisation (31/35). Scopes and pricing are drafted in `wave3-unscoped/digital_legacy/` and `wave3-unscoped/photo_digitisation/`; nothing was added to `BUSINESS_LINES` in `ops-hub/app/config.py`, deliberately. That's your call, not the scan's.

---

## 2026-08-07 — Overnight lead-gen + tailored email drafting, complete

Per Owner's "extensive search, continue until I return" instruction: researched
and drafted **81 individually tailored cold emails** (not one blanket email —
every one references a real, specific, verified pain signal for that business)
across `wave3-unscoped/lead_generation/offers/tailored_emails_master.md`:

- 45 direct trade-service prospects (GBP/reviews/missed-call angle) across 6
  regional batches — Perth/Adelaide, Brisbane allied health, Melbourne/Sydney
  hospitality, Gold Coast/Sunshine Coast, Newcastle/Hobart/Darwin, Adelaide/Canberra.
- 10 Land Tax referral-partnership emails (buyers agents/property tax accountants).
- 10 Video/Podcast Repurposing prospect emails.
- 12 Real Estate AI Lead-Response emails (UK/US/Canada solo & small-team agents).
- 4 older verified contacts (email channel) not already covered by an existing text.

Every other older verified contact already had a personalized ready-to-send
**text** (`msb_ready_to_send.md`/`missedcall_call_sheets.md`) — text being the
right channel for on-the-tools tradies, per `contact_channels_and_strategy.md`.
Copywriting structure researched and sourced (soft CTA ~3x reply rate, personalized
2-3x reply rate) — see the master file's own header for citations.

**Nothing has been sent.** Every item is a prepared draft awaiting per-item
confirmation, per the standing rule. Next real step is the Owner reviewing and
approving sends, one at a time, re-verifying each contact is still current first.

Also backfilled `ml_training_log/events.jsonl` with 48 structured events derived
from the full `DECISIONS.md` history (2026-07-29 onward) plus live-logged events
for tonight's research/drafting work, per Owner's follow-up instruction to log
every step taken so far, not just going forward.

---

## 2026-08-07 — Spring-clean audit pass (security fix, deploy fix, email re-check, 11 more leads)

Per Owner's "double check everything, get it ready for the morning" instruction:

**Security audit (real HIGH finding, fixed):** the ops-hub's login gate's exempt
list was missing the website-lead and SMS-inbound webhooks — with `HUB_PASSWORD`
set (the documented live config), both got 302-redirected to `/login` instead of
running their own secret check, meaning **every real contact-form lead submitted
through the live site right now would silently fail**. Fixed, plus hardened:
constant-time secret comparisons, an open-redirect guard on `/login`, fail-closed
behaviour on the intake webhook, `SESSION_COOKIE_SAMESITE=Lax`. Local hub process
restarted to pick up the fix — confirmed via direct request the webhook no longer
302s. Full findings: see the 2026-08-07 SECURITY entry in `DECISIONS.md`.

**Website deploy bug (found, fix pushed):** the live Render deployment was
serving a stale build missing the favicon/OG-image tags that already exist
correctly on GitHub's `main`. Pushed a fresh commit to trigger a redeploy — **as
of this write-up, still confirming it went through; check `watersandco.info`'s
page source for `<link rel="icon"` before relying on it, and if it's still
missing, trigger a manual deploy from the Render dashboard yourself.**

**Mobile + desktop re-check:** landing page, Small Business Support segment
(group headings intact), and Downsizing service page (the one that had the
mobile price-overflow bug) all checked at 375px and desktop — zero overflow,
correct pricing, correct segment order.

**Email re-audit:** programmatically checked all 92 drafted emails for
structure/duplicates/length. Found and fixed 1 real issue — Electrician Services
Adelaide was independently sourced twice with two different pitches; marked the
weaker one do-not-send.

**11 more leads found** (spring-clean opportunity scan): 5 Perth
downsizing/estate-clearance businesses as referral partners for Digital
Legacy/Photo Digitisation, 6 Geelong VIC trades (new geography, GBP/reviews
angle). Full writeup: `wave3-unscoped/lead_generation/new_verticals_2026-08-07.md`.

**New deliverable:** `wave3-unscoped/lead_generation/offers/morning_send_list.md`
— all 91 sendable emails reformatted into one easy-scan doc (who / what they do
/ what we're offering / the draft), grouped by offer type, exactly per the
Owner's requested format. This is the file to actually work through in the
morning — the `tailored_emails_master.md` file stays as the full sourcing-note
version for reference.

**Known issue, not fixable by me:** Owner reports the Linux desktop Claude app
can't connect to Gmail (times out on the OAuth callback), only claude.ai can.
This doesn't block tonight's work since nothing here needs Gmail access — every
email is a prepared draft for the Owner to paste and send from their own inbox.
If it matters for other workflows, worth reporting as a bug via the desktop
app's own feedback channel; it's outside what this session can fix.

## 2026-08-09 — daily opportunity scan: 1 drafted, 1 rejected

**Drafted: AI Search Visibility Audit (32/35)** —
`wave3-unscoped/ai_search_visibility/` (service_scope.md + pricing_sheet.md).
Flat-fee audit of whether a local business gets recommended by
ChatGPT/Gemini/Perplexity/AI Overviews, plus a 90-day fix list. Highest
infrastructure-reuse score yet: sells straight into the existing
GBP/ReviewGen/MissedCall client base using the same report-and-action-plan
format as LandTax/GrantFinder. Proposed $249–349 standard, $149–199 bolt-on
for existing clients, free snapshot as lead magnet.

Market gap scored 3 (not higher) on purpose — **the local tier already has a
Perth competitor**: SocialPulse247 sells a $497 AI Search Visibility Audit to
trades and local services, the same segment. AI Local Link $299, AIReady
Australia $497, against agency retainers of $2,500–15,000/mo and $27 self-serve
tools. Contested, not empty — but a Perth operator betting on this segment
validates the model.

**Owner decision needed:** own business line vs a `task_type` on GBP (the fix
half overlaps GBP heavily). Nothing wired into `config.py`, `PRICING.md` or the
website either way.

**Rejected: New Business Launch Concierge (20/35)** — verified against the
regulator, not assumed: TPB(I) 39/2023 lists applying for an ABN on a client's
behalf as a tax agent service, and TPB registration is required to provide those
for a fee. Same class as the held NDIS/Deceased-Estate lines. Logged with
reasoning in `candidates_log.md`.

**Process gap found:** the session buffer says two candidates were scored
2026-08-05 (AI Answer Visibility, Declutter-to-Cash) but neither was ever
written into `candidates_log.md` — no scores survive. AI Answer Visibility is
superseded by today's row; **Declutter-to-Cash remains genuinely open** and its
claimed WA-licensing blocker is unverified. Noted in the log.

## 2026-08-09 — website rebuild, pricing reconciliation, full audit, headline rework

Full-day session, five threads. **Where to find each one:**

1. **Website merge from Owner-supplied handover (v1/v2).** Compared, both
   turned out to share an identical strategy doc — only the website source
   in v2 was new. Merged the fixed-pricing config, new hero/wedge section,
   enquiry interest field; rejected two regressions (solo-run language,
   Doubleview mentions) that would have undone earlier fixes. Full record:
   `DECISIONS.md` (2026-08-09, "MASTER HANDOVER PROPOSAL"),
   `docs/handover-proposals/2026-08-09/COMPARISON.md`.
2. **Pricing reconciliation.** All 4 `wave1/*/pricing_sheet.md` files,
   `PRICING.md`'s master table (14 rows), and every outreach doc that had a
   hardcoded old price — brought in line with the new fixed pricing.
   `DECISIONS.md` (2026-08-09, "WAVE1 PRICING SHEETS...").
3. **Tech Concierge repriced** to $99/hr in-person (was $79), $69/hr remote
   (was $59, deliberately held back — different competitive market to
   in-person). Full competitor research (Geeks2U, IT 4 Retirees, Fixable,
   Dtech, IT Help at Home, Seniors Tech and Tea, My Senior IT) in
   `wave3-unscoped/tech_concierge/pricing_sheet.md` and two `DECISIONS.md`
   entries. Deployed, live on watersandco.info.
4. **Full audit before the email campaign goes out:** all 117 Gmail drafts
   checked directly (not the repo copies) — zero contain a price, nothing
   stale. Spam Act 2003 re-verified live against AustLII/ACMA — current
   practice already compliant, one flag raised (the 2026-08-05 SMS list
   needs the same consent check before outbound use). 8 new legal
   lead-gen channels found and written up:
   `wave3-unscoped/lead_generation/legal_channels_not_yet_tried_2026-08-09.md`.
   `DECISIONS.md` (2026-08-09, "FULL EMAIL/LEGAL/CHANNEL AUDIT").
5. **Landing page hero headline** reworked with the Owner through several
   rounds — final: "Find and fix what's quietly costing your business
   time, jobs and opportunities." Full creative-process record, including
   why "money" was rejected as a claim: `DECISIONS.md` (2026-08-09,
   "LANDING PAGE HERO HEADLINE").

**Structured/machine-readable version of all five:** `ml_training_log/events.jsonl`
(6 new events appended same day) — see `ml_training_log/README.md` for the
schema. This is now standing practice for every decision-bearing step, not
just when asked — see CLAUDE.md's "Memory and logging" section.

**Recurring tooling issue, not resolved this session:** the Semgrep
Guardian PreToolUse hook blocks `.py` (and occasionally other) file edits
until logged in, and its login needs an interactive browser OAuth callback
this environment can't complete. Worked around each time with the Owner's
explicit go-ahead (disclosed plainly, verified after writing) — but it
needs a real interactive-terminal `semgrep login` at some point to stop
recurring. `DECISIONS.md` (2026-08-09, "TECH CONCIERGE PRICING — THE TWO
BLOCKED CONFIG EDITS...").

## How to pick this back up

- Run both apps (see top of this file).
- `DECISIONS.md` has the full reasoning log for every assumption — read it before assuming something was guessed carelessly.
- `ROADMAP.md` is the phase-by-phase plan of attack.
- `docs/remote_access.md`, `docs/monitoring.md` explain the two infrastructure pieces in detail.
