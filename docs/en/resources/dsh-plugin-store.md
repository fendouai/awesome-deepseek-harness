---
title: "dsh-plugin-store"
description: "DeepSeek Harness 插件商店：浏览、搜索、筛选并一键安装 dsh-plugin 生态插件"
keywords: "dsh-plugin-store, registry, awesome-list, coding, deepseek harness, dsh"
---
# dsh-plugin-store

> ⭐ **6** · ✅ active · awesome-list

| | | | |
|---|---|---|---|
| Type | awesome-list | Category | Registries |
| Stars | ⭐ 6 | Status | ✅ active |
| Author | [0xKcyzz](https://github.com/0xKcyzz) | Updated | — |

## One-liner

> DeepSeek Harness 插件商店：浏览、搜索、筛选并一键安装 dsh-plugin 生态插件

## About

[简体中文](README.zh.md) **Discover, filter, install, and manage community plugins without leaving DeepSeek Harness.** DSH Plugin Store turns the growing DeepSeek Harness plugin ecosystem into a searchable product experience. It uses live catalog data from [DSH Plugin Leaderboard](https://dshpluginleaderboard.com/) and adds Agent tools for programmatic discovery. [Preview release](https://github.com/sandbaseai/dsh-plugin-store/releases/tag/v0.1.0-preview.5) · [Leaderboard listing](https://dshpluginleaderboard.com/plugins/sandbaseai-dsh-plugin-store) · [Open the catalog](https://dshpluginleaderboard.com/) · [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) · [Report an issue](https://github.com/sandbaseai/dsh-plugin-store/issues)

## ✨ Key Features

- Browse more than 4,000 plugin packages across 3,400 community repositories
- Search by name, repository, description, or category
- Filter with the complete leaderboard tag taxonomy
- Sort by leaderboard rank, GitHub stars, or weekly growth
- Install catalog entries into a local DSH Web profile
- Inspect plugins already loaded by Cordis

## 📦 Install

```bash
curl -fL https://github.com/sandbaseai/dsh-plugin-store/releases/download/v0.1.0-preview.5/sandbaseai-dsh-plugin-store-0.1.0-preview.5.tgz -o /tmp/sandbaseai-dsh-plugin-store-0.1.0-preview.5.tgz
dsh plugin --profile web add -w /tmp/sandbaseai-dsh-plugin-store-0.1.0-preview.5.tgz
```

## 🚀 Quick Start

```bash
cd /path/to/deepseek-harness
git clone https://github.com/sandbaseai/dsh-plugin-store.git packages/plugins/dsh-store
pnpm install
pnpm --filter @sandbaseai/dsh-plugin-store typecheck
pnpm --filter @sandbaseai/dsh-plugin-store bundle
```

## 📚 Learn more

**Reproducible development installation**

DeepSeek Harness is evolving rapidly. For the current source integration, clone this repository into a Harness checkout, install the workspace, and build the host and Web client faces: cd /path/to/deepseek-harness git clone https://github.com/sandbaseai/dsh-plugin-store.git packages/plugins/dsh-store pnpm install pnpm --filter @sandbaseai/dsh-plugin-store typecheck pnpm --filter @sandbaseai/dsh-pl

**Architecture**

flowchart LR Catalog[Leaderboard API] --> Host[Store Host plugin] Host --> Tools[Agent tools] Host --> Proxy[Same-origin catalog proxy] Proxy --> UI[Native Store UI] Inventory[Cordis plugin inventory] --> UI UI --> Profile[Local DSH Web profile]

## 🔗 Links

- [GitHub Repository](https://github.com/0xKcyzz/dsh-plugin-store)
- [Full README](https://github.com/0xKcyzz/dsh-plugin-store#readme)
- [Back to the Awesome Lists & Registries list](../awesome-lists.md)
