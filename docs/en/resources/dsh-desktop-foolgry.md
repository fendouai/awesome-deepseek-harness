---
title: "dsh_desktop"
description: "DeepSeek Harness (dsh) Windows desktop client - bundled Node.js + dsh CLI, one-click launch"
keywords: "dsh_desktop, desktop, client, coding, deepseek harness, dsh"
---
# dsh_desktop

> ⭐ **521** · ✅ active · client · ⬆️ +14 recently

| | | | |
|---|---|---|---|
| Type | client | Category | Desktop |
| Stars | ⭐ 521 | Status | ✅ active |
| Author | [myYangyunfan](https://github.com/myYangyunfan) | Updated | 2026-08-21 |

## One-liner

> DeepSeek Harness (dsh) Windows desktop client - bundled Node.js + dsh CLI, one-click launch

## About

- **零依赖** — 内置独立 Node 运行时与 npm CLI，目标机器无需安装任何环境 - **完整 dsh** — 打包 `@deepseek-ai/dsh` 及全部官方插件，离线可用 - **一键启动** — 双击即启 `dsh web`，优先复用上次端口，就绪后载入原生窗口 - **双形态** — 便携版（免安装、可放 U 盘）+ 安装版（桌面/开始菜单快捷方式）

## ✨ Key Features

- **零依赖** — 内置独立 Node 运行时与 npm CLI，目标机器无需安装任何环境
- **完整 dsh** — 打包 `@deepseek-ai/dsh` 及全部官方插件，离线可用
- **一键启动** — 双击即启 `dsh web`，优先复用上次端口，就绪后载入原生窗口
- **双形态** — 便携版（免安装、可放 U 盘）+ 安装版（桌面/开始菜单快捷方式）

## 🚀 Quick Start

```bash
xattr -dr com.apple.quarantine "/Applications/DSH Desktop.app"
```

## 📚 Learn more

**打包 win-x64 NSIS 安装包 + 安装态冒烟**

bash dsh-tauri/scripts/stage-payload.sh npx --yes @tauri-apps/cli build --config src-tauri/src/app/tauri.conf.json \ --target x86_64-pc-windows-msvc bash dsh-tauri/scripts/smoke-installed.sh 完整流程（含调试开关 `DSH_TAURI_DIAG` / `DSH_TAURI_DEVTOOLS` 等）见[开发手册 §6](dsh-tauri/docs/development.md)。

**📦 Tauri 架构可导出的安装包形式**

由 `tauri.conf.json` 的 `bundle.targets` 决定，按需增删即可扩展产物形式： > 便携版（免安装、可放 U 盘）不是 Tauri 内置 target——Tauri 版以 NSIS `currentUser` 安装为默认形态，独立便携包规划中以后续版本提供。

## 🔗 Links

- [GitHub Repository](https://github.com/myYangyunfan/dsh_desktop)
- [Full README](https://github.com/myYangyunfan/dsh_desktop#readme)
- [Back to the Clients (Desktop & TUI) list](../clients.md)
