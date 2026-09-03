---
title: "dsh-mcp-manager"
description: "MCP server manager: Settings page with OAuth (PKCE + dynamic client registration) or static-token auth."
keywords: "dsh-mcp-manager, mcp, integration, ui, deepseek harness, dsh"
---
# dsh-mcp-manager

> ⭐ **10** · ✅ active · integration · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | integration | Category | MCP |
| Stars | ⭐ 10 | Status | ✅ active |
| Author | [hyqhyq3](https://github.com/hyqhyq3) | Updated | 2026-08-16 |

## One-liner

> MCP server manager: Settings page with OAuth (PKCE + dynamic client registration) or static-token auth.

## About

[简体中文](README.zh-CN.md) | English **MCP server manager for [DeepSeek Harness (DSH)](https://github.com/deepseek-ai/deepseek-harness)** — a Settings → MCP page where you add MCP servers once (remote HTTP or local stdio process), authenticate HTTP servers with **OAuth in the browser**, and expose their tools either directly or through a compact on-demand broker. The built-in `@deepseek-ai/dsh-mcp-client` only accepts a static `headers` config — it has no OAuth support and no local stdio transport. This plugin fills that gap: - **OAuth (authorization code + PKCE)** with RFC 7591 dynamic client registration, `refresh_token` rotation, and auto-reconnect across restarts — one browser login, then it keeps working. - **Static Bearer token** mode for servers without OAuth — stored as an environment

## ✨ Key Features

- **OAuth (authorization code + PKCE)** with RFC 7591 dynamic client registration, `refresh_token` rotation, and auto-reconnect across restarts — one browser logi
- **Static Bearer token** mode for servers without OAuth — stored as an environment-variable **name** (Codex-style `tokenEnv`), never as plaintext in the config.
- **Custom HTTP headers** (`headers` for direct values, `headerEnv` for values read from environment variables) — matches Codex's `http_headers` / `env_http_heade
- **stdio local processes**: run `npx` / `uvx` / `python` etc. directly; the plugin speaks JSON-RPC over the child's stdin/stdout (spawns the process, reconnects,
- **Edit-in-place**: rename a server, switch stdio ↔ HTTP, or change auth/headers without deleting and re-adding it.
- **Tool registration** with the same `mcp__<server>__<rawName>` naming convention as the built-in client, including strict-schema sanitization for the DSH tool r

## 📦 Install

```bash
npx -p @deepseek-ai/dsh dsh plugin --profile web add github:hyqhyq3/dsh-mcp-manager
```

## 🚀 Quick Start

```bash
mcp__odin__search_tools     mcp__odin__describe_tool
mcp__odin__execute_tool     mcp__odin__list_tool_scopes
```

## 📚 Learn more

**Install**

npx -p @deepseek-ai/dsh dsh plugin --profile web add github:hyqhyq3/dsh-mcp-manager Then restart `dsh --profile web` and refresh the page. The package declares a `dsh.bundle.patch`, so the plugin activates automatically — no manual `cordis.patch.yml` editing. > The MCP server's OAuth provider must allow a loopback redirect (`http://127.0.0.1:<port>/mcp-manager/callback/<id>`), which is where the D

**Usage**

1. Open **Settings → MCP** in the DSH web UI. 2. **＋ Add MCP server** (and later **编辑 / Edit** to change it): - **Scope (作用域)**: `user` — a global server available in every workspace; or `workspace` — a server bound to one workspace (its config lives in that workspace's `.dsh/dshmm/mcp.json`). Pick the workspace from the second dropdown. - **HTTP**: name (becomes the `mcp__<name>__*` prefix), URL,

## 🔗 Links

- [GitHub Repository](https://github.com/hyqhyq3/dsh-mcp-manager)
- [Full README](https://github.com/hyqhyq3/dsh-mcp-manager#readme)
- [Back to the MCP & Integrations list](../integrations.md)
