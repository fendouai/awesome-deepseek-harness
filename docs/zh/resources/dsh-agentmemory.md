---
title: "dsh-agentmemory"
description: "agentmemory for DeepSeek Harness (dsh): full memory_* tools, capture hooks, and context injection over the local REST server"
keywords: "dsh-agentmemory, memory, plugin, coding, multi-agent, deepseek harness, dsh"
---
# dsh-agentmemory

> ⭐ **3** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 记忆与上下文 |
| 星数 | ⭐ 3 | 状态 | ✅ 活跃 |
| 作者 | [elementor-i](https://github.com/elementor-i) | 更新时间 | 2026-08-17 |
| 子分类 | 🧠 记忆系统 | 能力 | coding, memory, multi-agent |

## 一句话介绍

> agentmemory for DeepSeek Harness (dsh): full memory_* tools, capture hooks, and context injection over the local REST server

## 详细介绍

**agentmemory for DeepSeek Harness** — full `memory_*` tools, automatic capture hooks, and opt-in context injection over the local REST server. [English](./README.md) · [中文](./README_zh-CN.md) dsh-agentmemory connects [agentmemory](https://github.com/rohitg00/agentmemory), a local memory server for coding agents, to [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (DSH). It exposes the full `memory_*` tool set, captures observations automatically from sessions, prompts, and tool activity, and can inject recalled context into the system prompt — all over the local REST server, with no MCP bridge required.

## ✨ 核心特性

- **Full tool surface** — all 54 `memory_*` tools (8 core) mapped to `/agentmemory/*`, plus `memory_observe` and a `memory_http` escape hatch for any endpoint.
- **Automatic capture** — session, prompt, tool-use, subagent, workflow, and approval activity are recorded as observations in the background.
- **Context injection** — opt-in; recalled context from the session is added to the system prompt.
- **Safe by default** — credential redaction, per-call timeouts, non-blocking observation, and destructive tools gated behind a flag.
- **No MCP required** — no stdio bridge, no child process; the running REST server (`localhost:3111`) is the only dependency.

## 📦 安装

```bash
git clone https://github.com/elementor-i/dsh-agentmemory ~/dsh-plugins/dsh-agentmemory
```

## 🚀 快速开始

```bash
- insert:
    - id: dsh-agentmemory
      name: '$HOME/dsh-plugins/dsh-agentmemory/lib/index.js'
```

## 📚 更多信息

**Configuration**

All keys are optional and have safe defaults. The environment variables `AGENTMEMORY_URL`, `AGENTMEMORY_SECRET`, and `AGENTMEMORY_PROJECT_NAME` are honored as fallbacks. dsh-agentmemory: baseURL: http://127.0.0.1:3111 # empty -> $AGENTMEMORY_URL -> default secret: "" # empty -> $AGENTMEMORY_SECRET (Bearer) timeoutMs: 10000 observeTimeoutMs: 3000 # fire-and-forget hook timeout registerTools: true c

**The plugin manager fails to install — what else can I try?**

Oh-DSH-Desktop's plugin manager and the official CLI both end up running `dsh plugin --profile <name> add <package>`. If the plugin manager fails in your environment, the CLI is an equivalent fallback: npx -p @deepseek-ai/dsh dsh plugin --profile desktop add @elementor-i/dsh-agentmemory Replace `desktop` with your profile name, then restart DSH. If you are managing the desktop profile, run the com

## 🔗 链接

- [GitHub 仓库](https://github.com/elementor-i/dsh-agentmemory)
- [完整 README](https://github.com/elementor-i/dsh-agentmemory#readme)
- [返回dsh-agentmemory所在分类](../plugins.md)
