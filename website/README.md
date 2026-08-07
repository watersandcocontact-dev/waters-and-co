# Waters & Co — public website

Public marketing site, separate from the internal ops hub but writing into
the same lead database (`ops-hub/data/hub.sqlite3`) — every enquiry lands
in the same place as every other lead, tagged `source: website`.

Two modes, switched by the `HUB_MODE` env var (default `local`): local
development uses a direct Python import of the hub's `models.py` (both
apps on the same machine, same SQLite file); production (`HUB_MODE=remote`,
what Render uses) calls an authenticated webhook on the hub instead, since
a deployed website can't reach a local file/import. **See
`docs/website_deployment.md` for the full deployment walkthrough** —
Tailscale Funnel setup, Render config, DNS.

## Structure

**Rebuilt 2026-08-08** from a flat 5-segment structure to 4 practices, per
`docs/deep_research_growth_seo_ai_blueprint_2026-08-07.md` — see
`docs/implementation_workbook_2026-08-08.md` for the full build record.
This section reflects the rebuilt structure directly; verify against
`webapp/config.py`'s `PRACTICES`/`SERVICES` if in doubt, not this file.

- Landing page (`/`) — hero + a card per practice.
- Practice pages (`/<practice-slug>/`) — the services grouped under that
  practice (some practices sub-group with a heading, e.g. small-business
  splits "Get Found & Never Miss a Call" from "Books & Grants").
- Service pages (`/<practice-slug>/<service-slug>/`) — real pricing (from
  `webapp/config.py`, sourced from `wave1/*/pricing_sheet.md`) + a contact
  form. The 5 blueprint-flagged priority services (GBP, AI Tools for
  Business, AI Missed-Call Reception, AI Implementation for SMEs, Review
  Management) also carry who-it's-for/isn't-for, real process steps and
  FAQs — the template renders these sections only when present, so the
  other 11 services are unaffected.
- General enquiry (`/enquire`) — the "don't see what you need?" catch-all,
  linked from every page's footer and the landing page.
- About (`/about/`), How We Work (`/how-we-work/`), Privacy (`/privacy/`),
  Terms (`/terms/`) — new 2026-08-08, the site had none of these before.

**Every pre-2026-08-08 URL still works** — `/segment/<old-slug>` and
`/service/<old-slug>` both 301-redirect to the new URL (the old contact POST
route 307-redirects, preserving the form body). See `config.py`'s
`OLD_SEGMENT_REDIRECTS`/`OLD_SERVICE_REDIRECTS` for the full old→new map.

## Practices (current grouping — change in `webapp/config.py` if wrong)

4 practices, 16 services, in landing-page order:

1. **Local Business Growth** (`/small-business/`) — two sub-groups: "Get
   Found & Never Miss a Call" (GBP, ReviewGen, MissedCall) and "Books &
   Grants" (Bookkeeping, GrantFinder).
2. **AI Solutions for Small Business** (`/ai-solutions/`) — AI
   Implementation, AI Tools for Business, AI Lead-Response for Real Estate
   Agents. No longer cross-lists GBP/ReviewGen/MissedCall here (dropped in
   the 2026-08-08 rebuild — one clear home per service, matching the
   blueprint's own sitemap).
3. **Personal Digital Support** (`/personal-digital-support/`) — Age
   Pension/Centrelink, Tech Concierge, Crypto Literacy, Digital Legacy,
   Downsizing (coordination + labour), Photo & Memory Digitisation.
4. **Specialist Projects** (`/specialist-projects/`) — Video/Podcast
   Repurposing, Land Tax / Rates Objection.

(Lost Super was removed from the public site 2026-08-06 — it's free to the
client, revenue is referral-fee only, not worth a landing-page slot. Still
fully trackable internally via the hub's `LostSuper` business_line.)

## Contact form → hub → draft email

Every submission (service-specific or general enquiry):
1. Two spam checks first (`_is_spam()` in `routes.py`): a honeypot field
   real visitors never see/fill, and a minimum 2-second time-on-page.
   Either one fails silently — redirects to `/thanks` exactly like a real
   success, no signal to a bot that it was caught. Blocked attempts logged
   to `website/spam_blocked.log` (gitignored).
2. Creates a Lead in the hub, tagged to the right `business_line`
   (or `GeneralEnquiry` for the catch-all).
3. Generates a template-based draft reply (`webapp/draft_email.py` —
   deterministic, no AI API call, no cost) referencing the specific service
   and its real pricing.
4. Appends that draft to the lead's Notes field in the hub, clearly marked
   "DRAFTED REPLY (review before sending)".

**Nothing is sent automatically.** Review the draft in the hub's case
detail page and send it yourself (or ask Claude to review/refine it in a
session) — sending messages needs a human decision each time, and there's
no email-sending account configured anyway.

No phone number is shown anywhere on the site by design — every page pushes
toward the contact form instead of a call.

## Structured data

Every page carries a site-wide `ProfessionalService` JSON-LD block
(`webapp/structured_data.py`). Service pages add a `Service` block with
pricing (numeric `PriceSpecification` only for clean single-clause prices —
multi-clause pricing like "$45-65/hr, or $400-1,200 packaged" stays as free
text rather than risk a misleading number) plus a `BreadcrumbList`.
Practice/enquire/about/how-we-work/privacy/terms pages carry a
`BreadcrumbList` only.

## Run it (local development)

```bash
cd website
python3 run.py
```

Opens on **port 5050** (the ops hub uses 5000 — run both side by side, the
hub needs to be running for the contact form to actually save leads, since
local mode imports the hub's `models.py` directly rather than going over
HTTP). For production deployment (Render), see `docs/website_deployment.md`
— the app needs `HUB_MODE=remote` plus `HUB_WEBHOOK_URL`/`HUB_WEBHOOK_SECRET`
instead, since a deployed site can't import local files.

## Branding

Font files (`static/fonts/`) and the color system (`static/style.css`,
`static/overrides.css`) match the Waters & Co brand concept — deep slate
green (`#182019`), gold (`#D4AF37`/`#e3c787`), Fraunces for display type,
Jost for labels. Single dark theme by design, malachite background image.

## Status — LIVE

**Deployed and live at [watersandco.info](https://watersandco.info) since
2026-08-07.** The 2026-08-08 practice/AI rebuild described above is on the
`ai-practices-rebuild` branch, demoed but **not yet merged/deployed** —
check `git log`/the current branch before assuming it's live. Full
deployment walkthrough (Tailscale Funnel, Render, Cloudflare DNS) in
`docs/website_deployment.md`; deploy gotchas logged in `DECISIONS.md`'s
2026-08-07 entries.

Real bug fixed 2026-08-07 (see `webapp/routes.py`/`webapp/hub_bridge.py`):
a hub-unreachable failure on the contact form used to surface as a bare,
unbranded Flask 500 with the visitor's submission completely lost. Now
caught explicitly (`HubUnreachableError`), logged to
`website/failed_submissions.log` (gitignored — check it if a visitor
reports an error) so nothing's silently dropped, and the visitor sees a
proper branded message pointing them to a fallback email address.

## Known gaps, not yet addressed

- No CSRF token on the two POST forms. Low severity for a public marketing
  form with no session/account state to forge, and the honeypot + timing
  check (above) already covers the actual observed risk (bots), not a
  targeted CSRF attack scenario.
- The 21-article content cluster from the blueprint (`docs/
  deep_research_growth_seo_ai_blueprint_2026-08-07.md` §5.3) is
  deliberately not written yet — no Search Console/Keyword Planner access
  to validate demand first. Full title list kept in
  `docs/implementation_workbook_2026-08-08.md` §4.
- The 11 non-priority services don't have the upgraded who-for/process/FAQ
  content the 5 priority ones do — same "prove it's worth it first"
  reasoning.
