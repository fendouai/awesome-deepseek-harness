---
title: "dsh-desktop-electron"
description: "Cross-platform Electron shell for the DSH Web GUI: tray-resident standalone window."
keywords: "dsh-desktop-electron, desktop, client, deepseek harness, dsh"
---
# dsh-desktop-electron

> ⭐ **5** · ✅ active · client · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | client | Category | Desktop |
| Stars | ⭐ 5 | Status | ✅ active |
| Author | [Void0312Aurora](https://github.com/Void0312Aurora) | Updated | 2026-08-15 |

## One-liner

> Cross-platform Electron shell for the DSH Web GUI: tray-resident standalone window.

## About

An Electron desktop shell for the [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`) Web GUI: it spawns `dsh web`, waits for the server's readiness line, and hosts the GUI in a standalone window with tray residency. The shell targets the public [`@deepseek-ai/dsh`](https://www.npmjs.com/package/@deepseek-ai/dsh) package. It relies only on the maintained `dsh web --host --port ` arguments and the `dsh web: ` readiness line.

## 📦 Install

```bash
npm install
DSH_HOME=~/.dsh/source/current npm run dev
```

## 🚀 Quick Start

```bash
npm run dist        # installers under release/
npm run dist:dir    # unpacked dir only, for a quick smoke
```

## 🔗 Links

- [GitHub Repository](https://github.com/Void0312Aurora/dsh-desktop-electron)
- [Full README](https://github.com/Void0312Aurora/dsh-desktop-electron#readme)
- [Back to the Clients (Desktop & TUI) list](../clients.md)
