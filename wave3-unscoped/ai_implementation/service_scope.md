# AI Implementation for SMEs — Service Scope

**Status: validated 2026-08-01, not yet built or launched.** Distinct from
the existing light-touch `AIToolsBusiness` line ($200-600 one-off tool
setup/training) — this is custom automation *building*, i.e. literally
what Claude Code does for Waters & Co's own ops hub, sold as a service to
other small businesses. Genuinely new capability, not a repackage.

**Reconciliation note (2026-08-02):** this line was independently
validated with real market data on 2026-08-01 (see the pricing gap
below). A separate, older planning document described the same
opportunity as "AI Automation & Document Processing Consulting" with
three named sub-services and a sovereignty/privacy differentiator —
folded that framing in below since it's a genuinely useful way to scope
and pitch this, but the pricing stays anchored to tonight's actual
sourced data, not that document's earlier estimates.

## Three sub-services (priority order)

1. **Business-process automation & AI agent building** — the flagship,
   and what's actually described below (n8n/Make-style pipelines and
   custom agents, using Claude Code as the build engine).
2. **Custom RAG chatbots** — a client's own documents/website turned into
   an accurate assistant, positioned against generic API-wrapper
   competitors on accuracy and privacy (their data never leaves local
   infrastructure once that infrastructure exists — see the hardware
   note below).
3. **Document processing / intelligent document processing (IDP)** —
   extraction, classification, summarisation at volume. Worth watching
   specifically for Perth's resources/mining sector, which generates
   large volumes of compliance/safety documentation that's genuinely
   privacy- and sovereignty-sensitive — enterprise IDP tools cost
   thousands/year, real room for a nimble local operator. Not yet
   pursued, flagged as the standout of the three for later prioritising.

## The differentiator to lead with once local infrastructure exists

A local inference stack (in planning — you're setting this up directly
on a separate machine, not something built through this session) would
be directly reusable as *billable service infrastructure*, not just an
internal tool — zero marginal inference cost beyond electricity (a real
cost advantage over competitors paying per-token cloud fees at volume),
and genuine data sovereignty (processing never leaves local
infrastructure, relevant to Australian privacy law and specifically to
mining/resources compliance work, where offshore cloud AI providers can
be compelled to disclose data under foreign law regardless of physical
storage location). **Don't compete on price in the commoditised low end**
(generic content writing, simple FAQ bots, cheap API-wrapper chatbots) —
target privacy-sensitive, document-heavy niches instead: resources/
mining, legal, healthcare-adjacent (non-clinical), finance,
government-adjacent. This positioning doesn't depend on the local stack
being live yet — it's the pitch to build toward.

## What's actually delivered

- **A single, clearly-scoped automation build** for a small business with
  a real operational pain point — e.g. "leads from your website/inbox
  auto-logged into a simple CRM with confirmation emails and payment
  requests," the same shape of thing built for this business's own hub.
- Discovery call to scope the exact workflow (this is the real time cost,
  not the build itself — see pricing rationale below).
- One round of revisions, 1-2 week delivery for a single-automation
  build.
- A larger "small business system" tier for multi-step builds (lead
  capture + CRM + invoicing/payments + basic reporting).
- Optional light monitoring/tweaks retainer once built.

## Why this is genuinely different from AIToolsBusiness

`AIToolsBusiness` = "I'll help you set up and learn an existing AI tool
(ChatGPT, an off-the-shelf assistant)." This line = "I'll build you a
working custom system using Claude Code, the way I built my own
business's ops hub." Different skill, different price tier, different
client (someone with a specific broken workflow, not someone who wants
general AI literacy).

## The pricing gap (validated, not assumed)

Real competitor data gathered 2026-08-01 (Fiverr/Upwork live listings,
published boutique-agency rate cards, Big 4 pricing) — full sourcing in
`pricing_sheet.md`:

| Tier | Price band (AUD) | What it gets you |
|---|---|---|
| Fiverr/Upwork gig freelancer | $30-500 | Single automation, transactional, no discovery, variable quality |
| **The gap — nobody serves this well** | **$500-2,500** | — |
| Boutique AI agency | $2,500-25,000 (SME sweet spot $5k-15k) | Full discovery, project management, agency staff overhead |
| Big 4 | $250k+ | Irrelevant to SME, doesn't engage under ~500 employees |

A solo operator with zero staff overhead and Claude-Code build speed sits
naturally in the $500-$2,500 gap, undercutting boutiques by 60-80% while
staying meaningfully above the unreliable Fiverr floor.

## Honest cost-to-deliver check (don't oversell "near-zero cost")

Tooling/compute cost really is low (~$80-500/mo even servicing 10-20
clients, per solo-operator self-reports). **But the real bottleneck isn't
the build — it's discovery, scoping, and testing against a non-technical
client's messy real data.** Claude Code collapses coding time from days
to hours; it does not collapse the 3-8 hours per client spent figuring
out what a trades/retail owner actually needs and walking them through
using the result. Price needs to cover that time, not just compute —
this is a real side-business hour cost against a day job, not free money.

## What's out of scope

- Anything requiring ongoing infrastructure Waters & Co doesn't run
  (multi-channel ad management, per-seat SaaS platforms) — that's the
  boutique agencies' territory, not this line's.
- Regulated-advice creep: building a system is fine, advising the client
  on what to tell their accountant/lawyer through it is not.

## Client base and channel

Same reuse pattern as `AIToolsBusiness` — the trade/SME clients already
being reached via GBP/MissedCall outreach are a warm audience once they
trust you with one thing. Also a natural fit for direct outreach to SME
owners already posting automation-shaped pain on Upwork/forums (see
`pricing_sheet.md` for the demand-signal evidence).
