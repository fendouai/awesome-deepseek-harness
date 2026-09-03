---
title: "dsh-task-dispatcher"
description: "DeepSeek Harness 的滴答清单任务派发器：按间隔拉取今天到期任务，flomo+macOS 通知，可选自动执行（每任务一个 headless 会话）、执行会话工作区选择与 Web 任务看板。"
keywords: "dsh-task-dispatcher, automation, plugin, workflow, notifications, deepseek harness, dsh"
---
# dsh-task-dispatcher

> ⭐ **0** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 自动化 |
| 星数 | ⭐ 0 | 状态 | ✅ 活跃 |
| 作者 | [zhengjy01](https://github.com/zhengjy01) | 更新时间 | — |

## 一句话介绍

> DeepSeek Harness 的滴答清单任务派发器：按间隔拉取今天到期任务，flomo+macOS 通知，可选自动执行（每任务一个 headless 会话）、执行会话工作区选择与 Web 任务看板。

## 详细介绍

Use TickTick (滴答清单) as DSH's daily task dispatcher: a cordis timer pulls each morning (default 08:30) today's due tasks from the 5️⃣AI list, writes them to today's task file, and notifies via **flomo + macOS**. The agent reads the file, works through the items, and writes results back to TickTick with `ticktick_complete`.

## ✨ 核心特性

- **Interval dispatch**: cordis `ctx.interval` polls every minute and dispatches when the configured interval (minutes) has elapsed; 0 disables the timer; `dispat
- **Task source**: default the 5️⃣AI list (`projectName` / `projectId` configurable); `dueMode=today` pulls due-today/overdue + undated, `dueMode=all` pulls all i
- **Today task file**: writes a Markdown checklist (default `~/.dsh/dsh-task-dispatcher/today-tasks.md`).
- **Notify on change only**: `notifyFlomo` (reuses `~/.dsh/dsh-flomo.json`) + `notifyMac` (osascript); a repeated pull with no new tasks stays silent.
- **Auto-execute (autoExecute)**: when on, each pulled task runs in its own `dsh --profile headless` session (serial, one task per session); success writes back t
- **Worker workspace (workerWorkspaceId)**: the auto-execute worker session runs in the user's home dir by default; set a DSH workspace id and the worker spawns w
- **Agent tools**: `dispatcher_status` / `dispatcher_config` / `dispatcher_run` / `dispatcher_report` + a Web settings panel.

## 📦 安装

```bash
dsh plugin --profile web add link:/path/to/dsh-task-dispatcher
# restart dsh web to activate
```

## 🚀 快速开始

```bash
pnpm install
pnpm build && node tests/smoke.mjs
```

## 🔗 链接

- [GitHub 仓库](https://github.com/zhengjy01/dsh-task-dispatcher)
- [完整 README](https://github.com/zhengjy01/dsh-task-dispatcher#readme)
- [返回dsh-task-dispatcher所在分类](../plugins.md)
