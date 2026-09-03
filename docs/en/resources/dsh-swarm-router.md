---
title: "dsh-swarm-router"
description: "DSH plugin: sub-agent matrix swarm — routes heterogeneous tasks to the most suitable model (OpenRouter-like + cfgpu.com/llm/square), dispatches each via in-process subagents. 32/32 benchmark green."
keywords: "dsh-swarm-router, multi-agent, agent, coding, ui, deepseek harness, dsh"
---
# dsh-swarm-router

> ⭐ **2** · ✅ active · agent

| | | | |
|---|---|---|---|
| Type | agent | Category | Multi-agent |
| Stars | ⭐ 2 | Status | ✅ active |
| Author | [r600a-code](https://github.com/r600a-code) | Updated | — |

## One-liner

> DSH plugin: sub-agent matrix swarm — routes heterogeneous tasks to the most suitable model (OpenRouter-like + cfgpu.com/llm/square), dispatches each via in-process subagents. 32/32 benchmark green.

## About

[English](README.md) | [中文](README.zh.md) A DeepSeek Harness **bundle** that turns a batch of heterogeneous tasks into a **sub-agent matrix swarm**: it routes each task to the most suitable model from an OpenRouter-like gateway plus the `cfgpu.com/llm/square` catalog, then dispatches each assignment in parallel as a real in-process subagent (or a direct `ctx.llm` call) pinned to that model — quick tasks land on fast/cheap models, hard tasks on strong reasoning models. A formal design write-up lives in [`docs/PAPER.md`](docs/PAPER.md).

## 🚀 Quick Start

```bash
dsh --profile headless "$(cat benchmark/benchmark_prompt.txt)"          # subagent mode, 5 tasks
node benchmark/verify_benchmark.mjs                                     # 27/27 green
dsh --profile headless "$(cat benchmark/benchmark_direct_prompt.txt)"   # direct mode, 3 tasks
node benchmark/verify_benchmark.mjs benchmark_direct_RESULT.json        # 31/31 green
```

## 🔗 Links

- [GitHub Repository](https://github.com/r600a-code/dsh-swarm-router)
- [Full README](https://github.com/r600a-code/dsh-swarm-router#readme)
- [Back to the Agents & Multi-Agent list](../agents.md)
