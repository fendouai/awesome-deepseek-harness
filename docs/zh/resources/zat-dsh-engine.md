---
title: "zat-dsh-engine"
description: "Visual plugin marketplace for DeepSeek Harness — browse, search and install community plugins"
keywords: "zat-dsh-engine, registry, awesome-list, coding, search, deepseek harness, dsh"
---
# zat-dsh-engine

> ⭐ **76** · ✅ 活跃 · 精选列表 · 近期 ⬆️ +3

| | | | |
|---|---|---|---|
| 类型 | 精选列表 | 分类 | 注册表 |
| 星数 | ⭐ 76 | 状态 | ✅ 活跃 |
| 作者 | [mishibeikejie](https://github.com/mishibeikejie) | 更新时间 | 2026-08-19 |

## 一句话介绍

> Visual plugin marketplace for DeepSeek Harness — browse, search and install community plugins

## 详细介绍

[English](#zat-dsh-engine) · [中文说明](README.zh.md) Zat-DSH Engine adds a **Plugin Market** tab to **Settings → Plugins** in the DeepSeek Harness web GUI. It lists the entire `dsh-plugin` topic community from GitHub, shows bilingual intros, and installs plugins with one click.

## ✨ 核心特性

- **Full community catalog** — live GitHub search of the `dsh-plugin` topic (1700+ repositories, growing daily)
- **AI plugin finder** — in any conversation just say what you need (e.g. "find me a plugin that lets the model see images") and the AI searches the market, recom
- **12 categories** — Theme, Tools, Browser, Skills, Vision, Network, Agents, Data, Hardware, Design, Security…
- **Live search** — type to filter, no Enter key needed; clearing the box returns to the full list
- **Bilingual intros** — 999 pre-translated Chinese intros bundled; new plugins keep their English intro (on-the-fly model translation is removed — with peak/off-
- **Install / Update / Uninstall** — one click, powered by the official `dsh plugin` profile mechanism (`pnpm` under the hood)
- **Monorepo-aware install** — repositories that bundle several plugins install correctly: a single-plugin repo installs silently, multi-plugin repos offer a plai
- **Installed detection** — marks plugins you already have, with version comparison and an **update badge** when a newer version is released

## 📦 安装

```bash
dsh plugin --profile web add github:mishibeikejie/zat-dsh-engine
```

## 🚀 快速开始

```bash
dsh plugin --profile web add https://gh-proxy.com/https://github.com/mishibeikejie/zat-dsh-engine.git
```

## 📚 更多信息

**Installation**

> ⚠️ **Install it with the command below — do NOT hand-edit any patch file.** > Letting an AI "install" this project by pasting the repo URL and manually editing `cordis.patch.yml` breaks dsh: the market's own `plugin-market` row is auto-mounted by dsh from the bundled patch, and writing it by hand into two places (`app.asar.unpacked/cordis.patch.yml` and `~/.dsh/profiles/<profile>/cordis.patch.ym

**Usage**

1. Restart dsh after installing. 2. Open the web GUI → **Settings → Plugins**. 3. Click the **🛒 Plugin Market** tab on the right of the plugin list. 4. Browse, search, filter by category or install state, and click **Install** on any card. 5. Restart dsh to activate installed plugins.

**FAQ**

**The market shows at most 1000 plugins in the All view.** GitHub's search API caps any query at 1000 results. Search and category filters reach every plugin regardless. **Why do some plugins have no Chinese intro?** 999 Chinese intros ship with the plugin. Plugins released after the snapshot keep their English description — live on-the-fly translation is removed, because with DeepSeek's peak/off-

## 🔗 链接

- [GitHub 仓库](https://github.com/mishibeikejie/zat-dsh-engine)
- [完整 README](https://github.com/mishibeikejie/zat-dsh-engine#readme)
- [返回zat-dsh-engine所在分类](../awesome-lists.md)
