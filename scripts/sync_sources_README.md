# Sync / Refresh Instructions

The sandbox used to create this corpus did not have normal outbound DNS for Python/curl, so the crawler script is included for local use rather than executed here.

## Recommended refresh workflow

```bash
cd yc
python3 -m venv .venv
source .venv/bin/activate
pip install requests beautifulsoup4 lxml markdownify
python scripts/build_pg_manifest.py --output sources/pg_manifest.json --markdown sources/pg_manifest.md
```

## What the script does

- Downloads Paul Graham's essay index.
- Extracts essay titles and URLs.
- Writes JSON and Markdown manifests.
- Does not save full essay text unless you modify it.

## Next expansion

1. Build PG manifest.
2. Add summaries for the remaining P0/P1 essays.
3. Build a similar manifest for YC library pages.
4. Add transcript summaries manually where available.
5. Keep the office-hours playbooks action-oriented.
```
