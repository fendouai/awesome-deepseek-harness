---
title: "allinluna"
description: "面向 Codex 与 DeepSeek Harness 的资源感知多 Agent 编排。"
keywords: "allinluna, multi-agent, agent, workflow, deepseek harness, dsh"
---
# allinluna

> ⭐ **41** · ✅ 活跃 · 智能体 · 近期 ⬆️ +2

| | | | |
|---|---|---|---|
| 类型 | 智能体 | 分类 | 多智能体 |
| 星数 | ⭐ 41 | 状态 | ✅ 活跃 |
| 作者 | [zenx0x](https://github.com/zenx0x) | 更新时间 | 2026-08-14 |

## 一句话介绍

> 面向 Codex 与 DeepSeek Harness 的资源感知多 Agent 编排。

## 详细介绍

[简体中文](README.zh-CN.md) Give All in Luna one big goal. It turns the work into independent top-level tasks: **run what can run in parallel, wait only on real dependencies, keep each task's context separate, and bring the results back together.** Each task can still use its own subagents, tools, Skills, or MCPs. **Parallel across tasks. Recursive inside tasks.** ---

## ✨ 核心特性

- the context keeps growing;
- unrelated work starts contaminating other work;
- earlier constraints become easier to forget;
- one local blocker stalls the whole flow;
- subagent results become harder to manage;
- a new conversation has to reconstruct what really happened;

## 📦 安装

```bash
python -m pip install "allinluna==2.0.0rc7"

allinluna --db C:/absolute/path/runtime.db start --goal "Finish the authentication refactor" --repository-root C:/absolute/path/repository
allinluna --db C:/absolute/path/runtime.db status RUN_ID --invariants
allinluna --db C:/absolute/path/runtime.db drive RUN_ID
allinluna --db C:/absolute/path/runtime.db lane finalize RUN_ID TASK_ID
```

## 🚀 快速开始

```bash
allinluna --help
```

## 📚 更多信息

**Example**

Suppose you say: > **“Refactor this application's authentication system, including backend, frontend, migration, and tests.”** All in Luna can organize it as: Authentication refactor ├─ Task 1 — Auth backend │ ├─ session/token logic │ ├─ API │ └─ backend tests │ ├─ Task 2 — Frontend auth flow │ ├─ login │ ├─ logout │ └─ protected routes │ ├─ Task 3 — Migration │ └─ waits for auth contract │ └─ Tas

**You do not have to configure anything**

Most users do not need to choose a model policy first. If you do not specify one, All in Luna uses resources available through the current environment, host, or deployment policy. It does not require every user to use one fixed model or provider.

## 🔗 链接

- [GitHub 仓库](https://github.com/zenx0x/allinluna)
- [完整 README](https://github.com/zenx0x/allinluna#readme)
- [返回allinluna所在分类](../agents.md)
