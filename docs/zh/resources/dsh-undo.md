---
title: "dsh-undo"
description: "Context undo/redo plugin for DeepSeek Harness (dsh): roll the model context back to the last completed step and restore it again."
keywords: "dsh-undo, registry, awesome-list, coding, context, deepseek harness, dsh"
---
# dsh-undo

> ⭐ **4** · ✅ 活跃 · 精选列表

| | | | |
|---|---|---|---|
| 类型 | 精选列表 | 分类 | 注册表 |
| 星数 | ⭐ 4 | 状态 | ✅ 活跃 |
| 作者 | [LingLambda](https://github.com/LingLambda) | 更新时间 | — |

## 一句话介绍

> Context undo/redo plugin for DeepSeek Harness (dsh): roll the model context back to the last completed step and restore it again.

## 详细介绍

Durable, multi-level undo/redo for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`). It rewinds model context by real user turn and restores workspace files changed by tools in that turn. The commands are handled locally and are never sent to the model: - **`/undo`** rewinds the latest visible real user message and every surface message after it. - **`/undo `** rewinds from a specific visible user message, including all later turns. - **`/redo`** restores the latest active rewind. Repeated undo and redo operations use LIFO order. The WebUI client contributes an undo action to finalized real-user message bubbles. The action invokes `/undo `; the Host validates that the addressed message is still a legal rewind target.

## ✨ 核心特性

- **`/undo`** rewinds the latest visible real user message and every surface message after it.
- **`/undo <user-seq>`** rewinds from a specific visible user message, including all later turns.
- **`/redo`** restores the latest active rewind. Repeated undo and redo operations use LIFO order.

## 📦 安装

```bash
dsh plugin --profile demo add dsh-undo
```

## 🚀 快速开始

```bash
dsh plugin --profile demo add github:LingLambda/dsh-undo#<sha>
```

## 📚 更多信息

**Install**

The package is a [dsh bundle](https://deepseek-harness.github.io/deepseek-harness/develop/basic/publish/). `package.json` points `dsh.bundle` to `cordis.patch.yml`, which activates the Host plugin, and exposes a WebUI Client bundle. From npm: dsh plugin --profile demo add dsh-undo From git (the `prepare` script builds `lib/` during installation; authorize the build in the profile's `pnpm-workspace

**Usage**

/undo /undo 42 /redo Use `/undo` for the latest user turn, the action on an older user bubble to rewind from that point, and `/redo` to restore the most recent rewind.

## 🔗 链接

- [GitHub 仓库](https://github.com/LingLambda/dsh-undo)
- [完整 README](https://github.com/LingLambda/dsh-undo#readme)
- [返回dsh-undo所在分类](../awesome-lists.md)
