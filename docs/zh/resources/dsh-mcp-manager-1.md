---
title: "dsh-mcp-manager"
description: "在 DeepSeek Harness 设置页管理 MCP 服务器：运行时添加/编辑/启停/重连/删除，实时状态、自动重连，中英双语界面。MCP server manager for DeepSeek Harness — add, edit, enable/disable, reconnect & delete MCP servers from the web settings page, with live status and auto-reconnect."
keywords: "dsh-mcp-manager, mcp, integration, coding, deepseek harness, dsh"
---
# dsh-mcp-manager

> ⭐ **3** · ✅ 活跃 · 集成

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | MCP |
| 星数 | ⭐ 3 | 状态 | ✅ 活跃 |
| 作者 | [Nichts0v0](https://github.com/Nichts0v0) | 更新时间 | 2026-08-21 |

## 一句话介绍

> 在 DeepSeek Harness 设置页管理 MCP 服务器：运行时添加/编辑/启停/重连/删除，实时状态、自动重连，中英双语界面。MCP server manager for DeepSeek Harness — add, edit, enable/disable, reconnect & delete MCP servers from the web settings page, with live status and auto-reconnect.

## 详细介绍

[English](README.md) | [中文](README.zh.md) · · Manage **MCP servers** right from the DeepSeek Harness Web settings page — add, edit, enable/disable, reconnect and delete servers at runtime, with live status, automatic reconnect and config-file hot sync.

## ✨ 核心特性

- **Web settings UI** — a dedicated "MCP Server Manager" page: server cards with live status, an add/edit form, and two-step delete protection.
- **OAuth 2.0 / RFC 9728 support** — native MCP OAuth 2.1 authorization with PKCE, automated metadata discovery, browser-based login flow, token auto-refresh and 
- **Runtime connections** — servers connect/disconnect on the fly; tools are registered globally as `mcp__<serverName>__<tool>` for every session.
- **Live status** — reachability probing so a closed server shows **offline** instead of a stale "connected"; a stuck connection times out after 30 s.
- **Auto-reconnect** — a failed initial connect retries with exponential backoff (3 s → 60 s); pressing refresh retries immediately.
- **Enable/disable** — switch a server off to disconnect and unload its tools; switch it on to reconnect.
- **Config file hot sync** — `$DSH_HOME/mcp-servers.json` is watched; external edits take effect within ~1 s, no restart needed.
- **Themes & i18n** — follows DSH light/dark mode (and `--dsw-alias-*` token overrides from appearance plugins); UI ships in **简体中文 / English**.

## 📦 安装

```bash
dsh plugin --profile web add dsh-mcp-manager
```

## 🚀 快速开始

```bash
git clone https://github.com/Nichts0v0/dsh-mcp-manager.git
   cd dsh-mcp-manager && npm install      # the prepare script builds lib/ automatically
```

## 📚 更多信息

**Configuration file**

`$DSH_HOME/mcp-servers.json` — shared by every profile and session: { "version": 1, "servers": [ { "serverName": "my-http-server", "transport": "streamable-http", "url": "http://127.0.0.1:8080/mcp", "enabled": true }, { "serverName": "my-oauth-server", "transport": "streamable-http", "url": "https://api.example.com/mcp", "authType": "oauth", "enabled": true, "oauth": { "clientId": "client-id-123",

## 🔗 链接

- [GitHub 仓库](https://github.com/Nichts0v0/dsh-mcp-manager)
- [完整 README](https://github.com/Nichts0v0/dsh-mcp-manager#readme)
- [返回dsh-mcp-manager所在分类](../integrations.md)
