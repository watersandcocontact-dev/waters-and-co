# Waters & Co — public website

Public marketing site, separate from the internal ops hub but writing into
the same lead database (`ops-hub/data/hub.sqlite3`) via a direct import of
the hub's `models.create_lead()` — every enquiry lands in the same place as
every other lead, tagged `source: website`.

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

## Run it

```bash
cd website
python3 run.py
```

Opens on **port 5050** (the ops hub uses 5000 — run both side by side, the
hub needs to be running for the contact form to actually save leads, since
this app imports the hub's `models.py` directly rather than going over
HTTP).

## Branding

Font files (`static/fonts/`) and the color system (`static/style.css`)
match the Waters & Co brand concept — deep slate green (`#182019`), gold
(`#c7a459`), Cormorant for display type, Jost for labels. Single dark theme
by design, same reasoning as the original brand concept artifact: the
identity *is* the dark ground.

## Not yet done

- **Hosting/deployment** — this runs locally only right now. See
  `ROADMAP.md`'s accounts table for the hosting recommendation
  (Netlify/Vercel free tier) — but note that recommendation assumed a
  purely static site; a live contact-form backend needs either serverless
  functions on those platforms or a small always-on host instead. Revisit
  when ready to actually go public.
- **Domain name** — not registered.
- Visual QA of the landing-page hover animation — verified structurally
  (DOM, class toggling, CSS rules present and correctly scoped) but the
  actual fade transition couldn't be visually confirmed in this session's
  browser-testing sandbox (it doesn't run a real compositor). Worth a
  quick look in an actual browser before relying on it.
