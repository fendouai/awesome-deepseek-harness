---
title: "dsh-session-notification"
description: "提供会话完成等四种状态的通知响应，支持浏览器提示和提示词"
keywords: "dsh-session-notification, notifications, plugin, coding, deepseek harness, dsh"
---
# dsh-session-notification

> ⭐ **16** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Notifications |
| Stars | ⭐ 16 | Status | ✅ active |
| Author | [dingyi222666](https://github.com/dingyi222666) | Updated | — |

## One-liner

> 提供会话完成等四种状态的通知响应，支持浏览器提示和提示词

## About

A notification plugin for the dsh web GUI. When a session finishes, hits an error, asks you a question, or needs your permission, you get a heads-up: a sound plays, and when you step away from the tab a system notification keeps you in the loop.

## 📦 Install

```bash
# Install from npm (requires dsh >= 0.1.2-alpha.5)
dsh plugin --profile web add @dingyi222666/dsh-session-notification
# Restart dsh web for it to take effect
dsh web
```

## 📚 Learn more

**The Notifications settings section**

The plugin registers a **Notifications** section in the settings panel (Settings ⚙ → Notifications): Preferences are stored **browser-locally** (localStorage) under the `dsh-session-notification` key — no host settings-namespace exposure required — so they persist across sessions and sync across tabs, and never depend on a harness change.

## 🔗 Links

- [GitHub Repository](https://github.com/dingyi222666/dsh-session-notification)
- [Full README](https://github.com/dingyi222666/dsh-session-notification#readme)
- [Back to the Plugins list](../plugins.md)
