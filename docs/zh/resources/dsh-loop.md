---
title: "dsh-loop"
description: "DSH 插件：定时循环（/loop 命令 + loop 工具 + 活动状态条）。官方 bundle 插件，dsh plugin --profile web add 安装"
keywords: "dsh-loop, automation, workflow, coding, deepseek harness, dsh"
---
# dsh-loop

> ⭐ **5** · ✅ 活跃 · 工作流

| | | | |
|---|---|---|---|
| 类型 | 工作流 | 分类 | 自动化 |
| 星数 | ⭐ 5 | 状态 | ✅ 活跃 |
| 作者 | [vlln](https://github.com/vlln) | 更新时间 | — |

## 一句话介绍

> DSH 插件：定时循环（/loop 命令 + loop 工具 + 活动状态条）。官方 bundle 插件，dsh plugin --profile web add 安装

## 详细介绍

**Tool** (registered via `defineTool`, the model can self-adjust on every turn): **Commands** (user side): **UI** (dock slot above the input box on the chat page):

## 📦 安装

```bash
dsh plugin --profile web add "github:vlln/dsh-loop#main"   # one-line git source (build artifacts committed)
# or npm source: dsh plugin --profile web add @vlln/dsh-loop@0.3.0
```

## 🚀 快速开始

```bash
pnpm install
pnpm run build      # tsdown: Node half (lib/index.mjs) + client bundle (lib/client.js)
```

## 📚 更多信息

**Settings**

The plugin ships a settings card in **Settings → Plugins** (official `ctx.settings` namespace `dsh-loop`, rendered via the `settings.plugin.item` slot next to the official plugin cards). **Each tool gets its own row with an official-looking Switch:** The card fields are driven by the client `LOOP_TOOL_FIELDS` table, mirrored one-to-one by the Node-side tool definition table — adding a tool means a

**Installation**

**Recommended: one-line install from a git source** (build artifacts are committed, so a git source does not trigger a build): dsh plugin --profile web add "github:vlln/dsh-loop#main" # one-line git source (build artifacts committed)

## 🔗 链接

- [GitHub 仓库](https://github.com/vlln/dsh-loop)
- [完整 README](https://github.com/vlln/dsh-loop#readme)
- [返回dsh-loop所在分类](../workflows.md)
