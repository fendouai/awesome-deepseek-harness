---
title: "dsh-desktop (DataElement)"
description: "DeepSeek Harness 桌面应用。"
keywords: "dsh-desktop (DataElement), desktop, client, deepseek harness, dsh"
---
# dsh-desktop (DataElement)

> ⭐ **1,511** · ✅ 活跃 · 客户端 · 近期 ⬆️ +233

| | | | |
|---|---|---|---|
| 类型 | 客户端 | 分类 | 桌面端 |
| 星数 | ⭐ 1,511 | 状态 | ✅ 活跃 |
| 作者 | [dataelement](https://github.com/dataelement) | 更新时间 | 2026-08-21 |

## 一句话介绍

> DeepSeek Harness 桌面应用。

## 详细介绍

Download DSH Desktop for macOS and Windows from the [official website](https://www.dshdesktop.com/#download). Installed builds check for updates shortly after startup and every six hours. When a new version is available, DSH Desktop asks before downloading it; installation begins only after you choose **Restart and install**. You can also check manually from the application menu or skip one version without hiding future releases.

## ✨ 核心特性

- Starts and stops Harness without requiring a separate CLI or browser tab
- Uses the native system directory picker to add and manage project workspaces
- Supports official DeepSeek models and mainstream third-party model providers
- Imports and exports complete custom Agent presets as portable [`.dshpreset` packages](docs/preset-packages.md), with conflict checks and a trust warning before 
- Preserves profiles, plugins, workspaces, sessions, and model settings across app upgrades
- Detects startup and frontend plugin failures, keeps diagnostics in `harness.log`, and offers guided recovery actions

## 🚀 快速开始

```bash
open -a "DSH Desktop" --args --safe-mode
```

## 📚 更多信息

**Development and architecture**

Contributions are welcome. Start with the public engineering documentation: Before submitting a change, run `npm test`, `npm run typecheck`, and `npm run build`, then exercise the affected real application flow. Never include real API keys in issues, logs, screenshots, or test data.

## 🔗 链接

- [GitHub 仓库](https://github.com/dataelement/dsh-desktop)
- [完整 README](https://github.com/dataelement/dsh-desktop#readme)
- [返回dsh-desktop (DataElement)所在分类](../clients.md)
