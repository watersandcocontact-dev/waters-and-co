# AI Search Visibility Audit — Service Scope

Checking whether a local business actually gets recommended when someone
asks ChatGPT, Gemini, Perplexity or Google's AI Overviews for "a good
[trade] near me" — and fixing the reasons it doesn't. Delivered as a
flat-fee written audit plus a prioritised fix list, reusing the existing
GBP / ReviewGen / MissedCall client base and the same report-and-action-plan
delivery format already used by LandTax and GrantFinder.

**Scored 32/35 on 2026-08-09** (see `opportunity_scan/candidates_log.md`).
No licence, registration or qualification is required to deliver this — it
is in the same low-regulatory class as Crypto Literacy and AI Tools for
Business, not the held NDIS/Deceased-Estate lines.

## The open question the Owner needs to settle first

**This may be better as a GBP tier than as its own business line.** The
measurement half is genuinely new work, but the fix half — Google Business
Profile consistency, NAP accuracy across directories, review signals,
schema markup — is substantially what the existing **GBP / Local SEO** line
already does. Two defensible options:

1. **Own line** (`AISearchVisibility` key) — cleaner to market, matches how
   competitors package it, gives it its own website entry point.
2. **A `task_type` on GBP** (`audit` alongside `setup`/`management`) —
   the precedent being the 2026-08-06 Downsizing `coordination`/`labour`
   split, and the Concession re-classification into a bundled add-on.

**Recommendation revised to option 2 (a GBP tier), on evidence found after
the first draft.** The v2 handover pricing (uncommitted in the working tree
as at 2026-08-09) gives GBP a **$99 fixed "Visibility check and action
plan"** — the site's "Local Visibility Check" wedge offer, described as a
low-risk diagnostic that reviews the Google Business Profile, website
journey, contact path, review signals and local-search gaps, delivers a
ranked action plan, and explicitly does not promise ranking positions.

That is the *same product shape* as this audit: fixed fee, diagnostic,
ranked action plan, no outcome promises. The overlap in deliverable is
substantial — both review GBP, review signals, and the website. The only
genuinely new component here is live prompt testing across the AI
platforms and the entity/citation angle.

Two consequences the Owner should weigh:

1. **Pricing-ladder risk.** A $99 GBP visibility check sitting next to a
   $249–349 AI visibility audit invites the obvious question of what the
   extra $150–250 buys, and the honest answer is "the AI platform testing
   and entity work" — not a different class of service. Cleaner to present
   as one ladder: **$99 local visibility check → $249–349 the same check
   plus AI platform testing** than as two competing products.
2. **It makes the "rebranded SEO" objection concrete.** If the business
   itself sells a $99 check covering most of the same ground, charging
   $349 for a version with prompt testing bolted on has to be justifiable
   line by line.

Original argument for option 1 (competitors package it standalone with its
own lead magnet) still stands and is not worthless — but the existing $99
wedge is a stronger, closer precedent than a competitor's packaging.
Flagging rather than deciding: this is the Owner's call, and nothing has
been wired into `ops-hub/app/config.py` either way.

## What's actually delivered

- **Live AI platform testing** — running a fixed set of real buyer-intent
  prompts ("best emergency plumber Perth," "who should I call for
  [service] in [suburb]") across ChatGPT, Gemini and Perplexity, and
  recording whether the client appears, what's said about them, and who
  gets recommended instead
- **Competitor comparison** — the same prompts, showing which local
  competitors the AI names and, more usefully, *why* (what those
  competitors have that the client doesn't)
- **Google Business Profile assessment** — completeness, category
  accuracy, service-area setup, photo and post recency, Q&A
- **Entity and NAP consistency check** — name/address/phone agreement
  across the directories AI systems actually draw on; inconsistency here is
  a common, cheap-to-fix reason a business gets skipped
- **Review and reputation signals** — volume, recency, response rate, and
  how the review text itself reads to a model summarising it
- **Technical page health** — schema markup, headings, meta data, page
  structure; whether the site states plainly what the business does, where,
  and for whom
- **Plain-English findings report + prioritised 90-day action plan** —
  ranked by impact-over-effort, written so the client can hand it to
  anyone, including a different provider

## Client base and channel reuse

This is the strongest reuse case scored so far. Every existing **GBP**,
**ReviewGen** and **MissedCall** client is a warm prospect who has already
paid for local visibility work — the audit is a natural next conversation,
not a cold sell. It also runs the other way: the free snapshot is a
low-friction opener that surfaces GBP and ReviewGen problems, which are
existing paid lines.

Website-wise it belongs under the existing **Small Business Support** /
**AI Systems for Business** segments; no new segment needed.

## Market evidence (checked 2026-08-09, all figures fetched live)

The market is **real, priced, and already contested at the local tier** —
this is not an empty gap, and the scope doc should not pretend otherwise.

| Who | What | Price found |
|---|---|---|
| **SocialPulse247** — Perth-based, targets "trades, pet services, professional services, local services" | Free "AI Search Visibility Snapshot", paid "AI Search Visibility Audit" | **$497** |
| **AI Local Link** — SE QLD + Australia-wide, targets trades/legal/medical/real estate | "Premium AI Visibility Audit", single-location; free snapshot in 48hr | **$299** |
| **AIReady Australia** — sole traders and 2–10 person teams | Flat-fee AI readiness audit, 5 business days | **$497** |
| AU AEO/GEO agencies (Talons, Prosperity, Rocket, WebProfits et al.) | Ongoing retainers | **$3,000–$15,000/mo**; starter ~$2,500/mo |
| AU SEO market generally (StudioHawk) | Hourly / project audit | $150–300/hr; $2,000–10,000 per project audit |
| SeekON.AI | Self-serve automated audit, 3 keywords / 3 sites | **$27 one-time**, free tier |
| Searchable | Self-serve ongoing tracking, 100 prompts | **$125/mo** |

**What the shape of that table means:** the market is barbelled — a $27
DIY tool at one end, $2,500–15,000/mo retainers at the other — with a thin
but *already occupied* $299–$497 done-for-you band in between. One AU
industry source states flatly that anything under $1,500 is rebranded SEO
rather than real citation engineering; that is a competitor's marketing
line, not an established fact, but it is the objection this service will
meet and it should be answered with evidence rather than ignored.

**The honest differentiator is not price and not novelty — it is the warm
base.** SocialPulse247 has to buy every Perth customer cold. Waters & Co
can offer this to people who already pay it for GBP and reviews, at a lower
delivery cost, with the client's baseline already known.

## Boundaries (don't cross these)

- **Don't promise rankings, citations, or "we'll get you into ChatGPT."**
  No one controls what a model says. The deliverable is a measured
  baseline, a diagnosis, and a fix list — sell the audit, not an outcome.
  This is the same discipline as the Crypto Literacy line's
  no-investment-advice boundary.
- **Re-test before claiming improvement.** AI answers vary between runs and
  drift over time. A single before/after comparison is weak evidence; if
  improvement is claimed, it must rest on the same prompt set run the same
  way, and natural variance must be disclosed.
- **Don't let this drift into financial, legal or medical content advice**
  for clients in those sectors — the audit covers how a business is
  *represented*, not the substance of what it sells.
- **Don't quietly re-badge existing GBP work as AI-specific.** If a finding
  is really "your Google Business Profile is incomplete," say that plainly.
  Charging AI-audit prices for standard local-SEO findings is exactly the
  criticism the $1,500 line above is aimed at, and it would be earned.

## What's out of scope

- Implementing the fixes — that is GBP / ReviewGen / website work, quoted
  and billed at those lines' existing rates, not bundled into the audit fee
- Ongoing monthly AI visibility tracking — deliberately excluded for now;
  it needs tooling that doesn't exist yet in the hub, and the retainer end
  of this market is where the credibility risk is highest
- Content production and link building
- Anything for multi-location or franchise operations — competitors price
  those custom for a reason; out of scope until the single-location version
  has real delivery data behind it

## Status

**DRAFT 2026-08-09 — not validated by delivery, not wired into the hub.**
Pricing is benchmarked against live competitor figures but no client has
been quoted or delivered to. Deliberately NOT added to
`ops-hub/app/config.py` BUSINESS_LINES, `PRICING.md`, or the public
website — the own-line-vs-GBP-tier question above should be settled first.
