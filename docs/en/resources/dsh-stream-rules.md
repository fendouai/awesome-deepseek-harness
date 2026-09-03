---
title: "dsh-stream-rules"
description: "模式匹配自动注入 steering rules，不占系统上下文 - Inject rules when needed, without wasting context. Similar to oh-my-pi's \"Time-traveling stream rules\", but with a very simple and compact code implementation."
keywords: "dsh-stream-rules, memory, plugin, coding, context, deepseek harness, dsh"
---
# dsh-stream-rules

> ⭐ **5** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Memory & context |
| Stars | ⭐ 5 | Status | ✅ active |
| Author | [jiesou](https://github.com/jiesou) | Updated | — |
| Subcategory | 📦 Context management | Capabilities | coding, context |

## One-liner

> 模式匹配自动注入 steering rules，不占系统上下文 - Inject rules when needed, without wasting context. Similar to oh-my-pi's "Time-traveling stream rules", but with a very simple and compact code implementation.

## About

[简体中文](README.zh.md) Inject rules when needed, without wasting context. You can write custom streaming rules for the agent. These rules are injected only as a steering notice after a pattern match, then agent retry from the same point. This allows you to control the boundaries of agent behavior, without wasting context. Port of my [jiesou/opencode-stream-rules](https://github.com/jiesou/opencode-stream-rules) to DSH. Similar to oh-my-pi's "Time-traveling stream rules", but with a very simple and compact code implementation.

## ✨ Key Features

- **default** — injects a `SYSTEM NOTICE` steering message into the agent via `agent.inject()` (DSH's non-waking "queue model-facing context for the next pre-step
- **`reject: true`** — denies the FIRST tool call (`{ kind: 'deny' }`); later attempts are allowed. Steering without over-restricting, e.g. letting `pip install` 

## 📦 Install

```bash
dsh plugin --profile <name> add @jiesou/dsh-stream-rules
```

## 🚀 Quick Start

```bash
dsh plugin --profile <name> add github:jiesou/dsh-stream-rules
```

## 📚 Learn more

**Install**

From npm (prebuilt, recommended): dsh plugin --profile <name> add @jiesou/dsh-stream-rules Or from GitHub (runs `prepare` to build on install): dsh plugin --profile <name> add github:jiesou/dsh-stream-rules Or add the row to your profile's `cordis.patch.yml`: name: '@jiesou/dsh-stream-rules'

**After installing**

You need to write the rules in your own `.js` file. This plugin won't work by default until you edit the rules. 1. Locate the plugin's path: $DSH_HOME/profiles/<name>/node_modules/@jiesou/dsh-stream-rules where `$DSH_HOME` defaults to `~/.dsh`. 2. Write rules: mv rules/rules.js.example rules/rules.local.js name: '@jiesou/dsh-stream-rules' config: rules: /path/to/your/rules

## 🔗 Links

- [GitHub Repository](https://github.com/jiesou/dsh-stream-rules)
- [Full README](https://github.com/jiesou/dsh-stream-rules#readme)
- [Back to the Plugins list](../plugins.md)
