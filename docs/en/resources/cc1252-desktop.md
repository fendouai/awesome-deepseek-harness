---
title: "deepseek-harness-desktop (cc1252)"
description: "Unofficial open-source Windows Electron wrapper for DeepSeek Harness."
keywords: "deepseek-harness-desktop (cc1252), desktop, client, deepseek harness, dsh"
---
# deepseek-harness-desktop (cc1252)

> ⭐ **19** · ✅ active · client · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | client | Category | Desktop |
| Stars | ⭐ 19 | Status | ✅ active |
| Author | [cc1252](https://github.com/cc1252) | Updated | 2026-08-13 |

## One-liner

> Unofficial open-source Windows Electron wrapper for DeepSeek Harness.

## About

[English](README.en.md) · [下载 Releases](https://github.com/cc1252/deepseek-harness-desktop/releases) 一个面向 Windows 的、完整开源的 **DeepSeek Harness 非官方 Electron 桌面封装**。 它启动官方 `@deepseek-ai/dsh` 本地 Web 服务，再用隔离的 Electron `WebContentsView` 加载官方界面；桌面壳只负责进程生命周期、窗口、安全导航和自绘标题栏。

## ✨ Key Features

- `DeepSeek-Harness-Desktop-Setup-0.1.0-x64.exe`：完整 Windows 安装包；
- `DeepSeek-Harness-Desktop-Portable-0.1.0-x64.exe`：无需安装的便携单文件；
- `DeepSeek-Harness-Desktop-Source-0.1.0.zip`：与发布对应的源码快照；
- `SHA256SUMS.txt`：发布文件校验值；
- GitHub 自动生成的源码归档。

## 📦 Install

```bash
git clone https://github.com/cc1252/deepseek-harness-desktop.git
cd deepseek-harness-desktop
npm ci
npm run setup
npm run start
```

## 🚀 Quick Start

```bash
npm ci
npm run build:windows
```

## 🔗 Links

- [GitHub Repository](https://github.com/cc1252/deepseek-harness-desktop)
- [Full README](https://github.com/cc1252/deepseek-harness-desktop#readme)
- [Back to the Clients (Desktop & TUI) list](../clients.md)
