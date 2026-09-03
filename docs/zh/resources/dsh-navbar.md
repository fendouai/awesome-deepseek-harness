---
title: "dsh-navbar"
description: "DSH 插件：对话节点导航条（右缘节点串快速跳转 user 消息）。官方 bundle 插件，dsh plugin --profile web add 安装"
keywords: "dsh-navbar, ui, plugin, coding, deepseek harness, dsh"
---
# dsh-navbar

> ⭐ **52** · ✅ 活跃 · 插件 · 近期 ⬆️ +2

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 52 | 状态 | ✅ 活跃 |
| 作者 | [vlln](https://github.com/vlln) | 更新时间 | 2026-08-20 |
| 子分类 | 🧭 导航与跳转 | 能力 | coding |

## 一句话介绍

> DSH 插件：对话节点导航条（右缘节点串快速跳转 user 消息）。官方 bundle 插件，dsh plugin --profile web add 安装

## 详细介绍

Zero data-channel dependencies: driven only by official anchor attributes (`data-time-hover-root`, on user rows since 0806) — no polling, no routing, no tools.

## 📦 安装

```bash
dsh plugin --profile web add "github:vlln/dsh-navbar#main"   # one-line git-source install (build artifacts committed)
# or npm source: dsh plugin --profile web add @vlln/dsh-navbar@0.4.0
```

## 🚀 快速开始

```bash
pnpm install
pnpm run build      # tsdown: client bundle (lib/client.js)
```

## 📚 更多信息

**Installation**

**Recommended: one-line install from git source** (build artifacts are committed, so git source does not trigger a build): dsh plugin --profile web add "github:vlln/dsh-navbar#main" # one-line git-source install (build artifacts committed)

**Usage**

Works out of the box — no commands, no tools. The node rail appears on the right edge of the conversation page (Chat view); hover for a preview, click to jump. Animations are disabled under `prefers-reduced-motion`. **Pin**: hover an assistant message's action bar and click 📌 to pin that reply — the corresponding turn's navigation node becomes a golden slim elliptical disc (click to jump straight 

## 🔗 链接

- [GitHub 仓库](https://github.com/vlln/dsh-navbar)
- [完整 README](https://github.com/vlln/dsh-navbar#readme)
- [返回dsh-navbar所在分类](../plugins.md)
