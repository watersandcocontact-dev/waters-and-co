# ML Training Log

**Purpose (per Owner instruction, 2026-08-07):** a structured, machine-readable
record of how Waters & Co actually operates — the research methods used, how
leads/jobs enter and move through the system, what decisions get made and
why — separate from the narrative logs (`DECISIONS.md`, `PROGRESS.md`), which
stay human-readable prose for a person reading back through history. This log
exists so that, given enough history, a model could be trained on it to learn
the actual operating patterns of the business (research strategy, pricing
logic, lead-qualification criteria, outreach approach) well enough to help
automate parts of it later.

**Started 2026-08-07.** Originally scoped forward-only, but the Owner asked
to go back and log prior history too — **backfilled 2026-08-07** by
converting every dated `DECISIONS.md` entry (2026-07-29 through the website
launch) into structured events, tagged `"backfilled": true` so a future
reader/model can tell reconstructed-from-prose events apart from events
logged live as they happened. The backfill compresses each DECISIONS.md
entry's prose into decision/reasoning/outcome fields rather than reproducing
it verbatim — DECISIONS.md itself remains the full-detail prose record;
this log is the structured index over it. Anything from further back than
DECISIONS.md's own start (project inception) isn't separately reconstructed
— DECISIONS.md was itself started at project inception, so this covers the
full history that exists in any written form.

## Two complementary sources, not a replacement for either

1. **The hub's own database** (`ops-hub/data/hub.sqlite3`) is already the
   real structured record of the "jobs come in, go out" side — every lead,
   every status change (`updated_at`), every logged hour, every payment.
   That data already exists in exactly the queryable form a model would want;
   this log doesn't duplicate it. See `models.py` for the schema.
2. **This log** (`events.jsonl`) captures the *process* side that the
   database doesn't: what was searched for and why, what criteria were used
   to accept/reject a candidate lead, what pricing logic was applied, what
   copywriting approach was chosen and why, what got tried and abandoned.
   This is the "how a human (or Claude, acting as PA/GM) actually did the
   work" record — the database only has the outcome.

## Format

`events.jsonl` — one JSON object per line, append-only, never edited in
place (if something needs correcting, log a new `correction` event
referencing the original rather than rewriting history).

Common fields on every event:
```json
{
  "ts": "2026-08-07T02:55:00+08:00",
  "event_type": "research_query | lead_evaluated | lead_accepted | lead_rejected | pricing_decision | outreach_drafted | outreach_sent | decision | tool_used",
  "actor": "claude",
  "context": "free text — what task/thread this belongs to"
}
```
Plus event-type-specific fields (see examples already in `events.jsonl`).

## Why JSONL, not a database table

Cheap to append from anywhere (a single `echo ... >> events.jsonl` line),
human-diffable in git, and trivially converts to a dataframe/training set
later (`pd.read_json(path, lines=True)`) without needing a schema migration
every time a new event type shows up — just add a new `event_type` value.

## What "logging every step" means in practice going forward

Not every single tool call — that's already in the session transcripts if
ever needed. This log is for the *decision-bearing* steps: what was searched
and why, what made a lead good/bad, what pricing number got picked and the
reasoning, what outreach approach was used and why. The goal is a model
being able to learn the *judgment*, not just the raw actions.
