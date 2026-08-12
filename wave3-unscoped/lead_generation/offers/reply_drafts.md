# Campaign reply drafts — awaiting Owner confirmation before send

Drafts written in response to genuine replies caught by `campaign-reply-watch`.
Nothing here has been sent. Per CLAUDE.md's Action-authorization section
(updated 2026-08-11), a `PushNotification` fires before any send and the Owner
confirms or denies per item.

---

## 1. Queens of Clutter — Kirrilee (hub lead 29) — APPROVED 2026-08-11, IN GMAIL, NOT YET SENT

> **Status:** Owner approved the copy 2026-08-11 10:24 and asked for it to be
> sent. **It could not be sent from here** — the connected Gmail MCP connector
> has no send tool (create_draft / update_draft / list_drafts / search / read /
> label only). Created instead as a real Gmail draft threaded as a reply to her
> message: **draft `r8077696336028276226`**, in reply to message
> `19fee7898998e678`. **Needs one click on Send in Gmail.** See `ml_training_log`
> event `queens-of-clutter-reply-send-blocked-2026-08-11`.


**To:** info@queensofclutter.com.au
**Thread:** https://mail.google.com/mail/u/0/#inbox/19fdf516f32539f7
**Subject:** Re: A resource for your downsizing clients
**Their question:** "Can you send us a bit more information about what you do and your business?"

### Draft

> Hi Kirrilee,
>
> Of course — here's the short version.
>
> I'm Chris Waters and I run Waters & Co, here in Perth. The part of what I do
> that overlaps with your work is what happens to the photos, paperwork and
> online accounts once a house has actually been cleared.
>
> Two services specifically:
>
> **Photo and memory digitisation.** The box of loose photos, slides and old
> video tapes that gets set aside during a move. I sort through it with the
> client, work out what's genuinely worth keeping, manage the bulk scanning
> through a proper scanning bureau, and hand back organised digital copies —
> labelled and backed up, rather than a dumped folder of files. $149 to set the
> project up and do the sorting, $55/hr if there's extra curation on top. The
> scanning itself is charged at the bureau's cost and passed straight through
> (roughly 25–70c a photo, $24–35 a tape) — I don't mark it up.
>
> **Digital legacy / account organiser.** A written inventory of someone's
> online accounts and subscriptions — what's being paid for, what needs
> closing, what needs transferring to family. Most useful on the
> deceased-estate side of your work, and for older clients who'd rather get it
> sorted while they still can. $139 for a starter session, $289 for a full
> inventory, $89 for an annual refresh.
>
> Where I think it fits with what you do: you handle the physical side — the
> sorting, the clearing, the move itself. The material that gets set aside as
> "deal with this later" is the bit I pick up. Your job finishes cleanly, and
> the client doesn't end up with the same unopened box in the new place.
>
> One thing I'd rather say upfront than have you find out later: I don't touch
> the legal side of a deceased estate. No probate, no advising an executor on
> their obligations — that's reserved legal work and I stay well clear of it. I
> organise and digitise the material; if a family needs the legal side, I tell
> them to see a solicitor.
>
> I should also be straight with you that Waters & Co is newly registered, so
> I'm not going to pretend to a long client list. What I can do is send a
> one-page summary you could hand to a client, so you can look at it properly
> before deciding whether it's worth pointing anyone my way.
>
> Happy to jump on a call instead if that's easier.
>
> Chris Waters
> Waters & Co
> watersandco.contact@gmail.com
> watersandco.info

### Sourcing / checks behind this draft

- **Their service, verified live 2026-08-11** at queensofclutter.com.au — not
  taken from the 2026-08-07 sourcing note, which only recorded "dedicated
  downsizing service". The live site shows a materially wider scope:
  decluttering/organisation, **deceased estates**, hoarding and chronic
  disorganisation, moving prep, rental-inspection prep, **NDIS** (self and
  plan-managed), and government/non-government clients. Perth metro + Mandurah.
  Still **no** photo, document, scanning or online-account service mentioned —
  the original gap holds, and the deceased-estate line is a stronger hook than
  the downsizing angle we actually pitched.
- **Pricing** from `PRICING.md` rows 26 and 27, both fixed 2026-08-09:
  PhotoDigitisation $149 setup + $55/hr, bulk scanning passed through at
  supplier cost (25–70c/photo, $24–35/tape, deliberately never a per-photo
  menu); DigitalLegacy $139 / $289 / $89.
- **Regulatory boundary**, per CLAUDE.md and DECISIONS.md 2026-07-30:
  Deceased-Estate Admin is a **held** line precisely because it "brushes up
  against unauthorised legal practice if it drifts from 'organise documents'
  into 'advise on your legal obligations as executor.'" The draft states that
  boundary explicitly rather than staying quiet on it.
- **NDIS deliberately not pitched**, even though they serve NDIS clients — the
  NDIS lines are held pending registration/scope confirmation, so offering
  anything there would cross CLAUDE.md's non-negotiable list.
- **No referral fee offered.** No commission structure is documented anywhere
  for this line (only LostSuper row 7 has one, and its $/case is itself
  unconfirmed), so the draft doesn't invent terms.
- **No phone number included** — none is published for Waters & Co anywhere in
  the repo. Also avoided naming a suburb: the ABR record says WA 6021 while the
  site says Doubleview WA 6018, an unresolved discrepancy flagged in
  `ml_training_log` event `gbp-video-verification-2026-08-10`.

### Three judgement calls for the Owner to confirm or strike

1. **Real dollar figures are in the body.** Every one of the 117 audited
   campaign drafts deliberately contains none, so they can't go stale on price
   (DECISIONS.md 2026-08-09). This is a deliberate departure: she's assessing
   whether to stake her own client relationships on us, and vague pricing is
   what kills a referral conversation. Strike them if you'd rather quote live.
2. **"Waters & Co is newly registered."** True, verifiable in seconds via ABN
   lookup (registered 06 Aug 2026), and cheap to own before she finds it
   herself. It does cost something to say. Your call.
3. **Length.** She asked an open question and is evaluating a partner, so this
   is longer than the outreach email was. Can be cut to roughly half if you'd
   rather lead with the call.
