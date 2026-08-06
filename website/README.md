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

1. **Local Presence** — GBP + Review Generation
2. **Never Miss a Call** — AI Missed-Call Reception
3. **Property & Tax Review** — Land Tax Objection

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

## Not yet done

- **Actually deployed** — code/config is ready (`render.yaml`, `wsgi.py`,
  `requirements.txt`, `docs/website_deployment.md`), but nobody's clicked
  deploy yet. That needs a GitHub push + a Render account (your own
  account/payment — see the deployment doc).
- **Domain name** — not registered yet; going with a global `.com` per your
  call (not `.com.au`, since `.com.au` needs an ASIC business-name
  registration first and you want worldwide reach anyway).
- Visual QA of the landing-page hover animation — verified structurally
  (DOM, class toggling, CSS rules present and correctly scoped) but the
  actual fade transition couldn't be visually confirmed in this session's
  browser-testing sandbox (it doesn't run a real compositor). Worth a
  quick look in an actual browser before relying on it.
