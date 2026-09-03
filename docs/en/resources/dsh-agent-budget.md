---
title: "dsh-agent-budget"
description: "Native Harness agent-tree token budget plugin"
keywords: "dsh-agent-budget, developer, plugin, coding, multi-agent, deepseek harness, dsh"
---
# dsh-agent-budget

> ⭐ **2** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 2 | Status | ✅ active |
| Author | [vibeinging](https://github.com/vibeinging) | Updated | — |
| Subcategory | 💰 Cost & billing | Capabilities | coding, multi-agent |

## One-liner

> Native Harness agent-tree token budget plugin

## About

`dsh-agent-budget` gives one live agent session, or its complete local descendant tree, a durable Token limit and absolute deadline. It reserves capacity before every attributed `llm/stream` provider attempt and replaces that estimate with provider-reported usage after the stream settles, so concurrent child agents cannot all spend the same remaining balance. The plugin is an out-of-tree DSH bundle for one Host process. A hard budget refuses new provider attempts before dispatch; it is not an exact billing system and does not forcibly cancel work already in flight. Decision record: [durable agent-tree token admission](docs/design/2026-08-09-agent-budget-admission.md).

## ✨ Key Features

- Durable `session` and local descendant-tree scopes, restored through the DSH Storage Domain.
- Soft accounting or hard admission with concurrency-safe local reservations.
- Absolute deadlines that survive restart, plus fail-closed recovery when dispatched usage is unknown.
- Direct human control through `/budget`; optional model-facing tools are available for intentional manual compositions.
- Output convergence that reduces `maxTokens` as a bounded account approaches exhaustion.

## 📦 Install

```bash
dsh plugin --profile web add -w github:dsh-external/dsh-agent-budget#<reviewed-commit>
```

## 🚀 Quick Start

```bash
dsh --profile web --dump-config
dsh --profile web
```

## 📚 Learn more

**Install**

The shipped `web` and `headless` profiles provide the Storage, Storage Domain, Token Meter, and command services this bundle requires. A custom profile must provide those services itself.

## 🔗 Links

- [GitHub Repository](https://github.com/vibeinging/dsh-agent-budget)
- [Full README](https://github.com/vibeinging/dsh-agent-budget#readme)
- [Back to the Plugins list](../plugins.md)
