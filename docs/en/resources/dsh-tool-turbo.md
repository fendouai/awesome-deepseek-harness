---
title: "dsh-tool-turbo"
description: "Per-round reasoning_effort optimizer for DeepSeek Harness (dsh): auto-downgrades tool-call reasoning for simple tool chains, lifting back for heavy work. Cuts thinking time between tool calls."
keywords: "dsh-tool-turbo, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-tool-turbo

> ⭐ **7** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 7 | Status | ✅ active |
| Author | [Electricitysheep](https://github.com/Electricitysheep) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> Per-round reasoning_effort optimizer for DeepSeek Harness (dsh): auto-downgrades tool-call reasoning for simple tool chains, lifting back for heavy work. Cuts thinking time between tool calls.

## About

**Cut tool-call latency in [DeepSeek Harness (dsh)](https://github.com/deepseek-ai/deepseek-harness) by auto-adjusting `reasoning_effort` per tool round.** [中文文档](./README.zh.md) · English In a multi-step tool chain, the model re-thinks before **every** tool call — and that thinking dominates the wall-clock time (a 50-step agent task can spend minutes in reasoning between tools). `dsh-tool-turbo` watches the recent tool calls of a step and injects the *lowest sensible* reasoning effort into the next model request, then lifts it again the moment the work gets heavy.

## 🚀 Quick Start

```bash
[tool-turbo] agent/request: baseline=high calls=[]                    => reasoningEffort=high
[tool-turbo] agent/request: baseline=high calls=[{"name":"write",…}] => reasoningEffort=low
```

## 🔗 Links

- [GitHub Repository](https://github.com/Electricitysheep/dsh-tool-turbo)
- [Full README](https://github.com/Electricitysheep/dsh-tool-turbo#readme)
- [Back to the Plugins list](../plugins.md)
