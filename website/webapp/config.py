"""Content model for the public website — segments, services, pricing.

Real numbers pulled from wave1/*/pricing_sheet.md, not invented. Keep this
file in sync if pricing sheets change; it's a summary for web copy, not the
source of truth (the pricing sheets remain that).

A segment's "services" is a flat list of service slugs (most segments).
A segment can instead use "groups" — a list of {"heading", "services"} —
when it needs a visual sub-split on the segment page (currently just
small-business-support: local-presence/never-miss-a-call kept visually
distinct from bookkeeping/grant-finder even though they're one segment
now). See segment_groups() below — every segment normalises to the same
group shape either way, so the template doesn't need to know which kind
a given segment is.

A service can appear in more than one segment's list (e.g. gbp/reviewgen/
missedcall are cross-listed in business-systems too, since that audience
overlaps and might only browse one segment) — a service's own "segment"
field just names its primary home, it's not load-bearing for routing.
"""

SEGMENTS = [
    {
        "slug": "small-business-support",
        "name": "Small Business Support",
        "tagline": "The everyday work of running a small business — found, answered, and accounted for",
        "groups": [
            {
                "heading": "Local Presence & Never Miss a Call",
                "services": ["gbp", "reviewgen", "missedcall"],
            },
            {
                "heading": "Books & Grants",
                "services": ["bookkeeping", "grantfinder"],
            },
        ],
    },
    {
        "slug": "business-systems",
        "name": "AI Systems for Business",
        "tagline": "A working automation, built and delivered — not a boutique price tag",
        "services": [
            "ai_implementation", "aitoolsbusiness", "realestate",
            "gbp", "reviewgen", "missedcall",
        ],
    },
    {
        "slug": "seniors-support",
        "name": "Seniors & Family Support",
        "tagline": "Patient, plain-English help — tech, finances, and the paperwork nobody enjoys",
        "services": [
            "pension", "techconcierge", "cryptoliteracy",
            "digitallegacy", "downsizing", "photodigitisation",
        ],
    },
    {
        "slug": "content-repurposing",
        "name": "Content Repurposing",
        "tagline": "One recording, a week's worth of clips",
        "services": ["videorepurpose"],
    },
    {
        "slug": "property-tax-review",
        "name": "Property & Tax Review",
        "tagline": "If your land valuation looks too high, it might be",
        "services": ["landtax"],
    },
]

SERVICES = {
    "gbp": {
        "name": "Google Business Profile Management",
        "segment": "small-business-support",
        "business_line": "GBP",
        "one_liner": "Your Google listing, actually kept up to date.",
        "summary": (
            "A fully managed Google Business Profile — accurate, current, "
            "and actively kept up, so customers see the right information "
            "and choose you instead of a competitor with a better-looking "
            "listing."
        ),
        "pricing": [
            {"label": "One-off profile cleanup", "price": "$150–300"},
            {"label": "Ongoing monthly management", "price": "$100–200/mo"},
        ],
    },
    "reviewgen": {
        "name": "Review Generation & Reputation Management",
        "segment": "small-business-support",
        "business_line": "ReviewGen",
        "one_liner": "More reviews, and a considered reply to every one.",
        "summary": (
            "A steady flow of new reviews from your customers, plus a "
            "considered response to every one that comes in — good or bad. "
            "Most people check reviews before they call, and a thin or "
            "ignored review list quietly costs you the job."
        ),
        "pricing": [
            {"label": "One-off setup", "price": "$100–200"},
            {"label": "Ongoing monthly management", "price": "$100–300/mo"},
        ],
    },
    "missedcall": {
        "name": "AI Missed-Call Reception",
        "segment": "small-business-support",
        "business_line": "MissedCall",
        "one_liner": "The call you couldn't take still gets handled.",
        "summary": (
            "Every call you can't take still gets a response and the job "
            "still gets captured, reviewed daily so nothing slips through. "
            "A missed call is often a job that goes straight to whichever "
            "competitor picks up instead."
        ),
        "pricing": [
            {"label": "Setup", "price": "$300–600 one-off"},
            {"label": "Ongoing monthly management", "price": "$150–400/mo"},
        ],
    },
    "landtax": {
        "name": "Land Tax / Rates Valuation Objection",
        "segment": "property-tax-review",
        "business_line": "LandTax",
        "one_liner": "If the valuation looks wrong, there's a process to challenge it.",
        "summary": (
            "A properly built, evidence-backed case for why your land or "
            "rates valuation is too high, ready for you to lodge (most "
            "states require identity-verified lodgement, so that step "
            "stays with you). Most people who don't challenge an inflated "
            "valuation simply pay more than they should."
        ),
        "pricing": [
            {"label": "Standard residential objection", "price": "$400–800 flat"},
            {"label": "Commercial / complex property", "price": "Quote on assessment"},
        ],
    },
    "ai_implementation": {
        "name": "AI Implementation for SMEs",
        "segment": "business-systems",
        "business_line": "AIImplementation",
        "one_liner": "A working custom automation, built and delivered — not a DIY tool.",
        "summary": (
            "A working software system built around a real bottleneck in "
            "your business — tested and ready to use, so the manual, "
            "repetitive part of your day stops eating hours you don't "
            "have. No need to learn to build it yourself or pay "
            "boutique-agency rates to get it done. Larger multi-step "
            "systems available for more complex needs."
        ),
        "pricing": [
            {"label": "Single automation build", "price": "$990–1,490 fixed"},
            {"label": "Small business system (multi-step)", "price": "$2,500–4,000 fixed"},
            {"label": "Optional ongoing monitoring", "price": "$150–250/mo"},
        ],
    },
    "realestate": {
        "name": "AI Lead-Response for Real Estate Agents",
        "segment": "business-systems",
        "business_line": "RealEstateLeads",
        "one_liner": "Instant lead response, fully managed — no dashboard for you to run.",
        "summary": (
            "New leads get a response within moments of coming in, your "
            "cold database gets worked back through, and follow-ups keep "
            "happening — entirely hands-off. Leads go cold fast, and the "
            "agent who responds first is usually the one who wins the "
            "listing."
        ),
        "pricing": [
            {"label": "Managed lead-response service", "price": "$129–199/mo flat"},
        ],
    },
    "aitoolsbusiness": {
        "name": "AI Tools for Business",
        "segment": "business-systems",
        "business_line": "AIToolsBusiness",
        "one_liner": "Get set up on the AI tool you already pay for, properly.",
        "summary": (
            "Your AI tool set up properly and your whole team trained to "
            "actually use it well — not just installed and left to gather "
            "dust while you keep paying for it. Lighter and cheaper than a "
            "custom automation build (that's our AI Implementation "
            "service)."
        ),
        "pricing": [
            {"label": "Basic — 1 tool, 1 training session", "price": "$200–350 one-off"},
            {"label": "Standard — 2-3 tools, 2 sessions, template pack", "price": "$400–600 one-off"},
            {"label": "Optional ongoing support", "price": "$80–150/mo"},
        ],
    },
    "bookkeeping": {
        "name": "Small-Business Bookkeeping",
        "segment": "small-business-support",
        "business_line": "Bookkeeping",
        "one_liner": "Bank reconciliation and reporting, at a fixed monthly fee.",
        "summary": (
            "Your books kept accurate and current every month, with "
            "clear reporting you can actually understand — at one "
            "predictable fixed fee, never an open-ended hourly bill. "
            "Falling behind makes tax time stressful and makes it hard to "
            "know if you're actually profitable. BAS lodgement isn't "
            "included (that needs a registered BAS agent) and is referred "
            "out."
        ),
        "pricing": [
            {"label": "Micro (0-25 transactions/mo)", "price": "$149–179/mo"},
            {"label": "Small (25-100 transactions/mo)", "price": "$299–449/mo"},
        ],
    },
    "grantfinder": {
        "name": "SME Grant-Finder",
        "segment": "small-business-support",
        "business_line": "GrantFinder",
        "one_liner": "A curated shortlist of grants you actually qualify for.",
        "summary": (
            "A shortlist of the grants your business actually qualifies "
            "for, checked and ready to act on — so you're not the one "
            "spending hours working out what applies to you. A one-off "
            "report, not a subscription."
        ),
        "pricing": [
            {"label": "Grant-match shortlist report", "price": "$79–99 flat"},
        ],
    },
    "pension": {
        "name": "Age Pension / Centrelink Assistance",
        "segment": "seniors-support",
        "business_line": "Pension",
        "one_liner": "A flat, disclosed fee — no surprise minimums if you're found ineligible.",
        "summary": (
            "Your Age Pension claim or review handled and lodged "
            "properly — not financial advice. Centrelink's process is "
            "notoriously slow and easy to get wrong, and a mistake can "
            "cost you weeks of back-payments. A flat fee agreed and "
            "disclosed before we start, with no extra charge if the claim "
            "turns out not to be eligible."
        ),
        "pricing": [
            {"label": "New Age Pension claim", "price": "$349 flat"},
            {"label": "ARO appeal/review", "price": "$249 flat"},
        ],
    },
    "techconcierge": {
        "name": "Senior Technology Concierge",
        "segment": "seniors-support",
        "business_line": "TechConcierge",
        "one_liner": "Patient, plain-English tech help — teaching, not just fixing.",
        "summary": (
            "Patient, plain-English help with your devices, in-home or "
            "remote, at a fair per-session rate — no one-hour minimums, no "
            "jargon, and an eye kept out for anything that looks like a "
            "scam."
        ),
        "pricing": [
            {"label": "Standard session, in-person (~1hr)", "price": "$70–85"},
            {"label": "Standard session, remote (~1hr)", "price": "$55–65"},
            {"label": "Extended session (~1.5hr)", "price": "$105–125"},
            {"label": "Follow-up/check-in (~30min)", "price": "$40–50"},
        ],
    },
    "cryptoliteracy": {
        "name": "Crypto IT / Literacy Education",
        "segment": "seniors-support",
        "business_line": "CryptoLiteracy",
        "one_liner": "How wallets and exchanges actually work — not investment tips.",
        "summary": (
            "A clear, safe understanding of how crypto actually works, "
            "taught in plain English — enough to protect yourself and "
            "avoid costly mistakes. Education only, never investment or "
            "financial advice."
        ),
        "pricing": [
            {"label": "1:1 session", "price": "$85/hr"},
            {"label": "Small-group workshop", "price": "$59/head, or $349 flat for a private group up to 8"},
        ],
    },
    "digitallegacy": {
        "name": "Digital Legacy / Account Organiser",
        "segment": "seniors-support",
        "business_line": "DigitalLegacy",
        "one_liner": "A password manager set up, your accounts inventoried, written down for your family.",
        "summary": (
            "Your important accounts organised, secured, and properly "
            "documented, with a written handover your family can actually "
            "use — so the people who matter to you aren't left guessing if "
            "something ever happens to you."
        ),
        "pricing": [
            {"label": "Starter", "price": "$120–150"},
            {"label": "Full inventory", "price": "$250–320"},
            {"label": "Annual refresh", "price": "$80–100"},
        ],
    },
    "downsizing": {
        "name": "Senior Downsizing Support",
        "segment": "seniors-support",
        "business_line": "Downsizing",
        "one_liner": "Coordination for a move, or hands-on help — your choice.",
        "summary": (
            "A move handled for you — coordinated end-to-end, or with "
            "hands-on help packing and sorting, whichever you actually "
            "need. Downsizing alone means more decisions and phone calls "
            "than most people expect. Tell us which you need and we'll "
            "take it from there."
        ),
        "pricing": [
            {"label": "Coordination only", "price": "$45–65/hr, or $400–1,200 packaged"},
            {"label": "Hands-on labour/sorting", "price": "$80/hr flat"},
        ],
    },
    "photodigitisation": {
        "name": "Photo & Memory Digitisation",
        "segment": "seniors-support",
        "business_line": "PhotoDigitisation",
        "one_liner": "Your photos, slides, and videos, professionally digitised and organised for you.",
        "summary": (
            "Your photos, slides, and home videos collected, "
            "professionally digitised, and delivered back as one "
            "organised, easy-to-browse archive — not just a folder of "
            "files. Physical photos and old tapes degrade a little more "
            "every year they're left as they are."
        ),
        "pricing": [
            {"label": "Coordination/curation fee", "price": "~$55/hr, plus bureau scanning cost at their rate"},
        ],
    },
    "videorepurpose": {
        "name": "Video/Podcast Repurposing",
        "segment": "content-repurposing",
        "business_line": "VideoRepurpose",
        "one_liner": "One episode in, a week's worth of short clips out.",
        "summary": (
            "One recording turned into a full set of ready-to-post short "
            "clips for every platform that matters — polished, on-brand, "
            "and delivered without you touching an editing timeline. More "
            "content from the same effort means more chances to be found, "
            "without recording more."
        ),
        "pricing": [
            {"label": "Per episode (10 clips)", "price": "$249"},
            {"label": "Subscription (4 episodes/mo)", "price": "$199/episode"},
        ],
    },
}


def segment_by_slug(slug):
    return next((s for s in SEGMENTS if s["slug"] == slug), None)


def service_by_slug(slug):
    return SERVICES.get(slug)


def services_in_segment(slug):
    """Flat list of every service in a segment, regardless of whether it's
    defined as a flat list or as groups. Used where grouping doesn't
    matter (e.g. nothing currently, kept for any future flat listing)."""
    seg = segment_by_slug(slug)
    if not seg:
        return []
    if "groups" in seg:
        return [{"slug": s, **SERVICES[s]} for g in seg["groups"] for s in g["services"]]
    return [{"slug": s, **SERVICES[s]} for s in seg["services"]]


def segment_groups(slug):
    """Every segment normalised to the same shape for the template:
    [{"heading": str|None, "services": [service dicts]}, ...].
    Segments defined with a flat `services` list come back as one
    unheaded group; segments defined with `groups` come back as-is."""
    seg = segment_by_slug(slug)
    if not seg:
        return []
    if "groups" in seg:
        return [
            {"heading": g.get("heading"), "services": [{"slug": s, **SERVICES[s]} for s in g["services"]]}
            for g in seg["groups"]
        ]
    return [{"heading": None, "services": [{"slug": s, **SERVICES[s]} for s in seg["services"]]}]
