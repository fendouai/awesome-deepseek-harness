---
title: "dsh-plugin-hello"
description: "Hello-world style starter plugin for DSH."
keywords: "dsh-plugin-hello, learning, example, coding, deepseek harness, dsh"
---
# dsh-plugin-hello

> ⭐ **0** · ✅ active · example

| | | | |
|---|---|---|---|
| Type | example | Category | Learning |
| Stars | ⭐ 0 | Status | ✅ active |
| Author | [xu1132](https://github.com/xu1132) | Updated | 2026-08-14 |

## One-liner

> Hello-world style starter plugin for DSH.

## About

A minimal [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) community plugin. It registers a single model-callable tool, `hello`, that greets a caller by name. It is the smallest complete example of a `dsh-plugin` bundle and a good starting point for a first contribution.

## ✨ Key Features

- **Input:** `name` (string, required) — the person to greet.
- **Output:** `"<greeting>, <name>!"` — for example `Hello, Ada!`.

## 📦 Install

```bash
dsh plugin --profile demo add github:you/dsh-plugin-hello
```

## 🚀 Quick Start

```bash
dsh --profile demo --dump-config   # shows a "# == dsh-plugin-hello" layer
dsh --profile demo
```

## 📚 Learn more

**Install into a profile**

`dsh plugin` forwards to pnpm inside the profile directory, so any pnpm install form works: dsh plugin --profile demo add github:you/dsh-plugin-hello The first run initializes the profile with `@deepseek-ai/dsh-base`, links this package, and appends it to the profile's `dsh.profile.bundles` because `package.json` declares `dsh.bundle`. A git install fetches sources, so pnpm runs the `prepare` scri

**Configure**

Set a custom greeting by overriding the row in the profile's `cordis.patch.yml`: name: dsh-plugin-hello config: greeting: Howdy Invalid configuration fails the load.

## 🔗 Links

- [GitHub Repository](https://github.com/xu1132/dsh-plugin-hello)
- [Full README](https://github.com/xu1132/dsh-plugin-hello#readme)
- [Back to the Examples & Starters list](../examples.md)
