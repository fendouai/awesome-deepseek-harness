#!/usr/bin/env python3
"""Generate the MkDocs documentation site (docs/) from the data registries.

Produces bilingual pages (docs/en/, docs/zh/) with:
  - per-page SEO frontmatter (title / description / keywords)
  - a resource detail page for every registry entry (docs/*/resources/<id>.md)
  - a homepage built around the official awesome-deepseek-agent guide list

Usage:
    python3 scripts/generate-docs.py
"""
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
DOCS = ROOT / "docs"

READMES = {}
_RM = ROOT / "data" / "readmes.json"
if _RM.exists():
    READMES = json.loads(_RM.read_text())

SECTIONS = [
    ("plugins", "Plugins", "plugins.json"),
    ("skills", "Skills", "skills.json"),
    ("workflows", "Workflows & Automation", "workflows.json"),
    ("agents", "Agents & Multi-Agent", "agents.json"),
    ("clients", "Clients (Desktop & TUI)", "clients.json"),
    ("integrations", "MCP & Integrations", "integrations.json"),
    ("examples", "Examples & Starters", "examples.json"),
    ("tutorials", "Tutorials & Learning", "tutorials.json"),
    ("awesome-lists", "Awesome Lists & Registries", "awesome-lists.json"),
    ("related", "Related Agent Harnesses", "related.json"),
]

CATEGORY_EN = {
    "discovery": "Plugin discovery", "memory": "Memory & context", "search": "Search & research",
    "developer": "Developer tools", "ui": "UI & experience", "vision": "Vision & multimodal",
    "fun": "Fun & lifestyle", "input-editing": "Input & editing", "notifications": "Notifications",
    "browser": "Browser control", "workflow": "Workflows", "automation": "Automation",
    "research": "Research", "multi-agent": "Multi-agent", "desktop": "Desktop",
    "terminal": "Terminal", "mobile": "Mobile", "mcp": "MCP", "ide": "IDE & editors",
    "channel": "Channels", "acp": "ACP", "learning": "Learning", "registry": "Registries",
    "harness": "Harness", "coding": "Coding", "security": "Security",
}
CATEGORY_ZH = {
    "discovery": "插件发现", "memory": "记忆与上下文", "search": "搜索与研究",
    "developer": "开发者工具", "ui": "界面与体验", "vision": "视觉与多模态",
    "fun": "娱乐与生活", "input-editing": "输入与编辑", "notifications": "通知",
    "browser": "浏览器控制", "workflow": "工作流", "automation": "自动化",
    "research": "研究", "multi-agent": "多智能体", "desktop": "桌面端",
    "terminal": "终端", "mobile": "移动端", "mcp": "MCP", "ide": "IDE 与编辑器",
    "channel": "渠道", "acp": "ACP", "learning": "学习", "registry": "注册表",
    "harness": "Harness", "coding": "编码", "security": "安全",
}
STATUS_EN = {"active": "✅ active", "experimental": "🧪 experimental", "wip": "🚧 WIP", "inactive": "💤 inactive"}
STATUS_ZH = {"active": "✅ 活跃", "experimental": "🧪 实验性", "wip": "🚧 进行中", "inactive": "💤 停更"}

SUBCAT_EN = {
    "cost-billing": "💰 Cost & billing", "security-ops": "🛡️ Security & ops",
    "code-testing": "🧪 Code, tests & review", "files-import": "📁 Files & import",
    "tools": "🧰 Toolkits", "skins-themes": "🎨 Skins & themes", "desktop-pets": "🐋 Desktop pets",
    "sidebar-panels": "🖥️ Sidebars & panels", "status-stats": "📊 Status & stats",
    "input-enhancement": "⌨️ Input enhancement", "navigation": "🧭 Navigation",
    "memory-systems": "🧠 Memory systems", "context-management": "📦 Context management",
    "context-audit": "🔍 Context audit", "web-search": "🌐 Web search",
    "news-rss": "📰 News & RSS", "url-collection": "🔖 URL collection",
    "vision-tools": "👁️ Vision tools", "vision-bridges": "🔌 Vision bridges",
    "generative-ui": "💡 Generative UI",
}
SUBCAT_ZH = {
    "cost-billing": "💰 费用与统计", "security-ops": "🛡️ 安全与运维",
    "code-testing": "🧪 代码·测试·审查", "files-import": "📁 文件与导入",
    "tools": "🧰 工具与工具包", "skins-themes": "🎨 皮肤与主题", "desktop-pets": "🐋 桌面宠物",
    "sidebar-panels": "🖥️ 侧边栏与面板", "status-stats": "📊 状态与统计",
    "input-enhancement": "⌨️ 输入增强", "navigation": "🧭 导航与跳转",
    "memory-systems": "🧠 记忆系统", "context-management": "📦 上下文管理",
    "context-audit": "🔍 上下文审计", "web-search": "🌐 网页搜索",
    "news-rss": "📰 新闻与资讯", "url-collection": "🔖 URL 收藏",
    "vision-tools": "👁️ 视觉工具", "vision-bridges": "🔌 视觉桥接",
    "generative-ui": "💡 生成式界面",
}


def slug_id(e):
    return e["id"]


def yaml_q(s):
    """YAML-safe double-quoted string."""
    return '"' + str(s).replace("\\", "\\\\").replace('"', '\\"') + '"'


def frontmatter(title, description, keywords):
    kws = ", ".join(dict.fromkeys(k.strip() for k in keywords if k.strip()))
    return (f"---\ntitle: {yaml_q(title)}\ndescription: {yaml_q(description)}\n"
            f"keywords: {yaml_q(kws)}\n---\n")


def fmt_stars(n):
    return f"⭐{n:,}" if n else "–"


def badge(e, zh):
    return (STATUS_ZH if zh else STATUS_EN)[e["status"]]


def row(e, zh):
    desc = e["description_zh"] if zh else e["description"]
    link = f"resources/{slug_id(e)}.md"
    return f"| [{e['name']}]({link}) | {fmt_stars(e['stars'])} | {desc} | {badge(e, zh)} |"


def top_table(entries, zh, limit=10):
    if zh:
        head = "| # | 项目 | 星数 | 说明 | 状态 |\n|---|---|---|---|---|"
    else:
        head = "| # | Project | Stars | Description | Status |\n|---|---|---|---|---|"
    rows = [head]
    for i, e in enumerate(sorted(entries, key=lambda x: (-x["stars"], x["name"].lower()))[:limit], 1):
        desc = e["description_zh"] if zh else e["description"]
        rows.append(f"| {i} | [{e['name']}](resources/{slug_id(e)}.md) | {fmt_stars(e['stars'])} | {desc} | {badge(e, zh)} |")
    return "\n".join(rows)


def category_page(slug, title, entries, zh):
    n = len(entries)
    cat_map = CATEGORY_ZH if zh else CATEGORY_EN
    sub_map = SUBCAT_ZH if zh else SUBCAT_EN
    tr = trending_table(entries, zh)
    if zh:
        head = [f"# {title}", ""]
        if tr:
            head += ["## 🚀 Trending（近期增长最快）", "", tr, ""]
        head += [f"## 🔥 Top {min(10, n)}", "", top_table(entries, zh=True), "",
                 f"## 完整列表（{n}）", ""]
    else:
        head = [f"# {title}", ""]
        if tr:
            head += ["## 🚀 Trending (fastest growth)", "", tr, ""]
        head += [f"## 🔥 Top {min(10, n)}", "", top_table(entries, zh=False), "",
                 f"## Complete list ({n})", ""]
    lines = list(head)

    # group by category, then by subcategory when present
    groups = {}
    for e in entries:
        groups.setdefault(e["category"], []).append(e)

    table_head_zh = ["| 项目 | 星数 | 说明 | 状态 |", "|---|---|---|---|"]
    table_head_en = ["| Project | Stars | Description | Status |", "|---|---|---|---|"]
    other_label = "其他" if zh else "Other"

    for cat in sorted(groups, key=lambda c: -len(groups[c])):
        cat_entries = groups[cat]
        lines.append(f"\n**{cat_map.get(cat, cat)}（{len(cat_entries)}）**\n" if zh
                     else f"\n**{cat_map.get(cat, cat)} ({len(cat_entries)})**\n")

        subs = {}
        for e in cat_entries:
            subs.setdefault(e.get("subcategory") or "", []).append(e)
        has_sub = len(subs) > 1 or (len(subs) == 1 and "" not in subs and len(cat_entries) > 6)

        if has_sub:
            for sub in sorted(subs, key=lambda s: -len(subs[s])):
                sub_entries = sorted(subs[sub], key=lambda x: (-x["stars"], x["name"].lower()))
                label = sub_map.get(sub, sub) if sub else other_label
                lines.append(f"*{label}（{len(sub_entries)}）*\n" if zh
                             else f"*{label} ({len(sub_entries)})*\n")
                lines += table_head_zh if zh else table_head_en
                for e in sub_entries:
                    lines.append(row(e, zh))
        else:
            lines += table_head_zh if zh else table_head_en
            for e in sorted(cat_entries, key=lambda x: (-x["stars"], x["name"].lower())):
                lines.append(row(e, zh))
    lines.append("")
    return "\n".join(lines)


def resource_page(e, zh):
    name = e["name"]
    owner = e["repository"].replace("https://github.com/", "").split("/")[0]
    one = e["description_zh"] if zh else e["description"]
    readme = READMES.get(e["id"], {})
    intro = readme.get("intro") or one
    back = "../" + _back_slug(e) + ".md"
    cat_name = (CATEGORY_ZH if zh else CATEGORY_EN).get(e["category"], e["category"])
    type_label = {"plugin": "插件", "skill": "技能", "workflow": "工作流", "agent": "智能体",
                  "client": "客户端", "tool": "工具", "integration": "集成", "example": "示例",
                  "tutorial": "教程", "awesome-list": "精选列表", "related": "相关"}.get(e["type"], e["type"])
    subcat = (SUBCAT_ZH if zh else SUBCAT_EN).get(e.get("subcategory", ""), "") if e.get("subcategory") else ""
    updated = e.get("_updated", "—")
    growth = e.get("growth", 0)
    feats = [f for f in readme.get("features", []) if f]
    sections = [s for s in readme.get("sections", []) if s.get("t")]

    meta_lines = [f"# {name}", ""]
    if zh:
        meta_lines += [f"> ⭐ **{e['stars']:,}** · {badge(e, zh)} · {type_label}" + (f" · 近期 ⬆️ +{growth:,}" if growth else "") + "", ""]
        meta_lines += ["| | | | |", "|---|---|---|---|",
                       f"| 类型 | {type_label} | 分类 | {cat_name} |",
                       f"| 星数 | ⭐ {e['stars']:,} | 状态 | {badge(e, zh)} |",
                       f"| 作者 | [{owner}](https://github.com/{owner}) | 更新时间 | {updated} |"]
        if subcat:
            meta_lines.append(f"| 子分类 | {subcat} | 能力 | {', '.join(e.get('capabilities', []))} |")
        meta_lines += [""]
    else:
        meta_lines += [f"> ⭐ **{e['stars']:,}** · {badge(e, zh)} · {e['type']}" + (f" · ⬆️ +{growth:,} recently" if growth else "") + "", ""]
        meta_lines += ["| | | | |", "|---|---|---|---|",
                       f"| Type | {e['type']} | Category | {cat_name} |",
                       f"| Stars | ⭐ {e['stars']:,} | Status | {badge(e, zh)} |",
                       f"| Author | [{owner}](https://github.com/{owner}) | Updated | {updated} |"]
        if subcat:
            meta_lines.append(f"| Subcategory | {subcat} | Capabilities | {', '.join(e.get('capabilities', []))} |")
        meta_lines += [""]
    lines = meta_lines

    # one-liner
    lines += ["## 一句话介绍" if zh else "## One-liner", "", f"> {one}", ""]

    # about
    lines += ["## 详细介绍" if zh else "## About", "", intro, ""]

    # features
    if feats:
        lines.append("## ✨ 核心特性" if zh else "## ✨ Key Features")
        lines.append("")
        lines += [f"- {f}" for f in feats]
        lines.append("")

    # install + quick start
    if readme.get("install"):
        lines.append("## 📦 安装" if zh else "## 📦 Install")
        lines.append("")
        lines.append("```bash")
        lines.append(readme["install"])
        lines.append("```")
        lines.append("")
    if readme.get("usage"):
        lines.append("## 🚀 快速开始" if zh else "## 🚀 Quick Start")
        lines.append("")
        lines.append("```bash")
        lines.append(readme["usage"])
        lines.append("```")
        lines.append("")

    # extra sections from README
    if sections:
        lines.append("## 📚 更多信息" if zh else "## 📚 Learn more")
        lines.append("")
        for s in sections[:4]:
            lines.append(f"**{s['h']}**")
            lines.append("")
            lines.append(s["t"])
            lines.append("")

    # links
    if zh:
        lines += ["## 🔗 链接", "",
                  f"- [GitHub 仓库]({e['repository']})",
                  f"- [完整 README]({e['repository']}#readme)",
                  f"- [返回{e['name']}所在分类]({back})", ""]
    else:
        lines += ["## 🔗 Links", "",
                  f"- [GitHub Repository]({e['repository']})",
                  f"- [Full README]({e['repository']}#readme)",
                  f"- [Back to the {_back_title(e)} list]({back})", ""]
    return "\n".join(lines)


def _back_title(e):
    for slug, title, fname in SECTIONS:
        for entry in json.loads((DATA_DIR / fname).read_text()):
            if entry["id"] == e["id"]:
                return title
    return "overview"


def _back_slug(e):
    for slug, title, fname in SECTIONS:
        for entry in json.loads((DATA_DIR / fname).read_text()):
            if entry["id"] == e["id"]:
                return slug
    return "index"


def official_guides_table():
    guides = json.loads((DATA_DIR / "official-guides.json").read_text())
    lines = ["| Tool | Description | Guide |", "|---|---|---|"]
    for g in guides["tools"]:
        lines.append(f"| **{g['tool']}** | {g['description']} | [Guide]({g['guide']}) |")
    return "\n".join(lines)


def growth(e):
    return e.get("growth", 0) if isinstance(e.get("growth"), int) else 0


def trending_table(entries, zh, limit=5):
    grown = [e for e in entries if growth(e) > 0]
    if not grown:
        return None
    grown.sort(key=lambda x: (-growth(x), -x["stars"]))
    if zh:
        head = "| # | 项目 | 增长 | 星数 | 说明 |\n|---|---|---|---|---|"
    else:
        head = "| # | Project | Growth | Stars | Description |\n|---|---|---|---|---|"
    rows = [head]
    for i, e in enumerate(grown[:limit], 1):
        desc = e["description_zh"] if zh else e["description"]
        rows.append(f"| {i} | [{e['name']}](resources/{slug_id(e)}.md) | ⬆️ +{growth(e):,} | {fmt_stars(e['stars'])} | {desc} |")
    return "\n".join(rows)


def global_top(zh, limit=20):
    all_entries = []
    for slug, title, fname in SECTIONS:
        all_entries += json.loads((DATA_DIR / fname).read_text())
    return top_table(all_entries, zh, limit=limit)


def main():
    shutil.rmtree(DOCS, ignore_errors=True)
    (DOCS / "en" / "resources").mkdir(parents=True)
    (DOCS / "zh" / "resources").mkdir(parents=True)
    (DOCS / "assets").mkdir(parents=True)

    # category pages
    for slug, title, fname in SECTIONS:
        entries = json.loads((DATA_DIR / fname).read_text())
        n = len(entries)
        desc_en = f"Top {min(10, n)} and full list of {n} curated {title.lower()} for DeepSeek Harness (dsh)."
        desc_zh = f"DeepSeek Harness (dsh) 精选 {title.lower()}：🔥 Top {min(10, n)} 与完整列表（{n} 条）。"
        kws = ["deepseek harness", "dsh", title.lower().split(" (")[0].lower().replace(" & ", " "), "plugin", "awesome"]
        (DOCS / "en" / f"{slug}.md").write_text(
            frontmatter(title, desc_en, kws) + category_page(slug, title, entries, zh=False), encoding="utf-8")
        (DOCS / "zh" / f"{slug}.md").write_text(
            frontmatter(title, desc_zh, kws) + category_page(slug, title, entries, zh=True), encoding="utf-8")

    # resource detail pages
    count = 0
    for slug, title, fname in SECTIONS:
        for e in json.loads((DATA_DIR / fname).read_text()):
            kws = [e["name"], e.get("category", ""), e["type"],
                   *e.get("capabilities", []), "deepseek harness", "dsh"]
            (DOCS / "en" / "resources" / f"{slug_id(e)}.md").write_text(
                frontmatter(e["name"], e["description"], kws) + resource_page(e, zh=False), encoding="utf-8")
            (DOCS / "zh" / "resources" / f"{slug_id(e)}.md").write_text(
                frontmatter(e["name"], e["description_zh"], kws) + resource_page(e, zh=True), encoding="utf-8")
            count += 1

    # index pages
    all_entries = []
    for slug, title, fname in SECTIONS:
        all_entries += json.loads((DATA_DIR / fname).read_text())
    gtr = trending_table(all_entries, zh=False, limit=10)
    gtr_zh = trending_table(all_entries, zh=True, limit=10)
    (DOCS / "en" / "index.md").write_text(
        INDEX_EN.replace("{{GUIDES}}", official_guides_table())
                .replace("{{GTREND}}", gtr or "_数据积累中，下轮更新后显示。_")
                .replace("{{TOP}}", global_top(zh=False)),
        encoding="utf-8")
    (DOCS / "zh" / "index.md").write_text(
        INDEX_ZH.replace("{{GUIDES}}", official_guides_table())
                .replace("{{GTREND}}", gtr_zh or "_数据积累中，下轮更新后显示。_")
                .replace("{{TOP}}", global_top(zh=True)),
        encoding="utf-8")

    # robots.txt (served at site root in folder mode)
    (DOCS / "en" / "robots.txt").write_text(
        "User-agent: *\nAllow: /\n\nSitemap: https://deepseekserver.com/sitemap.xml\n", encoding="utf-8")

    print(f"docs/ generated: {len(SECTIONS)} category pages ×2, {count} resource pages ×2")
    return 0


INDEX_EN = """---
title: Awesome DeepSeek Harness — Everything is a Plugin
description: Curated ecosystem of plugins, skills, workflows, agents, clients, tools and examples for DeepSeek Harness (dsh). Official agent integration guides, trending Top 10 per category and 300+ verified resources.
keywords: deepseek harness, dsh, deepseek, ai agent, plugin, awesome, trending, agent harness, deepseek agent
---

# Awesome DeepSeek Harness 🐋

> A curated ecosystem of **plugins, skills, workflows, agents, clients, tools and examples** for the official [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) — with built-in 🔥 **Trending** rankings.

DeepSeek Harness (`dsh`) is DeepSeek AI's open-source agent harness built around a simple idea:

> **Everything is a Plugin.**

[简体中文](/zh/) · [Source](https://github.com/fendouai/awesome-deepseek-harness)

---

## 🚀 Official DeepSeek Agent Integration Guides

> 官方精选 —— [awesome-deepseek-agent](https://github.com/deepseek-ai/awesome-deepseek-agent)：将 DeepSeek 模型接入主流 Agent 与编码助手的一站式指南。

{{GUIDES}}

---

## 🚀 Global Trending

> Fastest-growing projects across the whole ecosystem in the last refresh cycle.

{{GTREND}}

## 🔥 Global Top 20

> The most starred projects in the whole ecosystem right now. Click any project for its detail page.

{{TOP}}

---

## Browse the ecosystem

| Section | What you'll find |
|---|---|
| [Plugins](plugins.md) | discovery, memory, search, developer tools, UI, vision, fun |
| [Skills](skills.md) | reusable agent procedures and knowledge |
| [Workflows & Automation](workflows.md) | deep research, plan → execute, automation |
| [Agents & Multi-Agent](agents.md) | teams, crosstalk, subagents, bridges |
| [Clients (Desktop & TUI)](clients.md) | desktop apps, terminal clients, mobile |
| [MCP & Integrations](integrations.md) | MCP servers, IDE, browser, channels, ACP |
| [Examples & Starters](examples.md) | templates you can run in minutes |
| [Tutorials & Learning](tutorials.md) | books, handbooks and courses |
| [Awesome Lists & Registries](awesome-lists.md) | directories and indexes |
| [Related Agent Harnesses](related.md) | the broader harness ecosystem |

## Project

- Source repository: [awesome-deepseek-harness](https://github.com/fendouai/awesome-deepseek-harness)
- Data registries: `data/*.json` (machine-readable, validated by CI)
- Every listed project has its own [detail page](plugins.md) with description, metadata and links.
"""

INDEX_ZH = """---
title: Awesome DeepSeek Harness — 一切皆插件
description: DeepSeek Harness (dsh) 生态精选：插件、技能、工作流、智能体、客户端、工具与示例。官方 DeepSeek Agent 集成指南、每类 Trending Top 10 与 300+ 已核验资源。
keywords: deepseek harness, dsh, deepseek, AI Agent, 插件, awesome, 热度榜, agent harness
---

# Awesome DeepSeek Harness 🐋

> 官方 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 生态精选：**插件 · 技能 · 工作流 · 智能体 · 客户端 · 工具 · 示例 · 教程**，内置 🔥 **Trending 热度榜**。

DeepSeek Harness（`dsh`）是 DeepSeek AI 开源的智能体 Harness，围绕一个简单理念构建：

> **一切皆插件（Everything is a Plugin）。**

[English](/index.html) · [源码仓库](https://github.com/fendouai/awesome-deepseek-harness)

---

## 🚀 官方 DeepSeek Agent 集成指南

> 官方精选 —— [awesome-deepseek-agent](https://github.com/deepseek-ai/awesome-deepseek-agent)：将 DeepSeek 模型接入主流 Agent 与编码助手的一站式指南。

{{GUIDES}}

---

## 🚀 全网 Trending

> 最近一轮更新中全生态增长最快的项目。

{{GTREND}}

## 🔥 全网 Top 20

> 整个生态当前星数最高的项目。点击任意项目进入详情页。

{{TOP}}

---

## 浏览生态

| 板块 | 内容 |
|---|---|
| [插件](plugins.md) | 发现、记忆、搜索、开发者工具、界面、视觉、娱乐 |
| [技能](skills.md) | 可复用的智能体流程与知识 |
| [工作流与自动化](workflows.md) | 深度研究、计划→执行、自动化 |
| [智能体与多智能体](agents.md) | 团队、跨会话、子代理、桥接 |
| [客户端（桌面与终端）](clients.md) | 桌面应用、终端客户端、移动端 |
| [MCP 与集成](integrations.md) | MCP 服务器、IDE、浏览器、渠道、ACP |
| [示例与模板](examples.md) | 几分钟即可运行的模板 |
| [教程与学习](tutorials.md) | 书籍、手册与课程 |
| [精选列表与注册表](awesome-lists.md) | 目录与索引 |
| [相关 Agent Harness](related.md) | 更广泛的 Harness 生态 |

## 项目说明

- 源码仓库：[awesome-deepseek-harness](https://github.com/fendouai/awesome-deepseek-harness)
- 数据注册表：`data/*.json`（机器可读，CI 校验）
- 每个上榜项目都有独立的[详情页](plugins.md)，包含介绍、元数据与链接。
"""


if __name__ == "__main__":
    raise SystemExit(main())
