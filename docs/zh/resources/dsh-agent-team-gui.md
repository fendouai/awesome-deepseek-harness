---
title: "dsh-agent-team-gui"
description: "Persistent multi-model workflow teams for DeepSeek Harness — dynamic lead planning, bounded DAGs, per-agent model/tools, Run Center and Token insights."
keywords: "dsh-agent-team-gui, workflow, coding, multi-agent, deepseek harness, dsh"
---
# dsh-agent-team-gui

> ⭐ **159** · ✅ 活跃 · 工作流

| | | | |
|---|---|---|---|
| 类型 | 工作流 | 分类 | 工作流 |
| 星数 | ⭐ 159 | 状态 | ✅ 活跃 |
| 作者 | [toolclub](https://github.com/toolclub) | 更新时间 | — |

## 一句话介绍

> Persistent multi-model workflow teams for DeepSeek Harness — dynamic lead planning, bounded DAGs, per-agent model/tools, Run Center and Token insights.

## 详细介绍

[English](README.md) | [简体中文](README-zh.md) **Persistent, reusable multi-model Agent teams for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness).** Give each member its own model, role, fallback route, token limit, and tool policy. Select a saved team beside the normal composer; the lead model plans the work, runs a bounded dependency graph, and synthesizes the result.

## 📦 安装

```bash
dsh plugin --profile web add -w github:toolclub/dsh-agent-team-gui#v1.0.1
dsh --profile web
```

## 🚀 快速开始

```bash
allowBuilds:
  dsh-agent-team-gui: true
```

## 📚 更多信息

**Install**

Requirements: DeepSeek Harness `>=0.1.0-rc.5 <0.2.0`, the **Web** profile, Node.js `>=22.19.0 <23` or `>=24.0.0` (Node.js 23 is not supported), pnpm, and at least one configured DSH provider/model route. dsh plugin --profile web add -w github:toolclub/dsh-agent-team-gui#v1.0.1 dsh --profile web Git dependencies run this repository's `prepare` build. On pnpm 10 or later, the first command may ask y

**Run Center and Token usage**

Every execution is written before planning starts. The Run Center exposes foreground/background state, live phase, elapsed time, child IDs, complete outputs, bounded handoffs, stop, linked whole or member retry, export, filters, and retention-safe clear. If a DSH child settles with `stopReason: "error"` after delivering non-empty plain text, the member counts as **Completed** instead of losing a v

**Host configuration**

The Web bundle inserts one unique Host row; it relies on the Web profile's existing storage, Connection RPC, models, sessions, and browser module services. name: dsh-agent-team-gui config: defaultProvider: spawn defaultExecutionMode: serial defaultContextMode: spawn historyMaxRuns: 0 historyMaxAgeDays: 0 versionMaxPerSquad: 0 If you override the row in a profile patch, restate every needed field: 

**Uninstall**

dsh plugin --profile web remove dsh-agent-team-gui Removing the package does not automatically delete durable plugin tables in the configured DSH storage backend.

## 🔗 链接

- [GitHub 仓库](https://github.com/toolclub/dsh-agent-team-gui)
- [完整 README](https://github.com/toolclub/dsh-agent-team-gui#readme)
- [返回dsh-agent-team-gui所在分类](../workflows.md)
