---
title: "dsh-web-ui-notify"
description: "为 DSH 增加桌面通知提醒。"
keywords: "dsh-web-ui-notify, notifications, plugin, deepseek harness, dsh"
---
# dsh-web-ui-notify

> ⭐ **21** · ✅ 活跃 · 插件 · 近期 ⬆️ +2

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 通知 |
| 星数 | ⭐ 21 | 状态 | ✅ 活跃 |
| 作者 | [bill9109](https://github.com/bill9109) | 更新时间 | 2026-08-14 |

## 一句话介绍

> 为 DSH 增加桌面通知提醒。

## 详细介绍

**Install:** `dsh plugin --profile web add github:omdsh-dev/dsh-web-ui-notify` **A DeepSeek Harness Web UI client plugin: when a tool needs approval, DSH asks you a question, or a turn finishes while you are looking at another tab, it pops a system desktop notification — so neither DSH nor you end up waiting.** [English](README.md) | [中文](README.zh.md)

## ✨ 核心特性

- **Notify on interaction with the current session**: tool approvals and DSH questions carry context in the body (approvals show the over-permission reason, quest
- **Notify on background sessions too**: sessions you are not looking at also notify when they need approval or a question (same contextual body as the current se
- **Notify on turn completion**: every finished turn of the current session notifies, with the first 80 characters of the final answer; tool-only turns without a 
- **Session name in the title**: every notification title names its session, e.g. "Refactor database · needs approval"
- **Click to jump to the session**: clicking a notification not only returns to the DSH page but also opens that session
- Notifies only while you are away from the tab; when the page is in the foreground DSH already shows its own prompts, so it does not double-notify
- Each event notifies once — reconnects do not repeat it, and opening a session with history does not replay old turns
- Notifications do not auto-dismiss after a few seconds; they wait for you

## 📦 安装

```bash
dsh plugin --profile web add github:omdsh-dev/dsh-web-ui-notify
```

## 🚀 快速开始

```bash
dsh plugin --profile web add /path/to/dsh-web-ui-notify
```

## 📚 更多信息

**Install**

The plugin is a DSH **bundle** (`package.json` declares `dsh.bundle` + `dsh.client`). Install it into the `web` profile with the standard `dsh plugin` mechanism — **no DSH source changes and no hand-written patch**: dsh plugin --profile web add github:omdsh-dev/dsh-web-ui-notify Internally the command runs `pnpm add <spec>` in the profile directory and automatically appends packages that declare `

**Uninstall**

dsh plugin --profile web remove dsh-web-ui-notify The command runs `pnpm remove <pkg>` in the profile directory and removes it from `dsh.profile.bundles`. After uninstalling, restart web and hard-refresh the browser.

**Usage**

After installation you must also grant browser notification permission, otherwise the plugin stays silent — without permission the browser simply blocks notifications. 1. Open **Settings → General → Desktop notifications** and click **Enable** 2. When the browser asks, choose Allow; the status becomes "Enabled" 3. On macOS, also allow your browser under **System Settings → Notifications** Then swi

## 🔗 链接

- [GitHub 仓库](https://github.com/bill9109/dsh-web-ui-notify)
- [完整 README](https://github.com/bill9109/dsh-web-ui-notify#readme)
- [返回dsh-web-ui-notify所在分类](../plugins.md)
