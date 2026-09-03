---
title: "dsh-undo"
description: "Context undo/redo plugin for DeepSeek Harness (dsh): roll the model context back to the last completed step and restore it again."
keywords: "dsh-undo, registry, awesome-list, coding, context, deepseek harness, dsh"
---
# dsh-undo

> ⭐ **4** · ✅ active · awesome-list

| | | | |
|---|---|---|---|
| Type | awesome-list | Category | Registries |
| Stars | ⭐ 4 | Status | ✅ active |
| Author | [LingLambda](https://github.com/LingLambda) | Updated | — |

## One-liner

> Context undo/redo plugin for DeepSeek Harness (dsh): roll the model context back to the last completed step and restore it again.

## About

Durable, multi-level undo/redo for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`). It rewinds model context by real user turn and restores workspace files changed by tools in that turn. The commands are handled locally and are never sent to the model: - **`/undo`** rewinds the latest visible real user message and every surface message after it. - **`/undo `** rewinds from a specific visible user message, including all later turns. - **`/redo`** restores the latest active rewind. Repeated undo and redo operations use LIFO order. The WebUI client contributes an undo action to finalized real-user message bubbles. The action invokes `/undo `; the Host validates that the addressed message is still a legal rewind target.

## ✨ Key Features

- **`/undo`** rewinds the latest visible real user message and every surface message after it.
- **`/undo <user-seq>`** rewinds from a specific visible user message, including all later turns.
- **`/redo`** restores the latest active rewind. Repeated undo and redo operations use LIFO order.

## 📦 Install

```bash
dsh plugin --profile demo add dsh-undo
```

## 🚀 Quick Start

```bash
dsh plugin --profile demo add github:LingLambda/dsh-undo#<sha>
```

## 📚 Learn more

**Install**

The package is a [dsh bundle](https://deepseek-harness.github.io/deepseek-harness/develop/basic/publish/). `package.json` points `dsh.bundle` to `cordis.patch.yml`, which activates the Host plugin, and exposes a WebUI Client bundle. From npm: dsh plugin --profile demo add dsh-undo From git (the `prepare` script builds `lib/` during installation; authorize the build in the profile's `pnpm-workspace

**Usage**

/undo /undo 42 /redo Use `/undo` for the latest user turn, the action on an older user bubble to rewind from that point, and `/redo` to restore the most recent rewind.

## 🔗 Links

- [GitHub Repository](https://github.com/LingLambda/dsh-undo)
- [Full README](https://github.com/LingLambda/dsh-undo#readme)
- [Back to the Awesome Lists & Registries list](../awesome-lists.md)
