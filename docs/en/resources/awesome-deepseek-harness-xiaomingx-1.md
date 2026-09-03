---
title: "awesome-deepseek-harness"
description: "Curated DeepSeek Harness (DSH) ecosystem catalog — plugins, tools & infrastructure. Filtered, multilingual (ZH/EN/KO/JA), with design patterns worth borrowing."
keywords: "awesome-deepseek-harness, registry, awesome-list, search, deepseek harness, dsh"
---
# awesome-deepseek-harness

> ⭐ **3** · ✅ active · awesome-list

| | | | |
|---|---|---|---|
| Type | awesome-list | Category | Registries |
| Stars | ⭐ 3 | Status | ✅ active |
| Author | [XiaomingX](https://github.com/XiaomingX) | Updated | 2026-08-20 |

## One-liner

> Curated DeepSeek Harness (DSH) ecosystem catalog — plugins, tools & infrastructure. Filtered, multilingual (ZH/EN/KO/JA), with design patterns worth borrowing.

## About

官方运行时（Node.js）： npx @deepseek-ai/dsh web 外部 profile bundle 安装（pnpm）： dsh plugin --profile web add "github:owner/repo#ref" `dsh plugin` 实际转发给 pnpm，支持 npm、Git/GitHub、本地路径、`file:` 与 `link:` 规格。仅声明 `dsh.bundle.patch` 的包会成为激活层。管理面板：设置 → 插件。

## ✨ Key Features

- **[dsh-deepresearch](https://github.com/dsh-external/dsh-deepresearch)** — DeepResearch 插件（cordis 架构）。
- **[dsh-plan-execute](https://github.com/dsh-external/dsh-plan-execute)** — 双模型规划/执行路由：规划模型思考，执行模型行动。
- **[dsh-toolkit](https://github.com/dsh-external/dsh-toolkit)** — 零依赖工具集（计算器/CSV/Diff/编码/JSON/Markdown/正则/时间）。
- **[dsh-101](https://github.com/dsh-external/dsh-101)** — DSH 文档阅读模式。
- **[dsh-equip-engine](https://github.com/wuykjl/dsh-equip-engine)** — 任务驱动的插件装备引擎：双路检索、组合打分、冲突检测。
- **[dsh-claude-move](https://github.com/PerryLink/dsh-claude-move)** — 迁移向导：把 Claude Code、Codex、OpenCode、Hermes 会话迁入 DSH。
- **[dsh_workflow](https://github.com/omdsh-dev/dsh_workflow)** — UltraCode 式 Workflow 层：把一次性多 Agent 调度升级为可生成/保存/治理/观察/恢复的工作流。

## 📦 Install

```bash
npx @deepseek-ai/dsh web
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add "github:owner/repo#ref"
```

## 📚 Learn more

**安装**

官方运行时（Node.js）： npx @deepseek-ai/dsh web 外部 profile bundle 安装（pnpm）： dsh plugin --profile web add "github:owner/repo#ref" `dsh plugin` 实际转发给 pnpm，支持 npm、Git/GitHub、本地路径、`file:` 与 `link:` 规格。仅声明 `dsh.bundle.patch` 的包会成为激活层。管理面板：设置 → 插件。

**可借鉴的设计思路**

在分析上述项目后，以下模式值得在自己的 harness/agent 项目中借鉴： 1. **双模型规划/执行（Plan-Execute）** — `dsh-plan-execute` 与 `dsh-plans` 把"思考"与"行动"拆分到不同模型，兼顾推理质量与执行成本。 2. **上下文压缩与透镜** — `dsh-compressor`、`dsh-scope`、`dsh-context-doctor` 揭示了"把上下文占用可视化 + 按需压缩"是长会话的核心难题。 3. **记忆的分层与审批** — `dsh-memento`、`dsh-memory-gate` 用有界/分层/需审批的设计，避免无限制记忆污染上下文。 4. **成本治理** — `dsh-budget`、`dsh-web-billing`、`dsh-change-budget` 提供了从 token 计量到每轮预算的控

## 🔗 Links

- [GitHub Repository](https://github.com/XiaomingX/awesome-deepseek-harness)
- [Full README](https://github.com/XiaomingX/awesome-deepseek-harness#readme)
- [Back to the Awesome Lists & Registries list](../awesome-lists.md)
