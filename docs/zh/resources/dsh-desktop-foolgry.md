---
title: "dsh_desktop"
description: "DeepSeek Harness (dsh) Windows desktop client - bundled Node.js + dsh CLI, one-click launch"
keywords: "dsh_desktop, desktop, client, coding, deepseek harness, dsh"
---
# dsh_desktop

> ⭐ **521** · ✅ 活跃 · 客户端 · 近期 ⬆️ +14

| | | | |
|---|---|---|---|
| 类型 | 客户端 | 分类 | 桌面端 |
| 星数 | ⭐ 521 | 状态 | ✅ 活跃 |
| 作者 | [myYangyunfan](https://github.com/myYangyunfan) | 更新时间 | 2026-08-21 |

## 一句话介绍

> DeepSeek Harness (dsh) Windows desktop client - bundled Node.js + dsh CLI, one-click launch

## 详细介绍

- **零依赖** — 内置独立 Node 运行时与 npm CLI，目标机器无需安装任何环境 - **完整 dsh** — 打包 `@deepseek-ai/dsh` 及全部官方插件，离线可用 - **一键启动** — 双击即启 `dsh web`，优先复用上次端口，就绪后载入原生窗口 - **双形态** — 便携版（免安装、可放 U 盘）+ 安装版（桌面/开始菜单快捷方式）

## ✨ 核心特性

- **零依赖** — 内置独立 Node 运行时与 npm CLI，目标机器无需安装任何环境
- **完整 dsh** — 打包 `@deepseek-ai/dsh` 及全部官方插件，离线可用
- **一键启动** — 双击即启 `dsh web`，优先复用上次端口，就绪后载入原生窗口
- **双形态** — 便携版（免安装、可放 U 盘）+ 安装版（桌面/开始菜单快捷方式）

## 🚀 快速开始

```bash
xattr -dr com.apple.quarantine "/Applications/DSH Desktop.app"
```

## 📚 更多信息

**打包 win-x64 NSIS 安装包 + 安装态冒烟**

bash dsh-tauri/scripts/stage-payload.sh npx --yes @tauri-apps/cli build --config src-tauri/src/app/tauri.conf.json \ --target x86_64-pc-windows-msvc bash dsh-tauri/scripts/smoke-installed.sh 完整流程（含调试开关 `DSH_TAURI_DIAG` / `DSH_TAURI_DEVTOOLS` 等）见[开发手册 §6](dsh-tauri/docs/development.md)。

**📦 Tauri 架构可导出的安装包形式**

由 `tauri.conf.json` 的 `bundle.targets` 决定，按需增删即可扩展产物形式： > 便携版（免安装、可放 U 盘）不是 Tauri 内置 target——Tauri 版以 NSIS `currentUser` 安装为默认形态，独立便携包规划中以后续版本提供。

## 🔗 链接

- [GitHub 仓库](https://github.com/myYangyunfan/dsh_desktop)
- [完整 README](https://github.com/myYangyunfan/dsh_desktop#readme)
- [返回dsh_desktop所在分类](../clients.md)
