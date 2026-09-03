---
title: "dsh-desktop (DataElement)"
description: "Desktop app for DeepSeek Harness."
keywords: "dsh-desktop (DataElement), desktop, client, deepseek harness, dsh"
---
# dsh-desktop (DataElement)

> ⭐ **1,511** · ✅ active · client · ⬆️ +233 recently

| | | | |
|---|---|---|---|
| Type | client | Category | Desktop |
| Stars | ⭐ 1,511 | Status | ✅ active |
| Author | [dataelement](https://github.com/dataelement) | Updated | 2026-08-21 |

## One-liner

> Desktop app for DeepSeek Harness.

## About

Download DSH Desktop for macOS and Windows from the [official website](https://www.dshdesktop.com/#download). Installed builds check for updates shortly after startup and every six hours. When a new version is available, DSH Desktop asks before downloading it; installation begins only after you choose **Restart and install**. You can also check manually from the application menu or skip one version without hiding future releases.

## ✨ Key Features

- Starts and stops Harness without requiring a separate CLI or browser tab
- Uses the native system directory picker to add and manage project workspaces
- Supports official DeepSeek models and mainstream third-party model providers
- Imports and exports complete custom Agent presets as portable [`.dshpreset` packages](docs/preset-packages.md), with conflict checks and a trust warning before 
- Preserves profiles, plugins, workspaces, sessions, and model settings across app upgrades
- Detects startup and frontend plugin failures, keeps diagnostics in `harness.log`, and offers guided recovery actions

## 🚀 Quick Start

```bash
open -a "DSH Desktop" --args --safe-mode
```

## 📚 Learn more

**Development and architecture**

Contributions are welcome. Start with the public engineering documentation: Before submitting a change, run `npm test`, `npm run typecheck`, and `npm run build`, then exercise the affected real application flow. Never include real API keys in issues, logs, screenshots, or test data.

## 🔗 Links

- [GitHub Repository](https://github.com/dataelement/dsh-desktop)
- [Full README](https://github.com/dataelement/dsh-desktop#readme)
- [Back to the Clients (Desktop & TUI) list](../clients.md)
