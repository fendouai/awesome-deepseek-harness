---
title: "dsh-budget"
description: "Cost governance for DeepSeek Harness: aggregated token/cost metering per model, session and day, budget caps with threshold alerts and over-limit policies, carbon footprint estimation, per-model latency benchmarks, a Settings budget tab, and the /budget command"
keywords: "dsh-budget, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-budget

> ⭐ **3** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 3 | Status | ✅ active |
| Author | [PerryLink](https://github.com/PerryLink) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> Cost governance for DeepSeek Harness: aggregated token/cost metering per model, session and day, budget caps with threshold alerts and over-limit policies, carbon footprint estimation, per-model latency benchmarks, a Settings budget tab, and the /budget command

## About

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-budget` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **Cost governance for DeepSeek Harness: budgets, carbon, and latency in one panel.** *Know what every session costs — before it costs you.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ Key Features

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-budget` (counts toward the [deepseek1024.com](https://deepseek1024.c

## 📦 Install

```bash
# 1. install the bundle into your profile
dsh plugin --profile web add "github:PerryLink/dsh-budget#main"

# or from npm (published releases)
dsh plugin --profile web add dsh-budget

# 2. restart and verify the row
dsh --profile web --dump-config | grep -A2 'id: budget'
```

## 📚 Learn more

**Install & uninstall**

> If pnpm reports `ERR_PNPM_IGNORED_BUILDS` for this package (esbuild's harmless platform-binary validation), add `allowBuilds: { esbuild: true }` to your `pnpm-workspace.yaml` — the `dsh` CLI prints the exact snippet.

**Configuration**

All tunables are Schemastery `Config` fields (changeable from cordis.yml). `cordis.patch.yml` documents each key inline.

## 🔗 Links

- [GitHub Repository](https://github.com/PerryLink/dsh-budget)
- [Full README](https://github.com/PerryLink/dsh-budget#readme)
- [Back to the Plugins list](../plugins.md)
