# AI Missed-Call Reception — Pricing Sheet

**Status: CONFIRMED 2026-08-01** — cross-checked against competitor research
(`docs/competitor_pricing_research.md`, sourced 2026-07-30, re-verified
2026-08-01). Re-verification found a new datapoint that *strengthens* this
pricing without needing a change: Valory AI's setup fee is now public at
"from $990, scope-dependent" — our $300-600 setup undercuts that by
$400-700+, on top of already beating Fully Booked's $2,500 setup. This is
the live client-facing quote and matches the public website exactly.

**Service area: Australia-wide.** Setup, script writing, call-log review, and
client reporting are all done remotely — the client's phone number can be
anywhere in the country (number porting/AU number setup is handled by the
platform, see `platform_research.md`). Market this nationally, not just
locally.

Pricing depends heavily on which underlying AI phone platform is chosen (see
`platform_research.md` once available) — the platform itself usually charges
a per-minute or per-call usage fee that gets passed through or marked up.
These numbers assume a typical small trade business call volume
(~30-100 calls/month, most short).

## Setup fee — $300-$600 one-off

Includes:

- Platform configuration (business hours, services, FAQs, pricing rules the
  client wants quoted or withheld)
- Script/prompt writing tailored to the client's trade and tone
- Number setup/porting coordination (client's existing number or a new one)
- Integration test calls
- Connecting call data into the ops hub (once webhook is live)

## Monthly management fee — $150-$400/month

Suggested tiers (on top of the underlying platform's own usage costs, which
should be itemized separately/passed through transparently to the client):

| Tier | Price/mo | Includes |
|------|----------|----------|
| Basic | $150/mo | Daily call log review, monthly summary report, script tweaks as needed |
| Standard | $250/mo | Basic + weekly call recording sampling, lead push into client's own system, same-day flag on urgent/mishandled calls |
| Premium | $400/mo | Standard + booking/calendar integration management, monthly script/knowledge-base refresh call with client, priority same-day support |

## Notes

- Underlying platform costs (the per-minute/per-call AI usage fee) should be
  passed through at cost or with a small transparent markup — don't bury it
  in the flat fee, or the pricing breaks down as call volume grows.
- First month often includes extra hand-holding — consider whether Basic tier
  in month 1 should be priced/bundled with the setup fee.
- Revisit real time-per-client after the first few clients (edge-case review
  load varies a lot by how "chatty" a trade's customers are).
