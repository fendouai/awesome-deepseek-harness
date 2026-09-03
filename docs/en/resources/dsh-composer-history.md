---
title: "dsh-composer-history"
description: "Terminal-style input history for the DeepSeek Harness web composer: edge-first arrows with exact draft/caret restore, browser-local persisted history, Ctrl+R reverse search, workspace recall - and sliding-context awareness (compaction summaries in recall/search, compaction notice with one-click /compact fill)."
keywords: "dsh-composer-history, registry, awesome-list, browser, coding, context, search, terminal, deepseek harness, dsh"
---
# dsh-composer-history

> ⭐ **8** · ✅ active · awesome-list

| | | | |
|---|---|---|---|
| Type | awesome-list | Category | Registries |
| Stars | ⭐ 8 | Status | ✅ active |
| Author | [PerryLink](https://github.com/PerryLink) | Updated | — |

## One-liner

> Terminal-style input history for the DeepSeek Harness web composer: edge-first arrows with exact draft/caret restore, browser-local persisted history, Ctrl+R reverse search, workspace recall - and sliding-context awareness (compaction summaries in recall/search, compaction notice with one-click /compact fill).

## About

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-composer-history` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **Terminal-style input history for the DeepSeek Harness Web GUI composer.** *Press ↑ like it's in a terminal — and keep your half-typed draft safe.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ Key Features

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-composer-history` (counts toward the [deepseek1024.com](https://deep

## 📦 Install

```bash
# 1. install the bundle into your profile
dsh plugin --profile web add "github:PerryLink/dsh-composer-history#main"

# or from npm (published releases)
dsh plugin --profile web add dsh-composer-history

# 2. restart and verify the row
dsh --profile web --dump-config | grep -A3 'id: composer-history'
```

## 🚀 Quick Start

```bash
/save ship-check --tag=release,ops
check the build, run the smoke suite, tag the release        ← the rest of the draft is the snippet
/save ship-check                                             → "snippet saved: ship-check"
/load ship-check                                             → the snippet fills the composer
Ctrl+R → search panel lists snippets (green badge = name) alongside history
```

## 📚 Learn more

**Install & uninstall**

The npm package ships the built bundles; a source checkout must be built first (`pnpm run build`) — the client-package check refuses to boot against an unbuilt bundle.

**Configuration**

All tunables are Schemastery `Config` fields (changeable from cordis.yml and the settings document). An id-targeted override replaces the whole row — restate every key you need. Invalid enum values fail the whole dsh boot loudly.

## 🔗 Links

- [GitHub Repository](https://github.com/PerryLink/dsh-composer-history)
- [Full README](https://github.com/PerryLink/dsh-composer-history#readme)
- [Back to the Awesome Lists & Registries list](../awesome-lists.md)
