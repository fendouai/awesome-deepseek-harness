#!/usr/bin/env python3
"""Deep-scan 0xsline/awesome-deepseek-harness and merge every live entry, categorized.

Parses the source README with its section structure, resolves dsh-external/*
redirects via the GitHub API, skips dead links and entries already in the
registry, then merges the remainder with proper type/category mapping.

Usage:
    python3 scripts/import-0xsline.py [--token gho_xxx] [--source /tmp/awesome0x.md]
"""
import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"

# 0xsline section heading -> (registry file, default type, default category)
SECTION_MAP = {
    "core": ("plugins.json", "plugin", "developer"),
    "context & search": ("plugins.json", "plugin", "search"),
    "input & editing": ("plugins.json", "plugin", "input-editing"),
    "ui & experience": ("plugins.json", "plugin", "ui"),
    "ide & clients": ("integrations.json", "integration", "ide"),
    "browser & remote": ("plugins.json", "plugin", "browser"),
    "models & inference": ("integrations.json", "integration", "developer"),
    "git & engineering": ("plugins.json", "plugin", "developer"),
    "output & deliverables": ("plugins.json", "plugin", "developer"),
    "notifications & channels": ("plugins.json", "plugin", "notifications"),
    "fun & lifestyle": ("plugins.json", "plugin", "fun"),
    "infrastructure & development": ("plugins.json", "plugin", "discovery"),
    "science & research": ("plugins.json", "plugin", "research"),
    "related": ("related.json", "related", "harness"),
}

HAS_CJK = re.compile(r"[\u4e00-\u9fff]")
URL_RE = re.compile(r"https://github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)")
HEAD_RE = re.compile(r"^##\s+(.*)$")
BULLET_RE = re.compile(r"^-\s+\[([^\]]*)\]\(([^)]*)\)(?:\s*-\s*(.*))?$")


def api_get(url, token):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "awesome-dsh-0xsline"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    for i in range(3):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=20) as resp:
                return json.loads(resp.read())
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            if e.code in (403, 429):
                time.sleep(5 * (i + 1))
            else:
                return None
        except Exception:  # noqa: BLE001
            time.sleep(2)
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--token", default=None)
    parser.add_argument("--source", default="/tmp/awesome0x.md")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    text = Path(args.source).read_text(encoding="utf-8", errors="ignore")

    # 1. parse sections and bullets
    section, items = None, []
    for line in text.splitlines():
        m = HEAD_RE.match(line)
        if m:
            section = m.group(1).strip().lower()
            continue
        m = BULLET_RE.match(line)
        if m and section:
            u = URL_RE.search(m.group(2))
            if u:
                items.append((section, u.group(1).rstrip("/"), m.group(3) or ""))

    # 2. resolve dsh-external/*
    resolved = {}
    for section, repo, desc in items:
        if repo.lower().startswith("dsh-external/"):
            meta = api_get(f"https://api.github.com/repos/{repo}", args.token)
            if not meta:
                print(f"  dead: {repo}")
                continue
            real = meta["html_url"].replace("https://github.com/", "").rstrip("/")
            resolved[real.lower()] = (section, desc, meta)
        else:
            resolved[repo.lower()] = (section, desc, None)

    # 3. existing registry
    existing = set()
    for f in DATA_DIR.glob("*.json"):
        if f.name in ("candidates.json", "readmes.json", "official-guides.json"):
            continue
        for e in json.loads(f.read_text()):
            if isinstance(e, dict) and "repository" in e:
                existing.add(e["repository"].replace("https://github.com/", "").lower())

    # 4. fetch metadata for missing ones
    new = []
    for repo, (section, desc, meta) in sorted(resolved.items()):
        if repo in existing:
            continue
        if not meta:
            meta = api_get(f"https://api.github.com/repos/{repo}", args.token)
        if not meta:
            print(f"  dead: {repo}")
            continue
        desc = (meta.get("description") or desc or "").strip()
        if not desc:
            desc = desc
        fname, etype, ecat = SECTION_MAP.get(section, ("plugins.json", "plugin", "developer"))
        e = {
            "id": re.sub(r"[^a-z0-9]+", "-", repo.split("/")[-1].lower()).strip("-"),
            "name": repo.split("/")[-1],
            "type": etype,
            "category": ecat,
            "repository": meta["html_url"],
            "description": desc,
            "description_zh": desc if HAS_CJK.search(desc) else desc,
            "capabilities": ["coding"],
            "status": "inactive" if meta.get("archived") else "active",
            "verified": False,
            "stars": meta.get("stargazers_count", 0),
        }
        d = (desc + " " + e["name"]).lower()
        if "terminal" in e["type"] or "tui" in d:
            e["type"], e["category"], fname = "client", "terminal", "clients.json"
        elif "desktop" in d or "launcher" in d:
            e["type"], e["category"], fname = "client", "desktop", "clients.json"
        elif "skill" in d:
            e["type"], e["category"], fname = "skill", "learning", "skills.json"
        elif "tutorial" in d or "学习" in d:
            e["type"], e["category"], fname = "tutorial", "learning", "tutorials.json"
        if "mcp" in d:
            e["capabilities"] = ["mcp", "coding"]
        elif "memory" in d or "记忆" in d:
            e["capabilities"] = ["memory"]
        elif "search" in d or "搜索" in d:
            e["capabilities"] = ["search"]
        new.append((fname, e))

    # 5. merge
    if args.dry_run:
        for fname, e in new:
            print(f"  {e['stars']:>5} [{fname}] {e['repository']} | {e['description'][:60]}")
        print(f"would add {len(new)} entries")
        return 0

    from collections import defaultdict
    groups = defaultdict(list)
    for fname, e in new:
        groups[fname].append(e)
    for fname, entries in groups.items():
        data = json.loads((DATA_DIR / fname).read_text())
        data.extend(entries)
        data.sort(key=lambda x: -x.get("stars", 0))
        (DATA_DIR / fname).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print(f"merged {len(new)} new entries from 0xsline list")
    return 0


if __name__ == "__main__":
    sys.exit(main())
