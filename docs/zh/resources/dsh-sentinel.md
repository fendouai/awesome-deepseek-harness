---
title: "dsh-sentinel"
description: "Condition-driven wakeup for DeepSeek Harness: durable file/command/http/process/webhook watches that wake the agent, with dock, sidebar branch, and a global dashboard."
keywords: "dsh-sentinel, search, plugin, coding, multi-agent, ui, deepseek harness, dsh"
---
# dsh-sentinel

> ⭐ **15** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 搜索与研究 |
| 星数 | ⭐ 15 | 状态 | ✅ 活跃 |
| 作者 | [fuhefei](https://github.com/fuhefei) | 更新时间 | — |
| 子分类 | 🌐 网页搜索 | 能力 | coding, multi-agent, ui |

## 一句话介绍

> Condition-driven wakeup for DeepSeek Harness: durable file/command/http/process/webhook watches that wake the agent, with dock, sidebar branch, and a global dashboard.

## 详细介绍

Condition-driven wakeup for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness): the agent registers a watch, goes to sleep — even closes the session — and the sentinel wakes it when the condition happens. Every subscription and every fire is a user-visible session event, and the browser dock shows what is on duty.

## 📦 安装

```bash
dsh plugin --profile web add dsh-sentinel
```

## 🚀 快速开始

```bash
dsh plugin --profile web add "github:fuhefei/dsh-sentinel#v0.11.0"
```

## 📚 更多信息

**Configuration**

All deployment-tunable knobs live in the plugin's config schema (defaults in parentheses); override them on the bundle row in your profile's `cordis.patch.yml`: name: dsh-sentinel config: heartbeatMs: 5000 # probe round interval probeConcurrency: 8 # in-flight probes per round maxSubscriptionsPerSession: 16 maxPendingWakeups: 8 # queued wakeups per session before dropping oldest defaultIntervalSec

**Install**

One line through the official bundle channel: dsh plugin --profile web add dsh-sentinel Or straight from git (build artifacts are committed, so the git-source install runs no build): dsh plugin --profile web add "github:fuhefei/dsh-sentinel#v0.11.0" Alternatively, add the node half manually through a patch-list configuration over the shipped base:

## 🔗 链接

- [GitHub 仓库](https://github.com/fuhefei/dsh-sentinel)
- [完整 README](https://github.com/fuhefei/dsh-sentinel#readme)
- [返回dsh-sentinel所在分类](../plugins.md)
