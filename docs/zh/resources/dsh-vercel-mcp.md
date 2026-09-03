---
title: "dsh-vercel-mcp"
description: "DeepSeek Harness 的 Vercel MCP 连接插件：官方 OAuth 2.0 客户端流程（动态客户端注册 + PKCE）对接 mcp.vercel.com，Vercel 平台工具以 mcp__vercel__* 形式在会话中可用，另有可视化设置面板。"
keywords: "dsh-vercel-mcp, mcp, plugin, deepseek harness, dsh"
---
# dsh-vercel-mcp

> ⭐ **0** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | MCP |
| 星数 | ⭐ 0 | 状态 | ✅ 活跃 |
| 作者 | [zhengjy01](https://github.com/zhengjy01) | 更新时间 | — |

## 一句话介绍

> DeepSeek Harness 的 Vercel MCP 连接插件：官方 OAuth 2.0 客户端流程（动态客户端注册 + PKCE）对接 mcp.vercel.com，Vercel 平台工具以 mcp__vercel__* 形式在会话中可用，另有可视化设置面板。

## 详细介绍

Vercel MCP connection for DeepSeek Harness (DSH): the official Vercel API MCP server ([mcp.vercel.com](https://mcp.vercel.com)) with the full OAuth 2.0 client dance — dynamic client registration, PKCE S256, loopback callback on the GUI's own web server, refresh-token grant — plus a web settings panel. Once authorized, the Vercel platform tools (deployments, projects, domains, environment variables, DNS records, deploy code, and more) become available in agent sessions as `mcp__vercel__*`, auto-refreshing its token on 401.

## 📦 安装

```bash
# local development (link)
dsh plugin --profile web add link:/path/to/dsh-vercel-mcp
```

## 🚀 快速开始

```bash
pnpm install
npm run typecheck
npm run test                  # offline store/provider smoke
DSH_VERCEL_MCP_LIVE=1 npm run test   # live OAuth phase-1 against mcp.vercel.com
npm run build                 # tsc declarations + tsdown (lib/ + lib/client.js)
```

## 🔗 链接

- [GitHub 仓库](https://github.com/zhengjy01/dsh-vercel-mcp)
- [完整 README](https://github.com/zhengjy01/dsh-vercel-mcp#readme)
- [返回dsh-vercel-mcp所在分类](../plugins.md)
