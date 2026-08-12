# Negative-Review Lead Research — 2026-08-10

Sourced per Owner request: businesses with real, documented Google/consumer
reviews specifically complaining about missed calls, no callback, or
general unresponsiveness — the exact signal that makes the MissedCall
pitch land, same pattern already used for Amazing Fencing/The Plumbing
Gang/D & N Plumbing in `tailored_emails_master.md`. Sourced from
ProductReview.com.au (Australia's main consumer review aggregator) via
targeted search, since it surfaces this exact review pattern more reliably
than Google Maps snippets do through web search.

**Deliberately excluded:** large franchise/call-centre operators found in
the same searches (Jim's Electrical, Jim's Roofing, Fallon Solutions,
Service Today, Mr Emergency Plumbing, 24/7 Melbourne Plumber, Allianz/
roadside-assistance brands). Wrong ICP for this pitch — they already have
reception staff, so their complaints are about service quality/culture,
not "no one answers the phone because it's a solo operator." The MissedCall
angle only lands on genuinely small/family-run operators.

## Drafted — 2026-08-10, Gmail drafts created, not sent

| Business | Trade | Location | Review evidence | Verified contact | Status |
|---|---|---|---|---|---|
| Northside Fencing | Fencing (Colorbond/timber/glass) | Burpengary, QLD | "Tried to contact them over and over again but never return any calls" | sales@northsidefencing.com.au — confirmed direct from their own contact page | Drafted (#93 in tailored_emails_master.md) |
| All Hills Fencing | Fencing & gates | Girraween/Sydney, NSW | "Does not turn up to appointment and does not call back to provide apology and acceptable explanation" | sales@allhills.com.au (Sydney region) / newcastle@allhills.com.au (Hunter region) | Drafted (#94) |
| Priority One Plumbing Services | Plumbing/gasfitting, 24/7 emergency | Canberra/Watson, ACT | Reviews describe the operations manager as someone who "never calls back" | info@priorityoneplumbingservices.com.au | Drafted (#95) |

## Real leads found, contact info needs one more verification pass

| Business | Trade | Location | Review evidence | Status |
|---|---|---|---|---|
| Fences R Us | Fencing | Yatala, QLD (also a Bayswater North, VIC listing — may be a different business, same name) | "they don't return calls" | Phone found (0404 924 507 / 07 3804 7105), but the domain search surfaced (fencesrus.com.au) shows a parked "domain may be for sale" page — **don't use that domain**, needs a fresh search for their actual current site or a phone call to confirm they're still trading |
| Rhino Roofing Solutions | Roof repair/replacement, family-owned 25+ years | Melbourne, VIC | "continually ring trying to get the operator to return but receive excuses for not turning up" | Phone found (0476 635 228), but rhinoroofingsolutions.com.au failed to resolve (DNS error) when checked live — needs re-verification before treating as a working contact channel |
| Your Choice Plumbers | Plumbing | Melbourne, VIC (metro area, exact suburb not confirmed) | Customer "still waiting to hear back after almost 4 weeks" | Contact info not yet sourced |
| Aussie's Concrete and Fencing Solutions | Concreting/fencing | Location not confirmed | "constantly chase to find out what was happening... never committed to booking dates" | Contact info not yet sourced |
| Total Fencing | Fencing | Location not confirmed | Warranty-period repair request — "won't return calls or reply to emails" | Contact info not yet sourced |
| Regional Retaining Walls & Landscaping | Retaining walls/landscaping | Regional (state not confirmed) | "numerous excuses... numerous phone calls and emails which were never answered" | Contact info not yet sourced |
| Broadview Fencing | Fencing | Location not confirmed | "numerous unreturned phone calls, SMS's and emails" — also general reliability complaints | Contact info not yet sourced |
| Canberra Roofing | Roofing | Canberra, ACT | Deposit-refund request emailed, "no response" after 3 attempts over weeks | Contact info not yet sourced |

## Found, but lower priority / handle differently

- **HSM Fencing** (Pearcedale/Hoppers Crossing, VIC) — strong review match ("keep chasing... wouldn't turn up for days") but **ProductReview itself notes the business is no longer trading**. Exclude — a defunct business can't become a client.
- **Friendly Home Improvement** — review says "will scam you for money, won't return calls, won't complete the job." That's a trust/fraud allegation, not just a communication gap — a different (and much harsher) situation than the rest of this list. Worth a more cautious approach if pursued at all, not the standard "quick thought" outreach angle.

## Verification pass — 2026-08-10 13:55, run on all 8 pending leads

**Result: none of the 8 clear the bar the 3 drafted ones cleared** (an email
confirmed from the business's own site). Nothing was drafted. Detail below
so this doesn't get re-researched from scratch.

| Business | Checked | Outcome |
|---|---|---|
| Fences R Us | `fencesrus.com.au` fetched live; DNS resolves to **103.224.182.253**, a known domain-parking IP; page says "This domain may be for sale" | **Dead — exclude.** Confirms the 2026-08-10 morning finding rather than contradicting it. Phone (0404 924 507 / 1300 091 780) is the only channel; Yellow Pages masks the email (`c*****t@f********`) |
| Rhino Roofing Solutions | `rhinoroofingsolutions.com.au` and `www.` variant — **NXDOMAIN, no A record at all** | **Dead — exclude.** Site is indexed by search engines but the domain no longer resolves; the business may still trade on phone (0476 635 228) but there is no email channel to reach |
| Your Choice Plumbers | `yourchoiceplumbers.com.au` resolves to **127.0.0.1** from this machine, so the site can't be fetched here | **Blocked, not disproven.** The site looks genuinely live in search results (services, service-area and about pages all indexed; Aspendale VIC, 1300 852 779, Master Plumbers member). Search results mask the email. Needs a fetch from a normal network — a 30-second job in a real browser, not a dead end |
| Aussie's Concrete and Fencing Solutions | ProductReview listing | **No longer operating — exclude**, same as HSM Fencing |
| Total Fencing | ProductReview listing; no location, no identifiable trading entity found | **Exclude on two grounds.** Can't identify which business it is, *and* the complaints are severity-wise closer to Friendly Home Improvement than to the rest of this list (a customer describing a $4,000+ loss, posts pulled out before the concrete set, refusal to rectify). Not a missed-call pitch |
| Regional Retaining Walls & Landscaping | Identified as **Regional Retaining Walls Australia Pty Ltd**, Ballarat Central/Bakery Hill VIC, `rrwaus.com.au`, services Ballarat/Melbourne/Geelong/Bendigo | **Partial — identity confirmed, email not.** Site fetch failed: **SSL certificate expired**. Worth noting the expired cert is itself a live "nobody's minding the shop" signal consistent with the review |
| Broadview Fencing | Likely **Broadview Fencing Co Pty Ltd**, 32 Millers Rd, Wingfield SA 5013, (08) 8445 9422, `broadviewfencing.com.au` | **Partial — two gaps.** The email found (`broadfen@chariot.net.au`) came from Yellow Pages/Top4 **directory listings, not their own contact page**, which is a lower bar than #93–95 used; and their own site sits behind a bot-protection challenge that blocks fetching. Separately, it is **not confirmed** that the SA business is the same "Broadview Fencing" the ProductReview complaint refers to |
| Canberra Roofing | Searched ACT roofers | **Exclude — can't identify the business.** "Canberra Roofing" as a name matches at least eight distinct ACT operators (ReAct/Roof Restoration Canberra, ACT Roofer & Painter, MK Roofing, Steelmax, Vertec, National Capital, Rebel, Alpha). The email references a specific complaint about a specific business — sending it to the wrong one tells an innocent operator you saw a complaint about them. Not worth the risk for one lead |

**Why nothing was drafted anyway:** every email in this batch names the
specific gap found in that business's own reviews. That is what makes the
pitch land, and it is also what makes a misdirected send actively harmful
rather than merely wasted. An unverified address is not a neutral risk here.

**The two worth one more minute each** (Your Choice Plumbers, Regional
Retaining Walls) both failed for environment reasons — a poisoned DNS answer
and an expired certificate — not because the businesses aren't there. Both
resolve from a normal browser.

### Bodies written and held — do NOT create Gmail drafts until the address is confirmed

Deliberately kept out of `tailored_emails_master.md` so they can't be picked
up by a scheduling pass by mistake. The writing is the slow part and it's
done; the address is one lookup each.

**Regional Retaining Walls Australia** (Ballarat, VIC — AEST batch)
**To:** _unconfirmed — needs `rrwaus.com.au` contact page (expired cert blocks fetching here)_

> Subject: Quick one for Regional Retaining Walls
>
> Hi — came across RRWA while looking at retaining wall builders around Ballarat. Noticed a review mentioning phone calls and emails that went unanswered over a stretch of time — the kind of gap that's easy to fall into when the same person quoting is also on the tools all day.
>
> I help trade businesses make sure every call gets answered or texted back, so an enquiry doesn't go quiet while you're mid-build. Worth a quick look, or happy to send through how it works?

**Broadview Fencing** (Wingfield, SA — SA/NT batch)
**To:** _`broadfen@chariot.net.au` — directory-sourced only; confirm from their own contact page first, and confirm the SA business is the one the review refers to_

> Subject: Quick one for Broadview Fencing
>
> Hi — was looking at fencing contractors around Adelaide and noticed a review mentioning unreturned calls, texts and emails. For an established outfit that's usually just a volume problem rather than a wilful one — the enquiries arrive faster than anyone can get back to them.
>
> I help trade businesses make sure every call gets answered or texted back, so a chased-up job doesn't turn into a review instead of a booking. Worth a quick look, or happy to send through how it works?

## Next step, not done in this pass

The 3 "ready to use" leads can go straight into the same tailored-email
format as the existing 117 (see `tailored_emails_master.md` for the
pattern — reference the specific gap found, offer the missed-call fix,
no pricing in the body). The other 8 need either a fresh contact-detail
search or a quick manual check that they're still trading before drafting
anything — flagged here rather than guessed at.
