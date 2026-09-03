---
title: "dsh-plannotator"
description: "DSH 计划批注插件：选中计划原文、逐条批注，并把结构化反馈送回 Agent。 / A DSH plan-review plugin for anchored annotations and structured Agent feedback."
keywords: "dsh-plannotator, workflow, coding, multi-agent, deepseek harness, dsh"
---
# dsh-plannotator

> ⭐ **10** · ✅ active · workflow

| | | | |
|---|---|---|---|
| Type | workflow | Category | Workflows |
| Stars | ⭐ 10 | Status | ✅ active |
| Author | [titanwings](https://github.com/titanwings) | Updated | — |

## One-liner

> DSH 计划批注插件：选中计划原文、逐条批注，并把结构化反馈送回 Agent。 / A DSH plan-review plugin for anchored annotations and structured Agent feedback.

## About

① The plan sounds plausible, but one sentence hides a migration risk? ② You found several independent problems, but the only choices are Approve or Reject? ③ You want every comment to stay attached to the exact text the agent must revise?

## 📦 Install

```bash
dsh plugin --profile web add github:titanwings/dsh-plannotator#v0.1.4
```

## 🚀 Quick Start

```bash
pnpm install
pnpm check

cd /path/to/deepseek-harness
pnpm dsh plugin --profile web add /path/to/dsh-plannotator
```

## 📚 Learn more

**📦 Install**

Install the GitHub bundle into the DSH Web profile, then restart `dsh web`: dsh plugin --profile web add github:titanwings/dsh-plannotator#v0.1.4 The repository ships its built Host and Web bundles, so installation runs no package build script and needs no `allowBuilds` entry. Pin a reviewed commit SHA instead of the release tag when you need an exact source revision. <details> <summary>Install fr

## 🔗 Links

- [GitHub Repository](https://github.com/titanwings/dsh-plannotator)
- [Full README](https://github.com/titanwings/dsh-plannotator#readme)
- [Back to the Workflows & Automation list](../workflows.md)
