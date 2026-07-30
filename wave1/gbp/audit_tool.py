#!/usr/bin/env python3
"""GBP audit scoring tool — companion to audit_checklist.md.

No API keys, no signup: you manually observe a business's Google Business
Profile (via Google Maps / Google Search) and answer the prompts, or pass a
JSON file with the same fields for batch scoring.

Usage:
    python3 audit_tool.py                      # interactive, one business
    python3 audit_tool.py --batch leads.json    # score many from a JSON file

JSON batch format (list of objects):
[
  {
    "name": "ABC Plumbing",
    "photo_count": 3, "photo_recent_90d": false,
    "post_last_30d": false,
    "review_count": 8,
    "review_response_rate_pct": 20,
    "review_response_fast": false,
    "hours_accurate": true,
    "category_correct": false,
    "description_quality": "generic",   // "none" | "generic" | "good"
    "website_link_works": true,
    "nap_consistent": true
  }
]
"""
import argparse
import json
import sys


def score_business(b):
    pts = {}

    # 1. Photos (15)
    photo_count = b.get("photo_count", 0)
    recent = b.get("photo_recent_90d", False)
    p1 = min(photo_count / 10, 1.0) * 10 + (5 if recent else 0)
    pts["photos"] = round(min(p1, 15), 1)

    # 2. Posts (15)
    pts["posts"] = 15 if b.get("post_last_30d") else 0

    # 3. Review count (15)
    rc = b.get("review_count", 0)
    pts["review_count"] = round(min(rc / 15, 1.0) * 15, 1)

    # 4. Review response rate (15)
    rr = b.get("review_response_rate_pct", 0)
    pts["review_response_rate"] = round((rr / 100) * 15, 1)

    # 5. Response speed (5)
    pts["review_response_speed"] = 5 if b.get("review_response_fast") else 0

    # 6. Hours (10)
    pts["hours"] = 10 if b.get("hours_accurate") else 0

    # 7. Category (10)
    pts["category"] = 10 if b.get("category_correct") else 0

    # 8. Description (5)
    desc = b.get("description_quality", "none")
    pts["description"] = {"none": 0, "generic": 2, "good": 5}.get(desc, 0)

    # 9. Website link (5)
    pts["website_link"] = 5 if b.get("website_link_works") else 0

    # 10. NAP consistency (5)
    pts["nap"] = 5 if b.get("nap_consistent") else 0

    total = round(sum(pts.values()), 1)
    return total, pts


def recommend(total, pts):
    tier = "STRONG OUTREACH TARGET" if total < 60 else ("QUICK WIN CANDIDATE" if total < 40 else "LOWER PRIORITY")
    if total < 40:
        tier = "QUICK WIN CANDIDATE (dramatic before/after possible)"
    weakest = sorted(pts.items(), key=lambda kv: kv[1])[:3]
    return tier, weakest


def print_result(name, total, pts):
    tier, weakest = recommend(total, pts)
    print(f"\n=== {name} ===")
    print(f"Score: {total}/100  ->  {tier}")
    print("Weakest areas (best pitch hooks):")
    for k, v in weakest:
        print(f"  - {k}: {v} pts")


def interactive():
    print("GBP Audit — answer for the business you're looking at:\n")
    b = {}
    name = input("Business name: ")
    b["photo_count"] = int(input("Total photo count: ") or 0)
    b["photo_recent_90d"] = input("Any photo added in last 90 days? (y/n): ").lower().startswith("y")
    b["post_last_30d"] = input("Google Post in last 30 days? (y/n): ").lower().startswith("y")
    b["review_count"] = int(input("Total review count: ") or 0)
    b["review_response_rate_pct"] = float(input("Approx. % of reviews with an owner reply: ") or 0)
    b["review_response_fast"] = input("Are replies posted within ~1 week? (y/n): ").lower().startswith("y")
    b["hours_accurate"] = input("Are listed hours accurate vs website/socials? (y/n): ").lower().startswith("y")
    b["category_correct"] = input("Is the primary category correct? (y/n): ").lower().startswith("y")
    desc = input("Description quality (none/generic/good): ").strip().lower() or "none"
    b["description_quality"] = desc if desc in ("none", "generic", "good") else "none"
    b["website_link_works"] = input("Does the website link work and go to a relevant page? (y/n): ").lower().startswith("y")
    b["nap_consistent"] = input("Is name/address/phone consistent with their website? (y/n): ").lower().startswith("y")

    total, pts = score_business(b)
    print_result(name, total, pts)


def batch(path):
    with open(path) as f:
        businesses = json.load(f)
    for b in businesses:
        total, pts = score_business(b)
        print_result(b.get("name", "Unnamed"), total, pts)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch", help="Path to a JSON file of businesses to score")
    args = parser.parse_args()
    if args.batch:
        batch(args.batch)
    else:
        try:
            interactive()
        except (EOFError, KeyboardInterrupt):
            sys.exit(0)
