---
name: save-idea
description: 'Quickly capture an idea into docs/ideas/ from any chat. Business/venture/service-line ideas go to BUSINESS-IDEAS.md; smaller marketing angles, content topics, questions, and observations go to CONTENT-TOPICS.md. Every entry gets a source line referencing the session it came from. Use when the user says "/save-idea", "save this idea", "write this down", "add a topic". Differentiator: appends to the idea backlog — not a reminder, task, or general note tool.'
---

# save-idea

Capture one thing fast, then get out of the way. Two buckets, two files (both in
`docs/ideas/` of the business app repo):

| Bucket | File | What belongs there |
|---|---|---|
| Business idea | `docs/ideas/BUSINESS-IDEAS.md` | A new service line, venture, product, or expansion concept |
| Topic | `docs/ideas/CONTENT-TOPICS.md` | Smaller stuff: marketing angles, content/post topics, questions, observations |

## Workflow

1. **Get the text.** Everything after `/save-idea` is the entry. Keep the user's wording verbatim — never rephrase, shorten, or "improve" it.
2. **Route it.**
   - Starts with `biz:` → business idea (strip the prefix).
   - Starts with `topic:` → topic (strip the prefix).
   - No prefix → judge: full venture/service concept → business idea; smaller thought → topic. Only if genuinely ambiguous, ask the user one short question.
3. **Read the target file** and find the last entry number. Next number = last + 1. Both files start at 1. Never renumber anything.
4. **Append at the bottom** (tab-indented context lines under the numbered line):

```
NNNN. Idea title exactly as the user said it
	source: Claude Code session, 2026-07-15
	any extra links or notes the user gave
```

5. **Build the source line.** Agent name plus session ID if the runtime exposes one; if unknown, just the agent name. Date: today, YYYY-MM-DD.
6. **Confirm back to the user**: the exact entry text, its number, and which file it went to.

## Rules

- Append only. Never edit, reorder, or renumber existing entries.
- Multiple ideas in one invocation → one numbered entry each.
- If a target file is missing, create it with a one-line header, then append entry 1.
- Indent context lines with a real tab character.
- Idea capture doesn't need Owner confirmation (it's local repo notes) — but acting on an idea later does.
