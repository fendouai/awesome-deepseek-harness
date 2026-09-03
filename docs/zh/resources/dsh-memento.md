---
title: "dsh-memento"
description: "有界分层、审批门控、可审计的跨会话记忆，支持冻结快照注入。"
keywords: "dsh-memento, memory, plugin, security, deepseek harness, dsh"
---
# dsh-memento

> ⭐ **59** · ✅ 活跃 · 插件 · 近期 ⬆️ +2

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 记忆与上下文 |
| 星数 | ⭐ 59 | 状态 | ✅ 活跃 |
| 作者 | [PerryLink](https://github.com/PerryLink) | 更新时间 | 2026-08-21 |
| 子分类 | 🧠 记忆系统 | 能力 | memory, security |

## 一句话介绍

> 有界分层、审批门控、可审计的跨会话记忆，支持冻结快照注入。

## 详细介绍

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-memento` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **Bounded, layered, approval-gated, auditable cross-session memory for DeepSeek Harness.** *A typed `ctx.memory` seam, a write-approval gate no model path can bypass, and audit trails rebuilt from the session log.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ 核心特性

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-memento` (counts toward the [deepseek1024.com](https://deepseek1024.

## 📦 安装

```bash
# 1. install the bundle into your profile
dsh plugin --profile web add "github:PerryLink/dsh-memento#main"

# or from npm (published releases)
dsh plugin --profile web add dsh-memento

# 2. restart and verify the row
dsh --profile web --dump-config | grep -A3 'id: memento'
```

## 🚀 快速开始

```bash
node bin/mcp-server.mjs
# or, after npm install: npx dsh-memento-mcp
```

## 📚 更多信息

**Configuration**

All tunables are Schemastery `Config` fields (changeable from cordis.yml). Invalid values fail loudly at load. Override under the `memento` row. **Settings panel.** When the DSH settings service is mounted, every field below (except `enabled`) is editable from the plugin's own **`dsh-memento` entry in the DSH settings sidebar** (a top-level section, like General or Plugins); edits land in the sett

**or, after npm install: npx dsh-memento-mcp**

The database path is `$DSH_MEMENTO_DB_PATH` (absolute, or relative to `$DSH_HOME`); it defaults to `$DSH_HOME/dsh-memento/memory.db`. Claude Desktop (`claude_desktop_config.json`) example: { "mcpServers": { "dsh-memento": { "command": "npx", "args": ["-y", "dsh-memento-mcp"], "env": { "DSH_MEMENTO_DB_PATH": "/home/you/.dsh/dsh-memento/memory.db" } } } } The server is read-only: no network, no writ

## 🔗 链接

- [GitHub 仓库](https://github.com/PerryLink/dsh-memento)
- [完整 README](https://github.com/PerryLink/dsh-memento#readme)
- [返回dsh-memento所在分类](../plugins.md)
