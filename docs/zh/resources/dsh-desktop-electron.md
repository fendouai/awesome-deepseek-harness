---
title: "dsh-desktop-electron"
description: "跨平台 Electron 桌面壳：托盘常驻独立窗口。"
keywords: "dsh-desktop-electron, desktop, client, deepseek harness, dsh"
---
# dsh-desktop-electron

> ⭐ **5** · ✅ 活跃 · 客户端 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 客户端 | 分类 | 桌面端 |
| 星数 | ⭐ 5 | 状态 | ✅ 活跃 |
| 作者 | [Void0312Aurora](https://github.com/Void0312Aurora) | 更新时间 | 2026-08-15 |

## 一句话介绍

> 跨平台 Electron 桌面壳：托盘常驻独立窗口。

## 详细介绍

An Electron desktop shell for the [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`) Web GUI: it spawns `dsh web`, waits for the server's readiness line, and hosts the GUI in a standalone window with tray residency. The shell targets the public [`@deepseek-ai/dsh`](https://www.npmjs.com/package/@deepseek-ai/dsh) package. It relies only on the maintained `dsh web --host --port ` arguments and the `dsh web: ` readiness line.

## 📦 安装

```bash
npm install
DSH_HOME=~/.dsh/source/current npm run dev
```

## 🚀 快速开始

```bash
npm run dist        # installers under release/
npm run dist:dir    # unpacked dir only, for a quick smoke
```

## 🔗 链接

- [GitHub 仓库](https://github.com/Void0312Aurora/dsh-desktop-electron)
- [完整 README](https://github.com/Void0312Aurora/dsh-desktop-electron#readme)
- [返回dsh-desktop-electron所在分类](../clients.md)
