---
title: "deepseek-harness-plugin-manager"
description: "Web plugin manager for DeepSeek Harness (DSH): inspect, search, group, enable, and disable Cordis plugins."
keywords: "deepseek-harness-plugin-manager, search, plugin, coding, deepseek harness, dsh"
---
# deepseek-harness-plugin-manager

> ⭐ **3** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 搜索与研究 |
| 星数 | ⭐ 3 | 状态 | ✅ 活跃 |
| 作者 | [hrhgit](https://github.com/hrhgit) | 更新时间 | 2026-08-21 |
| 子分类 | 🌐 网页搜索 | 能力 | coding, search |

## 一句话介绍

> Web plugin manager for DeepSeek Harness (DSH): inspect, search, group, enable, and disable Cordis plugins.

## 详细介绍

[简体中文](README.zh-CN.md) This repository contains two independent community plugins for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness): - [`dsh-plugin-manager`](packages/manager) hot-loads already installed plugins through Cordis HMR in a running profile and manages their enablement and runtime state. - [`@ruihuahe/dsh-plugin-marketplace`](packages/marketplace) discovers, inspects, and installs npm plugin bundles with verified package and repository facts. This repository does not define its own plugin specification. The automatically generated [`catalog/v2`](catalog/v2) discovers package manifests in `dsh-plugin` topic repositories; GitHub Actions centrally verifies an exact npm version and repository ownership, and records whether the published package declares the of

## ✨ 核心特性

- [`dsh-plugin-manager`](packages/manager) hot-loads already installed plugins through Cordis HMR in a running profile and manages their enablement and runtime st
- [`@ruihuahe/dsh-plugin-marketplace`](packages/marketplace) discovers, inspects, and installs npm plugin bundles with verified package and repository facts.

## 📦 安装

```bash
pnpm install
pnpm run typecheck
pnpm test
pnpm run build
pnpm run pack:check
```

## 🔗 链接

- [GitHub 仓库](https://github.com/hrhgit/deepseek-harness-plugin-manager)
- [完整 README](https://github.com/hrhgit/deepseek-harness-plugin-manager#readme)
- [返回deepseek-harness-plugin-manager所在分类](../plugins.md)
