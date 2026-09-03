---
title: "dsh-plannotator"
description: "DSH 计划批注插件：选中计划原文、逐条批注，并把结构化反馈送回 Agent。 / A DSH plan-review plugin for anchored annotations and structured Agent feedback."
keywords: "dsh-plannotator, workflow, coding, multi-agent, deepseek harness, dsh"
---
# dsh-plannotator

> ⭐ **10** · ✅ 活跃 · 工作流

| | | | |
|---|---|---|---|
| 类型 | 工作流 | 分类 | 工作流 |
| 星数 | ⭐ 10 | 状态 | ✅ 活跃 |
| 作者 | [titanwings](https://github.com/titanwings) | 更新时间 | — |

## 一句话介绍

> DSH 计划批注插件：选中计划原文、逐条批注，并把结构化反馈送回 Agent。 / A DSH plan-review plugin for anchored annotations and structured Agent feedback.

## 详细介绍

① The plan sounds plausible, but one sentence hides a migration risk? ② You found several independent problems, but the only choices are Approve or Reject? ③ You want every comment to stay attached to the exact text the agent must revise?

## 📦 安装

```bash
dsh plugin --profile web add github:titanwings/dsh-plannotator#v0.1.4
```

## 🚀 快速开始

```bash
pnpm install
pnpm check

cd /path/to/deepseek-harness
pnpm dsh plugin --profile web add /path/to/dsh-plannotator
```

## 📚 更多信息

**📦 Install**

Install the GitHub bundle into the DSH Web profile, then restart `dsh web`: dsh plugin --profile web add github:titanwings/dsh-plannotator#v0.1.4 The repository ships its built Host and Web bundles, so installation runs no package build script and needs no `allowBuilds` entry. Pin a reviewed commit SHA instead of the release tag when you need an exact source revision. <details> <summary>Install fr

## 🔗 链接

- [GitHub 仓库](https://github.com/titanwings/dsh-plannotator)
- [完整 README](https://github.com/titanwings/dsh-plannotator#readme)
- [返回dsh-plannotator所在分类](../workflows.md)
