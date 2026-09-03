---
title: "dsh-notification"
description: "回合完成桌面通知，按结果分控 + 关键词包含/排除过滤。"
keywords: "dsh-notification, notifications, plugin, deepseek harness, dsh"
---
# dsh-notification

> ⭐ **70** · ✅ 活跃 · 插件 · 近期 ⬆️ +2

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 通知 |
| 星数 | ⭐ 70 | 状态 | ✅ 活跃 |
| 作者 | [omdsh-dev](https://github.com/omdsh-dev) | 更新时间 | 2026-08-19 |

## 一句话介绍

> 回合完成桌面通知，按结果分控 + 关键词包含/排除过滤。

## 详细介绍

Desktop notifications for the DeepSeek Harness web GUI. When a session finishes a turn, the browser shows a system notification (via the `Notification` API), so you can switch tabs and still know when DSH is done. Per-outcome toggles and include/exclude keyword rules control exactly which completions notify. No harness change is needed: the host contributes a session projection (a bounded summary of each session's last completed turn), and the client watches the session list's completion reminder and applies its own persisted preferences. host: notification projection (last turn's reason/text/tools) --session/projection--> browser client: session list completion reminder (live, dedup) + persisted settings -> permission + current-session visibility gate -> new Notification("DSH finished", {

## 📦 安装

```bash
dsh plugin --profile web add https://github.com/omdsh-dev/dsh-notification/archive/refs/tags/v0.1.4.tar.gz
```

## 🚀 快速开始

```bash
- id: dsh-notification
  name: dsh-notification
  config:
    maxBodyChars: 400      # projection body budget; longer replies are ellipsized host-side
```

## 📚 更多信息

**Install**

dsh plugin --profile web add https://github.com/omdsh-dev/dsh-notification/archive/refs/tags/v0.1.4.tar.gz Restart the web server so the host half and the served client bundle pick up the plugin. The default `dsh web` profile has the required client composition (the session list, the settings shell, and locale). Version `0.1.4` supports both the 0.1.1 and 0.1.2 Harness client package layouts and p

**Settings**

Preferences persist in the browser (localStorage). The section also grants browser permission and sends a test notification.

**Configuration**

Host-side tunables live on the plugin row in `cordis.yml`: name: dsh-notification config: maxBodyChars: 400 # projection body budget; longer replies are ellipsized host-side

## 🔗 链接

- [GitHub 仓库](https://github.com/omdsh-dev/dsh-notification)
- [完整 README](https://github.com/omdsh-dev/dsh-notification#readme)
- [返回dsh-notification所在分类](../plugins.md)
