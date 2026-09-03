---
title: "dsh-noema"
description: "Noema long-term memory plugin for DSH: durable, inspectable agent memory with recall tools and a settings page."
keywords: "dsh-noema, memory, plugin, coding, multi-agent, deepseek harness, dsh"
---
# dsh-noema

> ⭐ **128** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 记忆与上下文 |
| 星数 | ⭐ 128 | 状态 | ✅ 活跃 |
| 作者 | [ZSeven-W](https://github.com/ZSeven-W) | 更新时间 | — |
| 子分类 | 🧠 记忆系统 | 能力 | coding, memory, multi-agent |

## 一句话介绍

> Noema long-term memory plugin for DSH: durable, inspectable agent memory with recall tools and a settings page.

## 详细介绍

DSH Noema connects [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) with [Noema](https://github.com/ZSeven-W/noema) — a local-first, non-vector memory system for coding agents — so an Agent keeps durable knowledge across sessions instead of starting every conversation from zero.

## 📦 安装

```bash
dsh plugin --profile web add @zseven-w/dsh-noema@latest
dsh web
```

## 🚀 快速开始

```bash
dsh plugin --profile web add link:/path/to/dsh-noema
dsh web
```

## 📚 更多信息

**🛠️ Settings-Page Management**

The Noema Memory settings page configures the server command, memory root, budgets, idle/call timeouts, and the guidance section — and a Manage memories card searches, browses, adds, reviews, and deletes stored memories directly. </td> <td width="50%">

**Install into DSH**

dsh plugin --profile web add @zseven-w/dsh-noema@latest dsh web Or, for local development straight from the source tree: dsh plugin --profile web add link:/path/to/dsh-noema dsh web The `link:` protocol symlinks the profile dependency to this repository, so rebuilds are visible immediately and Cordis HMR can watch the compiled output. The plugin bundles the `noema-mcp` binary through per-platform 

**Settings**

Open **Settings → Noema Memory**: The status card shows server health with restart/stop actions, and the import section manages the nine memory sources.

## 🔗 链接

- [GitHub 仓库](https://github.com/ZSeven-W/dsh-noema)
- [完整 README](https://github.com/ZSeven-W/dsh-noema#readme)
- [返回dsh-noema所在分类](../plugins.md)
