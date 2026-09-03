---
title: "dsh-task-dag"
description: "Persistent live DAG visualization of workflow runs, subagents, status and dependencies."
keywords: "dsh-task-dag, workflow, observability, multi-agent, deepseek harness, dsh"
---
# dsh-task-dag

> ⭐ **6** · ✅ active · workflow · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | workflow | Category | Workflows |
| Stars | ⭐ 6 | Status | ✅ active |
| Author | [LeemanCheung](https://github.com/LeemanCheung) | Updated | 2026-08-15 |

## One-liner

> Persistent live DAG visualization of workflow runs, subagents, status and dependencies.

## About

`dsh-task-dag` turns DSH's existing Client projections into three focused graph views. It keeps no parallel orchestration database and sends no polling requests: Session, Team, and Workflow state is rebuilt from the projections DSH already owns. Additional behavior: - **Agent communication:** directed channels aggregate message count and queued delivery state. Select a channel to inspect the latest 100 message records with quiet/wakeup and delivery metadata; only text blocks are previewed, while other block types are counted. - **Agent runtime metrics:** hover or keyboard-focus a teammate, subagent, or Workflow member to see the latest request Provider, model, concrete DSH effective reasoning-effort ID when one was durably recorded, its recorded source, and whole-Session cumulative input, 

## ✨ Key Features

- **Agent communication:** directed channels aggregate message count and queued delivery state. Select a channel to inspect the latest 100 message records with qu
- **Agent runtime metrics:** hover or keyboard-focus a teammate, subagent, or Workflow member to see the latest request Provider, model, concrete DSH effective re
- **Direct navigation:** selectable teammate, subagent, and Workflow member nodes open the real Session when it remains visible in the Session list.
- **Workflow definition preview:** select a Workflow run node to inspect the exact JavaScript orchestration body, definition summary, usage guidance, and declared
- **Canvas control:** fit the whole topology, pan the original-size canvas, or drag nodes while connected edges update.
- **Per-view layout:** manual positions survive view switches and reopening the panel for the current Session. Switching Sessions, refreshing the page, or restart

## 📦 Install

```bash
dsh plugin --profile web add github:LeemanCheung/dsh-task-dag
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add github:LeemanCheung/dsh-task-dag#v1.5.0
```

## 📚 Learn more

**Live screenshot**

Captured from a running DSH Web Session with labels anonymized. The panel, controls, layout, and graph presentation are the actual linked plugin UI. Select a Workflow run to open the v1.4.0 definition inspector beside the live topology:

**Install**

dsh plugin --profile web add github:LeemanCheung/dsh-task-dag Restart the current DSH Web process once after the first installation, then refresh the page. The **Task DAG** action appears in the Session header. For a version-pinned installation: dsh plugin --profile web add github:LeemanCheung/dsh-task-dag#v1.5.0

**Architecture**

The plugin combines six durable projections and Client-facing sources: A package-owned hidden Conversation Node Definition projects each supported Team v1 event into a small snapshot node. The graph model folds the latest task/member state, matches message delivery acknowledgements, aggregates directed communication channels, constructs explicit multi-parent edges, and applies a deterministic non-

## 🔗 Links

- [GitHub Repository](https://github.com/LeemanCheung/dsh-task-dag)
- [Full README](https://github.com/LeemanCheung/dsh-task-dag#readme)
- [Back to the Workflows & Automation list](../workflows.md)
