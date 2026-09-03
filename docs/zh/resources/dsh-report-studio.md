---
title: "dsh-report-studio"
description: "把 DSH 会话变成可交付工作报告（日报/周报/交接/文章），带可验证凭证。"
keywords: "dsh-report-studio, workflow, research, deepseek harness, dsh"
---
# dsh-report-studio

> ⭐ **1** · ✅ 活跃 · 工作流 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 工作流 | 分类 | 工作流 |
| 星数 | ⭐ 1 | 状态 | ✅ 活跃 |
| 作者 | [ciceroyang](https://github.com/ciceroyang) | 更新时间 | 2026-08-17 |

## 一句话介绍

> 把 DSH 会话变成可交付工作报告（日报/周报/交接/文章），带可验证凭证。

## 详细介绍

**When your agent finishes work, have it write up what happened — into something you can actually hand over.** The first "session → work deliverable" plugin in the DeepSeek Harness ecosystem: turn one session into a **daily report / weekly report / handoff document / WeChat-article draft**, each sealed with a verifiable receipt block (report hash + artifact hashes), so reports cannot be embellished.

## ✨ 核心特性

- **4 ready templates**: `daily`, `weekly`, `handoff`, `article`
- **Deterministic session extraction**: user asks, todo snapshots, turn/step stats,
- **Verifiable receipt block**: session id, workspace, generation time, report
- **Safe persistence**: target paths are confined to the session workspace;
- **Customizable templates**: override built-in templates wholesale (placeholders below)
- **No build step**: plain ESM; install via `dsh plugin` or load with a `--patch` overlay

## 📚 更多信息

**Usage**

Tell the agent either of: The bundled `work-report` skill teaches the agent the full workflow: 1. `report_generate` produces a draft with hard data plus `[[待写:…]]` prose slots; 2. the agent fills the slots from session facts only; 3. `report_save` writes the file and appends the receipt; 4. the agent replies with the saved path and the report hash. Default save location: `reports/<kind>-<date>.md`

**Receipt example**

## 报告凭据 Report Receipt | 项 | 值 | |---|---| | 会话 Session | session-1c1e5d0c-… | | 工作区 Workspace | /Users/you/project | | 生成时间 Generated | 2026-08-14T08:00:00.000Z | | 报告哈希 Report SHA-256 | 9f2c… | | 产物 Artifacts | README.md → 3a1b… |

## 🔗 链接

- [GitHub 仓库](https://github.com/ciceroyang/dsh-report-studio)
- [完整 README](https://github.com/ciceroyang/dsh-report-studio#readme)
- [返回dsh-report-studio所在分类](../workflows.md)
