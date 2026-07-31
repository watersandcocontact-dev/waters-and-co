# PROGRESS.md — live status

Last updated: 2026-07-31 — **21 business lines, ops hub with daily queue/expansion budget/tax tracking, public website, daily opportunity scanning. Audited end-to-end this session, zero known regressions.**

## Legend
✅ done · 🔶 partial · ⛔ blocked (needs you)

---

## The three systems, at a glance

1. **Ops hub** (`ops-hub/`, port 5000) — internal, password-gated, your daily driver. Daily Queue, all 21 business lines, expansion budget tracking, tax tracking.
2. **Public website** (`website/`, port 5050) — Waters & Co branded, public-facing, no auth. Writes leads straight into the hub's database.
3. **Standing docs & research** — `wave1/`, `wave2/`, `wave3-unscoped/`, `docs/`, `PRICING.md` — the actual content behind every business line.

Both apps need to be running for the website's contact form to work (it imports the hub's code directly). Run both:
```bash
cd ops-hub && python3 run.py &
cd website && python3 run.py &
```

---

## A. Central ops hub — ✅ complete, actively used

- ✅ **Daily Queue** (`/`, home page) — every open, actionable case across all 21 lines, sorted highest $/hr first, no other order
- ✅ Per-line separated views (`/lines` → `/line/<key>`)
- ✅ "All Cases" full list + filters (`/all`)
- ✅ Lead form with dynamic per-line fields, task-type rates (setup/management for GBP & MissedCall, session/course for Crypto Literacy), time tracking, done/left-for-you/source-link
- ✅ Intake webhook — built, inactive until you set `INTAKE_WEBHOOK_ENABLED`/`INTAKE_WEBHOOK_SECRET`
- ✅ Deadline alerts (14/30/60 day + overdue, state-aware for land tax — NT 30 days, others 60)
- ✅ Password gate (`HUB_PASSWORD`) + **Tailscale remote access live**: `http://m-hp.tail28a65e.ts.net:5000` from your phone
- ✅ Local monitoring script (`new_case_check.py`, cron-able) — cloud auto-monitoring isn't possible, see `docs/monitoring.md`
- ✅ **Expansion budget tracking** (`/expansion`) — spend logging, per-type evaluation windows, cost-per-outcome, keep/adjust/kill flags. Phase 1 = $0, `BUDGET_PHASE` in `app/config.py` is a code-level switch you flip yourself
- ✅ **Tax tracking** (`/tax`, export at `/tax/export`) — day-job pay periods (seeded with your real 19 July payslip + a derived catch-up entry so YTD is accurate from day one), deductible expenses (day job + any business), no-receipt cap tracking, combined income position, day-job-vs-business $/hr comparison with a mortgage-serviceability flag. Not tax advice — organisation and flagging only

## B. The 21 business lines

**Fully built (service scope + pricing, ready to pitch):**
GBP/Local SEO, Review Generation, AI Missed-Call Reception, Land Tax Objection (all 8 states), Senior Tech Concierge, Video/Podcast Repurposing, Senior Downsizing/Cleanout, Lost Super/TPD Navigation (referral model), Crypto IT/Literacy (investment-advice guardrail baked in), AI Tools for Business.

**Wave 2 — checklists/research built, not launched:**
Bookkeeping (non-BAS), Concession/Rebate Navigation, SME Grant-Finder, Age Pension/Centrelink Assistance.

**Lightweight, no dedicated marketing:**
General Enquiry (website catch-all), Odd Jobs/Gig Marketplace (one-off Airtasker-style pickups).

**Deliberately held — regulatory complexity, need your explicit sign-off first:**
- ⛔ Airbnb Co-Hosting — likely needs a real estate licence in most states incl. WA (prosecution precedent in QLD/VIC). Talk to a property lawyer, not more docs.
- ⛔ Deceased-Estate Admin, NDIS Plan Navigation, NDIS Provider Compliance — real regulatory frameworks, need a scope/qualifications conversation before building client-facing material.
- ⛔ Grant Writing (Nonprofit) — your own pricing note says it needs a portfolio first, not viable cold.

## C. Public website (Waters & Co) — ✅ built, 🔶 not publicly hosted

- ✅ Landing page (hover/tap reveals 3 segments) → segment pages → service pages with real pricing → contact form
- ✅ Contact form writes straight into the hub's lead database, tagged by service, with a template-based draft reply attached (no AI call, no cost) for you to review and send
- ✅ No phone number anywhere — every page pushes to the contact form
- ✅ Branding: dark slate green + gold, **Fraunces** for display type (switched from Cormorant after comparing 16+ fonts), Jost for labels
- ⛔ **Not hosted publicly** — runs locally only, no domain registered. The earlier Netlify/Vercel static-site recommendation needs revisiting now there's a live form backend (needs serverless functions there, or a small always-on host)

## D. Opportunity scanning — ✅ built, running daily

- ✅ Scoring rubric (`wave3-unscoped/opportunity_scan/scoring_rubric.md`) — 7 factors, infrastructure-reuse weighted highest, folds in every criterion you gave (learnable-via-self-research, low-cost, simple model, "can't be bothered doing it themselves")
- ✅ Gig-marketplace scanning process (Airtasker/Marketplace/etc.) — separate, lighter-weight lane for one-off jobs that don't need a dedicated business line
- ✅ **Daily scheduled task live** (`daily-opportunity-scan`, 9:08am daily) — researches 1-2 candidates, scores them, logs to `candidates_log.md`, drafts assets for anything scoring 25+ with no regulatory complexity, but never wires a new line into the live hub without your confirmation
- ✅ Local-cron fallback script documented as backup (`run_daily_scan.sh`), not currently needed

## E. Pricing & research foundations

- ✅ `PRICING.md` — full rate table for all 21 lines
- ✅ Competitor pricing research (`docs/competitor_pricing_research.md`)
- ✅ ATO tax figures verified for FY2026-27 (`wave3-unscoped/tax_tracking/ato_figures_verification.md`) — 9/11 confirmed, one correction made (super carry-forward expiry), one flagged unconfirmed (WFH rate)

---

## Audit note (2026-07-31)

Ran a full end-to-end pass after today's additions: all 21 business line views, all core hub routes, the expansion and tax modules, and the complete website→hub pipeline (contact form → lead creation → draft email, checked for the `None`-rendering bug that was fixed earlier in the build — confirmed still clean). Zero regressions found. Both apps confirmed running and reachable (hub via Tailscale, website locally).

---

## Things only you can do (the real punch list)

1. **Pick and sign up for an AI phone/reception platform** (`wave1/missedcall/platform_research.md`) and give me the API key to activate the webhook.
2. **Pick and sign up for a review-automation tool** (`wave1/reviewgen/tool_research.md` — NiceJob recommended).
3. **Set up Gmail, Stripe, etc.** — you mentioned doing this in parallel; see `ROADMAP.md`'s accounts table for the full list with cost + my pick for each.
4. **Pick accounting software (Xero or QBO)** for bookkeeping — clients invite you in, you generally don't pay.
5. **Review every draft template before client use** — none are legally vetted.
6. **If serious about Airbnb co-hosting: talk to a property/real estate lawyer first.**
7. **Decide if/when to pursue the 4 still-held lines** — each needs a scope/qualifications conversation.
8. **Click "Run now" on the `daily-opportunity-scan` scheduled task once**, in the Scheduled sidebar section — pre-approves the tools it needs so future automatic runs don't stall on a permission prompt.
9. **Log your day-job pay periods and business expenses as they happen** — the tax module is only as useful as what's actually entered; right now it only has the two entries I seeded from your 19 July payslip data.
10. **Flip `BUDGET_PHASE` to "on" in `ops-hub/app/config.py`** when you're actually ready to spend on expansion — it's a code-level switch, not automatic.
11. **Read `ROADMAP.md`** — the full plan of attack, phase by phase, updated today.

## How to pick this back up

- Run both apps (see top of this file).
- `DECISIONS.md` has the full reasoning log for every assumption — read it before assuming something was guessed carelessly.
- `ROADMAP.md` is the phase-by-phase plan of attack.
- `docs/remote_access.md`, `docs/monitoring.md` explain the two infrastructure pieces in detail.
