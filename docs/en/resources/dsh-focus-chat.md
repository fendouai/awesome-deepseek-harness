---
title: "dsh-focus-chat"
description: "为 dsh 提供新的「聚焦会话」精简会话视图，更轻松易于阅读，只关注最终产出结果。"
keywords: "dsh-focus-chat, ui, plugin, coding, deepseek harness, dsh"
---
# dsh-focus-chat

> ⭐ **21** · ✅ active · plugin · ⬆️ +5 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 21 | Status | ✅ active |
| Author | [dingyi222666](https://github.com/dingyi222666) | Updated | 2026-08-20 |

## One-liner

> 为 dsh 提供新的「聚焦会话」精简会话视图，更轻松易于阅读，只关注最终产出结果。

## About

A plugin for the dsh web GUI that adds a **focus chat** tab — a condensed, Claude Code–style way to read a conversation.

## ✨ Key Features

- **No Inspect / details-panel deep links.** The chat's Inspect affordance needs internals plugins can't touch. The tool cards render the same content, just witho
- **Third-party tool-card extensions don't render here.** Cards that other plugins add to the chat view won't appear in the focus view; the built-in card renderer
- **Folding is per consecutive tool-run.** Any visible content between two runs (a reply, a command, your interjection) keeps them separate.
- **Inline file links need the optional file-mentions service** — the same off switch the chat view uses.
- **Remote fold lines lack a few window-only readings.** The turn navigator rail lists window turns only; remote turns render no produced-file list (the ui-delive

## 📦 Install

```bash
# Install from npm (requires dsh >= 0.1.2-alpha.2)
dsh plugin --profile web add @dingyi222666/dsh-focus-chat
# Restart dsh web; the tab mounts automatically
dsh web
```

## 📚 Learn more

**Screenshots**

Instead of watching every step live, one assistant turn collapses into a single summary line: > Thought for 36s, edited 8 files, read 17 files, listed 18 directories, ran 2 shell commands, loaded 3 context items A whole turn can fold further into one `Worked for Xm Ys` line — expanding it draws the full detail (tool cards, thinking, context, produced files, copy/fork) exactly like the chat rows; m

## 🔗 Links

- [GitHub Repository](https://github.com/dingyi222666/dsh-focus-chat)
- [Full README](https://github.com/dingyi222666/dsh-focus-chat#readme)
- [Back to the Plugins list](../plugins.md)
