---
title: "dsh-noema"
description: "Noema long-term memory plugin for DSH: durable, inspectable agent memory with recall tools and a settings page."
keywords: "dsh-noema, memory, plugin, coding, multi-agent, deepseek harness, dsh"
---
# dsh-noema

> ⭐ **128** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Memory & context |
| Stars | ⭐ 128 | Status | ✅ active |
| Author | [ZSeven-W](https://github.com/ZSeven-W) | Updated | — |
| Subcategory | 🧠 Memory systems | Capabilities | coding, memory, multi-agent |

## One-liner

> Noema long-term memory plugin for DSH: durable, inspectable agent memory with recall tools and a settings page.

## About

DSH Noema connects [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) with [Noema](https://github.com/ZSeven-W/noema) — a local-first, non-vector memory system for coding agents — so an Agent keeps durable knowledge across sessions instead of starting every conversation from zero.

## 📦 Install

```bash
dsh plugin --profile web add @zseven-w/dsh-noema@latest
dsh web
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add link:/path/to/dsh-noema
dsh web
```

## 📚 Learn more

**🛠️ Settings-Page Management**

The Noema Memory settings page configures the server command, memory root, budgets, idle/call timeouts, and the guidance section — and a Manage memories card searches, browses, adds, reviews, and deletes stored memories directly. </td> <td width="50%">

**Install into DSH**

dsh plugin --profile web add @zseven-w/dsh-noema@latest dsh web Or, for local development straight from the source tree: dsh plugin --profile web add link:/path/to/dsh-noema dsh web The `link:` protocol symlinks the profile dependency to this repository, so rebuilds are visible immediately and Cordis HMR can watch the compiled output. The plugin bundles the `noema-mcp` binary through per-platform 

**Settings**

Open **Settings → Noema Memory**: The status card shows server health with restart/stop actions, and the import section manages the nine memory sources.

## 🔗 Links

- [GitHub Repository](https://github.com/ZSeven-W/dsh-noema)
- [Full README](https://github.com/ZSeven-W/dsh-noema#readme)
- [Back to the Plugins list](../plugins.md)
