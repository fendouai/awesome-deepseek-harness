---
title: "deepseek-harness-remote"
description: "基于 DeepSeek Harness 插件机制的多端远程访问方案，让桌面端与 Android 端安全连接并操作远程 Harness。（A multi-device remote access solution built on the DeepSeek Harness plugin system, enabling desktop and Android clients to securely connect to and operate a remote Harness.）"
keywords: "deepseek-harness-remote, mobile, client, coding, desktop, ui, deepseek harness, dsh"
---
# deepseek-harness-remote

> ⭐ **124** · ✅ 活跃 · 客户端

| | | | |
|---|---|---|---|
| 类型 | 客户端 | 分类 | 移动端 |
| 星数 | ⭐ 124 | 状态 | ✅ 活跃 |
| 作者 | [liguobao](https://github.com/liguobao) | 更新时间 | — |

## 一句话介绍

> 基于 DeepSeek Harness 插件机制的多端远程访问方案，让桌面端与 Android 端安全连接并操作远程 Harness。（A multi-device remote access solution built on the DeepSeek Harness plugin system, enabling desktop and Android clients to securely connect to and operate a remote Harness.）

## 详细介绍

Continue using your DeepSeek Harness instance from a phone, computer, or browser. Return to the same Harness session from whichever device is with you. Harness keeps running on your work computer, with the same workspaces, tools, and project setup. Remote is simply another window into that environment.

## ✨ 核心特性

- Continue active sessions and review their latest progress from another device
- Send new instructions, change direction, and use image prompts with Harness `dsh-v0.1.1-rc.2` or `dsh-v0.1.2-alpha.1`–`rc.1`
- Answer questions and permission requests from clients with live conversation controls
- Open workspaces from another authorized computer on the same account
- Reuse the native Harness interface instead of maintaining a separate desktop conversation UI
- Preview remote files between two Harness installations with the optional `dsh-file-viewer` plugin
- Run a terminal-only [dsh-TUI](https://github.com/ccch1mneyyy/dsh-TUI) profile as a Host and authorize it with a GitHub or Zhihu QR code
- The Harness Host does not need a public listening port. Connect securely from anywhere with internet access over a bidirectional end-to-end encrypted channel

## 📦 安装

```bash
dsh plugin --profile web add ds-harness-remote@0.4.7
```

## 🚀 快速开始

```bash
dsh plugin --profile dsh-tui add ds-harness-remote@0.4.7
```

## 📚 更多信息

**Path B: Existing DSH installation**

Add the exact package version through DSH's plugin manager for the `web` profile: dsh plugin --profile web add ds-harness-remote@0.4.7 Restart Harness after installation. Do not install this package directly with npm. Only `dsh plugin` updates the selected profile and adds the bundle's configuration layer.

**Quick start**

1. Open **Remote** from the Harness sidebar. 2. Sign in with a GitHub or Zhihu QR code, or use your account and password. New password accounts can register through [Remote Web](https://dsh.r2049.cn/app/register); the site shows the current invitation requirements. 3. Enable remote control for the current computer. 4. On another device, open DSH Desktop, Remote Web, or the Android client and sign 

## 🔗 链接

- [GitHub 仓库](https://github.com/liguobao/deepseek-harness-remote)
- [完整 README](https://github.com/liguobao/deepseek-harness-remote#readme)
- [返回deepseek-harness-remote所在分类](../clients.md)
