---
title: "dsh-start"
description: "macOS 上 DSH Web GUI 的一键启停启动器：前台/后台启动、停止、状态、防重复启动、自动打开浏览器，并可用脚本构建程序坞版 DSH.app。"
keywords: "dsh-start, desktop, client, automation, deepseek harness, dsh"
---
# dsh-start

> ⭐ **0** · ✅ 活跃 · 客户端

| | | | |
|---|---|---|---|
| 类型 | 客户端 | 分类 | 桌面端 |
| 星数 | ⭐ 0 | 状态 | ✅ 活跃 |
| 作者 | [zhengjy01](https://github.com/zhengjy01) | 更新时间 | 2026-08-18 |

## 一句话介绍

> macOS 上 DSH Web GUI 的一键启停启动器：前台/后台启动、停止、状态、防重复启动、自动打开浏览器，并可用脚本构建程序坞版 DSH.app。

## 详细介绍

A one-click launcher for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (DSH) Web on macOS. Stop typing `dsh web` by hand — start, stop, and check the server from a single command, or build a Dock-able **DSH.app** that behaves like a normal macOS application.

## ✨ 核心特性

- **One command, four modes** — `dsh-start` (foreground, logs visible, Ctrl+C to stop), `dsh-start -d` (daemon, logs to `~/.dsh/web.log`), `dsh-start stop`, `dsh-
- **Duplicate-launch guard** — if the server is already up (default port 3080), it just opens the browser instead of starting a second instance.
- **Auto-open browser** — polls the port after launch and opens `http://127.0.0.1:3080` once ready (both foreground and daemon modes).
- **Normal-app feel (DSH.app)** — `scripts/build-dsh-app.sh` compiles a stay-open launcher app at `~/Applications/DSH.app`: double-click to start, Cmd+Q (with a c
- **Permission-safe by design** — the app delegates the server process to Terminal (which has full file-access context), avoiding the macOS sandbox/TCC `EPERM` fa

## 📦 安装

```bash
npm install -g dsh-start
dsh-start            # start in foreground
dsh-start status     # is it running?
```

## 🚀 快速开始

```bash
git clone https://github.com/zhengjy01/dsh-start.git
cd dsh-start
./bin/dsh-start      # same CLI
```

## 📚 更多信息

**Usage**

The port defaults to `3080` (the `dsh web` default); override with the `DSH_PORT` environment variable.

## 🔗 链接

- [GitHub 仓库](https://github.com/zhengjy01/dsh-start)
- [完整 README](https://github.com/zhengjy01/dsh-start#readme)
- [返回dsh-start所在分类](../clients.md)
