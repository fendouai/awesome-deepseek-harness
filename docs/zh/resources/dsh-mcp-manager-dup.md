---
title: "dsh-mcp-manager"
description: "MCP 服务器管理器：设置页 OAuth（PKCE + 动态客户端注册）或静态 Token 认证。"
keywords: "dsh-mcp-manager, mcp, integration, ui, deepseek harness, dsh"
---
# dsh-mcp-manager

> ⭐ **10** · ✅ 活跃 · 集成 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | MCP |
| 星数 | ⭐ 10 | 状态 | ✅ 活跃 |
| 作者 | [hyqhyq3](https://github.com/hyqhyq3) | 更新时间 | 2026-08-16 |

## 一句话介绍

> MCP 服务器管理器：设置页 OAuth（PKCE + 动态客户端注册）或静态 Token 认证。

## 详细介绍

[简体中文](README.zh-CN.md) | English **MCP server manager for [DeepSeek Harness (DSH)](https://github.com/deepseek-ai/deepseek-harness)** — a Settings → MCP page where you add MCP servers once (remote HTTP or local stdio process), authenticate HTTP servers with **OAuth in the browser**, and expose their tools either directly or through a compact on-demand broker. The built-in `@deepseek-ai/dsh-mcp-client` only accepts a static `headers` config — it has no OAuth support and no local stdio transport. This plugin fills that gap: - **OAuth (authorization code + PKCE)** with RFC 7591 dynamic client registration, `refresh_token` rotation, and auto-reconnect across restarts — one browser login, then it keeps working. - **Static Bearer token** mode for servers without OAuth — stored as an environment

## ✨ 核心特性

- **OAuth (authorization code + PKCE)** with RFC 7591 dynamic client registration, `refresh_token` rotation, and auto-reconnect across restarts — one browser logi
- **Static Bearer token** mode for servers without OAuth — stored as an environment-variable **name** (Codex-style `tokenEnv`), never as plaintext in the config.
- **Custom HTTP headers** (`headers` for direct values, `headerEnv` for values read from environment variables) — matches Codex's `http_headers` / `env_http_heade
- **stdio local processes**: run `npx` / `uvx` / `python` etc. directly; the plugin speaks JSON-RPC over the child's stdin/stdout (spawns the process, reconnects,
- **Edit-in-place**: rename a server, switch stdio ↔ HTTP, or change auth/headers without deleting and re-adding it.
- **Tool registration** with the same `mcp__<server>__<rawName>` naming convention as the built-in client, including strict-schema sanitization for the DSH tool r

## 📦 安装

```bash
npx -p @deepseek-ai/dsh dsh plugin --profile web add github:hyqhyq3/dsh-mcp-manager
```

## 🚀 快速开始

```bash
mcp__odin__search_tools     mcp__odin__describe_tool
mcp__odin__execute_tool     mcp__odin__list_tool_scopes
```

## 📚 更多信息

**Install**

npx -p @deepseek-ai/dsh dsh plugin --profile web add github:hyqhyq3/dsh-mcp-manager Then restart `dsh --profile web` and refresh the page. The package declares a `dsh.bundle.patch`, so the plugin activates automatically — no manual `cordis.patch.yml` editing. > The MCP server's OAuth provider must allow a loopback redirect (`http://127.0.0.1:<port>/mcp-manager/callback/<id>`), which is where the D

**Usage**

1. Open **Settings → MCP** in the DSH web UI. 2. **＋ Add MCP server** (and later **编辑 / Edit** to change it): - **Scope (作用域)**: `user` — a global server available in every workspace; or `workspace` — a server bound to one workspace (its config lives in that workspace's `.dsh/dshmm/mcp.json`). Pick the workspace from the second dropdown. - **HTTP**: name (becomes the `mcp__<name>__*` prefix), URL,

## 🔗 链接

- [GitHub 仓库](https://github.com/hyqhyq3/dsh-mcp-manager)
- [完整 README](https://github.com/hyqhyq3/dsh-mcp-manager#readme)
- [返回dsh-mcp-manager所在分类](../integrations.md)
