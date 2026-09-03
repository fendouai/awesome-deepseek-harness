---
title: "nowledge-mem-deepseek-harness"
description: "将 Nowledge Mem 记忆服务接入 DeepSeek Harness 的社区插件包。"
keywords: "nowledge-mem-deepseek-harness, memory, plugin, deepseek harness, dsh"
---
# nowledge-mem-deepseek-harness

> ⭐ **5** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 记忆与上下文 |
| 星数 | ⭐ 5 | 状态 | ✅ 活跃 |
| 作者 | [nowledge-co](https://github.com/nowledge-co) | 更新时间 | 2026-08-17 |
| 子分类 | 🧠 记忆系统 | 能力 | memory |

## 一句话介绍

> 将 Nowledge Mem 记忆服务接入 DeepSeek Harness 的社区插件包。

## 详细介绍

One memory layer for every AI tool and agent, packaged as a DeepSeek Harness (`dsh`) bundle. Nowledge Mem brings DSH into the same durable memory system as your other agents, with startup context, prompt-time recall, MCP memory tools, and turn-end thread capture. This repository is the canonical standalone plugin package, mirrored in `nowledge-co/community` for the Nowledge Mem connector index.

## ✨ 核心特性

- Injects the Nowledge Mem Context Bundle once per DSH session through `agent/pre-step`.
- Runs prompt-time memory recall for continuation, release, regression, connector, plugin, and other recall-shaped prompts.
- Adds the Mem MCP server through DSH's reconnecting `@deepseek-ai/dsh-mcp-client`, so tools appear as `mcp__nowledge_mem__...`.
- Imports the real DSH surface transcript after completed turns with `nmem t import --source deepseek-harness`.
- Stamps CLI imports with `NMEM_IMPORT_ORIGIN=deepseek-harness`.

## 📦 安装

```bash
dsh plugin --profile web add github:nowledge-co/nowledge-mem-deepseek-harness
dsh web
```

## 🚀 快速开始

```bash
dsh plugin --profile web add ./nowledge-mem-deepseek-harness-plugin
dsh web
```

## 📚 更多信息

**Install**

dsh plugin --profile web add github:nowledge-co/nowledge-mem-deepseek-harness dsh web For a local checkout of `nowledge-co/community`, run this from the repository root: dsh plugin --profile web add ./nowledge-mem-deepseek-harness-plugin dsh web Make sure the `nmem` CLI is on `PATH`, then verify: nmem status nmem config mcp show --host deepseek-harness The bundle connects to the local Mem MCP endp

**Configuration**

The bundle accepts these row config fields in a later `cordis.patch.yml` override: config: cliPath: nmem sourceApp: deepseek-harness importOrigin: deepseek-harness contextOnSessionStart: true recallOnPrompt: true syncOnTurnEnd: true recallLimit: 8 spaceId: my-space-id agentId: deepseek-harness Ambient variables also work:

## 🔗 链接

- [GitHub 仓库](https://github.com/nowledge-co/nowledge-mem-deepseek-harness)
- [完整 README](https://github.com/nowledge-co/nowledge-mem-deepseek-harness#readme)
- [返回nowledge-mem-deepseek-harness所在分类](../plugins.md)
