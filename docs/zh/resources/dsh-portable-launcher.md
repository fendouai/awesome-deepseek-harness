---
title: "dsh-portable-launcher"
description: "One-click portable launcher for DeepSeek Harness (dsh) Web UI on Windows. Auto-installs Node.js and dsh with China mirror fallback, 3-stage progress with retries and resume, zero-download fast path when ready. No admin needed."
keywords: "dsh-portable-launcher, desktop, client, coding, deepseek harness, dsh"
---
# dsh-portable-launcher

> ⭐ **2** · ✅ 活跃 · 客户端

| | | | |
|---|---|---|---|
| 类型 | 客户端 | 分类 | 桌面端 |
| 星数 | ⭐ 2 | 状态 | ✅ 活跃 |
| 作者 | [15828148](https://github.com/15828148) | 更新时间 | 2026-08-14 |

## 一句话介绍

> One-click portable launcher for DeepSeek Harness (dsh) Web UI on Windows. Auto-installs Node.js and dsh with China mirror fallback, 3-stage progress with retries and resume, zero-download fast path when ready. No admin needed.

## 详细介绍

One-click launcher for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`) Web UI on Windows. Zero-config for end users: it auto-installs a portable Node.js and the `dsh` package when missing, then starts the local Web UI at `http://127.0.0.1:3080`.

## ✨ 核心特性

- **3 major stages with live progress**: `[1/3]` Node.js check → `[2/3]` dsh package check → `[3/3]` launch
- **Zero-download fast path**: when everything is already installed, launch is direct — no downloads, no registry checks
- **Automatic portable Node.js install** (no admin required; portable mode - no registry or system PATH changes, everything stays inside the package folder)
- **Automatic dsh install** via a local `npm install --prefix` into the package folder (no global install, no system changes; China npm mirror fallback on retries
- **Up to 3 retries per step** with clear prompts, then concrete manual instructions
- **Resume support**: close the window mid-setup, run again — it continues from where it stopped
- Boot-time log (`dsh-startup.log`) written next to the launcher
- 64-bit check, writable-folder check, port-conflict handling

## 📚 更多信息

**Usage**

1. Download `dsh-web-ui-portable.zip` from [Releases](../../releases) and extract it anywhere (e.g. `D:\` or Desktop — **not** Program Files) 2. Run `setup.bat` once — creates a desktop shortcut "DSH Web UI" with the icon 3. Double-click **DSH Web UI** (or `dsh-web.bat`) 4. First run: press `Y` if asked to download Node.js; downloads take a few minutes 5. Add your own DeepSeek API key in the UI Se

## 🔗 链接

- [GitHub 仓库](https://github.com/15828148/dsh-portable-launcher)
- [完整 README](https://github.com/15828148/dsh-portable-launcher#readme)
- [返回dsh-portable-launcher所在分类](../clients.md)
