---
title: "dsh-cost-meter"
description: "Provider-aware LLM cost meter and local ledger for DeepSeek Harness"
keywords: "dsh-cost-meter, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-cost-meter

> ⭐ **3** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 3 | 状态 | ✅ 活跃 |
| 作者 | [uruana33](https://github.com/uruana33) | 更新时间 | — |
| 子分类 | 👁️ 视觉工具 | 能力 | coding |

## 一句话介绍

> Provider-aware LLM cost meter and local ledger for DeepSeek Harness

## 详细介绍

Out-of-tree [dsh](https://github.com/deepseek-ai/deepseek-harness) plugin that shows a live **USD cost badge** for the open conversation in the Web UI. It is a dual-face `dsh.client` package: - **Host half** (`lib/index.js`) registers a `sessionCost` projection on the session-projection seam. The fold tracks the current provider/model from `request/header` events and accumulates cost from the provider-reported usage buckets (uncached input / output / cache-read / cache-write), reusing token-meter's "replace the same `(turn, step)` sample instead of double-counting" rule. The view exposes the whole-session totals plus a `byTurn` map keyed by turn number. - **Client half** (`lib/client.js`) registers a badge into the `conversation.chat.assistant-actions` slot — the action row at the end of e

## ✨ 核心特性

- **Host half** (`lib/index.js`) registers a `sessionCost` projection on the
- **Client half** (`lib/client.js`) registers a badge into the

## 📦 安装

```bash
dsh plugin --profile web add @steven-wu/dsh-cost-meter
# restart the web profile, then refresh the page
```

## 🚀 快速开始

```bash
dsh plugin --profile web add file:/path/to/dsh-cost-meter
```

## 📚 更多信息

**Install**

The package declares a `dsh.bundle` manifest, so `dsh plugin add` installs it **and** adds it to the profile's bundle layers automatically — no manual patch edit: dsh plugin --profile web add @steven-wu/dsh-cost-meter

## 🔗 链接

- [GitHub 仓库](https://github.com/uruana33/dsh-cost-meter)
- [完整 README](https://github.com/uruana33/dsh-cost-meter#readme)
- [返回dsh-cost-meter所在分类](../plugins.md)
