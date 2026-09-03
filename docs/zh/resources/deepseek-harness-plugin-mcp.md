---
title: "deepseek-harness-plugin-mcp"
description: "MCP server that lets any agent discover, install, and run DeepSeek Harness plugins (topic: dsh-plugin)."
keywords: "deepseek-harness-plugin-mcp, mcp, integration, coding, multi-agent, deepseek harness, dsh"
---
# deepseek-harness-plugin-mcp

> ⭐ **3** · ✅ 活跃 · 集成

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | MCP |
| 星数 | ⭐ 3 | 状态 | ✅ 活跃 |
| 作者 | [bobleer](https://github.com/bobleer) | 更新时间 | — |

## 一句话介绍

> MCP server that lets any agent discover, install, and run DeepSeek Harness plugins (topic: dsh-plugin).

## 详细介绍

Made by [BitFun](https://github.com/GCWing/BitFun/). MCP server that lets **any agent** discover, inspect, install, and run [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) plugins. Catalog source: [github.com/topics/dsh-plugin](https://github.com/topics/dsh-plugin).

## 📦 安装

```bash
npm install -g deepseek-harness-plugin-mcp
# or
npx deepseek-harness-plugin-mcp --help
```

## 🚀 快速开始

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

## 🔗 链接

- [GitHub 仓库](https://github.com/bobleer/deepseek-harness-plugin-mcp)
- [完整 README](https://github.com/bobleer/deepseek-harness-plugin-mcp#readme)
- [返回deepseek-harness-plugin-mcp所在分类](../integrations.md)
