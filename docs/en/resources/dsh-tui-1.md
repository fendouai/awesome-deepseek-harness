---
title: "dsh-tui"
description: "An open-source terminal front door for DeepSeek Harness (dsh)."
keywords: "dsh-tui, terminal, client, coding, deepseek harness, dsh"
---
# dsh-tui

> ⭐ **14** · ✅ active · client

| | | | |
|---|---|---|---|
| Type | client | Category | Terminal |
| Stars | ⭐ 14 | Status | ✅ active |
| Author | [tomowang](https://github.com/tomowang) | Updated | — |

## One-liner

> An open-source terminal front door for DeepSeek Harness (dsh).

## About

[简体中文](README.zh-CN.md) · [Changelog](CHANGELOG.md) A small terminal UI for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness), built as an out-of-tree DSH profile bundle. It is intentionally optimized for one-person daily use: start in the current directory, chat immediately, close the terminal, and continue the same workspace later.

## 📦 Install

```bash
npm install -g @deepseek-ai/dsh
npm install -g github:orriduck/dsh-tui
```

## 🚀 Quick Start

```bash
dsh-tui                         # new session in the current directory
dsh-tui -c                      # continue the newest session for this directory
dsh-tui "fix the failing test"  # start with a prompt
dsh-tui -r <session-id>         # resume an exact session
```

## 📚 Learn more

**Quick start**

Open a terminal in the project you want DeepSeek to work on: cd /path/to/your/project dsh-tui To continue the newest session for that same project later: cd /path/to/your/project dsh-tui -c

**Install**

Requirements: Node.js 22+, `pnpm`, and the official DeepSeek Harness CLI. npm install -g @deepseek-ai/dsh npm install -g github:orriduck/dsh-tui Then enter any project and run: cd /path/to/your/project dsh-tui The first launch creates the local `tui` profile and registers this bundle automatically. DSH remains responsible for credentials, model settings, sessions, tools, sandboxing, and approvals.

## 🔗 Links

- [GitHub Repository](https://github.com/tomowang/dsh-tui)
- [Full README](https://github.com/tomowang/dsh-tui#readme)
- [Back to the Clients (Desktop & TUI) list](../clients.md)
