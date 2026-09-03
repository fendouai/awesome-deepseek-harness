---
title: "dsh-web-restart"
description: "One-click restart button for the DeepSeek Harness Web UI: sidebar footer button, single click restarts the dsh web process. / DSH Web 界面一键重启按钮。"
keywords: "dsh-web-restart, search, plugin, coding, ui, deepseek harness, dsh"
---
# dsh-web-restart

> ⭐ **6** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 6 | Status | ✅ active |
| Author | [1123762794](https://github.com/1123762794) | Updated | — |
| Subcategory | 🌐 Web search | Capabilities | coding, ui |

## One-liner

> One-click restart button for the DeepSeek Harness Web UI: sidebar footer button, single click restarts the dsh web process. / DSH Web 界面一键重启按钮。

## About

One-click restart button for the **DeepSeek Harness Web UI**. Adds a small circular restart button (↻) to the sidebar footer, next to Settings. A **single click** immediately restarts the `dsh web` process — the page disconnects for ~15–20 seconds, then you refresh and everything is back (sessions are persisted on disk and recover automatically). The button is **persistent**: it survives the restart it triggers.

## ✨ Key Features

- Single-click restart — no confirmation step, no double-click dance.
- Persistent: survives the DSH restart it triggers (installed as a bundle-layer plugin, not a dynamic session plugin).
- Small footprint: sits beside the Settings trigger in the sidebar footer; icon-only in the 56px rail, icon + label in the wide sidebar.
- In-flight feedback: the button turns red and shows "重启中…" → "已触发" while the request is being processed.
- Re-entry guard: a second click while a restart is already in flight is rejected.
- Online status dot: the button also shows DSH liveness — a green dot polls `GET /dsh-health` every 5s (red when the harness is unreachable/restarting).

## 📦 Install

```bash
dsh plugin --profile web add github:YOUR_OWNER/dsh-web-restart
```

## 🚀 Quick Start

```bash
// ~/.dsh/profiles/web/package.json
{
  "dependencies": {
    "dsh-web-restart": "github:YOUR_OWNER/dsh-web-restart"
  }
}
```

## 🔗 Links

- [GitHub Repository](https://github.com/1123762794/dsh-web-restart)
- [Full README](https://github.com/1123762794/dsh-web-restart#readme)
- [Back to the Plugins list](../plugins.md)
