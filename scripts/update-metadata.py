#!/usr/bin/env python3
"""Refresh star counts, descriptions and update dates in the data registries.

Requires a GitHub token to avoid rate limits (but works without one too).

Usage:
    python3 scripts/update-metadata.py [--token gho_xxx]
"""
import argparse
import json
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
DATA_FILES = sorted(f for f in DATA_DIR.glob("*.json") if f.name not in ("candidates.json", "readmes.json", "official-guides.json"))


def repo_fullname(url):
    return url.replace("https://github.com/", "").rstrip("/")


def fetch(repo, token):
    headers = {"Accept": "application/vnd.github+json",
               "User-Agent": "awesome-dsh-metadata"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    url = "https://api.github.com/repos/" + repo
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=15) as resp:
        d = json.loads(resp.read())
    return {
        "stars": d["stargazers_count"],
        "description": (d.get("description") or "").strip(),
        "updated": d.get("pushed_at", "")[:10],
        "archived": d.get("archived", False),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--token", default=None)
    parser.add_argument("--jobs", type=int, default=8)
    args = parser.parse_args()

    repos = {}
    for f in DATA_FILES:
        data = json.loads(f.read_text())
        for e in data:
            repos[e["repository"]] = (f, e)

    results = {}
    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        futures = {pool.submit(fetch, repo_fullname(r), args.token): r for r in repos}
        for fut in as_completed(futures):
            r = futures[fut]
            try:
                results[r] = fut.result()
            except urllib.error.HTTPError as e:
                print(f"  [!] {r}: HTTP {e.code} — left unchanged")
            except Exception as e:  # noqa: BLE001
                print(f"  [!] {r}: {e} — left unchanged")
            time.sleep(0.05)

    updated = 0
    for f in DATA_FILES:
        data = json.loads(f.read_text())
        changed = False
        for e in data:
            meta = results.get(e["repository"])
            if not meta:
                continue
            if meta["stars"] != e.get("stars"):
                e["_stars_prev"] = e.get("stars", meta["stars"])
                e["stars"] = meta["stars"]
                e["growth"] = max(0, meta["stars"] - e.get("_stars_prev", meta["stars"]))
                changed = True
            if meta["description"] and meta["description"] != e.get("_source_description"):
                e["_source_description"] = meta["description"]
            if meta["archived"]:
                e["status"] = "inactive"
                changed = True
            e["_updated"] = meta["updated"]
        if changed:
            f.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
            updated += 1

    print(f"refreshed {len(results)}/{len(repos)} repos, rewrote {updated} files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
