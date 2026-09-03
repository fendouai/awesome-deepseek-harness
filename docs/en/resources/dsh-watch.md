---
title: "dsh-watch"
description: "Put a watch on a stream: background listeners that wake the DeepSeek Harness agent with new matching lines — and a daemon host so a watcher runs unattended for weeks, with no task and no browser. Not affiliated with DeepSeek."
keywords: "dsh-watch, browser, integration, coding, multi-agent, deepseek harness, dsh"
---
# dsh-watch

> ⭐ **3** · ✅ active · integration

| | | | |
|---|---|---|---|
| Type | integration | Category | Browser control |
| Stars | ⭐ 3 | Status | ✅ active |
| Author | [dshworks](https://github.com/dshworks) | Updated | 2026-08-20 |

## One-liner

> Put a watch on a stream: background listeners that wake the DeepSeek Harness agent with new matching lines — and a daemon host so a watcher runs unattended for weeks, with no task and no browser. Not affiliated with DeepSeek.

## About

The stock jobs subsystem says when work *finishes*. `dsh-watch` says when something *speaks*: arm a listener on a command or a growing file, and new lines arrive as filtered, batched, byte-bounded notices. Then take the human out. Declare the watches in profile config, mount the daemon, and the agent boots, idles at zero cost, and wakes for weeks on whatever its streams say.

## 📦 Install

```bash
dsh plugin --profile web add @dshworks/dsh-watch
dsh --profile web
```

## 🚀 Quick Start

```bash
watch(source: "command", command: "npm run dev", pattern: "error|warn|Ready", label: "dev")
→ Watch armed (watch-1) on command: npm run dev.

# …the agent keeps working. When the dev server logs "Ready in 130ms",
# a notice wakes it:
[watch dev · watch-1] 1 line:
Ready in 130ms
```

## 📚 Learn more

**Install**

dsh plugin --profile web add @dshworks/dsh-watch dsh --profile web `dsh plugin` forwards to pnpm, so pnpm must be on PATH. Nothing else to configure — the `watch` tool is available in the next session.

**Configuration**

Every bound is a validated `Config` field, not a constant. The daemon's own config is `brief` (required), `flushIntervalMs` (`300000`), and `journal` (`true`).

## 🔗 Links

- [GitHub Repository](https://github.com/dshworks/dsh-watch)
- [Full README](https://github.com/dshworks/dsh-watch#readme)
- [Back to the MCP & Integrations list](../integrations.md)
