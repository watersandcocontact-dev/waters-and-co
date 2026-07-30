# Call-Log Review Process — Daily/Weekly Checklist

"Reviewing edge cases" for an AI missed-call reception service means doing this
consistently, not just setting the AI up once. This is the day-to-day process
once a client is live.

## Daily (5-10 min per active client)

- [ ] Open the call log / dashboard for the AI phone platform.
- [ ] Skim every call transcript from the last 24h (not just the flagged ones —
      AI confidence flags miss things).
- [ ] For each call, check:
  - [ ] Did the AI correctly identify what the caller wanted?
  - [ ] Did it capture correct contact details (name, callback number)?
  - [ ] Did it book/schedule correctly if that's in scope, or hand off correctly
        if not?
  - [ ] Any call where the AI seemed confused, looped, or gave wrong info about
        pricing/availability/services?
- [ ] Push any new lead into the ops hub (manually today; automatically once the
      webhook is wired to the platform).
- [ ] For anything urgent (emergency callout requests, angry customers, clearly
      mis-handled calls) — notify the client same day.

## Weekly (per client, ~20-30 min)

- [ ] Review the week's call volume vs baseline — spot spikes/drops.
- [ ] Sample-listen to 3-5 full call recordings (not just transcripts) to catch
      tone/quality issues transcripts miss.
- [ ] Check for repeated failure patterns (e.g. AI always mishears a suburb name,
      always fumbles a specific question) — these become script/prompt fixes.
- [ ] Update the AI's script/knowledge base for anything that changed for the
      client that week (new services, price changes, availability changes,
      public holiday hours).
- [ ] Send the client a short weekly summary: calls handled, leads captured,
      anything flagged.

## Edge cases to specifically watch for

- Caller asking about a service the client doesn't actually offer (AI should
  say so, not guess).
- Caller trying to reach a specific staff member by name.
- Emergency/urgent situations (e.g. burst pipe, no power) — confirm the AI
  either escalates immediately or gives clear guidance, never just "we'll call
  you back" for genuine emergencies.
- Spam/robocalls — confirm the AI isn't wasting time or logging these as leads.
- Multi-language callers if relevant to the client's area.
- Price-fishing calls ("just wondering what you charge") — confirm the AI's
  answer matches what the client actually wants quoted over the phone (some
  trades don't want prices given without a look at the job).

## Escalation rule of thumb

Anything that could cost the client a genuine paying job (mishandled emergency,
wrong info given, lead not captured) = same-day client notification, not just
logged for the weekly review.
