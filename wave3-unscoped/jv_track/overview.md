# JV Track — Technical Partner in a Professional-Services Joint Venture

**Status: confirmed live 2026-08-02, prep work only — no client work, no
money, no agreement signed yet.** Structurally different from every other
line in this repo: everything else is 100% sole-trader owned; this is a
genuine partnership with a licensed professional friend who owns the
client relationship and carries the professional liability, split
30-40% to you as the technical partner. Tracked as its own entity, never
folded into the same P&L as the solo lines.

## The hard flag — read this before anything else moves forward

**A 30-40% split with someone who holds the licence and carries the
liability is a real business partnership, not a handshake.** Profit
share, liability allocation, IP ownership of anything built, and an exit
mechanism all need to be settled in writing — by an actual lawyer
drafting or reviewing the agreement — before any client's money or data
moves through this. This is the same category of flag as the Airbnb
co-hosting hold and the NDIS scope conversations elsewhere in this
repo: I can prepare everything up to that point, but I cannot draft or
review the agreement itself, and building real client-facing tooling
ahead of a signed agreement is a real exposure, not a formality to skip.
**If this hasn't happened yet, it's the actual next step, not this doc.**

## Structure

- **You**: technical partner. Build the AI/document tooling for each
  vertical, using the same infrastructure as the solo AI Automation
  Consulting line (see reconciliation note below).
- **Them**: licensed professional friend per vertical. Owns the client
  relationship, carries the professional liability and licensing
  requirement, brings the initial pilot clients from people they already
  know.
- **Split**: 30-40% to you, per the terms actually agreed with each
  friend (may differ by vertical) — get the real number confirmed and
  written down per partner, don't assume it's uniform.

## Sequencing (per your original plan — fastest-to-activate first)

1. **Accounting** — most standardised documents/workflows, likely
   fastest to get a working pilot.
2. **WHS** — second, per the same reasoning.
3. **Town planning** and **architecture** — launch once their respective
   friend is ready; more bespoke document types, likely slower to
   template.

Don't try to stand up all four at once — this mirrors the same
"sequence within each track, don't run everything at full intensity"
discipline used for the solo AI Automation Consulting sub-services.

## What's genuinely shared with the solo AI Automation Consulting line

The same local LLM/RAG pipeline (once the actual inference machine is
confirmed — see the hardware note below) and the same audit-layer
pattern (deterministic check → schema check → adversarial review) apply
to both tracks. Build the pipeline generically enough that both use it
with different document corpora and templates per vertical — not two
separate systems. Compute pools across both tracks too, subject to the
one hard boundary below.

## The one hard boundary

**Sensitive JV data (WHS, accounting, town planning, architecture client
documents) stays on sovereign/local infrastructure only — never offshore
GPU rental, regardless of cost.** Non-sensitive solo automation-consulting
work for clients without sensitivity requirements can use offshore
rental if it's cheaper. This needs to be enforced in whatever tooling
actually gets built (e.g. a hard-coded routing rule, not a manual
reminder) once real infrastructure exists — flagged here so it isn't
lost by the time building starts.

## Hardware — you're setting this up directly, not me

Checked the machine this session runs on: Intel integrated graphics only
(no discrete GPU found via `lspci`), no sudo access — the RTX 3070 is a
different physical machine. Per your call 2026-08-02: **you're setting up
Ollama/the local stack directly on that machine yourself, including the
~800GB of data** — I'm not touching that infrastructure. This doc's
shared-infrastructure plan (both this JV track and the solo AI Automation
Consulting line) stays as a written plan for now; wire the actual
service logic to it once you confirm the stack's up and reachable from
wherever the hub ends up running.

## Per-vertical prep (light — real scope needs the actual friend's input)

Each vertical needs its own scope conversation with the actual partner
before building client-facing tooling — the notes below are starting
points for that conversation, not a finished spec:

- **Accounting** — likely candidates: document extraction/categorisation
  from client records, reconciliation support, report drafting. Overlaps
  conceptually with the existing (non-JV) Bookkeeping line — keep them
  structurally separate in the hub regardless of any topical overlap,
  since ownership/liability models differ completely.
- **WHS** — safety document drafting, incident report processing,
  compliance-checklist generation against the relevant WHS Act/
  Regulations for the friend's state.
- **Town planning** — application/submission document assembly,
  compliance-matrix extraction against local planning schemes.
- **Architecture** — likely the most bespoke of the four; specification/
  documentation support rather than design work itself.

None of these are built yet — this is a placeholder structure, not a
commitment to a specific scope, until each friend actually weighs in.
