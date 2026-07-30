"""Content model for the public website — segments, services, pricing.

Real numbers pulled from wave1/*/pricing_sheet.md, not invented. Keep this
file in sync if pricing sheets change; it's a summary for web copy, not the
source of truth (the pricing sheets remain that).
"""

SEGMENTS = [
    {
        "slug": "local-presence",
        "name": "Local Presence",
        "tagline": "Show up, and look good when people find you",
        "services": ["gbp", "reviewgen"],
    },
    {
        "slug": "never-miss-a-call",
        "name": "Never Miss a Call",
        "tagline": "Every missed call still gets a response",
        "services": ["missedcall"],
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
        "segment": "local-presence",
        "business_line": "GBP",
        "one_liner": "Your Google listing, actually kept up to date.",
        "summary": (
            "A full audit and cleanup of your Google Business Profile — "
            "correct categories, current photos, an accurate description, "
            "and posts that actually go up — followed by ongoing monthly "
            "management so it never goes stale again."
        ),
        "pricing": [
            {"label": "One-off profile cleanup", "price": "$150–300"},
            {"label": "Ongoing monthly management", "price": "$100–200/mo"},
        ],
    },
    "reviewgen": {
        "name": "Review Generation & Reputation Management",
        "segment": "local-presence",
        "business_line": "ReviewGen",
        "one_liner": "More reviews, and a considered reply to every one.",
        "summary": (
            "An automated, compliant review-request flow for your "
            "customers, plus drafted responses to every review that comes "
            "in — good or bad. Often paired with Google Business Profile "
            "management, since the two feed each other directly."
        ),
        "pricing": [
            {"label": "One-off setup", "price": "$100–200"},
            {"label": "Ongoing monthly management", "price": "$100–300/mo"},
        ],
    },
    "missedcall": {
        "name": "AI Missed-Call Reception",
        "segment": "never-miss-a-call",
        "business_line": "MissedCall",
        "one_liner": "The call you couldn't take still gets handled.",
        "summary": (
            "An AI reception line that answers what you can't, texts the "
            "caller back, and captures the job — reviewed daily so nothing "
            "slips through. Underlying call costs are itemized separately, "
            "never hidden in the management fee."
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
            "Evidence research, comparable-sales analysis, and a properly "
            "drafted objection to your land or rates valuation. You lodge "
            "it yourself (most states require identity-verified lodgement) "
            "— the work is building the case that gets it reduced."
        ),
        "pricing": [
            {"label": "Standard residential objection", "price": "$400–800 flat"},
            {"label": "Commercial / complex property", "price": "Quote on assessment"},
        ],
    },
}


def segment_by_slug(slug):
    return next((s for s in SEGMENTS if s["slug"] == slug), None)


def service_by_slug(slug):
    return SERVICES.get(slug)


def services_in_segment(slug):
    seg = segment_by_slug(slug)
    if not seg:
        return []
    return [{"slug": s, **SERVICES[s]} for s in seg["services"]]
