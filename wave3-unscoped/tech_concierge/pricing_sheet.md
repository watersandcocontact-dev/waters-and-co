# Senior Tech Concierge — Pricing Sheet

## Pricing (raised 2026-08-09 — Owner's call)

| Session type | Price | Was |
|---|---|---|
| Standard session (up to 1hr, in-person) | **$99** | $79 |
| Standard session (up to 1hr, remote/screen-share) | **$69** | $59 |
| Extended session (up to 90min, multiple devices/complex setup) | **$145** | $119 |
| Follow-up/check-in (up to 30min, remote) | **$49** | $45 |

Effective rates: in-person $99/hr, extended $97/hr, remote $69/hr,
follow-up $98/hr-equivalent.

**The 30-minute follow-up is the wedge — keep it cheap and keep it
prominent.** The live site's promise of "no one-hour minimums" is the single
sharpest differentiator this line has, because the two premium competitors
both enforce one (Geeks2U explicitly; My Senior IT markets directly against
"others demand up to $198 for a minimum one-hour booking"). It was raised
only $4 for that reason. Do not add a call-out fee — it would contradict
live website copy and destroy the differentiator.

## Why in-person and remote moved differently

They compete in different markets, which the previous version of this sheet
did not separate:

- **In-person is Perth-only** (travel radius). The real local alternatives
  are Geeks2U at **$158/hr** and IT 4 Retirees at **$162/hr + $73/hr
  travel** — both national operators with Perth coverage. Against those,
  $99 is a **~37–55% undercut** and still comfortably clear of the Airtasker
  gig floor. Plenty of headroom.
- **Remote is Australia-wide**, so it competes against every interstate
  senior specialist — a much denser, cheaper field clustering at
  **$59–100/hr**. $69 keeps the undercut intact there. Pushing remote to $99
  would put it at the top of that cluster with nothing to justify it, since
  there is no travel cost to recover.

## Competitor evidence (re-verified live 2026-08-09)

| Competitor | Price | Market | Note |
|---|---|---|---|
| **Geeks2U** | **$158/hr Home**, $198/hr Business, **1hr minimum** | National incl. Perth | Re-confirmed direct from geeks2u.com.au/pricing 2026-08-09. Minimum exists so they don't charge travel separately |
| **IT 4 Retirees** | $162/hr **+ $73/hr travel**; group class $275/hr | Over-55 focus, has Perth trainers | ~$235/hr effective with travel — the most expensive comparable |
| **Seniors Tech and Tea** | **$129/hr**, discount for Seniors Card holders | AU | New datapoint 2026-08-09 |
| **My Senior IT** | $50/30min (**~$100/hr**) | AU | Explicitly markets against one-hour minimums |
| **IT Help at Home** | **$90/hr** senior rate (25% off their $120 standard) | Brisbane | New datapoint 2026-08-09 |
| **Fixable** | **$89/hr flat, no call-out fee** | Melbourne | New datapoint 2026-08-09 — closest positioning match found |
| **Dtech** | **from $59/hr**, pensioner/senior concession | Melbourne | New datapoint 2026-08-09 — the national floor |
| Tech 4 Seniors | $50/hr | AU | Floor |
| Computer Cures | ~$75/session; ~$228/yr membership | AU | Session-based, like ours |
| The Original PC Doctor | Diagnostic $0–99; malware removal $120–200 | AU | Task-priced, not hourly |
| Airtasker (Perth) | $10–100 typical, up to $200 full home visit | Perth | Gig floor — stay above it to avoid reading as hobbyist |

**Correction retained from 2026-08-06:** Geeks2U's "$198 minimum" is their
*Business* rate. The consumer *Home* rate is **$158/hr**. Use $158 in any
client-facing comparison — quoting $198 against a residential prospect is
overstating it and would be caught.

## Reasoning

At $99, in-person sits **~37% below Geeks2U's $158** and **~58% below IT 4
Retirees' effective $235 with travel** — the two operators a Perth senior
would actually otherwise call. The teaching-and-scam-safety framing (not
generic PC repair) plus no one-hour minimum carries the rest.

The honest trade-off the Owner should know: **$99 does move in-person above
the interstate senior-specialist cluster** (Fixable $89, IT Help at Home
$90, My Senior IT ~$100). That is acceptable because those operators do not
serve Perth in-person — but it is the reason remote was held at $69 rather
than moved in step. If remote ever becomes the main channel, revisit.

## Notes

- Multi-session pack (e.g. 3 for $270 at the new rate) still a good idea for
  repeat clients — not yet offered.
- Service area: in-person is local Perth (travel radius); remote is
  Australia-wide.
- No client has been charged at either the old or new rate yet — this line
  has no delivery history, so the time-per-session assumptions behind the
  extended/follow-up tiers remain estimates.

## Status

**RAISED 2026-08-09 at the Owner's request**, verified against live
competitor pricing the same day (4 new competitors found that were not in
the 2026-08-06 pass; Geeks2U re-confirmed direct from source). `PRICING.md`
row 13, `ops-hub/app/config.py` RATE_CARD, and `website/webapp/config.py`
all updated to match.

**NOT deployed to the live site** — `watersandco.info` still shows the old
$79/$59/$119/$45 until the Owner pushes. See DECISIONS.md 2026-08-09.
