---
title: "dsh-tui"
description: "Claude Code-style terminal UI for DeepSeek Harness agents, as an out-of-tree dsh plugin bundle"
keywords: "dsh-tui, terminal, client, coding, multi-agent, ui, deepseek harness, dsh"
---
# dsh-tui

> ⭐ **24** · ✅ 活跃 · 客户端

| | | | |
|---|---|---|---|
| 类型 | 客户端 | 分类 | 终端 |
| 星数 | ⭐ 24 | 状态 | ✅ 活跃 |
| 作者 | [dsh-tui](https://github.com/dsh-tui) | 更新时间 | 2026-08-14 |

## 一句话介绍

> Claude Code-style terminal UI for DeepSeek Harness agents, as an out-of-tree dsh plugin bundle

## 详细介绍

An interactive terminal (TUI) front door for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) agents — a Claude Code / Codex-style chat interface in your terminal, installed as an out-of-tree dsh plugin bundle. Built on [`@earendil-works/pi-tui`](https://www.npmjs.com/package/@earendil-works/pi-tui). It composes over the official `@deepseek-ai/dsh-base` bundle, so the whole plugin ecosystem — shell and filesystem tools, skills, subagents, workflows, sandbox approvals — is the same one the official web surface uses. Nothing is forked.

## ✨ 核心特性

- Streaming model output and reasoning, rendered as Markdown
- Tool-call cards with terminal / diff / generic render intents; Ctrl+O cycles collapsed → expanded → hidden
- Approval and `ask_user_question` dialogs, plan-mode review included
- `@file` path autocomplete and `@session` reference cards
- Slash commands: `/model` (with reasoning-effort selection), `/resume`, `/compact`, `/details`, `/help`, and every command other plugins register
- Standing todo panel, token usage and context-pressure status line, session titles
- Configurable theme; truecolor detected from `COLORTERM`

## 📦 安装

```bash
dsh plugin --profile tui add @dsh-tui/dsh-tui
dsh --profile tui                                      # start a session in the current directory
dsh --profile tui --resume <session-id>                # resume a persisted session
```

## 🚀 快速开始

```bash
allowBuilds:
  "@dsh-tui/dsh-tui": true
```

## 📚 更多信息

**Install**

Requires Node `^22.19 || >=24` and the `dsh` CLI (`npm i -g @deepseek-ai/dsh@next`). dsh plugin --profile tui add @dsh-tui/dsh-tui dsh --profile tui # start a session in the current directory dsh --profile tui --resume <session-id> # resume a persisted session To track the repo instead of the npm release, use `add github:dsh-tui/dsh-tui`. Git-hosted plugins build on install via their `prepare` scr

## 🔗 链接

- [GitHub 仓库](https://github.com/dsh-tui/dsh-tui)
- [完整 README](https://github.com/dsh-tui/dsh-tui#readme)
- [返回dsh-tui所在分类](../clients.md)
