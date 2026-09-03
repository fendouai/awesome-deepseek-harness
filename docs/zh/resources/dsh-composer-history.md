---
title: "dsh-composer-history"
description: "Terminal-style input history for the DeepSeek Harness web composer: edge-first arrows with exact draft/caret restore, browser-local persisted history, Ctrl+R reverse search, workspace recall - and sliding-context awareness (compaction summaries in recall/search, compaction notice with one-click /compact fill)."
keywords: "dsh-composer-history, registry, awesome-list, browser, coding, context, search, terminal, deepseek harness, dsh"
---
# dsh-composer-history

> ⭐ **8** · ✅ 活跃 · 精选列表

| | | | |
|---|---|---|---|
| 类型 | 精选列表 | 分类 | 注册表 |
| 星数 | ⭐ 8 | 状态 | ✅ 活跃 |
| 作者 | [PerryLink](https://github.com/PerryLink) | 更新时间 | — |

## 一句话介绍

> Terminal-style input history for the DeepSeek Harness web composer: edge-first arrows with exact draft/caret restore, browser-local persisted history, Ctrl+R reverse search, workspace recall - and sliding-context awareness (compaction summaries in recall/search, compaction notice with one-click /compact fill).

## 详细介绍

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-composer-history` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **Terminal-style input history for the DeepSeek Harness Web GUI composer.** *Press ↑ like it's in a terminal — and keep your half-typed draft safe.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ 核心特性

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-composer-history` (counts toward the [deepseek1024.com](https://deep

## 📦 安装

```bash
# 1. install the bundle into your profile
dsh plugin --profile web add "github:PerryLink/dsh-composer-history#main"

# or from npm (published releases)
dsh plugin --profile web add dsh-composer-history

# 2. restart and verify the row
dsh --profile web --dump-config | grep -A3 'id: composer-history'
```

## 🚀 快速开始

```bash
/save ship-check --tag=release,ops
check the build, run the smoke suite, tag the release        ← the rest of the draft is the snippet
/save ship-check                                             → "snippet saved: ship-check"
/load ship-check                                             → the snippet fills the composer
Ctrl+R → search panel lists snippets (green badge = name) alongside history
```

## 📚 更多信息

**Install & uninstall**

The npm package ships the built bundles; a source checkout must be built first (`pnpm run build`) — the client-package check refuses to boot against an unbuilt bundle.

**Configuration**

All tunables are Schemastery `Config` fields (changeable from cordis.yml and the settings document). An id-targeted override replaces the whole row — restate every key you need. Invalid enum values fail the whole dsh boot loudly.

## 🔗 链接

- [GitHub 仓库](https://github.com/PerryLink/dsh-composer-history)
- [完整 README](https://github.com/PerryLink/dsh-composer-history#readme)
- [返回dsh-composer-history所在分类](../awesome-lists.md)
