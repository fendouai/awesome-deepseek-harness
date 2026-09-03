---
title: "deepseek-harness-genui"
description: "Task-specific React apps for DeepSeek Harness with state carried into the next Agent turn"
keywords: "deepseek-harness-genui, learning, skill, coding, multi-agent, deepseek harness, dsh"
---
# deepseek-harness-genui

> ⭐ **107** · ✅ active · skill

| | | | |
|---|---|---|---|
| Type | skill | Category | Learning |
| Stars | ⭐ 107 | Status | ✅ active |
| Author | [pengyue-polaron](https://github.com/pengyue-polaron) | Updated | — |

## One-liner

> Task-specific React apps for DeepSeek Harness with state carried into the next Agent turn

## About

DeepSeek Harness GenUI lets an Agent build a focused interface when a task is awkward in text. The Coding Agent writes ordinary React + TypeScript—not a component-tree DSL—and the interface can save user selections for the next Agent turn. The result is a task-specific app that can explain a difficult relationship, collect connected choices, or continue a tool-backed workflow without asking the user to repeat their input. Related research: [*EvoGenUI-Bench: Evaluating LLMs as Multi-Turn Generative UI Assistants*](https://arxiv.org/abs/2608.29387).

## 📦 Install

```bash
dsh plugin --profile web add dsh-plugin-genui --allow-build=esbuild
dsh --profile web
```

## 🚀 Quick Start

```bash
Plan a Saturday route with a museum, a riverside garden, and dinner. Build an
interface where I can change the times and make the garden optional.
```

## 📚 Learn more

**Install**

Requires Node.js `^22.19.0 || ^24.0.0` and a supported DeepSeek Harness Web profile. dsh plugin --profile web add dsh-plugin-genui --allow-build=esbuild dsh --profile web v0.14 supports Inline, Canvas, fullscreen, and localhost on the tested Harness versions listed in the [release notes](docs/release-notes-v0.14.0.md). TUI/headless profiles are not supported. `--allow-build=esbuild` enables the lo

## 🔗 Links

- [GitHub Repository](https://github.com/pengyue-polaron/deepseek-harness-genui)
- [Full README](https://github.com/pengyue-polaron/deepseek-harness-genui#readme)
- [Back to the Skills list](../skills.md)
