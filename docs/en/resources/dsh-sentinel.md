---
title: "dsh-sentinel"
description: "Condition-driven wakeup for DeepSeek Harness: durable file/command/http/process/webhook watches that wake the agent, with dock, sidebar branch, and a global dashboard."
keywords: "dsh-sentinel, search, plugin, coding, multi-agent, ui, deepseek harness, dsh"
---
# dsh-sentinel

> ⭐ **15** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 15 | Status | ✅ active |
| Author | [fuhefei](https://github.com/fuhefei) | Updated | — |
| Subcategory | 🌐 Web search | Capabilities | coding, multi-agent, ui |

## One-liner

> Condition-driven wakeup for DeepSeek Harness: durable file/command/http/process/webhook watches that wake the agent, with dock, sidebar branch, and a global dashboard.

## About

Condition-driven wakeup for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness): the agent registers a watch, goes to sleep — even closes the session — and the sentinel wakes it when the condition happens. Every subscription and every fire is a user-visible session event, and the browser dock shows what is on duty.

## 📦 Install

```bash
dsh plugin --profile web add dsh-sentinel
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add "github:fuhefei/dsh-sentinel#v0.11.0"
```

## 📚 Learn more

**Configuration**

All deployment-tunable knobs live in the plugin's config schema (defaults in parentheses); override them on the bundle row in your profile's `cordis.patch.yml`: name: dsh-sentinel config: heartbeatMs: 5000 # probe round interval probeConcurrency: 8 # in-flight probes per round maxSubscriptionsPerSession: 16 maxPendingWakeups: 8 # queued wakeups per session before dropping oldest defaultIntervalSec

**Install**

One line through the official bundle channel: dsh plugin --profile web add dsh-sentinel Or straight from git (build artifacts are committed, so the git-source install runs no build): dsh plugin --profile web add "github:fuhefei/dsh-sentinel#v0.11.0" Alternatively, add the node half manually through a patch-list configuration over the shipped base:

## 🔗 Links

- [GitHub Repository](https://github.com/fuhefei/dsh-sentinel)
- [Full README](https://github.com/fuhefei/dsh-sentinel#readme)
- [Back to the Plugins list](../plugins.md)
