# v1 vs v2 — Master Handover comparison (2026-08-09)

Both files were delivered by the Owner on 2026-08-09:
- **v1** = `v1/Waters-and-Co-Master-Handover-2026-08-09.pdf` (27 pages)
- **v2** = `v2/Waters-and-Co-Website-and-Master-Handover-2026-08-09.zip`
  (contains `HANDOVER/` — the same PDF + a .docx — and `website/`, a full
  Flask site source)

Confirmed by md5sum: **the handover PDF inside v2 is byte-identical to v1.**
So there is no strategy-document diff to report — v1 and v2 tell the exact
same story. The only real difference is that **v2 also ships a working
website** that implements what the document describes. "Both formed from
the same data" checks out: this handover references this repo directly
(`worksite/CLAUDE.md`, `worksite/PRICING.md`, `worksite/website/`) and its
§10 "Applied lessons from eight videos" is an independent synthesis of the
same 8 YouTube videos processed into `docs/video-intel/` yesterday — a
different session did its own pass over the same inputs and went further:
it produced a full governance document (pricing, compliance, risk, decision
gates, 90-day roadmap, source register with regulator URLs) and rebuilt the
site to match it.

## What the document actually proposes

Not a demolition of the 25-line catalogue. The executive decision keeps the
full service list but stops promoting it as "all services equally":
**lead with one narrow commercial wedge** — Local Visibility Check → Never
Miss the Next Enquiry → Practical AI Workflow Pilot → Managed monitoring —
prove it with paid pilots, expand after. This lines up closely with the
**T6 flagship-focus theme** already written into
[`docs/video-intel/waters-co-implementation-plan.md`](../../video-intel/waters-co-implementation-plan.md)
from the video-intel work — two independent passes over the same source
material converged on the same "narrow first, prove it, then expand" call.

The document goes further than my implementation plan into pure operating
detail: fixed (not ranged) pricing tied to PRICING.md, an explicit AI-agent
autonomy ladder (0 Observe → 4 Expand), a weekly scorecard with continue/
change/stop gates, and an Appendix A source register with live ABS/ACMA/
OAIC/ACCC/AUSTRAC URLs for the regulatory claims.

## What v2's website actually changes vs the currently live `website/`

Diffed directly against this repo's `website/` (excluding `__pycache__`):

| File | Change |
|---|---|
| `webapp/config.py` | Every price range (`"$150–300"`) replaced with the exact fixed prices from handover §5 (`"$99 fixed"`, `"$349 fixed"`, etc.) — makes the site match the document instead of drifting from it |
| `webapp/routes.py` | Enquiry form gains an `interest` field, prefixed onto the internal lead message |
| `templates/landing.html` | New hero ("Fix the workflow that is costing your business time or enquiries"), new "Three practical entry points" section implementing the wedge, tweaked why-us copy |
| `templates/enquire.html`, `about.html`, `how_we_work.html`, `service.html` | Matching copy/field updates |
| `static/overrides.css`, `static/img/og-banner.png` | Supporting style + OG image tweaks |

Verified live: stood the v2 site up standalone (`SITE_PORT=5052`) and
browsed it — renders cleanly, malachite/gold brand intact, no console
errors, missed-call service page shows the new fixed pricing and a working
FAQ/process/who-it's-for layout, enquiry form carries the new interest
selector.

## One regression found

`templates/landing.html`'s "Why Waters & Co" copy in v2 reads **"A
solo-run Australian service business..."** — but earlier tonight (session
memory, 01:28) you explicitly asked to have the "solo-run" reference
removed from that exact page, and it was committed and verified live. v2
was built from an earlier snapshot and doesn't reflect that decision. It's
a one-line fix, not a reason to reject the rest of v2 — just needs applying
before anything from v2 goes live.

## Verdict

**v2 is the one to act on** — same strategy, plus a working implementation
of it, plus it independently arrived at the same "narrow wedge first"
conclusion as the video-intel plan. v1 (the standalone PDF) adds nothing v2
doesn't already contain.

Nothing from v2 has been merged into the live `website/` yet — pricing and
copy changes are outward-facing, so that's a confirm-before-I-act item per
house rules. If you want it in: I'd (1) fix the solo-run line, (2) merge
the fixed-pricing `config.py` values against current `PRICING.md`, (3)
bring in the new hero + three-entry-point section, (4) add the interest
field to the enquiry flow, (5) run the existing test suite before pushing.
