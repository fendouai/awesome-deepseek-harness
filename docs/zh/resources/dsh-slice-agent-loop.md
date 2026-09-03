---
title: "dsh-slice-agent-loop"
description: "可替换的 Agent 循环：上下文引擎是有界切片而非不断增长的记录。"
keywords: "dsh-slice-agent-loop, multi-agent, agent, context, workflow, deepseek harness, dsh"
---
# dsh-slice-agent-loop

> ⭐ **2** · ✅ 活跃 · 智能体 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 智能体 | 分类 | 多智能体 |
| 星数 | ⭐ 2 | 状态 | ✅ 活跃 |
| 作者 | [TT-Wang](https://github.com/TT-Wang) | 更新时间 | 2026-08-14 |

## 一句话介绍

> 可替换的 Agent 循环：上下文引擎是有界切片而非不断增长的记录。

## 详细介绍

That sounds like common sense, but today's mainstream coding agents replay the entire conversation history back to the model every call: the excess is never trimmed, and what falls short can never be recovered. This plugin brings a slice loop built around that one sentence into the [DeepSeek Harness](https://github.com/dsh2026): **same harness, same model, same tools and persistence — only the agent loop is swapped**, so in every comparison below the loop itself is the only variable. Early beta; tracks DSH `0.1.2-alpha.4` (`snapshotEvents`, typert `/api//` RPC with cookie auth; the bundled bench drivers speak the new protocol).

## 📦 安装

```bash
dsh plugin --profile web add "github:TT-Wang/dsh-slice-agent-loop#main"
```

## 🚀 快速开始

```bash
npm install --legacy-peer-deps   # the @deepseek-ai/* peers are unpublished
npm run link:dsh                 # symlink them from your dsh checkout
npm run typecheck && npm test
```

## 📚 更多信息

**Install**

dsh plugin --profile web add "github:TT-Wang/dsh-slice-agent-loop#main" Or from a local checkout: `git clone` then `dsh plugin --profile web add .` Restart web afterwards — bundles are composed at boot. The bundled patch disables the stock loop and compaction — the bounded rebuild replaces both. If your composition carries an `agent-loop-invariant` row, remove it: a rebuilt slice cannot equal the 

**Configuration**

Set them from your profile's `cordis.patch.yml`, targeting the existing row by id (`- id: slice-agent-loop` + `config:`).

## 🔗 链接

- [GitHub 仓库](https://github.com/TT-Wang/dsh-slice-agent-loop)
- [完整 README](https://github.com/TT-Wang/dsh-slice-agent-loop#readme)
- [返回dsh-slice-agent-loop所在分类](../agents.md)
