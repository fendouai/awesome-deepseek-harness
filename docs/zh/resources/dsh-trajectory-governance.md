---
title: "dsh-trajectory-governance"
description: "Agent trajectory governance & anomaly diagnosis plugin for DeepSeek Harness (dsh): multi-branch trajectory trees, loop-deadlock / invalid-retry / goal-drift detection, cost attribution, alerts, one-click interrupt & breakpoint fork, independent GUI tab. Zero kernel modification."
keywords: "dsh-trajectory-governance, ui, plugin, coding, multi-agent, deepseek harness, dsh"
---
# dsh-trajectory-governance

> ⭐ **4** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 4 | 状态 | ✅ 活跃 |
| 作者 | [dfycaly98931680](https://github.com/dfycaly98931680) | 更新时间 | — |
| 子分类 | 📊 状态与统计 | 能力 | coding, multi-agent, ui |

## 一句话介绍

> Agent trajectory governance & anomaly diagnosis plugin for DeepSeek Harness (dsh): multi-branch trajectory trees, loop-deadlock / invalid-retry / goal-drift detection, cost attribution, alerts, one-click interrupt & breakpoint fork, independent GUI tab. Zero kernel modification.

## 详细介绍

**Agent trajectory governance & anomaly diagnosis for DeepSeek Harness (dsh).** Rebuilds the flat `session/event` log into a **structured, multi-branch trajectory tree**, keeps **observation-layer snapshots**, and runs **three temporal anomaly strategies** (loop deadlock / invalid retry / goal drift) with results mounted on tree nodes and surfaced in an **independent GUI tab**. ---

## ✨ 核心特性

- which tool call belongs to which sub-task / subagent / fork branch,
- where the agent started drifting from the original goal,
- whether it is looping in place burning tokens (deadlock / invalid retry).

## 📦 安装

```bash
dsh plugin --profile web add github:dfycaly98931680/dsh-trajectory-governance#<commit-sha>
```

## 🚀 快速开始

```bash
allowBuilds:
  dsh-trajectory-governance: true
```

## 📚 更多信息

**Architecture**

dsh web profile ├─ @deepseek-ai/dsh-base (official core) └─ dsh-trajectory-governance (this bundle) │ │ ctx.on('session/event' | 'session/created' | 'session/disposed' │ | 'subagent/start' | 'subagent/end') ← emit-mode, post-commit, read-only ▼ ┌─ ingest ───────────────┐ ┌─ tree ─────────────────┐ │ normalize (scalars) │──▶│ cross-session trajectory │ │ sqlite (events/sessions)│ │ tree + branch at

**Install**

Requires dsh `>= 0.1.0-rc.6`. Two ways: **Bundle (published / git):** dsh plugin --profile web add github:dfycaly98931680/dsh-trajectory-governance#<commit-sha> A git install fetches sources, so the package ships a `prepare` build; pnpm requires an explicit allow-list for it (add the printed key to the profile's `pnpm-workspace.yaml`, then re-run): allowBuilds: dsh-trajectory-governance: true Alte

**Configuration**

The plugin row accepts `config` (all optional; deep-merged over defaults): - id: trajectory-governance name: dsh-trajectory-governance config: storage: path: C:/data/trajectory.db # default ~/.dsh-trajectory-governance/trajectory.db diagnosis: strategyA: enabled: true windowSize: 5 similarityThreshold: 0.85 resultSimilarityThreshold: 0.8 strategyB: enabled: true minRounds: 3 strategyC: enabled: tr

**Quick demo (reproduce loop deadlock & goal drift)**

**Instant (no waiting for a real loop):** seed a synthetic session into the live store, refresh the tab, pick `demo-session`: node scripts/demo-seed.mjs # writes into the default live DB You should see a tree with red-highlighted `loop_deadlock` (5 identical tool calls) and a severe `goal_drift` range, plus a snapshot mark (★). **Real agent:** 1. Give the agent a **long, open-ended refactor** prom

## 🔗 链接

- [GitHub 仓库](https://github.com/dfycaly98931680/dsh-trajectory-governance)
- [完整 README](https://github.com/dfycaly98931680/dsh-trajectory-governance#readme)
- [返回dsh-trajectory-governance所在分类](../plugins.md)
