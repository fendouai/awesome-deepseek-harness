---
title: "deepseek-harness-desktop (salathleizhang)"
description: "Desktop wrapper for DeepSeek Harness."
keywords: "deepseek-harness-desktop (salathleizhang), desktop, client, deepseek harness, dsh"
---
# deepseek-harness-desktop (salathleizhang)

> ⭐ **138** · ✅ active · client · ⬆️ +3 recently

| | | | |
|---|---|---|---|
| Type | client | Category | Desktop |
| Stars | ⭐ 138 | Status | ✅ active |
| Author | [salathleizhang](https://github.com/salathleizhang) | Updated | 2026-08-19 |

## One-liner

> Desktop wrapper for DeepSeek Harness.

## About

A desktop shell for DeepSeek Harness: it runs the harness as a supervised child process and hosts the existing Web GUI unchanged. The shell is a thin layer: it spawns `dsh web`, waits for the readiness line, opens one `BrowserWindow` at the served loopback origin, and owns shutdown and crash-restart. The renderer is Chromium loading that origin, so `window.__DSH_BOOT__` injection and the `/api` transport behave exactly as under `dsh web`. No UI is reimplemented.

## ✨ Key Features

- Opens directly into the harness Web GUI, showing a connecting page until the child reports ready.
- Holds a single-instance lock; a second launch focuses the existing window.
- Restarts the harness on unexpected exit with exponential backoff.
- Stops the child gracefully on exit (SIGTERM, then SIGKILL after a timeout).
- Forwards `dsh://` deep links to the renderer.
- Listens only on a random `127.0.0.1` port (`--port 0` by default).
- Uses the DSH brand icon in the window, the macOS dock, and the packaged `.icns`/`.ico`.
- Lives in the system tray; closing the window hides to tray instead of quitting.

## 🚀 Quick Start

```bash
pnpm --filter @deepseek-ai/dsh-desktop dev
```

## 📚 Learn more

**Runtime architecture**

DSH Desktop (Electron main) ├── HarnessSupervisor — child lifecycle, readiness, logs, crash-restart ├── Single-instance lock and dsh:// deep-link forwarding └── Hardened BrowserWindow └── http://127.0.0.1:<random> DeepSeek Harness Web UI Electron resources (packaged) ├── runtime/<platform>-<arch>/ bundled Node v22.19.0 └── harness/ deployed @deepseek-ai/dsh closure

## 🔗 Links

- [GitHub Repository](https://github.com/salathleizhang/deepseek-harness-desktop)
- [Full README](https://github.com/salathleizhang/deepseek-harness-desktop#readme)
- [Back to the Clients (Desktop & TUI) list](../clients.md)
