---
title: "dsh-stickers"
description: "DSH WebUI sticker plugin for bidirectional user and agent reactions"
keywords: "dsh-stickers, fun, plugin, coding, deepseek harness, dsh"
---
# dsh-stickers

> ⭐ **21** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Fun & lifestyle |
| Stars | ⭐ 21 | Status | ✅ active |
| Author | [william-jin-cmu](https://github.com/william-jin-cmu) | Updated | 2026-08-13 |

## One-liner

> DSH WebUI sticker plugin for bidirectional user and agent reactions

## About

`@dsh-external/dsh-stickers` 是一个纯 DSH 外部插件：同一份 catalog 同时服务 WebUI 用户的表情选择器、`/sticker` 命令和 Agent 的 `send_sticker` tool，不修改 DSH core。

## ✨ Key Features

- 用户在 WebUI 点击 🐋 选择器，或输入 `/sticker <id> [black]`。
- 24 张表情全部提供蓝鲸娘 / 黑鲸娘两套角色：选择器顶部可切换角色（默认蓝鲸娘），切换后发送同一张表情的黑鲸版本。
- Agent 在普通对话中按语境调用 `send_sticker({ id, variant? })`，不是等用户明确索要表情。
- 14 张 public 表情对双方开放，其中 4 张是工作流反应：`tests-passed`、`root-cause`、`running-tests`、`fixed-review`。
- 10 张彩蛋只出现在 Agent tool schema 中；用户命令和选择器都无法访问，例如 `restart-myself`、`hot-update`、`subagents-down`。
- Web 图片由插件自己的 `/api/dsh-stickers/*` route 提供，用户和 Agent 的卡片都进入持久会话历史。

## 📦 Install

```bash
pnpm install
pnpm run typecheck
pnpm test
pnpm run build

export DSH_HOME=/absolute/path/to/an/isolated-dsh-home
dsh plugin --profile web add /absolute/path/to/dsh-stickers
dsh web
```

## 📚 Learn more

**本地安装**

需要 Node 22 和一个可运行的 DSH checkout。 pnpm install pnpm run typecheck pnpm test pnpm run build export DSH_HOME=/absolute/path/to/an/isolated-dsh-home dsh plugin --profile web add /absolute/path/to/dsh-stickers dsh web

## 🔗 Links

- [GitHub Repository](https://github.com/william-jin-cmu/dsh-stickers)
- [Full README](https://github.com/william-jin-cmu/dsh-stickers#readme)
- [Back to the Plugins list](../plugins.md)
