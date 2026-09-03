---
title: "dsh-slice-agent-loop"
description: "Drop-in agent loop whose context engine is a bounded slice instead of a growing transcript."
keywords: "dsh-slice-agent-loop, multi-agent, agent, context, workflow, deepseek harness, dsh"
---
# dsh-slice-agent-loop

> ⭐ **2** · ✅ active · agent · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | agent | Category | Multi-agent |
| Stars | ⭐ 2 | Status | ✅ active |
| Author | [TT-Wang](https://github.com/TT-Wang) | Updated | 2026-08-14 |

## One-liner

> Drop-in agent loop whose context engine is a bounded slice instead of a growing transcript.

## About

That sounds like common sense, but today's mainstream coding agents replay the entire conversation history back to the model every call: the excess is never trimmed, and what falls short can never be recovered. This plugin brings a slice loop built around that one sentence into the [DeepSeek Harness](https://github.com/dsh2026): **same harness, same model, same tools and persistence — only the agent loop is swapped**, so in every comparison below the loop itself is the only variable. Early beta; tracks DSH `0.1.2-alpha.4` (`snapshotEvents`, typert `/api//` RPC with cookie auth; the bundled bench drivers speak the new protocol).

## 📦 Install

```bash
dsh plugin --profile web add "github:TT-Wang/dsh-slice-agent-loop#main"
```

## 🚀 Quick Start

```bash
npm install --legacy-peer-deps   # the @deepseek-ai/* peers are unpublished
npm run link:dsh                 # symlink them from your dsh checkout
npm run typecheck && npm test
```

## 📚 Learn more

**Install**

dsh plugin --profile web add "github:TT-Wang/dsh-slice-agent-loop#main" Or from a local checkout: `git clone` then `dsh plugin --profile web add .` Restart web afterwards — bundles are composed at boot. The bundled patch disables the stock loop and compaction — the bounded rebuild replaces both. If your composition carries an `agent-loop-invariant` row, remove it: a rebuilt slice cannot equal the 

**Configuration**

Set them from your profile's `cordis.patch.yml`, targeting the existing row by id (`- id: slice-agent-loop` + `config:`).

## 🔗 Links

- [GitHub Repository](https://github.com/TT-Wang/dsh-slice-agent-loop)
- [Full README](https://github.com/TT-Wang/dsh-slice-agent-loop#readme)
- [Back to the Agents & Multi-Agent list](../agents.md)
