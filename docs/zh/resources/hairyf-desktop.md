---
title: "deepseek-harness-desktop (hairyf)"
description: "一键桌面应用：全本地运行，核心自愈更新，零环境配置。Win/macOS/Linux。"
keywords: "deepseek-harness-desktop (hairyf), desktop, client, deepseek harness, dsh"
---
# deepseek-harness-desktop (hairyf)

> ⭐ **814** · ✅ 活跃 · 客户端 · 近期 ⬆️ +131

| | | | |
|---|---|---|---|
| 类型 | 客户端 | 分类 | 桌面端 |
| 星数 | ⭐ 814 | 状态 | ✅ 活跃 |
| 作者 | [hairyf](https://github.com/hairyf) | 更新时间 | 2026-08-21 |

## 一句话介绍

> 一键桌面应用：全本地运行，核心自愈更新，零环境配置。Win/macOS/Linux。

## 详细介绍

首次启动引导中提供的插件，按需勾选安装： - [DSH Win Terminal Inspector](https://github.com/clearkurt/dsh-win-terminal-inspector) — Windows 极简模式修复 - [DSH Market](https://github.com/dsh-market/dsh-market) — 浏览、搜索并一键安装社区插件（推荐） - [DSH Better Sidebar](https://github.com/omdsh-dev/DSH-better-sidebar) — 类 VSCode 右侧栏，按会话隔离（推荐） - [DSH Notification](https://github.com/omdsh-dev/dsh-notification) — 回合完成时的桌面通知

## ✨ 核心特性

- 🧩 **插件管理** — 插件面板管理已安装插件，出现异常时提供升级 / 卸载入口，错误详情。
- 🎁 **内置插件** — 随安装包内置插件，以及将来引入更多高质量的内置插件。
- 🪶 **原生轻量** — Tauri 2 外壳（非 Electron）：更小的安装包、更低的内存占用、原生窗口。
- ⌨️ **命令行集成** — 安装自动注册 `dsh` 命令，新开终端即用；不覆盖你已有 shell 配置。
- 🧭 **启动引导** — 首次启动可选推荐插件，也可在配置中重新选择。
- 🚀 **自更新** — 应用内更新，不需要在重新下载；

## 📦 安装

```bash
brew install dsh-tauri-desk/desktop/deepseek-harness
```

## 📚 更多信息

**工作原理**

┌──────────────────────────────────────────────┐ │ Tauri WebView (React) │ │ 安装状态机 → 下载进度 → iframe │ │ 加载 dsh Web 界面 + 侧边栏控制 │ └──────────────────────┬───────────────────────┘ │ invoke 命令 + 事件 ┌──────────────────────┴───────────────────────┐ │ Tauri Rust 后端 │ │ service/download 安装器 + 解压 │ │ service/core Harness 核心多版本管理 │ │ service/profile dsh 档案管理 │ │ service/plugin 插件卸载 / 升级 │ │ service/cli dsh 命

**说明**

> [!WARNING] > **开发预览** — 上游 `dsh` 仍在快速迭代，存在破坏性变更；本项目同步跟随。 > [!NOTE] > **安全声明** — `dsh` 具备本地代码执行能力。仅供学习 / 研究 / 测试，请在可信、隔离的环境中使用。

## 🔗 链接

- [GitHub 仓库](https://github.com/hairyf/deepseek-harness-desktop)
- [完整 README](https://github.com/hairyf/deepseek-harness-desktop#readme)
- [返回deepseek-harness-desktop (hairyf)所在分类](../clients.md)
