#!/usr/bin/env python3
"""Regenerate the AUTO-generated resource tables inside README.md and README.zh-CN.md.

Editorial prose is hand-written and preserved; only blocks between
<!-- AUTO:resources:START --> and <!-- AUTO:resources:END --> are replaced.

Usage:
    python3 scripts/generate-readme.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"

SECTIONS = [
    ("Plugins", "plugins.json", "plugin"),
    ("Skills", "skills.json", "skill"),
    ("Workflows & Automation", "workflows.json", "workflow"),
    ("Agents & Multi-Agent", "agents.json", "agent"),
    ("Clients (Desktop & TUI)", "clients.json", "client"),
    ("MCP & Integrations", "integrations.json", "integration"),
    ("Examples & Starters", "examples.json", "example"),
    ("Tutorials & Learning", "tutorials.json", "tutorial"),
    ("Awesome Lists & Registries", "awesome-lists.json", "awesome-list"),
    ("Related Agent Harnesses", "related.json", "related"),
]

MARK_START = "<!-- AUTO:resources:START -->"
MARK_END = "<!-- AUTO:resources:END -->"


def badge(e):
    status = e["status"]
    sym = {"active": "✅", "experimental": "🧪", "wip": "🚧", "inactive": "💤"}[status]
    return f"{sym} {status}"


ZH_STATUS = {"active": "活跃", "experimental": "实验性", "wip": "进行中", "inactive": "停更"}


def badge_zh(e):
    sym = {"active": "✅", "experimental": "🧪", "wip": "🚧", "inactive": "💤"}[e["status"]]
    return f"{sym} {ZH_STATUS[e['status']]}"


def fmt_stars(n):
    return f"⭐{n:,}" if n else ""


def top_table(entries, zh):
    """Markdown table of the top 10 entries (by stars)."""
    if zh:
        head = "| # | 项目 | 星数 | 说明 | 状态 |\n|---|---|---|---|---|"
    else:
        head = "| # | Project | Stars | Description | Status |\n|---|---|---|---|---|"
    rows = [head]
    for i, e in enumerate(sorted(entries, key=lambda x: (-x["stars"], x["name"].lower()))[:10], 1):
        desc = e["description_zh"] if zh else e["description"]
        b = badge_zh(e) if zh else badge(e)
        rows.append(f"| {i} | [{e['name']}]({e['repository']}) | {fmt_stars(e['stars'])} | {desc} | {b} |")
    return "\n".join(rows)


def render_en(entries):
    n = len(entries)
    if not n:
        return "_None yet._"
    lines = [f"\n#### 🔥 Top {min(10, n)}\n", top_table(entries, zh=False),
             f"\n#### Complete list ({n})\n"]
    for e in sorted(entries, key=lambda x: (-x["stars"], x["name"].lower())):
        lines.append(f"- [{e['name']}]({e['repository']}) {fmt_stars(e['stars'])} — {e['description']} ({badge(e)})")
    return "\n".join(lines)


def render_zh(entries):
    n = len(entries)
    if not n:
        return "_暂无。_"
    lines = [f"\n#### 🔥 Top {min(10, n)}\n", top_table(entries, zh=True),
             f"\n#### 完整列表（{n}）\n"]
    for e in sorted(entries, key=lambda x: (-x["stars"], x["name"].lower())):
        lines.append(f"- [{e['name']}]({e['repository']}) {fmt_stars(e['stars'])} — {e['description_zh']}（{badge_zh(e)}）")
    return "\n".join(lines)


def replace_block(text, new_body):
    pattern = re.compile(re.escape(MARK_START) + r".*?" + re.escape(MARK_END), re.S)
    if not pattern.search(text):
        raise RuntimeError(f"markers {MARK_START}...{MARK_END} not found in file")
    return pattern.sub(lambda m: MARK_START + "\n" + new_body.rstrip() + "\n" + MARK_END, text)


def build_body(render_fn):
    chunks = []
    for title, fname, _ in SECTIONS:
        entries = __import__("json").loads((DATA_DIR / fname).read_text())
        chunks.append(f"\n### {title}\n")
        chunks.append(render_fn(entries))
    return "\n".join(chunks).lstrip("\n")


def main():
    for readme in (ROOT / "README.md", ROOT / "README.zh-CN.md"):
        text = readme.read_text(encoding="utf-8")
        render_fn = render_zh if readme.name.endswith("zh-CN.md") else render_en
        readme.write_text(replace_block(text, build_body(render_fn)), encoding="utf-8")
        print(f"regenerated {readme.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
