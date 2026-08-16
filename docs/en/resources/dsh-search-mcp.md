---
title: "dsh-search-mcp"
description: "Replace DSH's built-in web search with search MCP servers (Tavily/Brave/Exa/Perplexity/DuckDuckGo)."
keywords: "dsh-search-mcp, mcp, integration, search, deepseek harness, dsh"
---
# dsh-search-mcp

> ⭐ 8 · ✅ active · integration

## One-liner

Replace DSH's built-in web search with search MCP servers (Tavily/Brave/Exa/Perplexity/DuckDuckGo).

## About

用**搜索类 MCP 服务器**完全替代 DeepSeek Harness（dsh）内置搜索的独立插件。 - 模型侧 `web_search` 工具**保留原名、原展示**，但执行全部走你配置的搜索 MCP 服务器（Tavily / Brave / Exa / Perplexity / DuckDuckGo / 任意自定义 MCP）。 - 插件启用期间**内置 DeepSeek 搜索 provider 不可用**（`web-search-deepseek` 行被禁用，`web.searchProvider` 切到 `search-mcp`）；卸载插件即完全还原。 - 所有服务器配置（类型、端点/命令、API key 或 key 环境变量、工具名）都可以在 **Web 设置 → Plugins → search-mcp** 卡片里增删改，保存后即时生效，无需重启。

## Author
**[gxpppp](https://github.com/gxpppp)**

## Links

- [GitHub Repository](https://github.com/gxpppp/dsh-search-mcp)
- [Full README](https://github.com/gxpppp/dsh-search-mcp#readme)
- [Back to the MCP & Integrations list](../integrations.md)
