---
title: "dsh-task-dispatcher"
description: "TickTick (滴答清单) daily task dispatcher for DeepSeek Harness: interval-based pulls of today's due tasks, notify (flomo + macOS), optional auto-execute in headless DSH sessions, worker workspace selection, and a web task board."
keywords: "dsh-task-dispatcher, automation, plugin, workflow, notifications, deepseek harness, dsh"
---
# dsh-task-dispatcher

> ⭐ **0** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Automation |
| Stars | ⭐ 0 | Status | ✅ active |
| Author | [zhengjy01](https://github.com/zhengjy01) | Updated | — |

## One-liner

> TickTick (滴答清单) daily task dispatcher for DeepSeek Harness: interval-based pulls of today's due tasks, notify (flomo + macOS), optional auto-execute in headless DSH sessions, worker workspace selection, and a web task board.

## About

Use TickTick (滴答清单) as DSH's daily task dispatcher: a cordis timer pulls each morning (default 08:30) today's due tasks from the 5️⃣AI list, writes them to today's task file, and notifies via **flomo + macOS**. The agent reads the file, works through the items, and writes results back to TickTick with `ticktick_complete`.

## ✨ Key Features

- **Interval dispatch**: cordis `ctx.interval` polls every minute and dispatches when the configured interval (minutes) has elapsed; 0 disables the timer; `dispat
- **Task source**: default the 5️⃣AI list (`projectName` / `projectId` configurable); `dueMode=today` pulls due-today/overdue + undated, `dueMode=all` pulls all i
- **Today task file**: writes a Markdown checklist (default `~/.dsh/dsh-task-dispatcher/today-tasks.md`).
- **Notify on change only**: `notifyFlomo` (reuses `~/.dsh/dsh-flomo.json`) + `notifyMac` (osascript); a repeated pull with no new tasks stays silent.
- **Auto-execute (autoExecute)**: when on, each pulled task runs in its own `dsh --profile headless` session (serial, one task per session); success writes back t
- **Worker workspace (workerWorkspaceId)**: the auto-execute worker session runs in the user's home dir by default; set a DSH workspace id and the worker spawns w
- **Agent tools**: `dispatcher_status` / `dispatcher_config` / `dispatcher_run` / `dispatcher_report` + a Web settings panel.

## 📦 Install

```bash
dsh plugin --profile web add link:/path/to/dsh-task-dispatcher
# restart dsh web to activate
```

## 🚀 Quick Start

```bash
pnpm install
pnpm build && node tests/smoke.mjs
```

## 🔗 Links

- [GitHub Repository](https://github.com/zhengjy01/dsh-task-dispatcher)
- [Full README](https://github.com/zhengjy01/dsh-task-dispatcher#readme)
- [Back to the Plugins list](../plugins.md)
