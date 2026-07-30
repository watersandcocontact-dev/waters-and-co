# PROGRESS.md — live status

Last updated: 2026-07-29 — **Wave 1 fully built, Wave 2 prep fully built. Everything on the original list is done.**

## Legend
✅ done · 🔶 partial · ⛔ blocked (needs you)

## A. Central ops hub — ✅ complete
- ✅ Data model (SQLite schema, all 8 business lines incl. Wave 2 tags) — `ops-hub/app/config.py`, `db.py`
- ✅ Web dashboard (list + filter by line/status + "due this week" view) — tested end-to-end
- ✅ Manual lead-entry form, with per-business-line dynamic fields
- ✅ Intake webhook receiver — built, safely inactive (503 until you set `INTAKE_WEBHOOK_ENABLED`/`INTAKE_WEBHOOK_SECRET`; see `ops-hub/README.md`)
- ✅ Deadline-alert mechanism — dashboard banner (14/30/60 day + overdue), state-aware for land tax (NT = 30 days, all others = 60, see DECISIONS.md)
- ✅ Optional desktop-notification cron script (`ops-hub/scripts/deadline_check.py`, uses `notify-send`, no signup)
- **Run it:** `cd ops-hub && python3 run.py` → http://127.0.0.1:5000

## B. GBP / local SEO — ✅ complete
- ✅ Audit checklist/scoring tool (`wave1/gbp/audit_checklist.md`, `audit_tool.py` — tested)
- ✅ 10 real target trade businesses in **Perth, WA** (`wave1/gbp/target_businesses_perth.md` — your confirmed city). A placeholder Melbourne list also exists (`target_businesses.md`) from before you confirmed location — kept for reference only, not operational.
- ✅ Content-calendar template, 3 outreach scripts (call/in-person/text-email), pricing sheet

## C. Review generation — ✅ complete
- ✅ Review-request templates (ACL-compliant — no incentives/gating, guardrails documented)
- ✅ AI-response templates (5★/3★/1★ + 2 more variants)
- ✅ Tool research (`tool_research.md`) — NiceJob, Podium, GatherUp compared; NiceJob recommended as starting point

## D. AI missed-call reception — ✅ complete
- ✅ Platform research (`platform_research.md`) — Smith.ai, My AI Front Desk, Dialzara, Retell AI+Twilio compared
- ✅ Call-log review checklist (daily/weekly process + edge cases)
- ✅ Pricing sheet

## E. Land tax / rates objection — ✅ complete
- ✅ Per-state reference docs, all 8 states/territories (`wave1/landtax/state_*.md`)
- ✅ Objection letter template (reusable, flags where your/client signature or portal login is required)
- ✅ Comps-research checklist (per-state free/public sources)
- ✅ Deadline logic in hub — auto-calculates from `valuation_notice_date`, state-aware (60 days default, 30 for NT — tested both)

## Wave 2 prep — ✅ complete
- ✅ Bookkeeping — onboarding checklist, monthly reconciliation checklist, Xero/QBO bank-feed research (BAS lodgement explicitly flagged out of scope, no TPB registration)
- ✅ Concession/rebate eligibility matrix — all 8 states, energy/rates/seniors programs (flagged informational/navigation only)
- ✅ SME grant-finder — business.gov.au monitoring research, eligibility-screening checklist, application-drafting template
- ✅ Age Pension/Centrelink — document checklist, ARO review letter template (13-week point specifically verified, not assumed — see the template file for the nuance)
- ✅ Hub schema already includes all 4 Wave 2 business-line tags and their extra fields (done as part of Wave 1's schema work, so no migration needed when you launch these)

---

## Things only you can do (this is the real punch list)

1. **Pick and sign up for an AI phone/reception platform** (see `wave1/missedcall/platform_research.md` for the shortlist — Smith.ai, My AI Front Desk, Dialzara, or Retell AI+Twilio) and give me the API key/webhook secret so I can activate `ops-hub/app/webhook.py`.
2. **Pick and sign up for a review-automation tool** (see `wave1/reviewgen/tool_research.md` — NiceJob recommended as a starting point).
3. **Pick accounting software (Xero or QBO)** if you want to run the bookkeeping service — see `wave2/bookkeeping/bank_feed_research.md`. Note: clients invite you into *their* subscription; you generally don't need to pay for your own.
4. **Review every draft template before using it with a real client** — none of these are legally vetted: the land tax objection letter, the ARO review letter, the review-request templates, and the AI response templates. They're solid starting drafts, not final client-facing copy.
5. **Re-verify the research docs before relying on them** — several files have explicit "unverified" flags where a government page blocked automated access or sources conflicted (notably: VIC's land.vic.gov.au objection page, WA/NSW/QLD energy rebate dollar amounts which are budget-indexed and conflicted across sources, NT's escalation-path ambiguity, and the exact ART/ARO time-limit wording). Search each file for "unverified" or "flagged" to find these before client-facing use.
6. **Re-verify the 20 GBP target businesses** (10 Perth, 10 Melbourne-reference) immediately before outreach — profiles change, and this is desk research from 29 July 2026.
7. Everything else is done and ready to use as-is.

## How to pick this back up

- Run the hub (`cd ops-hub && python3 run.py`) to start actually logging real leads.
- Every business line's assets live under `wave1/<line>/` or `wave2/<line>/`.
- `DECISIONS.md` has the full reasoning log for every assumption made along the way — read it before assuming something was guessed carelessly.
