---
title: "dsh-agent-budget"
description: "Native Harness agent-tree token budget plugin"
keywords: "dsh-agent-budget, developer, plugin, coding, multi-agent, deepseek harness, dsh"
---
# dsh-agent-budget

> ⭐ **2** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 2 | 状态 | ✅ 活跃 |
| 作者 | [vibeinging](https://github.com/vibeinging) | 更新时间 | — |
| 子分类 | 💰 费用与统计 | 能力 | coding, multi-agent |

## 一句话介绍

> Native Harness agent-tree token budget plugin

## 详细介绍

`dsh-agent-budget` gives one live agent session, or its complete local descendant tree, a durable Token limit and absolute deadline. It reserves capacity before every attributed `llm/stream` provider attempt and replaces that estimate with provider-reported usage after the stream settles, so concurrent child agents cannot all spend the same remaining balance. The plugin is an out-of-tree DSH bundle for one Host process. A hard budget refuses new provider attempts before dispatch; it is not an exact billing system and does not forcibly cancel work already in flight. Decision record: [durable agent-tree token admission](docs/design/2026-08-09-agent-budget-admission.md).

## ✨ 核心特性

- Durable `session` and local descendant-tree scopes, restored through the DSH Storage Domain.
- Soft accounting or hard admission with concurrency-safe local reservations.
- Absolute deadlines that survive restart, plus fail-closed recovery when dispatched usage is unknown.
- Direct human control through `/budget`; optional model-facing tools are available for intentional manual compositions.
- Output convergence that reduces `maxTokens` as a bounded account approaches exhaustion.

## 📦 安装

```bash
dsh plugin --profile web add -w github:dsh-external/dsh-agent-budget#<reviewed-commit>
```

## 🚀 快速开始

```bash
dsh --profile web --dump-config
dsh --profile web
```

## 📚 更多信息

**Install**

The shipped `web` and `headless` profiles provide the Storage, Storage Domain, Token Meter, and command services this bundle requires. A custom profile must provide those services itself.

## 🔗 链接

- [GitHub 仓库](https://github.com/vibeinging/dsh-agent-budget)
- [完整 README](https://github.com/vibeinging/dsh-agent-budget#readme)
- [返回dsh-agent-budget所在分类](../plugins.md)
