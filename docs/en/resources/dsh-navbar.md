---
title: "dsh-navbar"
description: "DSH 插件：对话节点导航条（右缘节点串快速跳转 user 消息）。官方 bundle 插件，dsh plugin --profile web add 安装"
keywords: "dsh-navbar, ui, plugin, coding, deepseek harness, dsh"
---
# dsh-navbar

> ⭐ **52** · ✅ active · plugin · ⬆️ +2 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 52 | Status | ✅ active |
| Author | [vlln](https://github.com/vlln) | Updated | 2026-08-20 |
| Subcategory | 🧭 Navigation | Capabilities | coding |

## One-liner

> DSH 插件：对话节点导航条（右缘节点串快速跳转 user 消息）。官方 bundle 插件，dsh plugin --profile web add 安装

## About

Zero data-channel dependencies: driven only by official anchor attributes (`data-time-hover-root`, on user rows since 0806) — no polling, no routing, no tools.

## 📦 Install

```bash
dsh plugin --profile web add "github:vlln/dsh-navbar#main"   # one-line git-source install (build artifacts committed)
# or npm source: dsh plugin --profile web add @vlln/dsh-navbar@0.4.0
```

## 🚀 Quick Start

```bash
pnpm install
pnpm run build      # tsdown: client bundle (lib/client.js)
```

## 📚 Learn more

**Installation**

**Recommended: one-line install from git source** (build artifacts are committed, so git source does not trigger a build): dsh plugin --profile web add "github:vlln/dsh-navbar#main" # one-line git-source install (build artifacts committed)

**Usage**

Works out of the box — no commands, no tools. The node rail appears on the right edge of the conversation page (Chat view); hover for a preview, click to jump. Animations are disabled under `prefers-reduced-motion`. **Pin**: hover an assistant message's action bar and click 📌 to pin that reply — the corresponding turn's navigation node becomes a golden slim elliptical disc (click to jump straight 

## 🔗 Links

- [GitHub Repository](https://github.com/vlln/dsh-navbar)
- [Full README](https://github.com/vlln/dsh-navbar#readme)
- [Back to the Plugins list](../plugins.md)
