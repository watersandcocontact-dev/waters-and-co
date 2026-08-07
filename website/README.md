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

- Landing page (`/`) — just the wordmark. Hover (or tap, on touch devices)
  fades the mark and reveals the 3 segments.
- Segment pages (`/segment/<slug>`) — the services grouped under that segment.
- Service pages (`/service/<slug>`) — real pricing (from `webapp/config.py`,
  sourced from `wave1/*/pricing_sheet.md`) + a contact form.
- General enquiry (`/enquire`) — the "don't see what you need?" catch-all,
  linked from every page's footer and the landing page.

## Segments (current grouping — change in `webapp/config.py` if wrong)

**Updated 2026-08-07 — this section was stale, out of sync with the actual
code since the 2026-08-06 restructure. Verify against `webapp/config.py`'s
`SEGMENTS` list directly if in doubt, not this file, since docs drift.**

5 segments, 16 services, in this landing-page order:

1. **Small Business Support** — two sub-groups: "Local Presence & Never Miss
   a Call" (GBP, ReviewGen, MissedCall) and "Books & Grants" (Bookkeeping,
   GrantFinder).
2. **AI Systems for Business** — AI Implementation, AI Tools for Business,
   AI Lead-Response for Real Estate Agents, plus GBP/ReviewGen/MissedCall
   cross-listed here too (audience overlap with segment 1).
3. **Seniors & Family Support** — Tech Concierge, Crypto Literacy, Digital
   Legacy, Downsizing (coordination + labour), Photo & Memory Digitisation.
4. **Content Repurposing** — Video/Podcast Repurposing.
5. **Property & Tax Review** — Land Tax / Rates Objection.

(Lost Super was removed from the public site 2026-08-06 — it's free to the
client, revenue is referral-fee only, not worth a landing-page slot. Still
fully trackable internally via the hub's `LostSuper` business_line.)

## Contact form → hub → draft email

Every submission (service-specific or general enquiry):
1. Creates a Lead in the hub, tagged to the right `business_line`
   (or `GeneralEnquiry` for the catch-all).
2. Generates a template-based draft reply (`webapp/draft_email.py` —
   deterministic, no AI API call, no cost) referencing the specific service
   and its real pricing.
3. Appends that draft to the lead's Notes field in the hub, clearly marked
   "DRAFTED REPLY (review before sending)".

**Nothing is sent automatically.** Review the draft in the hub's case
detail page and send it yourself (or ask Claude to review/refine it in a
session) — sending messages needs a human decision each time, and there's
no email-sending account configured anyway.

No phone number is shown anywhere on the site by design — every page pushes
toward the contact form instead of a call.

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

Font files (`static/fonts/`) and the color system (`static/style.css`)
match the Waters & Co brand concept — deep slate green (`#182019`), gold
(`#c7a459`), Fraunces for display type (switched from Cormorant 2026-07-31
after comparing options), Jost for labels. Single dark theme by design,
same reasoning as the original brand concept artifact: the identity *is*
the dark ground.

## Status — LIVE

**Deployed and live at [watersandco.info](https://watersandco.info) since
2026-08-07.** Full deployment walkthrough (Tailscale Funnel, Render,
Cloudflare DNS) in `docs/website_deployment.md`; the real gotchas hit along
the way are logged in `DECISIONS.md`'s 2026-08-07 entries — worth reading
before touching the deploy chain again, several non-obvious things bit us
(Funnel path-stripping, Render env-var overwrite, a `HUB_HOST`
localhost-vs-Tailscale-IP binding mismatch that silently 502'd every real
webhook call for a while).

Real bug fixed 2026-08-07 (see `webapp/routes.py`/`webapp/hub_bridge.py`):
a hub-unreachable failure on the contact form used to surface as a bare,
unbranded Flask 500 with the visitor's submission completely lost. Now
caught explicitly (`HubUnreachableError`), logged to
`website/failed_submissions.log` (gitignored — check it if a visitor
reports an error) so nothing's silently dropped, and the visitor sees a
proper branded message pointing them to a fallback email address.

## Known gaps, not yet addressed

- No CSRF token or spam mitigation (honeypot/rate-limit) on the two POST
  forms. Low severity for a public marketing form, but every submission
  creates a real record in the Daily Queue — an automated spam run could
  pollute it. Worth a lightweight honeypot field if it becomes a problem.
- Visual QA of the landing-page hover animation — verified structurally
  (DOM, class toggling, CSS rules present and correctly scoped) but the
  actual fade transition couldn't be visually confirmed in earlier
  browser-testing sessions (sandbox didn't run a real compositor). Worth a
  quick look in an actual browser if it ever seems off.
