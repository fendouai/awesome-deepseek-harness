---
title: "dsh-quickstart"
description: "Desktop launcher for DeepSeek Harness - start dsh web with no console window and auto-open the browser. Tested on Windows; macOS/Linux in progress."
keywords: "dsh-quickstart, desktop, client, coding, deepseek harness, dsh"
---
# dsh-quickstart

> ⭐ **0** · ✅ active · client

| | | | |
|---|---|---|---|
| Type | client | Category | Desktop |
| Stars | ⭐ 0 | Status | ✅ active |
| Author | [qzhqzh](https://github.com/qzhqzh) | Updated | 2026-08-18 |

## One-liner

> Desktop launcher for DeepSeek Harness - start dsh web with no console window and auto-open the browser. Tested on Windows; macOS/Linux in progress.

## About

Launch [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) from a desktop icon — `dsh web` starts **without a console window**, then the browser **opens automatically** once the web UI is ready. No more typing `npx @deepseek-ai/dsh web` and waiting for the page by hand — this double-click-and-go wrapper handles startup, readiness polling, and browser opening.

## ✨ Key Features

- `dsh web` blocks a terminal window and gives no feedback on when it is ready.
- Starting it from a desktop shortcut shows an ugly console box.
- Users who double-click and see nothing think the tool is broken.

## 📦 Install

```bash
# the launcher
npm i -g dsh-quickstart

# the harness itself (required)
npm i -g @deepseek-ai/dsh
```

## 🚀 Quick Start

```bash
# start dsh web, wait for readiness, open the browser
dsh-quickstart

# custom port / timeout
dsh-quickstart --port 3000 --timeout 120000

# wait but do not open the browser
dsh-quickstart --no-open

# spawn and exit immediately (no polling)
dsh-quickstart --no-wait

# pass extra args to dsh
dsh-quickstart -- web --port 3000
```

## 📚 Learn more

**dsh-quickstart**

<p align="center">  </p> Launch [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) from a desktop icon — `dsh web` starts **without a console window**, then the browser **opens automatically** once the web UI is ready. > **Status:** implemented and tested on **Windows**. macOS and Linux are in the > codebase but **not yet tested** — see [Roadmap](#roadmap). No more typing `npx @de

**~/.dsh-quickstart.json**

{ "watch": true, "maxRestarts": 10, "restartDelayMs": 3000 } The watchdog stays alive, restarts dsh up to `maxRestarts` times on exit, opens the browser on the first ready, and keeps the URL. `--watch` / `--no-watch` on the command line override the config. Stop it with Ctrl-C (or SIGTERM). > The watchdog deliberately stays **off by default** — it must be enabled by an > explicit `watch` command, 

**Linux quick start**

Linux already runs the same commands; only the "desktop double-click" surface differs. Three layers, from simplest to most "always-on":

**~/.config/systemd/user/dsh-web.service**

[Unit] Description=DeepSeek Harness web GUI Wants=network-online.target After=network-online.target [Service] Type=simple ExecStart=dsh web Restart=always RestartSec=3 [Install] WantedBy=default.target systemctl --user daemon-reload systemctl --user enable --now dsh-web.service # start + auto-start on login loginctl enable-linger $USER # optional: run before login too

## 🔗 Links

- [GitHub Repository](https://github.com/qzhqzh/dsh-quickstart)
- [Full README](https://github.com/qzhqzh/dsh-quickstart#readme)
- [Back to the Clients (Desktop & TUI) list](../clients.md)
