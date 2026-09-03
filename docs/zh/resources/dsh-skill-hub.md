---
title: "dsh-skill-hub"
description: "DSH Web GUI 技能中枢：基于官方 ctx.skills 注册表浏览、搜索、启停、查看、诊断并新建本地技能，附技能市场：来源快照跟踪、一键全量更新。"
keywords: "dsh-skill-hub, discovery, plugin, ui, workflow, deepseek harness, dsh"
---
# dsh-skill-hub

> ⭐ **4** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 插件发现 |
| 星数 | ⭐ 4 | 状态 | ✅ 活跃 |
| 作者 | [cheshireez](https://github.com/cheshireez) | 更新时间 | 2026-08-19 |

## 一句话介绍

> DSH Web GUI 技能中枢：基于官方 ctx.skills 注册表浏览、搜索、启停、查看、诊断并新建本地技能，附技能市场：来源快照跟踪、一键全量更新。

## 详细介绍

[中文版](README.zh.md) | [English](README.md) In-GUI skill hub for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) — browse the full `ctx.skills` catalog, toggle skills, inspect bodies, fix discovery issues, install from the market, and scaffold new ones.

## ✨ 核心特性

- **Browse** — every root of the `ctx.skills` registry: project / user / bundled + third-party providers. Search across name, description, `displayName`; filter b
- **Toggle** — per-skill switches and per-group tri-state switches with a conflict dialog (close all / keep on). Disabling renames the discovery file (never delet
- **Organize** — scenes (tags) plus auto-aggregated source collections, all drag-reorderable and persisted in `~/.dsh/dsh-skill-hub.json`. Edit mode reveals delet
- **Diagnose & fix** — files the provider skips (missing frontmatter, bad YAML, name mismatch, short description) show up with reasons; auto-fixable ones (e.g. un
- **Scaffold** — new-skill wizard writing to `~/.dsh/skills` or `~/.agents/skills` (`SKILL.md` template below).
- **Market** — built-in curated repos plus custom `owner/repo` sources. Any top-level directory containing `SKILL.md` scans as a root (no allowlist). Async import
- **Track updates** — imported skills record a repo + commit snapshot. Check all / update-all, per-source badges (installed / updatable / deleted upstream / new r
- **Stats** — per-skill call counts + last-used times from session logs (incremental cache), group summaries; window and scan interval live-configurable from the 

## 📦 安装

```bash
dsh plugin --profile web add dsh-skill-hub
# restart dsh web → Settings → 技能 → Market → scan → import
```

## 🚀 快速开始

```bash
---
name: my-skill
description: One line when the agent should use this skill.
---
# my-skill
Body...
```

## 📚 更多信息

**restart dsh web → Settings → 技能 → Market → scan → import**

Requires `Node ^22.19 || >=24` + dsh web (`0.1.2-alpha.5`, `0.1.x` forward compatible).

## 🔗 链接

- [GitHub 仓库](https://github.com/cheshireez/dsh-skill-hub)
- [完整 README](https://github.com/cheshireez/dsh-skill-hub#readme)
- [返回dsh-skill-hub所在分类](../plugins.md)
