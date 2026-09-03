---
title: "dsh-output-styles"
description: "Claude Code outputStyles for DeepSeek Harness - session-scoped, durable, runtime-switchable model output styles (/style command, output_style storage domain, systemPrompt injection)"
keywords: "dsh-output-styles, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-output-styles

> ⭐ **4** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 4 | Status | ✅ active |
| Author | [PerryLink](https://github.com/PerryLink) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> Claude Code outputStyles for DeepSeek Harness - session-scoped, durable, runtime-switchable model output styles (/style command, output_style storage domain, systemPrompt injection)

## About

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-output-styles` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **Claude Code `outputStyles` for DeepSeek Harness** — switch the model's output style at runtime, per session, durably. *`/style concise` — and every reply from now on is terse. `/style off` — back to the project default.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ Key Features

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-output-styles` (counts toward the [deepseek1024.com](https://deepsee

## 📦 Install

```bash
# 1. install the bundle into your profile
dsh plugin --profile web add "github:PerryLink/dsh-output-styles#main"

# or from npm (published releases)
dsh plugin --profile web add dsh-output-styles

# 2. restart and verify the row
dsh --profile web --dump-config | grep -A3 'id: output-styles'
```

## 🚀 Quick Start

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

## 📚 Learn more

**Demo**

You > /style output style off concise — Terse, direct answers — minimal prose, no preamble. (Daily coding work, tool-heavy sessions, or when prompt length matters.) explanatory — Educational answers with short "Insights" that teach as you work. (Learning a codebase, onboarding, …) formal — Formal, precise prose with complete sentences and defined terms. (Reports, documentation, release notes, …) l

**Configuration**

All tunables are Schemastery `Config` fields (changeable from cordis.yml). Invalid values fail the load.

## 🔗 Links

- [GitHub Repository](https://github.com/PerryLink/dsh-output-styles)
- [Full README](https://github.com/PerryLink/dsh-output-styles#readme)
- [Back to the Plugins list](../plugins.md)
