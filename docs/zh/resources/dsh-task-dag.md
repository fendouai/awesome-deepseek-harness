---
title: "dsh-task-dag"
description: "工作流运行、子代理、状态与依赖的持久化实时 DAG 可视化。"
keywords: "dsh-task-dag, workflow, observability, multi-agent, deepseek harness, dsh"
---
# dsh-task-dag

> ⭐ **6** · ✅ 活跃 · 工作流 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 工作流 | 分类 | 工作流 |
| 星数 | ⭐ 6 | 状态 | ✅ 活跃 |
| 作者 | [LeemanCheung](https://github.com/LeemanCheung) | 更新时间 | 2026-08-15 |

## 一句话介绍

> 工作流运行、子代理、状态与依赖的持久化实时 DAG 可视化。

## 详细介绍

`dsh-task-dag` turns DSH's existing Client projections into three focused graph views. It keeps no parallel orchestration database and sends no polling requests: Session, Team, and Workflow state is rebuilt from the projections DSH already owns. Additional behavior: - **Agent communication:** directed channels aggregate message count and queued delivery state. Select a channel to inspect the latest 100 message records with quiet/wakeup and delivery metadata; only text blocks are previewed, while other block types are counted. - **Agent runtime metrics:** hover or keyboard-focus a teammate, subagent, or Workflow member to see the latest request Provider, model, concrete DSH effective reasoning-effort ID when one was durably recorded, its recorded source, and whole-Session cumulative input, 

## ✨ 核心特性

- **Agent communication:** directed channels aggregate message count and queued delivery state. Select a channel to inspect the latest 100 message records with qu
- **Agent runtime metrics:** hover or keyboard-focus a teammate, subagent, or Workflow member to see the latest request Provider, model, concrete DSH effective re
- **Direct navigation:** selectable teammate, subagent, and Workflow member nodes open the real Session when it remains visible in the Session list.
- **Workflow definition preview:** select a Workflow run node to inspect the exact JavaScript orchestration body, definition summary, usage guidance, and declared
- **Canvas control:** fit the whole topology, pan the original-size canvas, or drag nodes while connected edges update.
- **Per-view layout:** manual positions survive view switches and reopening the panel for the current Session. Switching Sessions, refreshing the page, or restart

## 📦 安装

```bash
dsh plugin --profile web add github:LeemanCheung/dsh-task-dag
```

## 🚀 快速开始

```bash
dsh plugin --profile web add github:LeemanCheung/dsh-task-dag#v1.5.0
```

## 📚 更多信息

**Live screenshot**

Captured from a running DSH Web Session with labels anonymized. The panel, controls, layout, and graph presentation are the actual linked plugin UI. Select a Workflow run to open the v1.4.0 definition inspector beside the live topology:

**Install**

dsh plugin --profile web add github:LeemanCheung/dsh-task-dag Restart the current DSH Web process once after the first installation, then refresh the page. The **Task DAG** action appears in the Session header. For a version-pinned installation: dsh plugin --profile web add github:LeemanCheung/dsh-task-dag#v1.5.0

**Architecture**

The plugin combines six durable projections and Client-facing sources: A package-owned hidden Conversation Node Definition projects each supported Team v1 event into a small snapshot node. The graph model folds the latest task/member state, matches message delivery acknowledgements, aggregates directed communication channels, constructs explicit multi-parent edges, and applies a deterministic non-

## 🔗 链接

- [GitHub 仓库](https://github.com/LeemanCheung/dsh-task-dag)
- [完整 README](https://github.com/LeemanCheung/dsh-task-dag#readme)
- [返回dsh-task-dag所在分类](../workflows.md)
