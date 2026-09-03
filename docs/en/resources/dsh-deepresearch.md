---
title: "dsh-deepresearch"
description: "DeepResearch plugin (cordis) for the Harness."
keywords: "dsh-deepresearch, research, workflow, search, deepseek harness, dsh"
---
# dsh-deepresearch

> ⭐ **9** · 🧪 experimental · workflow · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | workflow | Category | Research |
| Stars | ⭐ 9 | Status | 🧪 experimental |
| Author | [havingautism](https://github.com/havingautism) | Updated | 2026-08-19 |

## One-liner

> DeepResearch plugin (cordis) for the Harness.

## About

[English](README.en.md) | 中文 `@deepseek-ai/dsh-deepresearch` 把证据优先的 Codemini 研究工作区带到 DSH。它提供持久工作流状态、模型工具、生成的 `deepResearch` Remote namespace 和“深度研究”Web 工作区，同时组合宿主已有的 Web 与 subagent 能力。

## ✨ Key Features

- 🧭 记录研究问题、目标、约束、种子材料和研究深度。
- 🧩 确认前编辑子问题、依赖关系和明确的成功标准。
- ✅ 未确认计划时拒绝写入证据。
- 🔎 为每个子问题关联论点、摘录、URL、置信度和已覆盖标准。
- 📊 跟踪问题覆盖度、搜索与抓取预算、局限和部分完成状态。
- 📝 保存结论，以及完整或明确标记为未完成的最终报告。
- 🗂️ 在 Web 资料库中搜索、筛选、排序、恢复、中止或删除项目。
- 🤖 创建项目后由私有规划 Agent 只提交计划；确认后再按子问题并行派出 Scout / Evaluator，最后用写作包撰写报告。普通聊天不挂研究工具，也不开通用 fetch。项目持久化在与随手记共用的 SQLite（默认 `~/.dsh/storages/dsh.sqlite`，domain `deepresea

## 📦 Install

```bash
dsh plugin --profile web add github:havingautism/dsh-deepresearch
dsh web
```

## 🔗 Links

- [GitHub Repository](https://github.com/havingautism/dsh-deepresearch)
- [Full README](https://github.com/havingautism/dsh-deepresearch#readme)
- [Back to the Workflows & Automation list](../workflows.md)
