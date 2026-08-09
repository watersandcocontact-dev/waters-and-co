# AI Missed-Call Reception — Pricing Sheet

**Status: CONFIRMED 2026-08-09** — moved from ranged to fixed pricing per
the Owner-supplied Master Handover (`docs/handover-proposals/2026-08-09/`,
§5). Original range pricing was cross-checked against competitor research
(`docs/competitor_pricing_research.md`, sourced 2026-07-30, re-verified
2026-08-01 — Valory AI's setup fee is public at "from $990, scope-dependent";
Fully Booked's setup is $2,500). The new $349 fixed setup still undercuts
Valory by $640+ and Fully Booked by $2,150+. This is the live client-facing
quote and matches the public website (`website/webapp/config.py`) exactly.

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

## Missed-call text-back setup — $349 fixed

Was a $300-600 one-off range — now a single fixed price toward the lower
end (the site's "Never Miss the Next Enquiry" wedge offer). Includes:

- Platform configuration (business hours, services, FAQs, pricing rules the
  client wants quoted or withheld)
- Script/prompt writing tailored to the client's trade and tone
- Number setup/porting coordination (client's existing number or a new one)
- Integration test calls
- Connecting call data into the ops hub (once webhook is live)

## Managed text-back and lead capture — $199/month

Was part of a $150-400/month tiered range (roughly the old "Basic"/entry
tier); now a single fixed price. Includes:

- Daily call log review
- Monthly summary report
- Script tweaks as needed

## AI reception and managed follow-up — from $299/month

The higher-touch tier (was the old "Standard"/"Premium" $250-400/mo band) —
kept as a **from** price since scope genuinely varies here (booking/calendar
integration, call-recording sampling, urgent-flag SLAs). Confirm exact scope
before quoting a number above $299/mo. Includes at minimum:

- Everything in the $199/mo tier
- Weekly call-recording sampling
- Lead push into the client's own system
- Same-day flag on urgent/mishandled calls
- Booking/calendar integration management on request

## Notes

- Underlying platform costs (the per-minute/per-call AI usage fee) should be
  passed through at cost or with a small transparent markup — don't bury it
  in the flat fee, or the pricing breaks down as call volume grows.
- First month often includes extra hand-holding — consider whether the
  $199/mo tier in month 1 should be priced/bundled with the $349 setup fee.
- Revisit real time-per-client after the first few clients (edge-case review
  load varies a lot by how "chatty" a trade's customers are).
