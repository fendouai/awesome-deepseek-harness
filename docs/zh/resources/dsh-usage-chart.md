---
title: "dsh-usage-chart"
description: "A DeepSeek Harness Web plugin for real-time Token usage, cost estimates, per-round charts, and DeepSeek API balance."
keywords: "dsh-usage-chart, search, plugin, coding, deepseek harness, dsh"
---
# dsh-usage-chart

> ⭐ **10** · ✅ 活跃 · 插件 · 近期 ⬆️ +3

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 搜索与研究 |
| 星数 | ⭐ 10 | 状态 | ✅ 活跃 |
| 作者 | [Max-Samson](https://github.com/Max-Samson) | 更新时间 | 2026-08-18 |
| 子分类 | 🌐 网页搜索 | 能力 | coding |

## 一句话介绍

> A DeepSeek Harness Web plugin for real-time Token usage, cost estimates, per-round charts, and DeepSeek API balance.

## 详细介绍

[简体中文](./README_ZH.md) · [Report an issue](https://github.com/Max-Samson/dsh-usage-chart/issues) · [Changelog (EN)](./CHANGELOG.md) · [更新日志（中文）](./CHANGELOG_ZH.md) Interface preview: light English on the left and dark Simplified Chinese on the right. Both variants follow the DSH theme and in-app language setting. Light theme · English Dark theme · 简体中文 The plugin adds a compact indicator below the conversation composer. It shows input/output tokens, cache-hit ratio, estimated cost, active model, a multi-segment context-pressure bar (system/tools/messages breakdown, v1.1.0), and DeepSeek account balance. Click it to open a zero-dependency SVG dashboard with per-turn usage history — including a cost view (every bar shows its own cost value, not just the current round), a duration overlay, an

## ✨ 核心特性

- **Session usage summary** — Input (uncached/cached), output, cache-hit percentage, and context occupancy (derived from official adapter `tokenUsage` / `contextP
- **Context breakdown & compaction diagnostics (v1.1.0)** — Official `contextBreakdown` projection breakdown (System prompt / Tools schema / Message history token
- **Cost estimation** — Estimated from official list prices (CNY/USD dual-currency per 1M tokens, peak/off-peak tiers) with verified source date; supports user ov
- **Peak / off-peak tiered billing (v1.0.1)** — Peak hours (Beijing time Monday–Friday 09:00–12:00 and 14:00–18:00, UTC 01:00–04:00 and 06:00–10:00) billed at 2× 
- **Official dual-currency list pricing (v1.0.1)** — Builtin official CNY and USD prices directly used according to the active display currency — **no FX conversi
- **Multi-currency display (v0.3 / v1.0.1)** — One-click toggle between USD and CNY (persisted in localStorage); indicator, panel, chart, and badges all follow.

## 📦 安装

```bash
dsh plugin --profile web add dsh-usage-chart   # installs and registers the profile plugin layer
dsh web --profile web                          # starts DSH Web (stop it first if already running)
```

## 🚀 快速开始

```bash
# Option ①: pin the target version explicitly
dsh plugin --profile web add dsh-usage-chart@1.1.2
# Option ②: remove, then re-add (back to latest)
dsh plugin --profile web remove dsh-usage-chart
dsh plugin --profile web add dsh-usage-chart
```

## 📚 更多信息

**dsh-usage-chart**

> A usage, cost, and account-balance dashboard for DeepSeek Harness Web.    [简体中文](./README_ZH.md) · [Report an issue](https://github.com/Max-Samson/dsh-usage-chart/issues) · [Changelog (EN)](./CHANGELOG.md) · [更新日志（中文）](./CHANGELOG_ZH.md) Interface preview: light English on the left and dark Simplified Chinese on the right. Both variants follow the DSH theme and in-app language setting. <table> <

**Install**

Prerequisites: **[DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) ≥ 0.1.0-rc.6** · **Node.js ≥ 20** · **[pnpm](https://pnpm.io/install) on PATH** (`dsh plugin` forwards installs to pnpm). > If you get `dsh: command not found` (or PowerShell `The term 'dsh' is not recognized…`), > you ran `npx @deepseek-ai/dsh` transiently — see FAQ item 1 (install globally, or prefix commands wi

**Option 2: install from GitHub (source build)**

dsh plugin --profile web add github:Max-Samson/dsh-usage-chart#<commit-sha> Git installs run the package `prepare` script (`node build.mjs`) to build from source. pnpm ≥ 10 blocks `prepare` scripts by default — allow this package in the profile's `pnpm-workspace.yaml`, then re-run: allowBuilds: dsh-usage-chart: true

**Verify the install**

1. The composed profile should contain the plugin row: ```sh dsh --profile web --dump-config | grep -A4 'id: dsh-usage-chart' ``` 2. Open DSH Web and enter any existing session: the "Usage" indicator (tokens / cost / model) appears below the composer, with the account balance on the right; click ▸ to open the dashboard.

## 🔗 链接

- [GitHub 仓库](https://github.com/Max-Samson/dsh-usage-chart)
- [完整 README](https://github.com/Max-Samson/dsh-usage-chart#readme)
- [返回dsh-usage-chart所在分类](../plugins.md)
