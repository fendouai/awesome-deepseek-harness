---
title: "dsh-stream-rules"
description: "模式匹配自动注入 steering rules，不占系统上下文 - Inject rules when needed, without wasting context. Similar to oh-my-pi's \"Time-traveling stream rules\", but with a very simple and compact code implementation."
keywords: "dsh-stream-rules, memory, plugin, coding, context, deepseek harness, dsh"
---
# dsh-stream-rules

> ⭐ **5** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 记忆与上下文 |
| 星数 | ⭐ 5 | 状态 | ✅ 活跃 |
| 作者 | [jiesou](https://github.com/jiesou) | 更新时间 | — |
| 子分类 | 📦 上下文管理 | 能力 | coding, context |

## 一句话介绍

> 模式匹配自动注入 steering rules，不占系统上下文 - Inject rules when needed, without wasting context. Similar to oh-my-pi's "Time-traveling stream rules", but with a very simple and compact code implementation.

## 详细介绍

[简体中文](README.zh.md) Inject rules when needed, without wasting context. You can write custom streaming rules for the agent. These rules are injected only as a steering notice after a pattern match, then agent retry from the same point. This allows you to control the boundaries of agent behavior, without wasting context. Port of my [jiesou/opencode-stream-rules](https://github.com/jiesou/opencode-stream-rules) to DSH. Similar to oh-my-pi's "Time-traveling stream rules", but with a very simple and compact code implementation.

## ✨ 核心特性

- **default** — injects a `SYSTEM NOTICE` steering message into the agent via `agent.inject()` (DSH's non-waking "queue model-facing context for the next pre-step
- **`reject: true`** — denies the FIRST tool call (`{ kind: 'deny' }`); later attempts are allowed. Steering without over-restricting, e.g. letting `pip install` 

## 📦 安装

```bash
dsh plugin --profile <name> add @jiesou/dsh-stream-rules
```

## 🚀 快速开始

```bash
dsh plugin --profile <name> add github:jiesou/dsh-stream-rules
```

## 📚 更多信息

**Install**

From npm (prebuilt, recommended): dsh plugin --profile <name> add @jiesou/dsh-stream-rules Or from GitHub (runs `prepare` to build on install): dsh plugin --profile <name> add github:jiesou/dsh-stream-rules Or add the row to your profile's `cordis.patch.yml`: name: '@jiesou/dsh-stream-rules'

**After installing**

You need to write the rules in your own `.js` file. This plugin won't work by default until you edit the rules. 1. Locate the plugin's path: $DSH_HOME/profiles/<name>/node_modules/@jiesou/dsh-stream-rules where `$DSH_HOME` defaults to `~/.dsh`. 2. Write rules: mv rules/rules.js.example rules/rules.local.js name: '@jiesou/dsh-stream-rules' config: rules: /path/to/your/rules

## 🔗 链接

- [GitHub 仓库](https://github.com/jiesou/dsh-stream-rules)
- [完整 README](https://github.com/jiesou/dsh-stream-rules#readme)
- [返回dsh-stream-rules所在分类](../plugins.md)
