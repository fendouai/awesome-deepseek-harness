---
title: "dsh-trajectory-debug"
description: "轨迹瀑布流、确定性回放、断点、编辑重跑、fork 对比与性能分析。"
keywords: "dsh-trajectory-debug, workflow, observability, deepseek harness, dsh"
---
# dsh-trajectory-debug

> ⭐ **1** · ✅ 活跃 · 工作流 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 工作流 | 分类 | 工作流 |
| 星数 | ⭐ 1 | 状态 | ✅ 活跃 |
| 作者 | [devmom](https://github.com/devmom) | 更新时间 | 2026-08-14 |

## 一句话介绍

> 轨迹瀑布流、确定性回放、断点、编辑重跑、fork 对比与性能分析。

## 详细介绍

Turn DSH's **event-sourced sessions** into debuggable assets: a waterfall trajectory view, deterministic single-step replay (zero token cost), breakpoints, sandboxed edit-and-rerun, fork comparison, and performance analytics — plus OTel GenAI trace export and `trajectory_*` model tools for agents to introspect their own runs.

## 📦 安装

```bash
dsh plugin --profile web add dsh-trajectory-debug-bundle
dsh web --dump-config   # expect trajectory-debug-host / -remotes / ui-trajectory-debug rows
```

## 🚀 快速开始

```bash
corepack pnpm check
node scripts\smoke.mjs
dsh plugin --profile web add ./packages/trajectory-debug-bundle
```

## 📚 更多信息

**Install into DSH**

Published on npm — install directly (no build required): dsh plugin --profile web add dsh-trajectory-debug-bundle dsh web --dump-config # expect trajectory-debug-host / -remotes / ui-trajectory-debug rows From a source checkout: corepack pnpm check node scripts\smoke.mjs dsh plugin --profile web add ./packages/trajectory-debug-bundle Restart `dsh web`: the **Debug** tab appears in the conversation

## 🔗 链接

- [GitHub 仓库](https://github.com/devmom/dsh-trajectory-debug)
- [完整 README](https://github.com/devmom/dsh-trajectory-debug#readme)
- [返回dsh-trajectory-debug所在分类](../workflows.md)
