---
title: "dsh-polyglot"
description: "dsh-polyglot — the model switch for DSH: generic OpenAI-compatible ctx.llm adapter, curated free/cheap DeepSeek presets, automatic provider fallback on rate limits"
keywords: "dsh-polyglot, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-polyglot

> ⭐ **4** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 4 | 状态 | ✅ 活跃 |
| 作者 | [Jesse-njx](https://github.com/Jesse-njx) | 更新时间 | — |
| 子分类 | 👁️ 视觉工具 | 能力 | coding |

## 一句话介绍

> dsh-polyglot — the model switch for DSH: generic OpenAI-compatible ctx.llm adapter, curated free/cheap DeepSeek presets, automatic provider fallback on rate limits

## 详细介绍

**The model switch for DSH.** Point DeepSeek Harness at any OpenAI-compatible endpoint — with curated presets for free and cheap DeepSeek providers and automatic fallback when a free tier rate-limits you. What claude-code-router is to Claude Code, dsh-polyglot is to DSH — except DSH's `ctx.llm` is a sanctioned extension seam, so there is no request interception: the generic adapter and the router are both real `LlmAdapter` registrations. - **One generic adapter.** A single OpenAI-compatible `ctx.llm` adapter parameterized by `{baseUrl, apiKey, model, headers?, quirks?}`. Streaming, tool calls, and usage extraction are all handled; per-provider deviations (reasoning field names, strict tool schemas, cache-folded usage) are small declarative `quirks` flags, never per-provider code. - **A rou

## ✨ 核心特性

- **One generic adapter.** A single OpenAI-compatible `ctx.llm` adapter
- **A router with fallback.** On 429 / quota-exceeded / 5xx (or a missing
- **Provider presets as data.** `presets/*.json` — community PRs add providers
- **Usage you can see.** Every attempt lands in the append-only session log as

## 📦 安装

```bash
dsh plugin --profile web add @dsh-polyglot/bundle
```

## 🚀 快速开始

```bash
nous-portal → opencode-zen → deepseek-official (5M grant) → kilo
```

## 📚 更多信息

**Quick start**

Install the bundle into a profile (a DSH profile is an ordered stack of plugin-bundle patch layers): dsh plugin --profile web add @dsh-polyglot/bundle The bundle's patch registers the `polyglot` plugin with the recommended default chain — *"code all day for free until something rate-limits, then degrade gracefully to cheapest-paid"*: nous-portal → opencode-zen → deepseek-official (5M grant) → kilo

**Roadmap**

free Flash); OAuth device flow for Nous Portal; preset auto-update check; provider benchmark/arena integration.

## 🔗 链接

- [GitHub 仓库](https://github.com/Jesse-njx/dsh-polyglot)
- [完整 README](https://github.com/Jesse-njx/dsh-polyglot#readme)
- [返回dsh-polyglot所在分类](../plugins.md)
