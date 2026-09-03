---
title: "dsh-cost-meter"
description: "Provider-aware LLM cost meter and local ledger for DeepSeek Harness"
keywords: "dsh-cost-meter, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-cost-meter

> ⭐ **3** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 3 | Status | ✅ active |
| Author | [uruana33](https://github.com/uruana33) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> Provider-aware LLM cost meter and local ledger for DeepSeek Harness

## About

Out-of-tree [dsh](https://github.com/deepseek-ai/deepseek-harness) plugin that shows a live **USD cost badge** for the open conversation in the Web UI. It is a dual-face `dsh.client` package: - **Host half** (`lib/index.js`) registers a `sessionCost` projection on the session-projection seam. The fold tracks the current provider/model from `request/header` events and accumulates cost from the provider-reported usage buckets (uncached input / output / cache-read / cache-write), reusing token-meter's "replace the same `(turn, step)` sample instead of double-counting" rule. The view exposes the whole-session totals plus a `byTurn` map keyed by turn number. - **Client half** (`lib/client.js`) registers a badge into the `conversation.chat.assistant-actions` slot — the action row at the end of e

## ✨ Key Features

- **Host half** (`lib/index.js`) registers a `sessionCost` projection on the
- **Client half** (`lib/client.js`) registers a badge into the

## 📦 Install

```bash
dsh plugin --profile web add @steven-wu/dsh-cost-meter
# restart the web profile, then refresh the page
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add file:/path/to/dsh-cost-meter
```

## 📚 Learn more

**Install**

The package declares a `dsh.bundle` manifest, so `dsh plugin add` installs it **and** adds it to the profile's bundle layers automatically — no manual patch edit: dsh plugin --profile web add @steven-wu/dsh-cost-meter

## 🔗 Links

- [GitHub Repository](https://github.com/uruana33/dsh-cost-meter)
- [Full README](https://github.com/uruana33/dsh-cost-meter#readme)
- [Back to the Plugins list](../plugins.md)
