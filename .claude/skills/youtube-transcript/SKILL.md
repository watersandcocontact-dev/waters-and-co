---
name: youtube-transcript
description: Use whenever the user needs the transcript of a YouTube video — fetching, extracting, downloading, or pulling captions/subtitles/transcript text from a YouTube URL. Triggers on "get the transcript", "transcript of this video", "pull the captions", "download subtitles", "what does this YouTube video say". Uses yt-dlp locally (latest standalone binary, not the stale system one).
---

# YouTube Transcript (via yt-dlp)

Fetch a YouTube video's transcript and save a clean raw `.txt` file.

## Known environment gotcha

The system `/usr/bin/yt-dlp` on this machine is outdated (fails with
"Precondition check failed" / "Requested format is not available"). **Always use
a current standalone binary.** Download one to the scratchpad if not already
present this session:

```bash
curl -sL -o "$SCRATCH/yt-dlp" https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp && chmod +x "$SCRATCH/yt-dlp"
```

## Save location
- If working in a real project dir → save there (for this repo: `docs/video-intel/transcripts/`).
- **Name the file `Channel_Title`** with spaces replaced by `_` (or the repo's existing `NN_slug.txt` convention if saving into `docs/video-intel/`). If metadata is unavailable, fall back to the video ID.

## Fetch

```bash
OUT="$(pwd)"
META=$("$YTDLP" --print "%(channel)s|%(title)s|%(duration_string)s" --skip-download "URL")
"$YTDLP" --skip-download --write-subs --write-auto-subs \
  --sub-langs "en.*,en" --sub-format json3 \
  -o "$OUT/%(id)s.%(ext)s" "URL"
```

- `--skip-download` = captions only. `--write-subs` + `--write-auto-subs` = manual first, auto as fallback.
- Prefer `json3`; if only VTT is produced, dedupe repeated lines (rolling captions repeat every line twice).

## Flatten json3 → raw text

```bash
python3 - "$OUT" <<'PY'
import json, html, re, glob, sys, pathlib
f = glob.glob(sys.argv[1] + "/*.json3")
if not f: sys.exit("no json3 file")
data = json.load(open(f[0], encoding="utf-8"))
parts = ["".join(s.get("utf8","") for s in e.get("segs") or []) for e in data.get("events", [])]
txt = re.sub(r"\s+", " ", html.unescape(" ".join(p.strip() for p in parts if p.strip()))).strip()
out = pathlib.Path(f[0]).with_suffix(".txt")
out.write_text(txt, encoding="utf-8"); print(out)
PY
```

For timestamped output (better for long videos that will be analyzed), parse VTT
cue times or json3 `tStartMs` and emit `[HH:MM:SS] text` blocks merged to ~30s.

## Failure handling
- Non-English / unknown language: run `--list-subs "URL"` first, then set `--sub-langs`.
- On first failure: re-download the latest binary, retry once, then stop.
- **429 / "Sign in to confirm you're not a bot"** = IP flagged. STOP — do NOT retry in a loop (makes it worse).
- Web transcript services (NoteGPT etc.) gate full transcripts behind login — don't bother; captions via yt-dlp are the same source data.
- Never fall back to downloading audio for Whisper unless the user explicitly asks.

## Output

Report the saved path; print the text if short. For multi-video batches, loop
with a 2s sleep between videos.
