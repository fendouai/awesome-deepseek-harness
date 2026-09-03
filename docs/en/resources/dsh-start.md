---
title: "dsh-start"
description: "One-click start/stop launcher for the DSH Web GUI on macOS: foreground/daemon start, stop, status, duplicate-launch guard, auto browser open, plus a Dock-able DSH.app built by script."
keywords: "dsh-start, desktop, client, automation, deepseek harness, dsh"
---
# dsh-start

> ⭐ **0** · ✅ active · client

| | | | |
|---|---|---|---|
| Type | client | Category | Desktop |
| Stars | ⭐ 0 | Status | ✅ active |
| Author | [zhengjy01](https://github.com/zhengjy01) | Updated | 2026-08-18 |

## One-liner

> One-click start/stop launcher for the DSH Web GUI on macOS: foreground/daemon start, stop, status, duplicate-launch guard, auto browser open, plus a Dock-able DSH.app built by script.

## About

A one-click launcher for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (DSH) Web on macOS. Stop typing `dsh web` by hand — start, stop, and check the server from a single command, or build a Dock-able **DSH.app** that behaves like a normal macOS application.

## ✨ Key Features

- **One command, four modes** — `dsh-start` (foreground, logs visible, Ctrl+C to stop), `dsh-start -d` (daemon, logs to `~/.dsh/web.log`), `dsh-start stop`, `dsh-
- **Duplicate-launch guard** — if the server is already up (default port 3080), it just opens the browser instead of starting a second instance.
- **Auto-open browser** — polls the port after launch and opens `http://127.0.0.1:3080` once ready (both foreground and daemon modes).
- **Normal-app feel (DSH.app)** — `scripts/build-dsh-app.sh` compiles a stay-open launcher app at `~/Applications/DSH.app`: double-click to start, Cmd+Q (with a c
- **Permission-safe by design** — the app delegates the server process to Terminal (which has full file-access context), avoiding the macOS sandbox/TCC `EPERM` fa

## 📦 Install

```bash
npm install -g dsh-start
dsh-start            # start in foreground
dsh-start status     # is it running?
```

## 🚀 Quick Start

```bash
git clone https://github.com/zhengjy01/dsh-start.git
cd dsh-start
./bin/dsh-start      # same CLI
```

## 📚 Learn more

**Usage**

The port defaults to `3080` (the `dsh web` default); override with the `DSH_PORT` environment variable.

## 🔗 Links

- [GitHub Repository](https://github.com/zhengjy01/dsh-start)
- [Full README](https://github.com/zhengjy01/dsh-start#readme)
- [Back to the Clients (Desktop & TUI) list](../clients.md)
