---
title: "dsh-budget"
description: "Cost governance for DeepSeek Harness: aggregated token/cost metering per model, session and day, budget caps with threshold alerts and over-limit policies, carbon footprint estimation, per-model latency benchmarks, a Settings budget tab, and the /budget command"
keywords: "dsh-budget, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-budget

> ⭐ **3** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 3 | 状态 | ✅ 活跃 |
| 作者 | [PerryLink](https://github.com/PerryLink) | 更新时间 | — |
| 子分类 | 👁️ 视觉工具 | 能力 | coding |

## 一句话介绍

> Cost governance for DeepSeek Harness: aggregated token/cost metering per model, session and day, budget caps with threshold alerts and over-limit policies, carbon footprint estimation, per-model latency benchmarks, a Settings budget tab, and the /budget command

## 详细介绍

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-budget` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **Cost governance for DeepSeek Harness: budgets, carbon, and latency in one panel.** *Know what every session costs — before it costs you.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ 核心特性

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-budget` (counts toward the [deepseek1024.com](https://deepseek1024.c

## 📦 安装

```bash
# 1. install the bundle into your profile
dsh plugin --profile web add "github:PerryLink/dsh-budget#main"

# or from npm (published releases)
dsh plugin --profile web add dsh-budget

# 2. restart and verify the row
dsh --profile web --dump-config | grep -A2 'id: budget'
```

## 📚 更多信息

**Install & uninstall**

> If pnpm reports `ERR_PNPM_IGNORED_BUILDS` for this package (esbuild's harmless platform-binary validation), add `allowBuilds: { esbuild: true }` to your `pnpm-workspace.yaml` — the `dsh` CLI prints the exact snippet.

**Configuration**

All tunables are Schemastery `Config` fields (changeable from cordis.yml). `cordis.patch.yml` documents each key inline.

## 🔗 链接

- [GitHub 仓库](https://github.com/PerryLink/dsh-budget)
- [完整 README](https://github.com/PerryLink/dsh-budget#readme)
- [返回dsh-budget所在分类](../plugins.md)
