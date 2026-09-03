---
title: "dsh-trajectory-governance"
description: "Agent trajectory governance & anomaly diagnosis plugin for DeepSeek Harness (dsh): multi-branch trajectory trees, loop-deadlock / invalid-retry / goal-drift detection, cost attribution, alerts, one-click interrupt & breakpoint fork, independent GUI tab. Zero kernel modification."
keywords: "dsh-trajectory-governance, ui, plugin, coding, multi-agent, deepseek harness, dsh"
---
# dsh-trajectory-governance

> ⭐ **4** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 4 | Status | ✅ active |
| Author | [dfycaly98931680](https://github.com/dfycaly98931680) | Updated | — |
| Subcategory | 📊 Status & stats | Capabilities | coding, multi-agent, ui |

## One-liner

> Agent trajectory governance & anomaly diagnosis plugin for DeepSeek Harness (dsh): multi-branch trajectory trees, loop-deadlock / invalid-retry / goal-drift detection, cost attribution, alerts, one-click interrupt & breakpoint fork, independent GUI tab. Zero kernel modification.

## About

**Agent trajectory governance & anomaly diagnosis for DeepSeek Harness (dsh).** Rebuilds the flat `session/event` log into a **structured, multi-branch trajectory tree**, keeps **observation-layer snapshots**, and runs **three temporal anomaly strategies** (loop deadlock / invalid retry / goal drift) with results mounted on tree nodes and surfaced in an **independent GUI tab**. ---

## ✨ Key Features

- which tool call belongs to which sub-task / subagent / fork branch,
- where the agent started drifting from the original goal,
- whether it is looping in place burning tokens (deadlock / invalid retry).

## 📦 Install

```bash
dsh plugin --profile web add github:dfycaly98931680/dsh-trajectory-governance#<commit-sha>
```

## 🚀 Quick Start

```bash
allowBuilds:
  dsh-trajectory-governance: true
```

## 📚 Learn more

**Architecture**

dsh web profile ├─ @deepseek-ai/dsh-base (official core) └─ dsh-trajectory-governance (this bundle) │ │ ctx.on('session/event' | 'session/created' | 'session/disposed' │ | 'subagent/start' | 'subagent/end') ← emit-mode, post-commit, read-only ▼ ┌─ ingest ───────────────┐ ┌─ tree ─────────────────┐ │ normalize (scalars) │──▶│ cross-session trajectory │ │ sqlite (events/sessions)│ │ tree + branch at

**Install**

Requires dsh `>= 0.1.0-rc.6`. Two ways: **Bundle (published / git):** dsh plugin --profile web add github:dfycaly98931680/dsh-trajectory-governance#<commit-sha> A git install fetches sources, so the package ships a `prepare` build; pnpm requires an explicit allow-list for it (add the printed key to the profile's `pnpm-workspace.yaml`, then re-run): allowBuilds: dsh-trajectory-governance: true Alte

**Configuration**

The plugin row accepts `config` (all optional; deep-merged over defaults): - id: trajectory-governance name: dsh-trajectory-governance config: storage: path: C:/data/trajectory.db # default ~/.dsh-trajectory-governance/trajectory.db diagnosis: strategyA: enabled: true windowSize: 5 similarityThreshold: 0.85 resultSimilarityThreshold: 0.8 strategyB: enabled: true minRounds: 3 strategyC: enabled: tr

**Quick demo (reproduce loop deadlock & goal drift)**

**Instant (no waiting for a real loop):** seed a synthetic session into the live store, refresh the tab, pick `demo-session`: node scripts/demo-seed.mjs # writes into the default live DB You should see a tree with red-highlighted `loop_deadlock` (5 identical tool calls) and a severe `goal_drift` range, plus a snapshot mark (★). **Real agent:** 1. Give the agent a **long, open-ended refactor** prom

## 🔗 Links

- [GitHub Repository](https://github.com/dfycaly98931680/dsh-trajectory-governance)
- [Full README](https://github.com/dfycaly98931680/dsh-trajectory-governance#readme)
- [Back to the Plugins list](../plugins.md)
