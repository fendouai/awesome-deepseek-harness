---
title: "dsh-memento"
description: "Bounded, layered, approval-gated and auditable cross-session memory with frozen snapshot injection."
keywords: "dsh-memento, memory, plugin, security, deepseek harness, dsh"
---
# dsh-memento

> ⭐ **59** · ✅ active · plugin · ⬆️ +2 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Memory & context |
| Stars | ⭐ 59 | Status | ✅ active |
| Author | [PerryLink](https://github.com/PerryLink) | Updated | 2026-08-21 |
| Subcategory | 🧠 Memory systems | Capabilities | memory, security |

## One-liner

> Bounded, layered, approval-gated and auditable cross-session memory with frozen snapshot injection.

## About

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-memento` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **Bounded, layered, approval-gated, auditable cross-session memory for DeepSeek Harness.** *A typed `ctx.memory` seam, a write-approval gate no model path can bypass, and audit trails rebuilt from the session log.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ Key Features

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-memento` (counts toward the [deepseek1024.com](https://deepseek1024.

## 📦 Install

```bash
# 1. install the bundle into your profile
dsh plugin --profile web add "github:PerryLink/dsh-memento#main"

# or from npm (published releases)
dsh plugin --profile web add dsh-memento

# 2. restart and verify the row
dsh --profile web --dump-config | grep -A3 'id: memento'
```

## 🚀 Quick Start

```bash
node bin/mcp-server.mjs
# or, after npm install: npx dsh-memento-mcp
```

## 📚 Learn more

**Configuration**

All tunables are Schemastery `Config` fields (changeable from cordis.yml). Invalid values fail loudly at load. Override under the `memento` row. **Settings panel.** When the DSH settings service is mounted, every field below (except `enabled`) is editable from the plugin's own **`dsh-memento` entry in the DSH settings sidebar** (a top-level section, like General or Plugins); edits land in the sett

**or, after npm install: npx dsh-memento-mcp**

The database path is `$DSH_MEMENTO_DB_PATH` (absolute, or relative to `$DSH_HOME`); it defaults to `$DSH_HOME/dsh-memento/memory.db`. Claude Desktop (`claude_desktop_config.json`) example: { "mcpServers": { "dsh-memento": { "command": "npx", "args": ["-y", "dsh-memento-mcp"], "env": { "DSH_MEMENTO_DB_PATH": "/home/you/.dsh/dsh-memento/memory.db" } } } } The server is read-only: no network, no writ

## 🔗 Links

- [GitHub Repository](https://github.com/PerryLink/dsh-memento)
- [Full README](https://github.com/PerryLink/dsh-memento#readme)
- [Back to the Plugins list](../plugins.md)
