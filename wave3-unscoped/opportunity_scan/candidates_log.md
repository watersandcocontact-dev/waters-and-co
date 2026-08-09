# Opportunity Candidates Log

Every candidate scored against `scoring_rubric.md`, including rejects — a
documented "no" is useful later if circumstances change (e.g. new
infrastructure changes the reuse score).

| Date | Candidate | $0 entry | Market gap | Audience | Reuse | Learnable | Simple model | "Can't be bothered" | Total /35 | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-07-31 | Crypto Literacy | 5 | 4 | 5 | 5 (Tech Concierge infra) | 4 | 5 | 5 | 33 | Built — see `wave3-unscoped/crypto_literacy/` |
| 2026-07-31 | AI Tools for Business | 5 | 4 | 5 | 5 (GBP/ReviewGen/MissedCall client base) | 4 | 5 | 5 | 33 | Built — see `wave3-unscoped/ai_tools_business/` |
| 2026-08-01 | Digital Legacy / Account Organiser | 5 | 4 | 5 | 5 (Tech Concierge base + session booking flow) | 4 | 5 | 5 | 33 | Built — see `wave3-unscoped/digital_legacy/`. Proven near-identical AU competitor (Digital Care Services, Illawarra NSW) with nothing equivalent found serving Perth; CHOICE has a mainstream consumer guide on it. Two boundaries documented: never take credential custody, never touch will/estate drafting |
| 2026-08-01 | Photo & Memory Digitisation Concierge | 4 | 3 | 5 | 5 (Downsizing cleanouts physically unearth this; same visit) | 5 | 4 | 5 | 31 | Built — see `wave3-unscoped/photo_digitisation/`. Market gap scored LOW (3) deliberately: Perth scanning itself is commoditised (Pixelfied from $0.60/photo, videotapes2dvd $100 min, Camera House, Pixels Plus) — the gap is only the sorting/logistics layer, which is inferred, not documented. Built as a coordination bolt-on, NOT a competing scan bureau |
| 2026-08-09 | AI Search Visibility Audit | 5 | 3 | 5 | 5 (GBP/ReviewGen/MissedCall client base + existing report-and-action-plan delivery format) | 4 | 5 | 5 | 32 | **Drafted — see `wave3-unscoped/ai_search_visibility/`.** Market gap scored 3, NOT higher, because the sub-$500 local tier is already occupied: **SocialPulse247 is Perth-based, sells a $497 AI Search Visibility Audit to trades/professional/local services — the identical customer segment**; AI Local Link $299 (SE QLD + national); AIReady Australia $497. Market is barbelled ($27 self-serve tool ↔ $2,500–15,000/mo agency retainers) with a thin but contested band between. Contested ≠ empty, but a Perth operator betting on this segment is real validation the model sells. Differentiator is the warm base (existing GBP clients), not price or novelty. **Open question flagged for Owner: own line vs a `task_type` on GBP** — not wired into config.py either way. Recommendation revised mid-scan to **GBP tier** after finding the v2 handover gives GBP a **$99 fixed "Local Visibility Check"** (same shape: fixed-fee diagnostic, ranked action plan, no ranking promises) — best presented as one ladder, $99 check → $249–349 check-plus-AI-testing, rather than two competing products |
| 2026-08-09 | New Business Launch Concierge (ABN / business name / GST / GBP setup for new sole traders) | 1 | 2 | 4 | 3 | 2 | 4 | 4 | 20 | **REJECT — hard regulatory blocker, verified against the regulator.** TPB(I) 39/2023 lists *applying to the Registrar for an ABN on behalf of a client* as an example of a tax agent service, and TPB requires registration to provide tax agent services **for a fee or reward** (application fee $290, plus qualification, experience and PI-insurance requirements). Same class as the held NDIS/Deceased-Estate lines — this is exactly what rubric criteria #1 and #5 are designed to filter. Incumbents compete precisely on being registered agents (ABN Registration Australia $89.95 service fee; business name $199/1yr, $299/3yr; Cosec $234/$295), so there is no gap to attack anyway. The residual non-regulated slice (business name via ASIC, domain, email, GBP listing) is already covered by existing GBP setup work and does not justify a line. **Revisit only if the Owner ever registers with the TPB** |

Add a row every time the daily scan (or an ad-hoc idea) gets scored —
don't skip logging rejects.

## Open loop — two candidates with no surviving record

The session-history buffer (`.remember/recent.md`, 2026-08-05) states that
**AI Answer Visibility (BUILD; GBP reuse)** and **Declutter-to-Cash (HOLD;
WA licensing)** were scored that day. Neither appears in this log, in
`DECISIONS.md`, in `PROGRESS.md`, or anywhere else in the repo — checked
2026-08-09. The scores themselves are therefore lost; only the verdicts
survive, in a buffer that is a compressed summary and not an authoritative
record.

- **AI Answer Visibility** is almost certainly the same idea as the AI
  Search Visibility Audit row above, which has now been researched and
  logged properly with live competitor figures. Treat that row as
  superseding it.
- **Declutter-to-Cash** has *not* been re-researched. The noted blocker (WA
  second-hand dealer licensing) is plausible and would be a rubric reject
  on criterion #1, but it is unverified. Flagged as genuinely open — worth
  a future scan, since a real licensing check would settle it either way.

Lesson for the process: the scan is only useful if every scored candidate
lands in this file the same day. A verdict remembered in a chat buffer but
not written down here is not a documented "no."
