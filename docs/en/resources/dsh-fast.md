---
title: "dsh-fast"
description: "Read-only performance diagnostics: session load timing, spill/compaction stats, context volume and LLM cache hit rate."
keywords: "dsh-fast, developer, plugin, observability, deepseek harness, dsh"
---
# dsh-fast

> ⭐ **3** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 3 | Status | ✅ active |
| Author | [PerryLink](https://github.com/PerryLink) | Updated | — |
| Subcategory | 💰 Cost & billing | Capabilities | observability |

## One-liner

> Read-only performance diagnostics: session load timing, spill/compaction stats, context volume and LLM cache hit rate.

## About

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-fast` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **Read-only performance diagnostics for DeepSeek Harness.** *Observes the session event stream — never the model hot path — and reports where latency and context budget actually go.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ Key Features

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-fast` (counts toward the [deepseek1024.com](https://deepseek1024.com

## 📦 Install

```bash
# From a scratch profile (pins the commit; runs the self-contained `prepare` build)
dsh plugin --profile demo add "github:YOUR_ORG/dsh-fast#<sha>"
# The profile's pnpm-workspace.yaml gains an allowBuilds entry for dsh-fast on first add.
```

## 🚀 Quick Start

```bash
dsh plugin --profile demo add dsh-fast
```

## 📚 Learn more

**Install & uninstall**

dsh plugin --profile demo add dsh-fast # install dsh plugin --profile demo remove dsh-fast # uninstall Verify the row mounts: `dsh --profile demo --dump-config | grep dsh-fast`.

**Configuration**

All tunables are Schemastery `Config` fields; invalid values fail the profile load loudly.

## 🔗 Links

- [GitHub Repository](https://github.com/PerryLink/dsh-fast)
- [Full README](https://github.com/PerryLink/dsh-fast#readme)
- [Back to the Plugins list](../plugins.md)
