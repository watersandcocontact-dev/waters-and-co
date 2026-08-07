"""Schema.org JSON-LD builders for the public website.

Kept deliberately conservative: only produce fields we can back with real,
unambiguous data.

Pricing in particular is a known trap here -- `SERVICES[*]["pricing"]`
holds human copy like "$45-65/hr, or $400-1,200 packaged" or "Quote on
assessment", not clean numbers. `parse_price_for_schema()` only emits a
numeric `PriceSpecification` for a single, unambiguous clause; anything
with alternatives ("or"), extras ("plus"), an approximation ("~"), or a
cap ("up to") -- or anything that plain doesn't match -- is left as free
text on the Offer instead. A wrong or misleading rich-result price is
worse than no price. Every unique price string in config.py was tested
against this parser before it shipped (30 of 33 parse cleanly; the other
3 are exactly the multi-clause ones described above, correctly rejected).

No phone number and no street address anywhere in this file -- matches
the deliberate site-wide decision (every page pushes to the contact form,
not a phone number; the business is home-based, so only the service area
is published, not a street address).
"""

import re

CANONICAL_DOMAIN = "https://watersandco.info"

BUSINESS_NAME = "Waters & Co"
BUSINESS_DESCRIPTION = (
    "Practical support across small business, AI systems, seniors and "
    "family technology, content repurposing and property valuation "
    "objections."
)

_PRICE_DISALLOWED_TOKENS = (" or ", " plus ", "~", "up to")
_PRICE_RE = re.compile(
    r"^\$(?P<low>[\d,]+)(?:\s*[–\-]\s*\$?(?P<high>[\d,]+))?"
    r"(?P<unit>/mo|/hr|/episode|/head)?"
    r"\s*(?P<qualifier>flat|fixed|one-off)?$"
)
_UNIT_CODE = {"/mo": "MON", "/hr": "HUR"}
_UNIT_TEXT = {"/episode": "per episode", "/head": "per head"}


def parse_price_for_schema(price_str):
    """Return {'minPrice', 'maxPrice', 'unitCode', 'unitText'} for a clean,
    single-clause price string, or None if it's a multi-clause range, an
    approximation, or free text (e.g. 'Quote on assessment') -- those
    aren't safe to collapse into a single numeric schema.org price.
    """
    lower = price_str.lower()
    if any(tok in lower for tok in _PRICE_DISALLOWED_TOKENS):
        return None
    m = _PRICE_RE.match(price_str.strip())
    if not m:
        return None
    low = int(m.group("low").replace(",", ""))
    high = int(m.group("high").replace(",", "")) if m.group("high") else low
    unit = m.group("unit")
    return {
        "minPrice": low,
        "maxPrice": high,
        "unitCode": _UNIT_CODE.get(unit),
        "unitText": _UNIT_TEXT.get(unit),
    }


def organization_ld():
    """Site-wide ProfessionalService block -- injected on every page via
    the `business_ld` context processor in routes.py."""
    return {
        "@context": "https://schema.org",
        "@type": "ProfessionalService",
        "@id": f"{CANONICAL_DOMAIN}/#business",
        "name": BUSINESS_NAME,
        "url": f"{CANONICAL_DOMAIN}/",
        "image": f"{CANONICAL_DOMAIN}/static/img/og-banner.png",
        "description": BUSINESS_DESCRIPTION,
        "address": {
            "@type": "PostalAddress",
            "addressLocality": "Perth",
            "addressRegion": "WA",
            "addressCountry": "AU",
        },
        "areaServed": "AU",
        "priceRange": "$$",
    }


def breadcrumb_ld(items):
    """items: list of (name, absolute_url) tuples, home first."""
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": name, "item": url}
            for i, (name, url) in enumerate(items)
        ],
    }


def service_ld(service, slug):
    offers = []
    for row in service.get("pricing", []):
        offer = {"@type": "Offer", "name": row["label"], "description": row["price"]}
        parsed = parse_price_for_schema(row["price"])
        if parsed:
            price_spec = {
                "@type": "PriceSpecification",
                "minPrice": parsed["minPrice"],
                "maxPrice": parsed["maxPrice"],
                "priceCurrency": "AUD",
            }
            if parsed["unitCode"]:
                price_spec["unitCode"] = parsed["unitCode"]
            if parsed["unitText"]:
                price_spec["unitText"] = parsed["unitText"]
            offer["priceSpecification"] = price_spec
        offers.append(offer)

    return {
        "@context": "https://schema.org",
        "@type": "Service",
        "@id": f"{CANONICAL_DOMAIN}/service/{slug}#service",
        "name": service["name"],
        "url": f"{CANONICAL_DOMAIN}/service/{slug}",
        "description": service["one_liner"],
        "provider": {"@id": f"{CANONICAL_DOMAIN}/#business"},
        "areaServed": "AU",
        "offers": offers,
    }
