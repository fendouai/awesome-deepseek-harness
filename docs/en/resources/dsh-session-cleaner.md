---
title: "dsh-session-cleaner"
description: "为 DeepSeek Harness 提供会话删除能力，支持侧边栏 ⋮ 菜单入口"
keywords: "dsh-session-cleaner, discovery, plugin, coding, deepseek harness, dsh"
---
# dsh-session-cleaner

> ⭐ **5** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Plugin discovery |
| Stars | ⭐ 5 | Status | ✅ active |
| Author | [fountunt](https://github.com/fountunt) | Updated | 2026-08-15 |

## One-liner

> 为 DeepSeek Harness 提供会话删除能力，支持侧边栏 ⋮ 菜单入口

## About

[English](README.md) | [中文](README.zh.md) Delete DeepSeek Harness sessions from a **running** web runtime — files, live store, and workspace records — without restarting `dsh web`. The official web API only offers `workspace.archiveSession` (hide); there is no `session.delete`. This bundle closes that gap.

## 📦 Install

```bash
dsh plugin --profile web add dsh-session-cleaner            # from npm
dsh plugin --profile web add github:fountunt/dsh-session-cleaner   # from git

# or from a local checkout
dsh plugin --profile web add file:/path/to/dsh-session-cleaner
```

## 🚀 Quick Start

```bash
POST /api-ext/session.delete
Content-Type: application/json

{ "sessionId": "session-1bb8d361-ea6b-4b92-bab2-c858c92e8822" }
```

## 📚 Learn more

**Install**

dsh plugin --profile web add dsh-session-cleaner # from npm dsh plugin --profile web add github:fountunt/dsh-session-cleaner # from git

## 🔗 Links

- [GitHub Repository](https://github.com/fountunt/dsh-session-cleaner)
- [Full README](https://github.com/fountunt/dsh-session-cleaner#readme)
- [Back to the Plugins list](../plugins.md)
