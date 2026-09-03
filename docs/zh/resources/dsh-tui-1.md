---
title: "dsh-tui"
description: "An open-source terminal front door for DeepSeek Harness (dsh)."
keywords: "dsh-tui, terminal, client, coding, deepseek harness, dsh"
---
# dsh-tui

> ⭐ **14** · ✅ 活跃 · 客户端

| | | | |
|---|---|---|---|
| 类型 | 客户端 | 分类 | 终端 |
| 星数 | ⭐ 14 | 状态 | ✅ 活跃 |
| 作者 | [tomowang](https://github.com/tomowang) | 更新时间 | — |

## 一句话介绍

> An open-source terminal front door for DeepSeek Harness (dsh).

## 详细介绍

[简体中文](README.zh-CN.md) · [Changelog](CHANGELOG.md) A small terminal UI for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness), built as an out-of-tree DSH profile bundle. It is intentionally optimized for one-person daily use: start in the current directory, chat immediately, close the terminal, and continue the same workspace later.

## 📦 安装

```bash
npm install -g @deepseek-ai/dsh
npm install -g github:orriduck/dsh-tui
```

## 🚀 快速开始

```bash
dsh-tui                         # new session in the current directory
dsh-tui -c                      # continue the newest session for this directory
dsh-tui "fix the failing test"  # start with a prompt
dsh-tui -r <session-id>         # resume an exact session
```

## 📚 更多信息

**Quick start**

Open a terminal in the project you want DeepSeek to work on: cd /path/to/your/project dsh-tui To continue the newest session for that same project later: cd /path/to/your/project dsh-tui -c

**Install**

Requirements: Node.js 22+, `pnpm`, and the official DeepSeek Harness CLI. npm install -g @deepseek-ai/dsh npm install -g github:orriduck/dsh-tui Then enter any project and run: cd /path/to/your/project dsh-tui The first launch creates the local `tui` profile and registers this bundle automatically. DSH remains responsible for credentials, model settings, sessions, tools, sandboxing, and approvals.

## 🔗 链接

- [GitHub 仓库](https://github.com/tomowang/dsh-tui)
- [完整 README](https://github.com/tomowang/dsh-tui#readme)
- [返回dsh-tui所在分类](../clients.md)
