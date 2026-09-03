---
title: "deepseek-harness-desktop (hongfeiyucode)"
description: "Desktop wrapper for DeepSeek Harness."
keywords: "deepseek-harness-desktop (hongfeiyucode), desktop, client, deepseek harness, dsh"
---
# deepseek-harness-desktop (hongfeiyucode)

> ⭐ **37** · ✅ active · client

| | | | |
|---|---|---|---|
| Type | client | Category | Desktop |
| Stars | ⭐ 37 | Status | ✅ active |
| Author | [hongfeiyucode](https://github.com/hongfeiyucode) | Updated | 2026-08-18 |

## One-liner

> Desktop wrapper for DeepSeek Harness.

## About

**DeepSeek Harness Desktop** 是 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 的桌面客户端：不需要终端、不需要安装 Node.js、也不需要 `dsh web` 命令。双击图标，完整的 DeepSeek Harness 网页版界面就会在自己的窗口里打开。 **DeepSeek Harness Desktop** is the desktop client of [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness): no terminal, no Node.js installation, no `dsh web` command. Double-click the icon and the full DeepSeek Harness web GUI opens in its own window.

## 📦 Install

```bash
git clone https://github.com/hongfeiyucode/deepseek-harness-desktop.git
cd deepseek-harness-desktop
npm install
npm start          # 启动应用（Electron + 内嵌引擎）
```

## 🚀 Quick Start

```bash
# PowerShell
$env:ELECTRON_MIRROR="https://npmmirror.com/mirrors/electron/"
$env:ELECTRON_BUILDER_BINARIES_MIRROR="https://npmmirror.com/mirrors/electron-builder-binaries/"

# bash
export ELECTRON_MIRROR=https://npmmirror.com/mirrors/electron/
export ELECTRON_BUILDER_BINARIES_MIRROR=https://npmmirror.com/mirrors/electron-builder-binaries/
```

## 📚 Learn more

**工作原理——用 deepseek-harness 自举**

桌面客户端**不重新实现任何 harness 功能**，它在两个层面上由 deepseek-harness 自举： **运行时自举。** 应用打包了 npm 上的 `@deepseek-ai/dsh` 发行包（一个完全自包含的分发：CLI 入口、全部 `@deepseek-ai/*` 插件以及构建好的网页前端）。启动时，桌面外壳用 Electron 自带的 Node.js 24 运行时（`ELECTRON_RUN_AS_NODE=1`）把 `dsh web` 作为子进程拉起——用户无需安装任何 Node——然后等待它在回环地址上提供服务，窗口再加载 `http://127.0.0.1:<端口>` 上的上游界面。harness 的所有功能、插件、预设和会话都原封不动，因为它本身就是那个正在运行的 harness。没有一行复刻的界面代码。有一个 Electron 特有的细节：web 配置档的热

## 🔗 Links

- [GitHub Repository](https://github.com/hongfeiyucode/deepseek-harness-desktop)
- [Full README](https://github.com/hongfeiyucode/deepseek-harness-desktop#readme)
- [Back to the Clients (Desktop & TUI) list](../clients.md)
