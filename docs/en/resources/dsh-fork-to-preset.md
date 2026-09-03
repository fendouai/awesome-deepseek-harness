---
title: "dsh-fork-to-preset"
description: "Fork any session into a different agent preset from the conversation header: a preset-picker button that creates a new child session mounted on the chosen preset, inheriting the source session completed turns."
keywords: "dsh-fork-to-preset, ui, plugin, deepseek harness, dsh"
---
# dsh-fork-to-preset

> ⭐ **0** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 0 | Status | ✅ active |
| Author | [bpc-oss](https://github.com/bpc-oss) | Updated | 2026-08-21 |
| Subcategory | 🧭 Navigation | Capabilities | ui |

## One-liner

> Fork any session into a different agent preset from the conversation header: a preset-picker button that creates a new child session mounted on the chosen preset, inheriting the source session completed turns.

## About

A [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) plugin that adds a **"Fork to preset"** button to every conversation's header. Pick any agent preset from the roster and fork the current session into a fresh independent child session running under that preset — inheriting the parent's completed turns.

## ✨ Key Features

- Click the **↴ Fork to preset** dropdown in the conversation header
- Select a target agent preset from the roster
- Click the button → a new session opens, mounted on the chosen preset, with the parent's completed-turn history

## 🚀 Quick Start

```bash
:: Windows
mklink /J "<plugin-dir>\node_modules" "<harness>\resources\host\node_modules"
```

## 📚 Learn more

**1. Link the package into the harness install**

:: Windows mklink /J "<plugin-dir>\node_modules" "<harness>\resources\host\node_modules"

## 🔗 Links

- [GitHub Repository](https://github.com/bpc-oss/dsh-fork-to-preset)
- [Full README](https://github.com/bpc-oss/dsh-fork-to-preset#readme)
- [Back to the Plugins list](../plugins.md)
