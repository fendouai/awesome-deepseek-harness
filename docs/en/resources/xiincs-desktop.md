---
title: "deepseek-harness-desktop (xiincs)"
description: "Native desktop built on Tauri 2 with bundled Node.js runtime, tray residency and auto-update."
keywords: "deepseek-harness-desktop (xiincs), desktop, client, deepseek harness, dsh"
---
# deepseek-harness-desktop (xiincs)

> ⭐ 36 · ✅ active · client

## One-liner

Native desktop built on Tauri 2 with bundled Node.js runtime, tray residency and auto-update.

## About

把 harness 自带的 Web 服务（`dsh web`）装进原生窗口：一键启动、托盘常驻、崩溃自动恢复、自动更新， `~/.dsh` 下的数据与浏览器版完全通用。因为用的是系统自带 WebView2 而不是打包一份 Chromium， 安装包小很多；而且刻意**不**给内嵌页面开 Tauri IPC 权限——它接触不到你的文件系统。 macOS（`.dmg`）和 Linux（`.deb`）也在每个 Release 里提供，Windows 版经过签名并接入自动更新； mac/Linux 版**未签名、未公证**（没有 Apple Developer 账号）——macOS 需要在"系统设置 → 隐私与 安全性"里手动允许打开一次，Linux 直接 `dpkg -i`/系统安装器装即可，两者暂不参与自动更新。 <p align="center"> &nbsp;&nbsp; </p> **[⬇️ 下载最新版本](https://github.com/xiincs/deepseek-harness-desktop/releases/latest)**

## Author
**[xiincs](https://github.com/xiincs)**

## Links

- [GitHub Repository](https://github.com/xiincs/deepseek-harness-desktop)
- [Full README](https://github.com/xiincs/deepseek-harness-desktop#readme)
- [Back to the Clients (Desktop & TUI) list](../clients.md)
