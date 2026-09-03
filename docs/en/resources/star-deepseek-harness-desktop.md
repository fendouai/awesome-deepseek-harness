---
title: "star-deepseek-harness-desktop"
description: "Star-deepseek-harness-desktop — DeepSeek Harness,一站式桌面运维台。Harness 自动规划并调用数据库 / SSH / SFTP / Docker 执行。本地优先、跨平台。本项目由自研的starhub 做的再次改进，现在改进中... 尽情期待吧，如果想使用老版本可以下载 0.6X.X 版本"
keywords: "star-deepseek-harness-desktop, desktop, client, coding, deepseek harness, dsh"
---
# star-deepseek-harness-desktop

> ⭐ **7** · ✅ active · client · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | client | Category | Desktop |
| Stars | ⭐ 7 | Status | ✅ active |
| Author | [dabaicai001](https://github.com/dabaicai001) | Updated | 2026-08-21 |

## One-liner

> Star-deepseek-harness-desktop — DeepSeek Harness,一站式桌面运维台。Harness 自动规划并调用数据库 / SSH / SFTP / Docker 执行。本地优先、跨平台。本项目由自研的starhub 做的再次改进，现在改进中... 尽情期待吧，如果想使用老版本可以下载 0.6X.X 版本

## About

**All-in-One DevOps Desktop Command Center** StarHub 是一个跨平台桌面应用,把开发运维每天要用到的工具收进同一个窗口:数据库客户端、SSH 终端、SFTP 文件传输、Docker 面板、AI 助手。不用再在 Navicat、Xshell、Portainer 和 AI 对话框之间来回切换。 官网:[starthub.waouzzz.cc](https://starthub.waouzzz.cc/)

## ✨ Key Features

- **Rust 主进程(Tauri 2)** — 桌面壳。负责多窗口管理、SSH/SFTP 会话(russh)、系统密钥环、AI 浏览器、Updater。
- **Go Sidecar** — 数据库与中间件代理。独立进程,经 stdio JSON-RPC 与主进程通信,承载 MySQL / PostgreSQL / SQLite / Redis / ClickHouse / SQL Server / Elasticsearch / Docker / Excel 等适配器和连
- **前端(React)** — 基于 DeepSeek Harness(dsh)主壳,StarHub 的工作台和插件住在 `vendor/deepseek-harness` 里:`apps/starhub-window` 是资产工作台构建入口,`packages/starhub/*` 是 11 个内置插件(导航、工具桥

## 📦 Install

```bash
git clone https://github.com/dabaicai001/star-dsh-desktop.git
cd starhub
npm install
pnpm --dir vendor/deepseek-harness install

npm run tauri:dev        # 完整开发:构建 sidecar + React 工作台,启动桌面壳
```

## 🔗 Links

- [GitHub Repository](https://github.com/dabaicai001/star-deepseek-harness-desktop)
- [Full README](https://github.com/dabaicai001/star-deepseek-harness-desktop#readme)
- [Back to the Clients (Desktop & TUI) list](../clients.md)
