---
title: "deepseek-harness-desktop"
description: "Unofficial in-process desktop app for DeepSeek Harness: the host composition boots inside the Electron main process with zero ports and an IPC bridge. Not affiliated with DeepSeek."
keywords: "deepseek-harness-desktop, desktop, client, coding, deepseek harness, dsh"
---
# deepseek-harness-desktop

> ⭐ **3** · ✅ active · client · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | client | Category | Desktop |
| Stars | ⭐ 3 | Status | ✅ active |
| Author | [Easyhoov](https://github.com/Easyhoov) | Updated | 2026-08-19 |

## One-liner

> Unofficial in-process desktop app for DeepSeek Harness: the host composition boots inside the Electron main process with zero ports and an IPC bridge. Not affiliated with DeepSeek.

## About

多数社区桌面版是**拉起 `dsh web` 子进程**、再把浏览器窗口指到 `127.0.0.1:3080`。本项目的做法不同：整份官方组合**跑在 Electron 主进程内部**（进程内集成），前端从本地加载，全部 `/api` 请求与事件走 **IPC 桥**——**零端口、零子进程、无本地 HTTP 服务**。会话、目标、后台任务、插件都是应用内的一等状态：关掉窗口（驻留托盘）它们照常运行。

## 📦 Install

```bash
dsh plugin --profile web add <包名>
dsh plugin --profile web add github:<仓库>
```

## 🚀 Quick Start

```bash
npm ci
npm start       # 开发运行
npm run dist    # 构建安装包（输出到 release/）
```

## 🔗 Links

- [GitHub Repository](https://github.com/Easyhoov/deepseek-harness-desktop-windows)
- [Full README](https://github.com/Easyhoov/deepseek-harness-desktop-windows#readme)
- [Back to the Clients (Desktop & TUI) list](../clients.md)
