---
title: "dsh-report-studio"
description: "Turn a DSH session into deliverable work reports (daily/weekly/handoff/article) with verifiable receipts."
keywords: "dsh-report-studio, workflow, research, deepseek harness, dsh"
---
# dsh-report-studio

> ⭐ **1** · ✅ active · workflow · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | workflow | Category | Workflows |
| Stars | ⭐ 1 | Status | ✅ active |
| Author | [ciceroyang](https://github.com/ciceroyang) | Updated | 2026-08-17 |

## One-liner

> Turn a DSH session into deliverable work reports (daily/weekly/handoff/article) with verifiable receipts.

## About

**When your agent finishes work, have it write up what happened — into something you can actually hand over.** The first "session → work deliverable" plugin in the DeepSeek Harness ecosystem: turn one session into a **daily report / weekly report / handoff document / WeChat-article draft**, each sealed with a verifiable receipt block (report hash + artifact hashes), so reports cannot be embellished.

## ✨ Key Features

- **4 ready templates**: `daily`, `weekly`, `handoff`, `article`
- **Deterministic session extraction**: user asks, todo snapshots, turn/step stats,
- **Verifiable receipt block**: session id, workspace, generation time, report
- **Safe persistence**: target paths are confined to the session workspace;
- **Customizable templates**: override built-in templates wholesale (placeholders below)
- **No build step**: plain ESM; install via `dsh plugin` or load with a `--patch` overlay

## 📚 Learn more

**Usage**

Tell the agent either of: The bundled `work-report` skill teaches the agent the full workflow: 1. `report_generate` produces a draft with hard data plus `[[待写:…]]` prose slots; 2. the agent fills the slots from session facts only; 3. `report_save` writes the file and appends the receipt; 4. the agent replies with the saved path and the report hash. Default save location: `reports/<kind>-<date>.md`

**Receipt example**

## 报告凭据 Report Receipt | 项 | 值 | |---|---| | 会话 Session | session-1c1e5d0c-… | | 工作区 Workspace | /Users/you/project | | 生成时间 Generated | 2026-08-14T08:00:00.000Z | | 报告哈希 Report SHA-256 | 9f2c… | | 产物 Artifacts | README.md → 3a1b… |

## 🔗 Links

- [GitHub Repository](https://github.com/ciceroyang/dsh-report-studio)
- [Full README](https://github.com/ciceroyang/dsh-report-studio#readme)
- [Back to the Workflows & Automation list](../workflows.md)
