---
title: "memsearch"
description: "Persistent, unified memory layer for all your AI agents (e.g. Claude Code, Codex, DSH), backed by Markdown and Milvus. / 面向所有 AI Agent（如 Claude Code、Codex、DSH）的持久化统一记忆层，基于 Markdown 与 Milvus。"
keywords: "memsearch, memory, plugin, deepseek harness, dsh"
---
# memsearch

> ⭐ **2,538** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Memory & context |
| Stars | ⭐ 2,538 | Status | ✅ active |
| Author | [zilliztech](https://github.com/zilliztech) | Updated | — |
| Subcategory | 🧠 Memory systems | Capabilities | memory |

## One-liner

> Persistent, unified memory layer for all your AI agents (e.g. Claude Code, Codex, DSH), backed by Markdown and Milvus. / 面向所有 AI Agent（如 Claude Code、Codex、DSH）的持久化统一记忆层，基于 Markdown 与 Milvus。

## About

- **DeepSeek Harness support** — MemSearch now brings automatic capture, pre-step memory injection, native skill-based recall, background maintenance, and a read-only memory browser to [DeepSeek Harness (DSH)](https://zilliztech.github.io/memsearch/platforms/dsh/). - **Skills from memory** — MemSearch now distills the workflows you repeat into reusable, installable agent skills (a third "procedural memory" layer) and keeps them up to date in the background. See [Skills from Memory](#skills-from-memory). - **Advanced memory maintenance** — optional background tasks keep durable `PROJECT.md` and `USER.md` notes current across sessions. See [Advanced Memory Maintenance](#advanced-memory-maintenance). ---

## ✨ Key Features

- **DeepSeek Harness support** — MemSearch now brings automatic capture, pre-step memory injection, native skill-based recall, background maintenance, and a read-
- **Skills from memory** — MemSearch now distills the workflows you repeat into reusable, installable agent skills (a third "procedural memory" layer) and keeps t
- **Advanced memory maintenance** — optional background tasks keep durable `PROJECT.md` and `USER.md` notes current across sessions. See [Advanced Memory Maintena

## 📦 Install

```bash
# Install
git clone --depth 1 https://github.com/zilliztech/memsearch.git
bash memsearch/plugins/codex/scripts/install.sh
codex --yolo  # needed for ONNX model network access
```

## 🚀 Quick Start

```bash
ls .memsearch/memory/
```

## 📚 Learn more

**Install**

git clone --depth 1 https://github.com/zilliztech/memsearch.git bash memsearch/plugins/codex/scripts/install.sh codex --yolo # needed for ONNX model network access After installing, chat as usual. Hooks capture and summarize each turn. **Verify it's working:** ls .memsearch/memory/ **Recall memories** — use the skill: $memory-recall what did we discuss about deployment? > 📖 [Codex Plugin docs](htt

**Install the published plugin into your DSH profile**

uv tool install "memsearch[onnx]" dsh plugin --profile web add @zilliz/memsearch-dsh

**Install from ClawHub**

openclaw plugins install --force clawhub:memsearch openclaw config set plugins.entries.memsearch.hooks.allowConversationAccess true openclaw config set plugins.entries.memsearch.hooks.allowPromptInjection true openclaw gateway restart After installing, chat in TUI as usual. The plugin captures each turn automatically. **Verify it's working** — memory files are stored in your agent's workspace:

**🏗️ Architecture Overview**

┌──────────────────────────────────────────────────────────────┐ │ 🧑‍💻 For Agent Users (Plugins) │ │ Claude Code · Codex · DSH · OpenClaw · OpenCode · Your App │ │ │ │ ├────────────────────────────┬─────────────────────────────────┤ │ 🛠️ For Agent Developers │ Build your own with ↓ │ │ ┌─────────────────────────┴──────────────────────────────┐ │ │ │ memsearch CLI / Python API │ │ │ │ index · searc

## 🔗 Links

- [GitHub Repository](https://github.com/zilliztech/memsearch)
- [Full README](https://github.com/zilliztech/memsearch#readme)
- [Back to the Plugins list](../plugins.md)
