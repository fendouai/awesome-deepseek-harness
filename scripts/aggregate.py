#!/usr/bin/env python3
"""Cross-source aggregation for the Awesome DeepSeek Harness registry.

Collects candidates from:
  1. Existing curated data/ (kept as-is, metadata refreshed)
  2. GitHub topic:dsh-plugin (top 100 by stars)
  3. GitHub topic:dsh (top 100 by stars, noise-filtered)
  4. "DeepSeek Harness" / "dsh-plugin" name+description searches
  5. Community awesome lists (parsed for github.com links)

Then: dedupe -> resolve dsh-external redirects -> filter noise ->
fetch metadata -> heuristic classification -> merge into data/*.json.

Usage:
    python3 scripts/aggregate.py --token gho_xxx [--dry-run]
"""
import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"

# --------------------------------------------------------------------------
# Source files (produced by the research phase)
# --------------------------------------------------------------------------
SOURCES = [
    "/tmp/dsh_r2/topic_plugin.json",
    "/tmp/dsh_r2/topic_dsh.json",
    "/tmp/dsh_r2/name_desc.json",
    "/tmp/dsh_refresh/name_dsh_plugin.json",
    "/tmp/dsh_search/q2_dsh-skill.json",
    "/tmp/dsh_search/q2_dsh-mcp.json",
    "/tmp/dsh_search/q2_dsh-agent.json",
    "/tmp/dsh_search/q_dsh-market.json",
    "/tmp/dsh_search/q_dsh-memory.json",
    "/tmp/dsh_search/q_dsh-toolkit.json",
    "/tmp/dsh_search/name_harness.json",
]
AWESOME_FILES = sorted(Path("/tmp/awesome_lists").glob("*.md")) + [
    Path("/tmp/awesome0x.md"),
]

# dsh-external org was emptied; known-good redirect targets (verified via API).
DSH_EXTERNAL_REDIRECTS = {}

REPO_RE = re.compile(r"github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)")
HAS_CJK = re.compile(r"[\u4e00-\u9fff]")


def is_noise(name, desc):
    """Filter repos that use 'dsh'/'deepseek' but are unrelated to the Harness."""
    n = name.lower()
    d = (desc or "").lower()
    if "dsh-external" in n:
        return True  # dead org namespace (redirects handled separately)
    if "dsharp" in n or "discord" in d:
        return True  # DSharpPlus etc.
    if n in ("deepseek-ai/deepseek-harness", "deepseek-ai/deepseek-harness.git"):
        return True  # the official repo itself is not a plugin
    if n in EXCLUDE:
        return True
    # keep only strongly-DSH-related signals
    return not (
        n.startswith("dsh")
        or n.startswith("deepseek-harness")
        or "deepseek harness" in d
        or "dsh-plugin" in d
        or " dsh " in d
        or d.startswith("dsh ")
        or "for deepseek harness" in d
        or "deepseek harness" in d
    )


# Known-unrelated projects using the same name space (see "Not the Same Project").
EXCLUDE = {
    "henryz838978/deepseek-harness",     # standalone DeepSeek API wrapper (pip lib)
    "devin-axis/ipollowork",             # general AI workspace, no DSH support
    "pm-shawn/abu-cowork",               # multi-model desktop app, no DSH support
    "morlay/deepseek-harness",           # redirected/unrelated ("use playpen instead")
    "octo-o-o-o/deepseek-harness-applicants",
}


def api_get(url, token, retries=3):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "awesome-dsh-aggregate"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=20) as resp:
                return json.loads(resp.read())
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            if e.code == 403 or e.code == 429:
                time.sleep(5 * (i + 1))
                continue
            return None
        except Exception:  # noqa: BLE001
            time.sleep(2)
    return None


def fetch_meta(repo, token):
    d = api_get(f"https://api.github.com/repos/{repo}", token)
    if not d:
        return None
    return {
        "repository": d["html_url"],
        "stars": d["stargazers_count"],
        "description": (d.get("description") or "").strip(),
        "updated": d.get("pushed_at", "")[:10],
        "archived": d.get("archived", False),
    }


def load_candidates():
    """repo(lower) -> dict(repository=..., stars=..., description=..., updated=..., source=...)."""
    pool = {}

    for f in SOURCES:
        p = Path(f)
        if not p.exists():
            continue
        try:
            items = json.loads(p.read_text())
        except Exception:  # noqa: BLE001
            continue
        for it in items:
            full = it.get("full_name") or it.get("fullName")
            if not full:
                continue
            key = full.lower()
            pool.setdefault(key, {
                "repository": f"https://github.com/{full}",
                "stars": it.get("stargazers_count") or it.get("stars") or 0,
                "description": (it.get("description") or "").strip(),
                "updated": (it.get("updated_at") or it.get("updated") or "")[:10],
                "source": str(f),
            })

    # community awesome lists
    for f in AWESOME_FILES:
        if not f.exists():
            continue
        text = f.read_text(encoding="utf-8", errors="ignore")
        for m in REPO_RE.finditer(text):
            full = m.group(1).rstrip("/")
            parts = full.split("/")
            if len(parts) != 2:
                continue
            key = full.lower()
            pool.setdefault(key, {
                "repository": f"https://github.com/{full}",
                "stars": 0,
                "description": "",
                "updated": "",
                "source": f.name,
            })

    return pool


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--token", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--min-stars", type=int, default=3,
                        help="Skip brand-new candidates below this star count (0 keeps all).")
    args = parser.parse_args()

    pool = load_candidates()

    # 1. resolve dsh-external/* via API redirects
    external = {k: v for k, v in pool.items() if k.startswith("dsh-external/")}
    for key in external:
        meta = fetch_meta(key, args.token)
        if meta:
            real = meta["repository"].replace("https://github.com/", "").lower()
            if real != key:
                pool.setdefault(real, meta | {"source": "dsh-external-redirect"})
                pool[real]["description"] = pool[real].get("description") or ""
        pool.pop(key, None)

    # 2. existing curated entries (metadata refreshed later by update-metadata)
    existing = {}
    for f in DATA_DIR.glob("*.json"):
        if f.name in ("candidates.json", "readmes.json", "official-guides.json"):
            continue
        for e in json.loads(f.read_text()):
            if not isinstance(e, dict) or "repository" not in e:
                continue
            existing[e["repository"].replace("https://github.com/", "").lower()] = e

    # 3. filter noise
    fresh = {}
    for key, cand in pool.items():
        if key in existing:
            continue
        if is_noise(key, cand.get("description", "")):
            continue
        fresh[key] = cand
    print(f"existing: {len(existing)} | new candidates after filter: {len(fresh)}")

    # 4. fetch metadata for new candidates
    metas = {}
    with ThreadPoolExecutor(max_workers=10) as ex:
        futs = {ex.submit(fetch_meta, k, args.token): k for k in fresh}
        for fut in as_completed(futs):
            k = futs[fut]
            m = fut.result()
            if m:
                metas[k] = m
    print(f"metadata fetched: {len(metas)} (missing: {len(fresh) - len(metas)})")

    # 5. apply star floor + build entries
    new_entries = []
    for key, cand in sorted(fresh.items(), key=lambda kv: -(kv[1].get("stars") or 0)):
        m = metas.get(key)
        if not m:
            continue
        if m["stars"] < args.min_stars:
            continue
        desc = m["description"]
        if not desc:
            continue
        entry = {
            "id": re.sub(r"[^a-z0-9]+", "-", key.split("/")[-1].lower()).strip("-"),
            "name": key.split("/")[-1],
            "type": "plugin",
            "category": "developer",
            "repository": m["repository"],
            "description": desc,
            "description_zh": desc if HAS_CJK.search(desc) else desc,
            "capabilities": ["coding"],
            "status": "inactive" if m["archived"] else "active",
            "verified": False,
            "stars": m["stars"],
        }
        new_entries.append(entry)

    # 6. heuristic classification
    classify(new_entries)

    if args.dry_run:
        by_file = {}
        for e in new_entries:
            by_file.setdefault(e["_file"], []).append(e)
        for f, es in sorted(by_file.items()):
            print(f"\n== {f} ({len(es)}) ==")
            for e in es[:60]:
                print(f"  {e['stars']:>5}  {e['repository']}  {e['description'][:60]}")
        return 0

    # 7. merge into data files
    merged = {f: json.loads((DATA_DIR / f).read_text()) for f in FILE_ORDER}
    for e in new_entries:
        file = e.pop("_file")
        merged[file].append(e)
    for f, entries in merged.items():
        entries.sort(key=lambda x: -x["stars"])
        (DATA_DIR / f).write_text(json.dumps(entries, ensure_ascii=False, indent=2) + "\n")
    print(f"merged {len(new_entries)} new entries into data/")
    return 0


# --- classification heuristics -------------------------------------------------

FILE_ORDER = [
    "plugins.json", "skills.json", "workflows.json", "agents.json", "clients.json",
    "integrations.json", "examples.json", "tutorials.json", "awesome-lists.json", "related.json",
]


def classify(entries):
    for e in entries:
        n = e["name"].lower()
        d = (e["description"] + " " + n).lower()
        e["_file"] = "plugins.json"  # default

        if any(k in d for k in ("awesome", "registry", "marketplace", "plugin-hub", "plugin-store",
                                "plugin directory", "curated list", "collection of plugins",
                                "聚合社区", "插件目录", "directory of plugins", "plugins community",
                                "store", "market")):
            e["_file"] = "awesome-lists.json"
            e["type"] = "awesome-list"
            e["category"] = "registry"
        elif any(k in d for k in ("tutorial", "handbook", "orange book", "learning", "learn ",
                                  "101", "from scratch", "入门", "教程", "手册", "学习", "从零")):
            e["_file"] = "tutorials.json"
            e["type"] = "tutorial"
            e["category"] = "learning"
        elif any(k in d for k in ("desktop", "electron", "tauri", "launcher", "tray",
                                  "termux", "android", "windows app", "桌面", "打包",
                                  "fnos", "desktop client", "desktop app", "desktop shell")):
            e["_file"] = "clients.json"
            e["type"] = "client"
            e["category"] = "desktop" if not any(k in d for k in ("termux", "android")) else "mobile"
        elif any(k in d for k in ("tui", "terminal client", "terminal ui", "terminal interface",
                                  "cli client", "command line")):
            e["_file"] = "clients.json"
            e["type"] = "client"
            e["category"] = "terminal"
        elif any(k in d for k in ("mcp", "bridge", "vscode", "ide ", "webstorm", "browser",
                                  "chrome", "telegram", "wechat", "feishu", "bot", "acp",
                                  "slack", "discord", "集成", "桥接")):
            e["_file"] = "integrations.json"
            e["type"] = "integration"
            e["category"] = ("mcp" if "mcp" in d else
                             "browser" if any(k in d for k in ("browser", "chrome", "computer use")) else
                             "channel" if any(k in d for k in ("telegram", "wechat", "feishu", "bot", "slack", "discord")) else
                             "ide" if any(k in d for k in ("vscode", "ide")) else "developer")
        elif any(k in d for k in ("内容发现", "content discovery", "recommendation agent", "推荐 agent",
                                  "推荐agent") or k.startswith("openbiliclaw")):
            e["_file"] = "agents.json"
            e["type"] = "agent"
            e["category"] = "research"
        elif any(k in d for k in ("skill", "工作流", "workflow", "workflow agent",
                                  "subagent", "agent team", "multi-agent", "crosstalk",
                                  "orchestr", "plan", "roleplay", "automation", "auto-continue",
                                  "deep research", "task", "scheduler", "定时", "自动化")):
            if any(k in d for k in ("workflow", "plan", "automation", "auto-continue", "scheduler",
                                    "deep research", "定时", "自动化", "loop engineering", "task-dag")):
                e["_file"] = "workflows.json"
                e["type"] = "workflow"
                e["category"] = "automation" if any(k in d for k in ("automation", "scheduler", "定时", "auto-continue")) else "workflow"
            elif any(k in d for k in ("subagent", "agent team", "multi-agent", "crosstalk",
                                      "orchestr", "roleplay", "a2a", "agent2agent", "会话")):
                e["_file"] = "agents.json"
                e["type"] = "agent"
                e["category"] = "multi-agent"
            else:
                e["_file"] = "skills.json"
                e["type"] = "skill"
                e["category"] = "learning"
        else:
            # plugins by capability keywords
            e["type"] = "plugin"
            if any(k in d for k in ("memory", "remember", "recall", "memo", "context",
                                    "压缩", "记忆", "上下文")):
                e["category"] = "memory" if "memory" in d or "记忆" in d else "memory"
            elif any(k in d for k in ("search", "web", "news", "rss", "检索", "搜索")):
                e["category"] = "search"
            elif any(k in d for k in ("skin", "theme", "sidebar", "panel", "pet", "whale",
                                      "ui", "avatar", "皮肤", "主题", "宠物", "侧边栏")):
                e["category"] = "ui"
            elif any(k in d for k in ("vision", "image", "ocr", "visual", "see", "图片",
                                      "视觉", "看图", "multimodal")):
                e["category"] = "vision"
            elif any(k in d for k in ("game", "emoji", "sticker", "fun", "joke", "摸鱼",
                                      "游戏", "表情", "整活")):
                e["category"] = "fun"
            elif any(k in d for k in ("notify", "notification", "通知")):
                e["category"] = "notifications"
            elif any(k in d for k in ("paste", "input", "drag", "quote", "annotation",
                                      "composer", "粘贴", "输入", "批注")):
                e["category"] = "input-editing"
            elif any(k in d for k in ("market", "find", "discover", "hub", "store",
                                      "市场", "发现", "安装")):
                e["category"] = "discovery"
            else:
                e["category"] = "developer"

        # capability hints
        caps = {"coding"}
        if any(k in e["description"].lower() for k in ("memory", "context", "recall")):
            caps.add("memory" if "memory" in e["description"].lower() else "context")
        if any(k in e["description"].lower() for k in ("search", "web search", "news")):
            caps.add("search")
        if any(k in e["description"].lower() for k in ("browser", "chrome", "computer use")):
            caps.add("browser")
        if "mcp" in e["description"].lower():
            caps.add("mcp")
        if "git" in e["description"].lower():
            caps.add("git")
        if any(k in e["description"].lower() for k in ("vision", "image", "ocr", "multimodal")):
            caps.add("multimodal")
        if any(k in e["description"].lower() for k in ("agent", "subagent", "team", "crosstalk")):
            caps.add("multi-agent")
        if any(k in e["description"].lower() for k in ("workflow", "plan", "automation")):
            caps.add("workflow")
        if any(k in e["description"].lower() for k in ("skin", "theme", "ui", "panel", "sidebar")):
            caps.add("ui")
        if any(k in e["description"].lower() for k in ("desktop", "electron", "tauri")):
            caps.add("desktop")
        if any(k in e["description"].lower() for k in ("terminal", "tui")):
            caps.add("terminal")
        e["capabilities"] = sorted(caps)


if __name__ == "__main__":
    sys.exit(main())
