---
title: "dsh-vercel-mcp"
description: "Vercel MCP connection for DeepSeek Harness: official OAuth 2.0 flow (dynamic client registration + PKCE) against mcp.vercel.com, Vercel API tools under mcp__vercel__*, and a web settings panel."
keywords: "dsh-vercel-mcp, mcp, plugin, deepseek harness, dsh"
---
# dsh-vercel-mcp

> ⭐ **0** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | MCP |
| Stars | ⭐ 0 | Status | ✅ active |
| Author | [zhengjy01](https://github.com/zhengjy01) | Updated | — |

## One-liner

> Vercel MCP connection for DeepSeek Harness: official OAuth 2.0 flow (dynamic client registration + PKCE) against mcp.vercel.com, Vercel API tools under mcp__vercel__*, and a web settings panel.

## About

Vercel MCP connection for DeepSeek Harness (DSH): the official Vercel API MCP server ([mcp.vercel.com](https://mcp.vercel.com)) with the full OAuth 2.0 client dance — dynamic client registration, PKCE S256, loopback callback on the GUI's own web server, refresh-token grant — plus a web settings panel. Once authorized, the Vercel platform tools (deployments, projects, domains, environment variables, DNS records, deploy code, and more) become available in agent sessions as `mcp__vercel__*`, auto-refreshing its token on 401.

## 📦 Install

```bash
# local development (link)
dsh plugin --profile web add link:/path/to/dsh-vercel-mcp
```

## 🚀 Quick Start

```bash
pnpm install
npm run typecheck
npm run test                  # offline store/provider smoke
DSH_VERCEL_MCP_LIVE=1 npm run test   # live OAuth phase-1 against mcp.vercel.com
npm run build                 # tsc declarations + tsdown (lib/ + lib/client.js)
```

## 🔗 Links

- [GitHub Repository](https://github.com/zhengjy01/dsh-vercel-mcp)
- [Full README](https://github.com/zhengjy01/dsh-vercel-mcp#readme)
- [Back to the Plugins list](../plugins.md)
