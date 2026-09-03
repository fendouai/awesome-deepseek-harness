---
title: "dsh-polyglot"
description: "dsh-polyglot — the model switch for DSH: generic OpenAI-compatible ctx.llm adapter, curated free/cheap DeepSeek presets, automatic provider fallback on rate limits"
keywords: "dsh-polyglot, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-polyglot

> ⭐ **4** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 4 | Status | ✅ active |
| Author | [Jesse-njx](https://github.com/Jesse-njx) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> dsh-polyglot — the model switch for DSH: generic OpenAI-compatible ctx.llm adapter, curated free/cheap DeepSeek presets, automatic provider fallback on rate limits

## About

**The model switch for DSH.** Point DeepSeek Harness at any OpenAI-compatible endpoint — with curated presets for free and cheap DeepSeek providers and automatic fallback when a free tier rate-limits you. What claude-code-router is to Claude Code, dsh-polyglot is to DSH — except DSH's `ctx.llm` is a sanctioned extension seam, so there is no request interception: the generic adapter and the router are both real `LlmAdapter` registrations. - **One generic adapter.** A single OpenAI-compatible `ctx.llm` adapter parameterized by `{baseUrl, apiKey, model, headers?, quirks?}`. Streaming, tool calls, and usage extraction are all handled; per-provider deviations (reasoning field names, strict tool schemas, cache-folded usage) are small declarative `quirks` flags, never per-provider code. - **A rou

## ✨ Key Features

- **One generic adapter.** A single OpenAI-compatible `ctx.llm` adapter
- **A router with fallback.** On 429 / quota-exceeded / 5xx (or a missing
- **Provider presets as data.** `presets/*.json` — community PRs add providers
- **Usage you can see.** Every attempt lands in the append-only session log as

## 📦 Install

```bash
dsh plugin --profile web add @dsh-polyglot/bundle
```

## 🚀 Quick Start

```bash
nous-portal → opencode-zen → deepseek-official (5M grant) → kilo
```

## 📚 Learn more

**Quick start**

Install the bundle into a profile (a DSH profile is an ordered stack of plugin-bundle patch layers): dsh plugin --profile web add @dsh-polyglot/bundle The bundle's patch registers the `polyglot` plugin with the recommended default chain — *"code all day for free until something rate-limits, then degrade gracefully to cheapest-paid"*: nous-portal → opencode-zen → deepseek-official (5M grant) → kilo

**Roadmap**

free Flash); OAuth device flow for Nous Portal; preset auto-update check; provider benchmark/arena integration.

## 🔗 Links

- [GitHub Repository](https://github.com/Jesse-njx/dsh-polyglot)
- [Full README](https://github.com/Jesse-njx/dsh-polyglot#readme)
- [Back to the Plugins list](../plugins.md)
