---
title: "nowledge-mem-deepseek-harness"
description: "Community plugin bundle integrating the Nowledge Mem memory service with DeepSeek Harness."
keywords: "nowledge-mem-deepseek-harness, memory, plugin, deepseek harness, dsh"
---
# nowledge-mem-deepseek-harness

> ⭐ **5** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Memory & context |
| Stars | ⭐ 5 | Status | ✅ active |
| Author | [nowledge-co](https://github.com/nowledge-co) | Updated | 2026-08-17 |
| Subcategory | 🧠 Memory systems | Capabilities | memory |

## One-liner

> Community plugin bundle integrating the Nowledge Mem memory service with DeepSeek Harness.

## About

One memory layer for every AI tool and agent, packaged as a DeepSeek Harness (`dsh`) bundle. Nowledge Mem brings DSH into the same durable memory system as your other agents, with startup context, prompt-time recall, MCP memory tools, and turn-end thread capture. This repository is the canonical standalone plugin package, mirrored in `nowledge-co/community` for the Nowledge Mem connector index.

## ✨ Key Features

- Injects the Nowledge Mem Context Bundle once per DSH session through `agent/pre-step`.
- Runs prompt-time memory recall for continuation, release, regression, connector, plugin, and other recall-shaped prompts.
- Adds the Mem MCP server through DSH's reconnecting `@deepseek-ai/dsh-mcp-client`, so tools appear as `mcp__nowledge_mem__...`.
- Imports the real DSH surface transcript after completed turns with `nmem t import --source deepseek-harness`.
- Stamps CLI imports with `NMEM_IMPORT_ORIGIN=deepseek-harness`.

## 📦 Install

```bash
dsh plugin --profile web add github:nowledge-co/nowledge-mem-deepseek-harness
dsh web
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add ./nowledge-mem-deepseek-harness-plugin
dsh web
```

## 📚 Learn more

**Install**

dsh plugin --profile web add github:nowledge-co/nowledge-mem-deepseek-harness dsh web For a local checkout of `nowledge-co/community`, run this from the repository root: dsh plugin --profile web add ./nowledge-mem-deepseek-harness-plugin dsh web Make sure the `nmem` CLI is on `PATH`, then verify: nmem status nmem config mcp show --host deepseek-harness The bundle connects to the local Mem MCP endp

**Configuration**

The bundle accepts these row config fields in a later `cordis.patch.yml` override: config: cliPath: nmem sourceApp: deepseek-harness importOrigin: deepseek-harness contextOnSessionStart: true recallOnPrompt: true syncOnTurnEnd: true recallLimit: 8 spaceId: my-space-id agentId: deepseek-harness Ambient variables also work:

## 🔗 Links

- [GitHub Repository](https://github.com/nowledge-co/nowledge-mem-deepseek-harness)
- [Full README](https://github.com/nowledge-co/nowledge-mem-deepseek-harness#readme)
- [Back to the Plugins list](../plugins.md)
