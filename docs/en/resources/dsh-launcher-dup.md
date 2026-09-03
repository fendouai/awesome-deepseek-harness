---
title: "dsh-launcher"
description: "Lightweight Windows launcher: silent autostart at logon plus a minimal WebView2 window."
keywords: "dsh-launcher, desktop, client, deepseek harness, dsh"
---
# dsh-launcher

> ⭐ **165** · ✅ active · client · ⬆️ +4 recently

| | | | |
|---|---|---|---|
| Type | client | Category | Desktop |
| Stars | ⭐ 165 | Status | ✅ active |
| Author | [Ruler4396](https://github.com/Ruler4396) | Updated | 2026-08-20 |

## One-liner

> Lightweight Windows launcher: silent autostart at logon plus a minimal WebView2 window.

## About

一个 Windows 原生壳：双击启动 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)（`dsh`）、可设置开机自启，高度重视服务生命周期与出错诊断。安装包大小仅为 **~1.4MB**，不内置 dsh；缺失的依赖（Node.js 等）按需补齐，不改动系统环境。 **克制**：本项目意在打造一个舒适的 dsh 原版体验，不添加文件面板、内置终端等额外功能，一切交给dsh的插件，由用户自行决定。仅在推出安全性更新和dsh版本更新时弹出系统通知。

## ✨ Key Features

- 开机自启 · 独立小窗口（WebView2）· 自动拉起服务并等待就绪
- 出错弹窗带错误码，统一日志 `~/.dsh\dsh-launcher\dsh.log`
- `DshWeb.exe --diagnose` 一键导出信息脱敏诊断包
- 服务生命周期：跟随窗口 / 常驻 / 托盘驻留（见下"插件"）
- 主题跟随 · 窗口位置记忆 · dsh 延迟更新（不打断会话）

## 📦 Install

```bash
dsh plugin --profile web add dsh-launcher-lifetime
```

## 📚 Learn more

**安装**

**MSI（推荐新手）**：从 [Releases](https://github.com/Ruler4396/dsh-launcher/releases) 下载 `dsh-launcher-<版本>.msi`，双击安装（向导里可勾选开机自启）。卸载：设置 → 应用 → dsh-launcher。 **便携版 ZIP**：下载 `dsh-launcher-windows-<版本>.zip`，解压后双击 `DshWeb.exe`；删文件夹即卸载。 > 双击没反应？先运行解压目录里的 `check-prereq.cmd`，它会检测 .NET / WebView2 / Node 并给出缺失项的安装命令。

## 🔗 Links

- [GitHub Repository](https://github.com/Ruler4396/dsh-launcher)
- [Full README](https://github.com/Ruler4396/dsh-launcher#readme)
- [Back to the Clients (Desktop & TUI) list](../clients.md)
