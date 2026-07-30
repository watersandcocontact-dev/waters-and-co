# PROGRESS.md — live status

Last updated: 2026-07-30 — **Wave 1 + Wave 2 prep fully built, plus the daily-queue/$-per-hr rework, remote access, and monitoring.**

## Legend
✅ done · 🔶 partial · ⛔ blocked (needs you)

## A. Central ops hub — ✅ complete
- ✅ Data model (SQLite schema, all **17** business lines — the original 8 plus 9 introduced via your pricing table, see F below)
- ✅ **Daily Queue is now the home page** (`/`) — every open, actionable case across all 17 lines, sorted **highest $/hr first, only sort order**, per your instruction
- ✅ Per-business-line separated views (`/lines` → `/line/<key>`) — a land tax case and an NDIS case never blur together
- ✅ "All Cases" full list + filters at `/all` (the old dashboard, kept for when you want the unfiltered view)
- ✅ Manual lead-entry form, with per-business-line dynamic fields, task-type (setup/management) for GBP & MissedCall, time tracking, and done/left-for-you/source-link fields
- ✅ Intake webhook receiver — built, safely inactive (503 until you set `INTAKE_WEBHOOK_ENABLED`/`INTAKE_WEBHOOK_SECRET`)
- ✅ Deadline-alert mechanism — dashboard banner (14/30/60 day + overdue), state-aware for land tax (NT = 30 days, all others = 60)
- ✅ **Password gate** (`HUB_PASSWORD` env var) — required before any remote exposure, backward-compatible (no password = no login wall, same as before)
- ✅ **Remote access** — zero-signup Cloudflare quick tunnel built & tested (`ops-hub/scripts/start_remote.sh`); Tailscale recommended as the real daily-use option (needs your signup, see `docs/remote_access.md`)
- ✅ **Monitoring** — local `ops-hub/scripts/new_case_check.py` (cron-able, no cloud dependency) surfaces new/changed cases in the what/why + done-vs-left format; cloud auto-monitoring isn't possible (see `docs/monitoring.md` for why)
- **Run it:** `cd ops-hub && python3 run.py` → http://127.0.0.1:5000 (home page is now the Daily Queue)

## B. GBP / local SEO — ✅ complete
- ✅ Audit checklist/scoring tool, 10 real Perth WA target businesses, content calendar, 3 outreach scripts, pricing sheet, Australia-wide positioning

## C. Review generation — ✅ complete
- ✅ Templates (ACL-compliant), tool research (NiceJob recommended)

## D. AI missed-call reception — ✅ complete
- ✅ Platform research, call-log checklist, pricing sheet

## E. Land tax / rates objection — ✅ complete
- ✅ All 8 states/territories, objection letter template, comps checklist, state-aware deadline logic

## Wave 2 prep — ✅ complete
- ✅ Bookkeeping, concessions, grant-finder, pension — all checklists/templates/research built (see prior entries below for detail)

## F. Pricing table expansion (2026-07-30) — 🔶 partial by design
- ✅ `PRICING.md` — your full 17-business rate table, reconciled with existing pricing sheets
- ✅ All 9 new business lines wired into the hub schema + rate card — priced, filterable, ranked in the queue
- ✅ Competitor pricing research for the 4 live Wave 1 businesses — `docs/competitor_pricing_research.md`
- ✅ ReviewGen and LandTax pricing sheets filled in from that research
- ✅ **4 of the 9 new lines fully built out** (low regulatory risk): Senior Tech Concierge, Video/Podcast Repurposing, Senior Downsizing/Cleanout, Lost Super/TPD Navigation (referral model, with a compliance note on financial-services referral-fee disclosure) — service scope + pricing under `wave3-unscoped/<line>/`
- ⛔ **Airbnb Co-Hosting — likely blocked, not built.** Research (`wave3-unscoped/airbnb_cohost/regulatory_research.md`) found paid co-hosting almost certainly needs a real estate/property agent licence in most states — QLD and VIC have actual prosecution precedent for unlicensed operators doing exactly this. WA (your state) has the same statutory pattern. Didn't build sales material for a business that may be illegal to run without a licence you don't have — real next step is confirming with a property lawyer, not templates.
- ⛔ **5 lines deliberately still held**: Airbnb Co-Hosting (above), Deceased-Estate Admin, Grant Writing (needs a portfolio first per your own pricing note anyway), NDIS Plan Navigation, NDIS Provider Compliance/Audit-Prep — these touch real regulatory frameworks where building client-facing assets needs your explicit scope/qualifications confirmation first, not a reasonable-assumption default. See DECISIONS.md 2026-07-30 entries.

---

## Things only you can do (this is the real punch list)

1. **Sign up for Tailscale** (free) if you want permanent remote access from your phone — see `docs/remote_access.md`. The zero-signup Cloudflare tunnel works tonight but the URL is public and changes every restart.
2. **Set `HUB_PASSWORD`** before using either remote-access option — the hub has no login until you do.
3. **Pick and sign up for an AI phone/reception platform** (`wave1/missedcall/platform_research.md`) and give me the API key to activate the webhook.
4. **Pick and sign up for a review-automation tool** (`wave1/reviewgen/tool_research.md` — NiceJob recommended).
5. **Pick accounting software (Xero or QBO)** for bookkeeping — clients invite you into theirs, you generally don't pay.
6. **Review the pricing** — GBP/MissedCall unchanged, and ReviewGen + LandTax now have full pricing sheets built from competitor research (`wave1/reviewgen/pricing_sheet.md`, `wave1/landtax/pricing_sheet.md`) — land tax specifically found zero public competitor pricing anywhere, so that price point is a judgment call worth your sign-off before quoting a real client.
7. **Review every draft template before client use** — none are legally vetted.
8. **Re-verify research docs with "unverified" flags** before relying on them (search each file for the word).
9. **If you're serious about Airbnb co-hosting: talk to a property/real estate lawyer first** — the research points to a real estate licence requirement in most states including WA. Don't market this until that's confirmed either way.
10. **Decide if/when to pursue the 4 still-held business lines** (Deceased-Estate Admin, Grant Writing, NDIS Nav, NDIS Compliance) — each needs an explicit scope/qualifications conversation before I'd build client-facing assets for them.
11. **Fill in `done_summary`/`left_for_you_summary`/`source_url` on cases as you create them** — the monitoring script and case-detail view are only as useful as these fields; blank ones just say "no summary set yet."

## How to pick this back up

- Run the hub (`cd ops-hub && python3 run.py`) — home page is now the Daily Queue, sorted by $/hr.
- Every business line's assets live under `wave1/<line>/` or `wave2/<line>/`.
- `DECISIONS.md` has the full reasoning log — read it before assuming something was guessed carelessly.
- `docs/remote_access.md` and `docs/monitoring.md` explain the two newest pieces in detail.
