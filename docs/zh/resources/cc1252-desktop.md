---
title: "deepseek-harness-desktop (cc1252)"
description: "非官方 Windows Electron 封装。"
keywords: "deepseek-harness-desktop (cc1252), desktop, client, deepseek harness, dsh"
---
# deepseek-harness-desktop (cc1252)

> ⭐ **19** · ✅ 活跃 · 客户端 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 客户端 | 分类 | 桌面端 |
| 星数 | ⭐ 19 | 状态 | ✅ 活跃 |
| 作者 | [cc1252](https://github.com/cc1252) | 更新时间 | 2026-08-13 |

## 一句话介绍

> 非官方 Windows Electron 封装。

## 详细介绍

[English](README.en.md) · [下载 Releases](https://github.com/cc1252/deepseek-harness-desktop/releases) 一个面向 Windows 的、完整开源的 **DeepSeek Harness 非官方 Electron 桌面封装**。 它启动官方 `@deepseek-ai/dsh` 本地 Web 服务，再用隔离的 Electron `WebContentsView` 加载官方界面；桌面壳只负责进程生命周期、窗口、安全导航和自绘标题栏。

## ✨ 核心特性

- `DeepSeek-Harness-Desktop-Setup-0.1.0-x64.exe`：完整 Windows 安装包；
- `DeepSeek-Harness-Desktop-Portable-0.1.0-x64.exe`：无需安装的便携单文件；
- `DeepSeek-Harness-Desktop-Source-0.1.0.zip`：与发布对应的源码快照；
- `SHA256SUMS.txt`：发布文件校验值；
- GitHub 自动生成的源码归档。

## 📦 安装

```bash
git clone https://github.com/cc1252/deepseek-harness-desktop.git
cd deepseek-harness-desktop
npm ci
npm run setup
npm run start
```

## 🚀 快速开始

```bash
npm ci
npm run build:windows
```

## 🔗 链接

- [GitHub 仓库](https://github.com/cc1252/deepseek-harness-desktop)
- [完整 README](https://github.com/cc1252/deepseek-harness-desktop#readme)
- [返回deepseek-harness-desktop (cc1252)所在分类](../clients.md)
