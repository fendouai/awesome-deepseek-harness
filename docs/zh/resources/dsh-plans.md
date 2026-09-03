---
title: "dsh-plans"
description: "从 prime-plans 移植的人机协同规划预设：调研、评审、执行。"
keywords: "dsh-plans, workflow, multi-agent, deepseek harness, dsh"
---
# dsh-plans

> ⭐ **42** · ✅ 活跃 · 工作流 · 近期 ⬆️ +6

| | | | |
|---|---|---|---|
| 类型 | 工作流 | 分类 | 工作流 |
| 星数 | ⭐ 42 | 状态 | ✅ 活跃 |
| 作者 | [Optim-Agent](https://github.com/Optim-Agent) | 更新时间 | 2026-08-17 |

## 一句话介绍

> 从 prime-plans 移植的人机协同规划预设：调研、评审、执行。

## 详细介绍

Human-in-the-loop planning preset for the [DeepSeek Harness] (DSH): researched, refined Markdown plans before any code changes, then goal-driven execution after an explicit handoff. Turn a rough repository-change request into a traceable plan under `./dsh-plans/`, refine that plan with reviewer or criticizer subagent rounds, and hand the accepted plan to a persistent DSH goal that drives implementation until the plan's Verifier Checklist passes. Everything runs on DSH's native mechanisms — `ask_user_question`, subagents, the goal loop, and bundled skills — with no separate execution engine.

## ✨ 核心特性

- Per workspace, the language setting is asked once before the first planning question, and persisted.
- Per role, the model for reviewer / criticizer / executor is asked once, at that role's first actual use, and persisted. Reviewer and criticizer children run thr
- One planning question at a time; the final scope confirmation gates `PLAN_v1.md`.
- After every plan version, a refinement mode question — a reviewer or criticizer never runs without it.
- After refinement, an explicit execution handoff question with no auto-complete: execute the plan now as a DSH goal, or stop after planning.
- Execution runs as a DSH goal with `ponytail` simplification discipline and the MVP minimum-test set, so token cost stays proportional to the work.

## 📦 安装

```bash
mkdir -p ~/.dsh/.agent-presets
git clone https://github.com/Optim-Agent/dsh-plans.git ~/.dsh/.agent-presets/dsh-plans
```

## 🚀 快速开始

```bash
Create a plan for <your change>
```

## 📚 更多信息

**Install**

mkdir -p ~/.dsh/.agent-presets git clone https://github.com/Optim-Agent/dsh-plans.git ~/.dsh/.agent-presets/dsh-plans The roster re-scans its roots on every read, so the new preset appears in the preset picker immediately — select `dsh-plans` for a new session (no restart needed). Then from any directory ask: Create a plan for <your change> Update an existing install with `git -C ~/.dsh/.agent-pre

## 🔗 链接

- [GitHub 仓库](https://github.com/Optim-Agent/dsh-plans)
- [完整 README](https://github.com/Optim-Agent/dsh-plans#readme)
- [返回dsh-plans所在分类](../workflows.md)
