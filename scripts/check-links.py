#!/usr/bin/env python3
"""Check that every repository URL in the data registries is reachable.

Uses the GitHub API (unauthenticated, subject to rate limits) when available,
falling back to plain HTTP status checks.

Usage:
    python3 scripts/check-links.py [--token gho_xxx] [data/plugins.json ...]

Files listed on the command line limit the check to those registries
(useful for PR-scoped runs); with no files, every registry is checked.
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"


def load_entries(files):
    if files:
        names = {Path(f).name for f in files}
    entries = []
    for f in sorted(DATA_DIR.glob("*.json")):
        if f.name == "candidates.json":
            continue
        if files and f.name not in names:
            continue
        for e in json.loads(f.read_text()):
            if not isinstance(e, dict) or "repository" not in e:
                continue
            e["_file"] = f.name
            entries.append(e)
    return entries


def repo_fullname(url):
    return url.replace("https://github.com/", "").rstrip("/")


def check_github(repo, token):
    headers = {"Accept": "application/vnd.github+json",
               "X-GitHub-Api-Version": "2022-11-28"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    url = "https://api.github.com/repos/" + repo
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.status == 200, ""
    except urllib.error.HTTPError as e:
        if e.code in (403, 429):
            # Rate-limited (shared GITHUB_TOKEN quota): fall back to a plain
            # HEAD request against the public page, which is not rate-limited
            # the same way and still distinguishes 404 from existing repos.
            return check_plain("https://github.com/" + repo)
        return False, f"HTTP {e.code}"
    except Exception as e:  # noqa: BLE001
        return False, str(e)


def check_plain(url):
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "awesome-dsh-check"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.status in (200, 301, 302), f"HTTP {resp.status}"
    except urllib.error.HTTPError as e:
        return False, f"HTTP {e.code}"
    except Exception as e:  # noqa: BLE001
        return False, str(e)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--token", default=os.environ.get("GH_TOKEN"),
                        help="GitHub token to raise rate limits (defaults to $GH_TOKEN).")
    parser.add_argument("--jobs", type=int, default=8)
    parser.add_argument("files", nargs="*", help="Only check these data files (default: all).")
    args = parser.parse_args()

    entries = load_entries(args.files)
    failures = []
    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        futures = {pool.submit(check_github, repo_fullname(e["repository"]), args.token): e for e in entries}
        for fut in as_completed(futures):
            e = futures[fut]
            ok, msg = fut.result()
            if not ok:
                failures.append((e, msg))

    print(f"checked {len(entries)} repositories, {len(failures)} failures")
    for e, msg in failures:
        print(f"  [x] {e['repository']} ({e['_file']}) — {msg}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
