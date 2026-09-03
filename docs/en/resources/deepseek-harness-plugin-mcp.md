---
title: "deepseek-harness-plugin-mcp"
description: "MCP server that lets any agent discover, install, and run DeepSeek Harness plugins (topic: dsh-plugin)."
keywords: "deepseek-harness-plugin-mcp, mcp, integration, coding, multi-agent, deepseek harness, dsh"
---
# deepseek-harness-plugin-mcp

> ⭐ **3** · ✅ active · integration

| | | | |
|---|---|---|---|
| Type | integration | Category | MCP |
| Stars | ⭐ 3 | Status | ✅ active |
| Author | [bobleer](https://github.com/bobleer) | Updated | — |

## One-liner

> MCP server that lets any agent discover, install, and run DeepSeek Harness plugins (topic: dsh-plugin).

## About

Made by [BitFun](https://github.com/GCWing/BitFun/). MCP server that lets **any agent** discover, inspect, install, and run [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) plugins. Catalog source: [github.com/topics/dsh-plugin](https://github.com/topics/dsh-plugin).

## 📦 Install

```bash
npm install -g deepseek-harness-plugin-mcp
# or
npx deepseek-harness-plugin-mcp --help
```

## 🚀 Quick Start

```bash
{
  "mcpServers": {
    "dsh-plugins": {
      "command": "npx",
      "args": ["-y", "deepseek-harness-plugin-mcp"],
      "env": {
        "GITHUB_TOKEN": "ghp_optional_but_recommended"
      }
    }
  }
}
```

## 🔗 Links

- [GitHub Repository](https://github.com/bobleer/deepseek-harness-plugin-mcp)
- [Full README](https://github.com/bobleer/deepseek-harness-plugin-mcp#readme)
- [Back to the MCP & Integrations list](../integrations.md)
