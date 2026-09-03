---
title: "dsh-loop"
description: "DSH 插件：定时循环（/loop 命令 + loop 工具 + 活动状态条）。官方 bundle 插件，dsh plugin --profile web add 安装"
keywords: "dsh-loop, automation, workflow, coding, deepseek harness, dsh"
---
# dsh-loop

> ⭐ **5** · ✅ active · workflow

| | | | |
|---|---|---|---|
| Type | workflow | Category | Automation |
| Stars | ⭐ 5 | Status | ✅ active |
| Author | [vlln](https://github.com/vlln) | Updated | — |

## One-liner

> DSH 插件：定时循环（/loop 命令 + loop 工具 + 活动状态条）。官方 bundle 插件，dsh plugin --profile web add 安装

## About

**Tool** (registered via `defineTool`, the model can self-adjust on every turn): **Commands** (user side): **UI** (dock slot above the input box on the chat page):

## 📦 Install

```bash
dsh plugin --profile web add "github:vlln/dsh-loop#main"   # one-line git source (build artifacts committed)
# or npm source: dsh plugin --profile web add @vlln/dsh-loop@0.3.0
```

## 🚀 Quick Start

```bash
pnpm install
pnpm run build      # tsdown: Node half (lib/index.mjs) + client bundle (lib/client.js)
```

## 📚 Learn more

**Settings**

The plugin ships a settings card in **Settings → Plugins** (official `ctx.settings` namespace `dsh-loop`, rendered via the `settings.plugin.item` slot next to the official plugin cards). **Each tool gets its own row with an official-looking Switch:** The card fields are driven by the client `LOOP_TOOL_FIELDS` table, mirrored one-to-one by the Node-side tool definition table — adding a tool means a

**Installation**

**Recommended: one-line install from a git source** (build artifacts are committed, so a git source does not trigger a build): dsh plugin --profile web add "github:vlln/dsh-loop#main" # one-line git source (build artifacts committed)

## 🔗 Links

- [GitHub Repository](https://github.com/vlln/dsh-loop)
- [Full README](https://github.com/vlln/dsh-loop#readme)
- [Back to the Workflows & Automation list](../workflows.md)
