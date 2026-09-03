---
title: "memsearch"
description: "面向所有 AI Agent（如 Claude Code、Codex、DSH）的持久化统一记忆层，基于 Markdown 与 Milvus 构建。"
keywords: "memsearch, memory, plugin, deepseek harness, dsh"
---
# memsearch

> ⭐ **2,538** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 记忆与上下文 |
| 星数 | ⭐ 2,538 | 状态 | ✅ 活跃 |
| 作者 | [zilliztech](https://github.com/zilliztech) | 更新时间 | — |
| 子分类 | 🧠 记忆系统 | 能力 | memory |

## 一句话介绍

> 面向所有 AI Agent（如 Claude Code、Codex、DSH）的持久化统一记忆层，基于 Markdown 与 Milvus 构建。

## 详细介绍

- **DeepSeek Harness support** — MemSearch now brings automatic capture, pre-step memory injection, native skill-based recall, background maintenance, and a read-only memory browser to [DeepSeek Harness (DSH)](https://zilliztech.github.io/memsearch/platforms/dsh/). - **Skills from memory** — MemSearch now distills the workflows you repeat into reusable, installable agent skills (a third "procedural memory" layer) and keeps them up to date in the background. See [Skills from Memory](#skills-from-memory). - **Advanced memory maintenance** — optional background tasks keep durable `PROJECT.md` and `USER.md` notes current across sessions. See [Advanced Memory Maintenance](#advanced-memory-maintenance). ---

## ✨ 核心特性

- **DeepSeek Harness support** — MemSearch now brings automatic capture, pre-step memory injection, native skill-based recall, background maintenance, and a read-
- **Skills from memory** — MemSearch now distills the workflows you repeat into reusable, installable agent skills (a third "procedural memory" layer) and keeps t
- **Advanced memory maintenance** — optional background tasks keep durable `PROJECT.md` and `USER.md` notes current across sessions. See [Advanced Memory Maintena

## 📦 安装

```bash
# Install
git clone --depth 1 https://github.com/zilliztech/memsearch.git
bash memsearch/plugins/codex/scripts/install.sh
codex --yolo  # needed for ONNX model network access
```

## 🚀 快速开始

```bash
ls .memsearch/memory/
```

## 📚 更多信息

**Install**

git clone --depth 1 https://github.com/zilliztech/memsearch.git bash memsearch/plugins/codex/scripts/install.sh codex --yolo # needed for ONNX model network access After installing, chat as usual. Hooks capture and summarize each turn. **Verify it's working:** ls .memsearch/memory/ **Recall memories** — use the skill: $memory-recall what did we discuss about deployment? > 📖 [Codex Plugin docs](htt

**Install the published plugin into your DSH profile**

uv tool install "memsearch[onnx]" dsh plugin --profile web add @zilliz/memsearch-dsh

**Install from ClawHub**

openclaw plugins install --force clawhub:memsearch openclaw config set plugins.entries.memsearch.hooks.allowConversationAccess true openclaw config set plugins.entries.memsearch.hooks.allowPromptInjection true openclaw gateway restart After installing, chat in TUI as usual. The plugin captures each turn automatically. **Verify it's working** — memory files are stored in your agent's workspace:

**🏗️ Architecture Overview**

┌──────────────────────────────────────────────────────────────┐ │ 🧑‍💻 For Agent Users (Plugins) │ │ Claude Code · Codex · DSH · OpenClaw · OpenCode · Your App │ │ │ │ ├────────────────────────────┬─────────────────────────────────┤ │ 🛠️ For Agent Developers │ Build your own with ↓ │ │ ┌─────────────────────────┴──────────────────────────────┐ │ │ │ memsearch CLI / Python API │ │ │ │ index · searc

## 🔗 链接

- [GitHub 仓库](https://github.com/zilliztech/memsearch)
- [完整 README](https://github.com/zilliztech/memsearch#readme)
- [返回memsearch所在分类](../plugins.md)
