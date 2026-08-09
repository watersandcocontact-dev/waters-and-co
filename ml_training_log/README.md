# ML Training Log

**Purpose (per Owner instruction, 2026-08-07, scope confirmed 2026-08-09):**
a structured, machine-readable record of how Waters & Co actually operates —
the Owner's actual requests, what was done in response, the reasoning, and
the outcome once known — separate from the narrative logs (`DECISIONS.md`,
`PROGRESS.md`), which stay human-readable prose for a person reading back
through history. This log exists so that, given enough history, a model
could be trained on it to learn the Owner's actual process and desired
outcomes — not just the business's operating patterns (research strategy,
pricing logic, lead-qualification criteria, outreach approach), but *how the
Owner personally makes those calls* — well enough to help automate or
pre-empt parts of it later.

**Scope — deliberately this project only (Owner's call, 2026-08-09).** The
Owner runs the identical pattern separately in other projects rather than
one shared cross-project log, specifically so unrelated business context
never confuses either log. Don't merge, reference, or infer from another
project's log here.

**Who reads and writes this.** Anyone/anything working in this repo — a
live session, a future session, a background/autonomous scan, a subagent —
not just whichever one wrote the first batch of entries. Write to it as a
standing habit for decision-bearing steps (see CLAUDE.md's "Memory and
logging" section). Read it too, before a similar decision-bearing task —
the point is for the Owner's judgment to compound across sessions, not get
re-derived from scratch each time.

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
  "event_type": "research_query | lead_evaluated | lead_accepted | lead_rejected | pricing_decision | outreach_drafted | outreach_sent | decision | tool_used | correction | outcome",
  "actor": "claude",
  "context": "free text — what task/thread this belongs to"
}
```
Plus event-type-specific fields (see examples already in `events.jsonl`).

**Schema note (added 2026-08-09, applies going forward — events before this
date don't have these fields and that's fine, don't backfill them):** where
a real back-and-forth with the Owner drove the outcome (a copy edit, a
pricing call, a scope decision), also capture the actual exchange, not just
a narrative summary of it:
```json
{
  "user_input": "the Owner's actual request/feedback, close to verbatim — this is the signal a future model most needs, don't paraphrase it away",
  "claude_output": "what was actually said/done in response — can summarize a long tool-call sequence, but keep the substance and any options offered",
  "iteration_of": "optional — event this one revises/follows on from, so a multi-round exchange (e.g. a copy workshop) reconstructs as a real sequence, not disconnected snapshots"
}
```
The existing `decision`/`method`/`outcome`/`lesson` fields stay — they're
the *analysis* of what happened; `user_input`/`claude_output` are the *raw
exchange* that analysis is drawn from. Use both where there was a real
back-and-forth; `decision`/`method`/`outcome` alone is still fine for
single-shot research/tooling events with no real dialogue to capture.

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
