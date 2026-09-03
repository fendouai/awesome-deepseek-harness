---
title: "dsh-watch"
description: "Put a watch on a stream: background listeners that wake the DeepSeek Harness agent with new matching lines — and a daemon host so a watcher runs unattended for weeks, with no task and no browser. Not affiliated with DeepSeek."
keywords: "dsh-watch, browser, integration, coding, multi-agent, deepseek harness, dsh"
---
# dsh-watch

> ⭐ **3** · ✅ 活跃 · 集成

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | 浏览器控制 |
| 星数 | ⭐ 3 | 状态 | ✅ 活跃 |
| 作者 | [dshworks](https://github.com/dshworks) | 更新时间 | 2026-08-20 |

## 一句话介绍

> Put a watch on a stream: background listeners that wake the DeepSeek Harness agent with new matching lines — and a daemon host so a watcher runs unattended for weeks, with no task and no browser. Not affiliated with DeepSeek.

## 详细介绍

The stock jobs subsystem says when work *finishes*. `dsh-watch` says when something *speaks*: arm a listener on a command or a growing file, and new lines arrive as filtered, batched, byte-bounded notices. Then take the human out. Declare the watches in profile config, mount the daemon, and the agent boots, idles at zero cost, and wakes for weeks on whatever its streams say.

## 📦 安装

```bash
dsh plugin --profile web add @dshworks/dsh-watch
dsh --profile web
```

## 🚀 快速开始

```bash
watch(source: "command", command: "npm run dev", pattern: "error|warn|Ready", label: "dev")
→ Watch armed (watch-1) on command: npm run dev.

# …the agent keeps working. When the dev server logs "Ready in 130ms",
# a notice wakes it:
[watch dev · watch-1] 1 line:
Ready in 130ms
```

## 📚 更多信息

**Install**

dsh plugin --profile web add @dshworks/dsh-watch dsh --profile web `dsh plugin` forwards to pnpm, so pnpm must be on PATH. Nothing else to configure — the `watch` tool is available in the next session.

**Configuration**

Every bound is a validated `Config` field, not a constant. The daemon's own config is `brief` (required), `flushIntervalMs` (`300000`), and `journal` (`true`).

## 🔗 链接

- [GitHub 仓库](https://github.com/dshworks/dsh-watch)
- [完整 README](https://github.com/dshworks/dsh-watch#readme)
- [返回dsh-watch所在分类](../integrations.md)
