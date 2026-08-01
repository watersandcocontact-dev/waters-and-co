# Cowork skill templates

Reusable [Claude Cowork](https://claude.com) Skills — SKILL.md files for
Claude's Gmail/Calendar connectors (draft-only, human-approves-every-send
by design). Two tiers:

- **`templates/`** — general-purpose patterns, business-agnostic, safe to
  reuse in any future project. Sourced from the "reviving stale deals"
  research (2026-08-01) plus Anthropic's own small-business skill library
  pattern (`/crm-cleanup`, `/invoice-chase`, `/monday-brief`, etc.).
- **`waters-and-co/`** — the same patterns made project-specific, wired to
  the actual `ops-hub` data model (leads, payments, referral_bonuses) so
  the skill's instructions reference real fields/routes, not a generic
  CRM.

## Not active yet — needs your setup

These are **not usable until you connect Gmail + Calendar** to Claude
Cowork/claude.ai yourself (account connection, same "leave anything I need
to sign into" category as Twilio/GitHub — I can write the skill, not
connect your inbox). Once connected: copy the relevant `SKILL.md` (and its
`reference/` folder, if any) into your Cowork skills folder, or paste the
whole file as a custom skill.

## The shared discipline (apply this to every new skill you add)

1. **One skill = one signal + one drafted action + one human approval.**
   If describing a skill needs more than a sentence, split it.
2. **Never send — draft only.** Every skill below ends at "saved as a
   Gmail draft," never "sent." This isn't just caution: Cowork's Gmail
   connector is draft-only by design, so this matches the platform, not
   just prudence.
3. **Reference real context, not "just checking in."** Quote the actual
   lead's notes/business line/last action from the hub — the whole reason
   these are project-specific templates and not generic ones.
4. **Keep SKILL.md lean** (short, per Anthropic's own guidance) — detailed
   copy templates live in `reference/templates.md`, loaded only when the
   skill actually runs.
5. **Run manually 3-5 times before scheduling.** Verify the drafts are
   good (real context, no hallucinated specifics) before attaching a
   `/schedule` cron to any of these.
