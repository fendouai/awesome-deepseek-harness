---
title: "dsh-trajectory-debug"
description: "Trajectory waterfall, deterministic replay, breakpoints, edit-and-rerun, fork compare and performance analytics."
keywords: "dsh-trajectory-debug, workflow, observability, deepseek harness, dsh"
---
# dsh-trajectory-debug

> ⭐ **1** · ✅ active · workflow · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | workflow | Category | Workflows |
| Stars | ⭐ 1 | Status | ✅ active |
| Author | [devmom](https://github.com/devmom) | Updated | 2026-08-14 |

## One-liner

> Trajectory waterfall, deterministic replay, breakpoints, edit-and-rerun, fork compare and performance analytics.

## About

Turn DSH's **event-sourced sessions** into debuggable assets: a waterfall trajectory view, deterministic single-step replay (zero token cost), breakpoints, sandboxed edit-and-rerun, fork comparison, and performance analytics — plus OTel GenAI trace export and `trajectory_*` model tools for agents to introspect their own runs.

## 📦 Install

```bash
dsh plugin --profile web add dsh-trajectory-debug-bundle
dsh web --dump-config   # expect trajectory-debug-host / -remotes / ui-trajectory-debug rows
```

## 🚀 Quick Start

```bash
corepack pnpm check
node scripts\smoke.mjs
dsh plugin --profile web add ./packages/trajectory-debug-bundle
```

## 📚 Learn more

**Install into DSH**

Published on npm — install directly (no build required): dsh plugin --profile web add dsh-trajectory-debug-bundle dsh web --dump-config # expect trajectory-debug-host / -remotes / ui-trajectory-debug rows From a source checkout: corepack pnpm check node scripts\smoke.mjs dsh plugin --profile web add ./packages/trajectory-debug-bundle Restart `dsh web`: the **Debug** tab appears in the conversation

## 🔗 Links

- [GitHub Repository](https://github.com/devmom/dsh-trajectory-debug)
- [Full README](https://github.com/devmom/dsh-trajectory-debug#readme)
- [Back to the Workflows & Automation list](../workflows.md)
