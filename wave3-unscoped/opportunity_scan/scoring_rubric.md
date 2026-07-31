# Opportunity Scoring Rubric — the filter for everything new from here on

Applies to two different things, scored differently (see below): **new
recurring business lines** (runs daily) and **one-off gig/job
opportunities** (also ongoing — see `gig_marketplace_scan.md`).

## Core criteria (every candidate gets scored 0-5 on each)

1. **$0 barrier to entry** — can it start with no paid signup, no license,
   no formal qualification? (5 = genuinely free to start, 0 = needs real
   capital/licensing before the first client)
2. **Documented market gap** — is there real, checkable evidence people
   want this and current options are thin/expensive/annoying? Not a guess.
3. **Defined target audience** — can you name who buys this in one
   sentence, not "everyone"?
4. **Infrastructure reuse** — how much of this already exists in the hub
   (client base, booking flow, outreach channel, website segment)?
   (5 = slots directly into something already built, 0 = needs everything
   built from scratch — this is the single highest-weighted factor per
   your "reuse what exists" instruction)
5. **Learnable without formal expertise** — can the actual skill be picked
   up via self-directed research or AI assistance, not a degree/licence/
   years of training? (5 = a focused weekend of research + practice gets
   you competent, 0 = needs a real qualification — this rules out things
   like the held-back NDIS/deceased-estate lines by design)
6. **Simple business model** — can you explain how it makes money in one
   or two sentences? Complexity in the *business model itself* (not the
   skill) is a red flag even if the skill is easy.
7. **"Can't be bothered doing it themselves"** — is the actual value
   proposition convenience/effort-arbitrage? People who have money but not
   time/patience/willingness are the best customers for a $0-entry service
   — score high if the target customer clearly *could* do this themselves
   but won't.

## Scoring and cutoffs

- **Total /35.** Below 15: reject, don't build. 15-24: worth a closer look,
  not urgent. 25+: strong candidate, prioritise.
- **Infrastructure reuse (#4) acts as a multiplier in practice, not just
  an additive score** — two candidates with the same total, the one that
  slots into existing infrastructure should be built first regardless of
  raw score, since it costs less to actually stand up.
- Log every candidate scored, even rejected ones, in
  `wave3-unscoped/opportunity_scan/candidates_log.md` — a documented "no"
  is useful later if circumstances change (e.g. infrastructure gets built
  that changes the reuse score).

## What this explicitly filters OUT (by design, not oversight)

- Anything needing a real licence/registration before the first client
  (this is why NDIS Nav/Compliance and Deceased-Estate Admin stayed held
  — see DECISIONS.md 2026-07-30/31)
- Anything needing meaningful up-front capital
- Anything where the business model itself needs a long explanation
- Anything with no clear "who's the customer" answer

## How this differs from the original 8 businesses

The original Wave 1/2 businesses were spec'd directly by you, not scored
against this rubric — this rubric governs *new* additions from here on,
starting with Crypto Literacy and AI Tools for Business (both score well:
reuse Tech Concierge/existing-client infrastructure, learnable via
self-research, simple "teach a skill" or "set up a tool" business models,
targeting people who want the outcome but not the learning curve).
