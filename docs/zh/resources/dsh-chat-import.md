---
title: "dsh-chat-import"
description: "从 Claude Code、Codex、ChatGPT、Cursor、Gemini、Reasonix、OpenCode 导入历史消息并在 DSH 中继续对话。"
keywords: "dsh-chat-import, developer, plugin, files, coding, deepseek harness, dsh"
---
# dsh-chat-import

> ⭐ **87** · ✅ 活跃 · 插件 · 近期 ⬆️ +2

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 87 | 状态 | ✅ 活跃 |
| 作者 | [Nwflower](https://github.com/Nwflower) | 更新时间 | 2026-08-21 |
| 子分类 | 📁 文件与导入 | 能力 | files, coding |

## 一句话介绍

> 从 Claude Code、Codex、ChatGPT、Cursor、Gemini、Reasonix、OpenCode 导入历史消息并在 DSH 中继续对话。

## 详细介绍

**A DeepSeek Harness plugin that imports conversation history from 17+ AI coding tools, so you can continue right where you left off.**

## 📦 安装

```bash
dsh plugin --profile web add dsh-chat-import                    # npm package
dsh plugin --profile web add -w link:/path/to/dsh-chat-import   # local checkout (symlink)
```

## 🚀 快速开始

```bash
import_chat({ format: "claude", path: "~/.claude/projects" })
import_chat({ format: "chatgpt", path: "~/Downloads/chatgpt-export/conversations.json" })
import_chat({ format: "local-jsonl", path: "D:\downloads\session.jsonl" })
```

## 📚 更多信息

**Install**

dsh plugin --profile web add dsh-chat-import # npm package dsh plugin --profile web add -w link:/path/to/dsh-chat-import # local checkout (symlink)

**Usage**

1. **Import** — pick the conversations to import from the "Import sessions" panel in the bottom-right of the GUI and import with one click, or have your agent call the context tool: import_chat({ format: "claude", path: "~/.claude/projects" }) import_chat({ format: "chatgpt", path: "~/Downloads/chatgpt-export/conversations.json" }) import_chat({ format: "local-jsonl", path: "D:\downloads\session.j

**Companion tool: config migration**

Only need to migrate **configuration** (skills, hooks, global settings) rather than conversation history? [dsh-movein](https://github.com/sjh9714/dsh-movein) handles config migration and complements this plugin -- DSH Chat Import only handles conversation history, and each tool works standalone. Its first-migration guide ([中文](https://github.com/sjh9714/dsh-movein/blob/main/docs/first-migration.zh

## 🔗 链接

- [GitHub 仓库](https://github.com/Nwflower/dsh-chat-import)
- [完整 README](https://github.com/Nwflower/dsh-chat-import#readme)
- [返回dsh-chat-import所在分类](../plugins.md)
