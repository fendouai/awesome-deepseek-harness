---
title: "dsh-chat-import"
description: "Import conversation history from Claude Code, Codex, ChatGPT, Cursor, Gemini, Reasonix and OpenCode into resumable DSH sessions."
keywords: "dsh-chat-import, developer, plugin, files, coding, deepseek harness, dsh"
---
# dsh-chat-import

> ⭐ **87** · ✅ active · plugin · ⬆️ +2 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 87 | Status | ✅ active |
| Author | [Nwflower](https://github.com/Nwflower) | Updated | 2026-08-21 |
| Subcategory | 📁 Files & import | Capabilities | files, coding |

## One-liner

> Import conversation history from Claude Code, Codex, ChatGPT, Cursor, Gemini, Reasonix and OpenCode into resumable DSH sessions.

## About

**A DeepSeek Harness plugin that imports conversation history from 17+ AI coding tools, so you can continue right where you left off.**

## 📦 Install

```bash
dsh plugin --profile web add dsh-chat-import                    # npm package
dsh plugin --profile web add -w link:/path/to/dsh-chat-import   # local checkout (symlink)
```

## 🚀 Quick Start

```bash
import_chat({ format: "claude", path: "~/.claude/projects" })
import_chat({ format: "chatgpt", path: "~/Downloads/chatgpt-export/conversations.json" })
import_chat({ format: "local-jsonl", path: "D:\downloads\session.jsonl" })
```

## 📚 Learn more

**Install**

dsh plugin --profile web add dsh-chat-import # npm package dsh plugin --profile web add -w link:/path/to/dsh-chat-import # local checkout (symlink)

**Usage**

1. **Import** — pick the conversations to import from the "Import sessions" panel in the bottom-right of the GUI and import with one click, or have your agent call the context tool: import_chat({ format: "claude", path: "~/.claude/projects" }) import_chat({ format: "chatgpt", path: "~/Downloads/chatgpt-export/conversations.json" }) import_chat({ format: "local-jsonl", path: "D:\downloads\session.j

**Companion tool: config migration**

Only need to migrate **configuration** (skills, hooks, global settings) rather than conversation history? [dsh-movein](https://github.com/sjh9714/dsh-movein) handles config migration and complements this plugin -- DSH Chat Import only handles conversation history, and each tool works standalone. Its first-migration guide ([中文](https://github.com/sjh9714/dsh-movein/blob/main/docs/first-migration.zh

## 🔗 Links

- [GitHub Repository](https://github.com/Nwflower/dsh-chat-import)
- [Full README](https://github.com/Nwflower/dsh-chat-import#readme)
- [Back to the Plugins list](../plugins.md)
