---
title: "dsh-mcp-panel"
description: "Read-only runtime management panel for the official DSH MCP client: /mcp command and a Settings tab."
keywords: "dsh-mcp-panel, mcp, integration, ui, observability, deepseek harness, dsh"
---
# dsh-mcp-panel

> ⭐ **26** · ✅ active · integration · ⬆️ +6 recently

| | | | |
|---|---|---|---|
| Type | integration | Category | MCP |
| Stars | ⭐ 26 | Status | ✅ active |
| Author | [PerryLink](https://github.com/PerryLink) | Updated | 2026-08-21 |

## One-liner

> Read-only runtime management panel for the official DSH MCP client: /mcp command and a Settings tab.

## About

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-mcp-panel` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **The MCP management console for the official DeepSeek Harness MCP client — add, edit, remove, and trial-call MCP servers from a settings page, with honest status, health diagnostics, and safe, reversible profile writes.** *Official client = bridge, this plugin = console: read status through the `mcp/status` seam, write only append-only, approval-gated profile patches.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ Key Features

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-mcp-panel` (counts toward the [deepseek1024.com](https://deepseek102

## 📦 Install

```bash
# 1. install the bundle into your profile
dsh plugin --profile web add "github:PerryLink/dsh-mcp-panel#main"

# or from npm (published releases)
dsh plugin --profile web add dsh-mcp-panel

# 2. restart and verify the row
dsh --profile web --dump-config | grep -A3 'id: mcp-panel'
```

## 🚀 Quick Start

```bash
/mcp
/mcp everything tools
/mcp everything health
/mcp everything call echo '{"message": "hi"}'
```

## 📚 Learn more

**Architecture: official client = bridge, this plugin = consol**

[`@deepseek-ai/dsh-mcp-client`](https://github.com/deepseek-ai/deepseek-harness/tree/master/packages/mcp/mcp-client) is the **only bridge**: one plugin instance per MCP server, configured as a hand-written `cordis.yml` row, connecting the transport, syncing tools, and registering `mcp__<server>__<tool>` names. This plugin never replaces it — it is the **experience layer on top**: ┌────────────────

**Configuration**

All tunables are Schemastery `Config` fields (changeable from cordis.yml). `cordis.patch.yml` documents each key inline.

## 🔗 Links

- [GitHub Repository](https://github.com/PerryLink/dsh-mcp-panel)
- [Full README](https://github.com/PerryLink/dsh-mcp-panel#readme)
- [Back to the MCP & Integrations list](../integrations.md)
