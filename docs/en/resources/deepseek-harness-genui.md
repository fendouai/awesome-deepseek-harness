---
title: "deepseek-harness-genui"
description: "Task-specific React apps for DeepSeek Harness with state carried into the next Agent turn"
keywords: "deepseek-harness-genui, ui, plugin, deepseek harness, dsh"
---
# deepseek-harness-genui

> ⭐ **107** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 107 | Status | ✅ active |
| Author | [pengyue-polaron](https://github.com/pengyue-polaron) | Updated | — |
| Subcategory | 💡 Generative UI | Capabilities | ui |

## One-liner

> Task-specific React apps for DeepSeek Harness with state carried into the next Agent turn

## About

DeepSeek Harness GenUI lets an Agent build a focused interface when a task is awkward in text. The Coding Agent writes ordinary React + TypeScript—not a component-tree DSL—and the interface can save user selections for the next Agent turn. The result is a task-specific app that can explain a difficult relationship, collect connected choices, or continue a tool-backed workflow without asking the user to repeat their input. Related research: [*EvoGenUI-Bench: Evaluating LLMs as Multi-Turn Generative UI Assistants*](https://arxiv.org/abs/2608.29387).

## 📦 Install

```bash
dsh plugin --profile web add dsh-plugin-genui
dsh --profile web
```

## 🚀 Quick Start

```bash
Plan a Saturday route with a museum, a riverside garden, and dinner. Build an
interface where I can change the times and make the garden optional.
```

## 📚 Learn more

**Install**

Requires Node.js `^22.19.0 || ^24.0.0` and DeepSeek Harness Web. Supports Inline, Canvas, fullscreen, and localhost surfaces within Web; TUI/headless profiles are unsupported. Uses esbuild-wasm since v0.14.1: no `--allow-build=esbuild` flag and no Chrome/Chromium/Playwright installation are needed. See the [v0.14.2 release notes](https://github.com/pengyue-polaron/deepseek-harness-genui/releases/tag/v0.14.2).

## 🔗 Links

- [GitHub Repository](https://github.com/pengyue-polaron/deepseek-harness-genui)
- [Full README](https://github.com/pengyue-polaron/deepseek-harness-genui#readme)
- [Back to the Plugins list](../plugins.md)
