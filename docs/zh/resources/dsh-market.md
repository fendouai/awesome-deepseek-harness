---
title: "dsh-market"
description: "DSH 内置可视化插件市场：浏览、搜索、一键安装。"
keywords: "dsh-market, discovery, plugin, ui, workflow, deepseek harness, dsh"
---
# dsh-market

> ⭐ **1,582** · ✅ 活跃 · 插件 · 近期 ⬆️ +187

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 插件发现 |
| 星数 | ⭐ 1,582 | 状态 | ✅ 活跃 |
| 作者 | [dsh-market](https://github.com/dsh-market) | 更新时间 | 2026-08-21 |

## 一句话介绍

> DSH 内置可视化插件市场：浏览、搜索、一键安装。

## 详细介绍

The plugin market inside DeepSeek Harness. Open Settings → **Plugin Market** → browse, search, one-click install. One-click themes: install, switch live, no restart.

## ✨ 核心特性

- **Browse & search** the full community catalog (2300+ plugins, growing daily) — category filters, star counts, top/new sorting, bilingual descriptions that foll
- **Host-aware discovery** — cards show the DSH requirement declared by `engines.dsh` or lockstep `@deepseek-ai/dsh-*` peers; an opt-in filter hides only confirme
- **Screenshots** — AppStore-style screenshots, auto-carousel when there's more than one, click to preview full-size: author-curated shots show right on the card 
- **Comments** — every card opens the plugin's discussion thread in place. It is the same thread its pages on [dshmarket.com](https://dshmarket.com) and the [cata
- **Favorites** — bookmark plugins and themes from Discover or the Themes tab; a dedicated Favorites tab lists them with search, sort, and install actions. Bookma
- **Themes** — a dedicated tab for community themes and skins: install → active immediately, switch with one click (themes are mutually exclusive, your choice sur

## 📦 安装

```bash
dsh plugin --profile web add dshmarket
```

## 🚀 快速开始

```bash
- id: dsh-market
    name: dshmarket
    config:
      allowRestart: false   # NOT at the top level beside `name:`
```

## 📚 更多信息

**Install**

dsh plugin --profile web add dshmarket Restart `dsh web`, then open **Settings → Plugin Market**. **Requires dsh web 0.1.0-rc.6 or newer.** On an older host the market disables itself and says so in the browser console rather than rendering against primitives that are not there — if the Plugin Market entry never appears, that is usually why. Worth checking when a desktop build bundles its own dsh:

## 🔗 链接

- [GitHub 仓库](https://github.com/dsh-market/dsh-market)
- [完整 README](https://github.com/dsh-market/dsh-market#readme)
- [返回dsh-market所在分类](../plugins.md)
