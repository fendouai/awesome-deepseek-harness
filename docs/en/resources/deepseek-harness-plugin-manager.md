---
title: "deepseek-harness-plugin-manager"
description: "Web plugin manager for DeepSeek Harness (DSH): inspect, search, group, enable, and disable Cordis plugins."
keywords: "deepseek-harness-plugin-manager, search, plugin, coding, deepseek harness, dsh"
---
# deepseek-harness-plugin-manager

> ⭐ **3** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 3 | Status | ✅ active |
| Author | [hrhgit](https://github.com/hrhgit) | Updated | 2026-08-21 |
| Subcategory | 🌐 Web search | Capabilities | coding, search |

## One-liner

> Web plugin manager for DeepSeek Harness (DSH): inspect, search, group, enable, and disable Cordis plugins.

## About

[简体中文](README.zh-CN.md) This repository contains two independent community plugins for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness): - [`dsh-plugin-manager`](packages/manager) hot-loads already installed plugins through Cordis HMR in a running profile and manages their enablement and runtime state. - [`@ruihuahe/dsh-plugin-marketplace`](packages/marketplace) discovers, inspects, and installs npm plugin bundles with verified package and repository facts. This repository does not define its own plugin specification. The automatically generated [`catalog/v2`](catalog/v2) discovers package manifests in `dsh-plugin` topic repositories; GitHub Actions centrally verifies an exact npm version and repository ownership, and records whether the published package declares the of

## ✨ Key Features

- [`dsh-plugin-manager`](packages/manager) hot-loads already installed plugins through Cordis HMR in a running profile and manages their enablement and runtime st
- [`@ruihuahe/dsh-plugin-marketplace`](packages/marketplace) discovers, inspects, and installs npm plugin bundles with verified package and repository facts.

## 📦 Install

```bash
pnpm install
pnpm run typecheck
pnpm test
pnpm run build
pnpm run pack:check
```

## 🔗 Links

- [GitHub Repository](https://github.com/hrhgit/deepseek-harness-plugin-manager)
- [Full README](https://github.com/hrhgit/deepseek-harness-plugin-manager#readme)
- [Back to the Plugins list](../plugins.md)
