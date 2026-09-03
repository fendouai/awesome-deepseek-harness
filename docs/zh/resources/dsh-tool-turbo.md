---
title: "dsh-tool-turbo"
description: "Per-round reasoning_effort optimizer for DeepSeek Harness (dsh): auto-downgrades tool-call reasoning for simple tool chains, lifting back for heavy work. Cuts thinking time between tool calls."
keywords: "dsh-tool-turbo, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-tool-turbo

> ⭐ **7** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 7 | 状态 | ✅ 活跃 |
| 作者 | [Electricitysheep](https://github.com/Electricitysheep) | 更新时间 | — |
| 子分类 | 👁️ 视觉工具 | 能力 | coding |

## 一句话介绍

> Per-round reasoning_effort optimizer for DeepSeek Harness (dsh): auto-downgrades tool-call reasoning for simple tool chains, lifting back for heavy work. Cuts thinking time between tool calls.

## 详细介绍

**Cut tool-call latency in [DeepSeek Harness (dsh)](https://github.com/deepseek-ai/deepseek-harness) by auto-adjusting `reasoning_effort` per tool round.** [中文文档](./README.zh.md) · English In a multi-step tool chain, the model re-thinks before **every** tool call — and that thinking dominates the wall-clock time (a 50-step agent task can spend minutes in reasoning between tools). `dsh-tool-turbo` watches the recent tool calls of a step and injects the *lowest sensible* reasoning effort into the next model request, then lifts it again the moment the work gets heavy.

## 🚀 快速开始

```bash
[tool-turbo] agent/request: baseline=high calls=[]                    => reasoningEffort=high
[tool-turbo] agent/request: baseline=high calls=[{"name":"write",…}] => reasoningEffort=low
```

## 🔗 链接

- [GitHub 仓库](https://github.com/Electricitysheep/dsh-tool-turbo)
- [完整 README](https://github.com/Electricitysheep/dsh-tool-turbo#readme)
- [返回dsh-tool-turbo所在分类](../plugins.md)
