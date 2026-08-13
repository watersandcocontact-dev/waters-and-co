# Scam & Online Safety Check (seniors, in-home) — Service Scope

A single in-home visit that leaves an older person's phone, computer and
accounts in a state where the common scams don't work: bank and email
two-factor turned on, scam-call blocking switched on, remote-access apps
removed, a written one-page "what to do if it happens" card left on the
fridge, and the adult child added as the person to ring first.

Reuses the Tech Concierge client base, the same in-home visit and the same
booking flow. Nothing new to build.

**Recommended shape: a named, priced inclusion of the existing Tech
Concierge line — a `task_type` at most, not a new business line.** The
market evidence below is the reason, and it is the most important thing on
this page. Nothing has been wired into `ops-hub/app/config.py`.

## What's actually delivered

- **Account hardening** — two-factor on email, myGov and internet banking;
  recovery phone/email checked and actually working; passwords moved out of
  the notebook into something the person can genuinely use
- **Device clean-up** — remote-access tools (AnyDesk, TeamViewer, QuickSupport)
  removed unless there's a legitimate reason for them; unknown admin/profile
  entries checked; automatic updates switched on
- **Call and message screening** — carrier scam-blocking enabled, silence-
  unknown-callers configured, SMS sender filtering on, and the bank's real
  number saved as a contact so an incoming "your bank" call is visibly not it
- **The fridge card** — one page, large print: the three things that mean
  it's a scam (urgency, remote access, payment by card/crypto/gift card),
  who to ring in what order (adult child → bank's saved number → 1300 IDCARE),
  and the fact that hanging up is always allowed
- **Family handover note** — what was changed, what wasn't, and what the
  adult child should check in three months

## Boundaries — non-negotiable, and sharper here than anywhere else

1. **Never take credential custody.** Same boundary as Digital Legacy. The
   client types every password; nothing is written down, photographed or
   taken away.
2. **Never touch money in the room.** No banking transactions, no transfers,
   no "let's just check your balance". Reading a screen is fine; operating
   the account is not.
3. **No recovery work.** If the person has already been scammed, that is a
   referral to IDCARE (free, 1800 595 160) and their bank — not billable
   work. Attempting fund-recovery for a fee is a category the business does
   not touch.
4. **The service itself looks exactly like the scam it prevents.** A stranger
   arriving at an older person's home offering to "check your online safety"
   and asking about bank accounts is the precise shape of the door-knock
   fraud Scamwatch warns about. So: booked by the adult child, never
   cold-called; arrive with ID; adult child on speakerphone if not present;
   never the initiator of contact. Any outreach goes to the family, not the
   senior.

## Market evidence (checked 2026-08-13)

**Demand for the outcome is enormous and well documented. Demand for it as
a paid product is not — and that gap is the finding.**

Losses (secondary sources — industry/press summaries of ACCC and National
Anti-Scam Centre data, **not fetched from the primary report**; re-verify
against the ACCC Targeting Scams report before quoting to a client):

- People aged 55+ reported **more than $53 million** in losses in 2025
- Remote-access scams targeting older Australians average **~$17,943 per
  victim**
- Survey figure quoted in the same sources: ~85% of people aged 50+ believe
  they have encountered or been the victim of a scam

Against that, the deliverable is already supplied free, by well-funded
bodies whose entire purpose is to supply it:

| Who | What | Price |
|---|---|---|
| **WA ScamNet / Consumer Protection WA** | Scam presentations to community groups and seniors' groups, on request; stalls and briefings | **Free** |
| **IDCARE** | Cyber Resilience Outreach Clinics run in WA; free case management for victims | **Free** (government-funded) |
| **eSafety Commissioner — Be Connected** | National digital-literacy and online-safety program with a community partner network delivering in-person help | **Free** |
| **ID Support NSW** | Face-to-face scam support roadshow for seniors, one-on-one sessions, launched March 2026 across regional and metro NSW | **Free** — other state, but shows the model is being taken up as a government service |
| Banks (ANZ and others), National Seniors Australia | Dedicated seniors cyber-security hubs and guides | **Free** |

And where it *is* paid, it is already bundled into the incumbent's existing
senior tech session rather than sold separately:

| Who | Coverage | Evidence |
|---|---|---|
| **Geeks Perth — "Tech Help for Seniors"** | 1–2hr in-home one-on-one sessions; site states it covers spotting scam emails, avoiding phishing, strong passwords, staying safe online | Page fetched 2026-08-13; **no pricing published** |
| **The Original PC Doctor** | In-room tech help at Perth aged-care facilities (claims 204 sites), plain-English explanation, written update to family | Search results only, not fetched |

So the competitive position is: a free tier that is government-funded and
actively expanding, and a paid tier that already includes this as a feature
of a session Waters & Co itself sells at $99. There is no separable product
here — which is why this is scoped as an inclusion, not a line.

## Why it is still worth naming

The finding is not "drop it". It is "stop treating it as a new thing to
sell and start treating it as the reason to book the thing already sold."

- Tech Concierge outreach currently has no single sharp hook. "Scam &
  Online Safety Check" is a concrete, urgent, nameable reason for an adult
  child to book a visit for a parent — which is the actual buyer.
- It gives the follow-up session (the $49 30-minute check-in, already the
  line's stated wedge) an obvious recurring purpose: re-check the settings.
- It costs nothing to add. No new base, no new page, no new pricing model —
  a named inclusion on an existing service page.

## What would change this verdict

- Evidence that anyone in Australia sells a standalone paid scam/safety
  audit to seniors at a real price (none found).
- A referral channel that pays — e.g. a bank, insurer or aged-care provider
  funding the visits rather than the family. That would be a different
  business model entirely and would need its own scoring.
- The free tier contracting. Currently it is expanding (ID Support NSW's
  2026 roadshow), which points the other way.

## Status

Drafted 2026-08-13 by the daily opportunity scan. Scored **30/35** — over
the 25 threshold on the strength of reuse (5) and $0 entry (5), but held to
**2 on documented market gap** for the reasons above. Not a business line;
not in `config.py`. Owner's call on whether to add it as a Tech Concierge
`task_type` and put the name on the website's Tech Concierge section.
