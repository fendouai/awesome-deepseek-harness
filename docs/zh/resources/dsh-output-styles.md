---
title: "dsh-output-styles"
description: "Claude Code outputStyles for DeepSeek Harness - session-scoped, durable, runtime-switchable model output styles (/style command, output_style storage domain, systemPrompt injection)"
keywords: "dsh-output-styles, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-output-styles

> ⭐ **4** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 4 | 状态 | ✅ 活跃 |
| 作者 | [PerryLink](https://github.com/PerryLink) | 更新时间 | — |
| 子分类 | 👁️ 视觉工具 | 能力 | coding |

## 一句话介绍

> Claude Code outputStyles for DeepSeek Harness - session-scoped, durable, runtime-switchable model output styles (/style command, output_style storage domain, systemPrompt injection)

## 详细介绍

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-output-styles` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **Claude Code `outputStyles` for DeepSeek Harness** — switch the model's output style at runtime, per session, durably. *`/style concise` — and every reply from now on is terse. `/style off` — back to the project default.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ 核心特性

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-output-styles` (counts toward the [deepseek1024.com](https://deepsee

## 📦 安装

```bash
# 1. install the bundle into your profile
dsh plugin --profile web add "github:PerryLink/dsh-output-styles#main"

# or from npm (published releases)
dsh plugin --profile web add dsh-output-styles

# 2. restart and verify the row
dsh --profile web --dump-config | grep -A3 'id: output-styles'
```

## 🚀 快速开始

```bash
flowchart LR
    U[You type /style concise] --> C[command registry]
    C -->|command/run logged| L[(session log)]
    C -->|put {style, source}| D[(output_style domain)]
    D --> R[OutputStyleRuntime]
    R -->|body at every assembly| S[systemPrompt section order 90]
    S --> M[Model request]
    M -->|full system prompt| H[request/header logged]
```

## 📚 更多信息

**Demo**

You > /style output style off concise — Terse, direct answers — minimal prose, no preamble. (Daily coding work, tool-heavy sessions, or when prompt length matters.) explanatory — Educational answers with short "Insights" that teach as you work. (Learning a codebase, onboarding, …) formal — Formal, precise prose with complete sentences and defined terms. (Reports, documentation, release notes, …) l

**Configuration**

All tunables are Schemastery `Config` fields (changeable from cordis.yml). Invalid values fail the load.

## 🔗 链接

- [GitHub 仓库](https://github.com/PerryLink/dsh-output-styles)
- [完整 README](https://github.com/PerryLink/dsh-output-styles#readme)
- [返回dsh-output-styles所在分类](../plugins.md)
