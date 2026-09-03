---
title: "deepseek-harness-desktop (steven-kid)"
description: "极简跨平台桌面端：免配置，开箱即用。"
keywords: "deepseek-harness-desktop (steven-kid), desktop, client, deepseek harness, dsh"
---
# deepseek-harness-desktop (steven-kid)

> ⭐ **157** · ✅ 活跃 · 客户端 · 近期 ⬆️ +2

| | | | |
|---|---|---|---|
| 类型 | 客户端 | 分类 | 桌面端 |
| 星数 | ⭐ 157 | 状态 | ✅ 活跃 |
| 作者 | [steven-kid](https://github.com/steven-kid) | 更新时间 | 2026-08-16 |

## 一句话介绍

> 极简跨平台桌面端：免配置，开箱即用。

## 详细介绍

All current and historical packages are available on the [GitHub Releases page](https://github.com/agent-earth/deepseek-harness-desktop/releases), and you can also download from the Quark Drive mirror: [Quark Drive - DeepSeek Harness Desktop v0.3.1](https://pan.quark.cn/s/e2dfc232c52d)

## ✨ 核心特性

- Opens the official Harness interface as soon as the local service is ready
- Shows a lightweight loading screen while the local Harness service starts
- Includes **Settings → Plugin Market**, powered by [dsh-market](https://github.com/dsh-market/dsh-market) and the curated [awesome-dsh-plugin](https://github.com
- Bundles pnpm so catalog plugins can be installed, updated, and removed without a separate Node.js toolchain
- Keeps running in the system tray when the main window is closed
- Opens the active local Harness URL in the system browser from the tray menu
- Preserves the complete settings, models, sessions, plugins, and agent experience
- Gracefully terminates the Harness child process on application exit

## 🚀 快速开始

```bash
DeepSeek Harness Desktop
├── Electron Main
│   ├── Single-instance window
│   ├── Harness child-process lifecycle
│   ├── Random loopback port and readiness checks
│   └── Platform menu and external-link handling
│
├── Harness Child Process
│   └── @deepseek-ai/dsh web
│       └── http://127.0.0.1:<random-port>
│
└── Sandboxed BrowserWindow
    └── DeepSeek Harness Web UI
```

## 📚 更多信息

**Runtime architecture**

DeepSeek Harness Desktop ├── Electron Main │ ├── Single-instance window │ ├── Harness child-process lifecycle │ ├── Random loopback port and readiness checks │ └── Platform menu and external-link handling │ ├── Harness Child Process │ └── @deepseek-ai/dsh web │ └── http://127.0.0.1:<random-port> │ └── Sandboxed BrowserWindow └── DeepSeek Harness Web UI

## 🔗 链接

- [GitHub 仓库](https://github.com/steven-kid/deepseek-harness-desktop)
- [完整 README](https://github.com/steven-kid/deepseek-harness-desktop#readme)
- [返回deepseek-harness-desktop (steven-kid)所在分类](../clients.md)
