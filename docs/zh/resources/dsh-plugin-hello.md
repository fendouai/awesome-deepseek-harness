---
title: "dsh-plugin-hello"
description: "Hello-world 风格 DSH 起步插件。"
keywords: "dsh-plugin-hello, learning, example, coding, deepseek harness, dsh"
---
# dsh-plugin-hello

> ⭐ **0** · ✅ 活跃 · 示例

| | | | |
|---|---|---|---|
| 类型 | 示例 | 分类 | 学习 |
| 星数 | ⭐ 0 | 状态 | ✅ 活跃 |
| 作者 | [xu1132](https://github.com/xu1132) | 更新时间 | 2026-08-14 |

## 一句话介绍

> Hello-world 风格 DSH 起步插件。

## 详细介绍

A minimal [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) community plugin. It registers a single model-callable tool, `hello`, that greets a caller by name. It is the smallest complete example of a `dsh-plugin` bundle and a good starting point for a first contribution.

## ✨ 核心特性

- **Input:** `name` (string, required) — the person to greet.
- **Output:** `"<greeting>, <name>!"` — for example `Hello, Ada!`.

## 📦 安装

```bash
dsh plugin --profile demo add github:you/dsh-plugin-hello
```

## 🚀 快速开始

```bash
dsh --profile demo --dump-config   # shows a "# == dsh-plugin-hello" layer
dsh --profile demo
```

## 📚 更多信息

**Install into a profile**

`dsh plugin` forwards to pnpm inside the profile directory, so any pnpm install form works: dsh plugin --profile demo add github:you/dsh-plugin-hello The first run initializes the profile with `@deepseek-ai/dsh-base`, links this package, and appends it to the profile's `dsh.profile.bundles` because `package.json` declares `dsh.bundle`. A git install fetches sources, so pnpm runs the `prepare` scri

**Configure**

Set a custom greeting by overriding the row in the profile's `cordis.patch.yml`: name: dsh-plugin-hello config: greeting: Howdy Invalid configuration fails the load.

## 🔗 链接

- [GitHub 仓库](https://github.com/xu1132/dsh-plugin-hello)
- [完整 README](https://github.com/xu1132/dsh-plugin-hello#readme)
- [返回dsh-plugin-hello所在分类](../examples.md)
