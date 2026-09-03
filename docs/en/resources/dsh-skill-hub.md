---
title: "dsh-skill-hub"
description: "In-GUI skill manager for DeepSeek Harness: browse, search, toggle, inspect, diagnose and scaffold local skills from the official ctx.skills registry, plus a skill market with tracked source sync and one-click update-all."
keywords: "dsh-skill-hub, discovery, plugin, ui, workflow, deepseek harness, dsh"
---
# dsh-skill-hub

> ⭐ **4** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Plugin discovery |
| Stars | ⭐ 4 | Status | ✅ active |
| Author | [cheshireez](https://github.com/cheshireez) | Updated | 2026-08-19 |

## One-liner

> In-GUI skill manager for DeepSeek Harness: browse, search, toggle, inspect, diagnose and scaffold local skills from the official ctx.skills registry, plus a skill market with tracked source sync and one-click update-all.

## About

[中文版](README.zh.md) | [English](README.md) In-GUI skill hub for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) — browse the full `ctx.skills` catalog, toggle skills, inspect bodies, fix discovery issues, install from the market, and scaffold new ones.

## ✨ Key Features

- **Browse** — every root of the `ctx.skills` registry: project / user / bundled + third-party providers. Search across name, description, `displayName`; filter b
- **Toggle** — per-skill switches and per-group tri-state switches with a conflict dialog (close all / keep on). Disabling renames the discovery file (never delet
- **Organize** — scenes (tags) plus auto-aggregated source collections, all drag-reorderable and persisted in `~/.dsh/dsh-skill-hub.json`. Edit mode reveals delet
- **Diagnose & fix** — files the provider skips (missing frontmatter, bad YAML, name mismatch, short description) show up with reasons; auto-fixable ones (e.g. un
- **Scaffold** — new-skill wizard writing to `~/.dsh/skills` or `~/.agents/skills` (`SKILL.md` template below).
- **Market** — built-in curated repos plus custom `owner/repo` sources. Any top-level directory containing `SKILL.md` scans as a root (no allowlist). Async import
- **Track updates** — imported skills record a repo + commit snapshot. Check all / update-all, per-source badges (installed / updatable / deleted upstream / new r
- **Stats** — per-skill call counts + last-used times from session logs (incremental cache), group summaries; window and scan interval live-configurable from the 

## 📦 Install

```bash
dsh plugin --profile web add dsh-skill-hub
# restart dsh web → Settings → 技能 → Market → scan → import
```

## 🚀 Quick Start

```bash
---
name: my-skill
description: One line when the agent should use this skill.
---
# my-skill
Body...
```

## 📚 Learn more

**restart dsh web → Settings → 技能 → Market → scan → import**

Requires `Node ^22.19 || >=24` + dsh web (`0.1.2-alpha.5`, `0.1.x` forward compatible).

## 🔗 Links

- [GitHub Repository](https://github.com/cheshireez/dsh-skill-hub)
- [Full README](https://github.com/cheshireez/dsh-skill-hub#readme)
- [Back to the Plugins list](../plugins.md)
