---
title: "dsh-session-notification"
description: "提供会话完成等四种状态的通知响应，支持浏览器提示和提示词"
keywords: "dsh-session-notification, notifications, plugin, coding, deepseek harness, dsh"
---
# dsh-session-notification

> ⭐ **16** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 通知 |
| 星数 | ⭐ 16 | 状态 | ✅ 活跃 |
| 作者 | [dingyi222666](https://github.com/dingyi222666) | 更新时间 | — |

## 一句话介绍

> 提供会话完成等四种状态的通知响应，支持浏览器提示和提示词

## 详细介绍

A notification plugin for the dsh web GUI. When a session finishes, hits an error, asks you a question, or needs your permission, you get a heads-up: a sound plays, and when you step away from the tab a system notification keeps you in the loop.

## 📦 安装

```bash
# Install from npm (requires dsh >= 0.1.2-alpha.5)
dsh plugin --profile web add @dingyi222666/dsh-session-notification
# Restart dsh web for it to take effect
dsh web
```

## 📚 更多信息

**The Notifications settings section**

The plugin registers a **Notifications** section in the settings panel (Settings ⚙ → Notifications): Preferences are stored **browser-locally** (localStorage) under the `dsh-session-notification` key — no host settings-namespace exposure required — so they persist across sessions and sync across tabs, and never depend on a harness change.

## 🔗 链接

- [GitHub 仓库](https://github.com/dingyi222666/dsh-session-notification)
- [完整 README](https://github.com/dingyi222666/dsh-session-notification#readme)
- [返回dsh-session-notification所在分类](../plugins.md)
