---
title: "dsh-oauth-mcp-client"
description: "OAuth 2.1 Streamable HTTP MCP 客户端插件。"
keywords: "dsh-oauth-mcp-client, mcp, integration, security, deepseek harness, dsh"
---
# dsh-oauth-mcp-client

> ⭐ **9** · ✅ 活跃 · 集成 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | MCP |
| 星数 | ⭐ 9 | 状态 | ✅ 活跃 |
| 作者 | [springbrand-lab](https://github.com/springbrand-lab) | 更新时间 | 2026-08-14 |

## 一句话介绍

> OAuth 2.1 Streamable HTTP MCP 客户端插件。

## 详细介绍

An OAuth 2.1 Streamable HTTP MCP client plugin for [DeepSeek Harness](https://github.com/deepseek-ai/DeepSeek-Harness). It extends the native `dsh-mcp-client` connection flow with PKCE, dynamic client registration, browser authorization, a loopback callback, persistent token storage, reconnect handling, and MCP tool registration. The bundled configuration connects to the Springbrand production MCP Gateway. This plugin is maintained by [SpringBrand](https://springbrand.ai), an AI-assisted marketplace for business services. See the [SpringBrand DeepSeek Harness page](https://springbrand.ai/deepseek-harness) for product information.

## ✨ 核心特性

- OAuth 2.1 authorization code flow with PKCE
- Dynamic OAuth client registration
- Browser login with a loopback callback
- Token and client metadata storage through the DSH credential service
- Streamable HTTP transport with automatic reconnects
- MCP tool discovery, registration, and execution
- DSH Web connection management with live status and capability discovery
- One-click persistent connection setup followed by browser OAuth

## 📦 安装

```bash
git clone https://github.com/springbrand-lab/dsh-oauth-mcp-client.git
cd dsh-oauth-mcp-client
corepack enable
pnpm install
pnpm build
```

## 🚀 快速开始

```bash
PLUGIN_DIR="$PWD"
npx --yes @deepseek-ai/dsh@latest plugin --profile web add "$PLUGIN_DIR"
npx --yes @deepseek-ai/dsh@latest web
```

## 📚 更多信息

**Install**

Clone and build the plugin: git clone https://github.com/springbrand-lab/dsh-oauth-mcp-client.git cd dsh-oauth-mcp-client corepack enable pnpm install pnpm build Install the built checkout into a DSH profile and start DSH: PLUGIN_DIR="$PWD" npx --yes @deepseek-ai/dsh@latest plugin --profile web add "$PLUGIN_DIR" npx --yes @deepseek-ai/dsh@latest web This repository is not published to npm, so inst

**Configuration**

The bundled defaults are defined in [`springbrand.cordis.yml`](./springbrand.cordis.yml):

**Manual configuration**

The Web page is the default setup path. To configure a connection manually, add it to the same permanent Web profile file at `~/.dsh/profiles/web/cordis.patch.yml`: - id: my-oauth-mcp name: '@dsh-external/dsh-oauth-mcp-client' config: serverName: my-mcp url: https://mcp.example.com/mcp credentialRef: MY_MCP_OAUTH failOnStartupError: true The server must support OAuth and MCP Streamable HTTP. Its f

## 🔗 链接

- [GitHub 仓库](https://github.com/springbrand-lab/dsh-oauth-mcp-client)
- [完整 README](https://github.com/springbrand-lab/dsh-oauth-mcp-client#readme)
- [返回dsh-oauth-mcp-client所在分类](../integrations.md)
