---
title: "deepseek-harness-desktop (steven-kid)"
description: "Minimal cross-platform desktop wrapper: no config, out of the box."
keywords: "deepseek-harness-desktop (steven-kid), desktop, client, deepseek harness, dsh"
---
# deepseek-harness-desktop (steven-kid)

> ⭐ **157** · ✅ active · client · ⬆️ +2 recently

| | | | |
|---|---|---|---|
| Type | client | Category | Desktop |
| Stars | ⭐ 157 | Status | ✅ active |
| Author | [steven-kid](https://github.com/steven-kid) | Updated | 2026-08-16 |

## One-liner

> Minimal cross-platform desktop wrapper: no config, out of the box.

## About

All current and historical packages are available on the [GitHub Releases page](https://github.com/agent-earth/deepseek-harness-desktop/releases), and you can also download from the Quark Drive mirror: [Quark Drive - DeepSeek Harness Desktop v0.3.1](https://pan.quark.cn/s/e2dfc232c52d)

## ✨ Key Features

- Opens the official Harness interface as soon as the local service is ready
- Shows a lightweight loading screen while the local Harness service starts
- Includes **Settings → Plugin Market**, powered by [dsh-market](https://github.com/dsh-market/dsh-market) and the curated [awesome-dsh-plugin](https://github.com
- Bundles pnpm so catalog plugins can be installed, updated, and removed without a separate Node.js toolchain
- Keeps running in the system tray when the main window is closed
- Opens the active local Harness URL in the system browser from the tray menu
- Preserves the complete settings, models, sessions, plugins, and agent experience
- Gracefully terminates the Harness child process on application exit

## 🚀 Quick Start

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

## 📚 Learn more

**Runtime architecture**

DeepSeek Harness Desktop ├── Electron Main │ ├── Single-instance window │ ├── Harness child-process lifecycle │ ├── Random loopback port and readiness checks │ └── Platform menu and external-link handling │ ├── Harness Child Process │ └── @deepseek-ai/dsh web │ └── http://127.0.0.1:<random-port> │ └── Sandboxed BrowserWindow └── DeepSeek Harness Web UI

## 🔗 Links

- [GitHub Repository](https://github.com/steven-kid/deepseek-harness-desktop)
- [Full README](https://github.com/steven-kid/deepseek-harness-desktop#readme)
- [Back to the Clients (Desktop & TUI) list](../clients.md)
