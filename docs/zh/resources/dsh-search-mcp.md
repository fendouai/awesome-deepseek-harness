---
title: "dsh-search-mcp"
description: "用搜索 MCP 服务器（Tavily/Brave/Exa/Perplexity/DDG）替换 DSH 内置搜索。"
keywords: "dsh-search-mcp, mcp, integration, search, deepseek harness, dsh"
---
# dsh-search-mcp

> ⭐ **12** · ✅ 活跃 · 集成 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | MCP |
| 星数 | ⭐ 12 | 状态 | ✅ 活跃 |
| 作者 | [gxpppp](https://github.com/gxpppp) | 更新时间 | 2026-08-19 |

## 一句话介绍

> 用搜索 MCP 服务器（Tavily/Brave/Exa/Perplexity/DDG）替换 DSH 内置搜索。

## 详细介绍

- 模型侧继续使用原生 `web_search`，插件只替换底层 search provider。 - 支持 Tavily、Brave、Exa、Perplexity、DuckDuckGo 和自定义 HTTP/stdio MCP。 - 已知 provider 只需选择服务商并填写 CDKey/API key，不需要填写 URL、命令、鉴权参数或工具名。 - 自定义 MCP 保留 URL、stdio 命令、鉴权方式和工具名等高级配置。 - 密钥通过 DSH credentials domain 写入；设置读取接口只返回是否已配置，不返回密钥值。 - DSH RC2 支持一次 `web_search` 提交多个查询，默认上限为 4。 - 卸载插件后 bundle 覆盖层随之移除，DSH 内置搜索组合恢复。

## ✨ 核心特性

- 模型侧继续使用原生 `web_search`，插件只替换底层 search provider。
- 支持 Tavily、Brave、Exa、Perplexity、DuckDuckGo 和自定义 HTTP/stdio MCP。
- 已知 provider 只需选择服务商并填写 CDKey/API key，不需要填写 URL、命令、鉴权参数或工具名。
- 自定义 MCP 保留 URL、stdio 命令、鉴权方式和工具名等高级配置。
- 密钥通过 DSH credentials domain 写入；设置读取接口只返回是否已配置，不返回密钥值。
- DSH RC2 支持一次 `web_search` 提交多个查询，默认上限为 4。
- 卸载插件后 bundle 覆盖层随之移除，DSH 内置搜索组合恢复。

## 📦 安装

```bash
git clone https://github.com/gxpppp/dsh-search-mcp.git
cd dsh-search-mcp
npm install
dsh plugin --profile web add link:<dsh-search-mcp 的绝对路径>
dsh web
```

## 🚀 快速开始

```bash
TAVILY_API_KEY: <your-key>
EXA_API_KEY: <your-key>
PERPLEXITY_API_KEY: <your-key>
BRAVE_API_KEY: <your-key>
```

## 📚 更多信息

**安装**

git clone https://github.com/gxpppp/dsh-search-mcp.git cd dsh-search-mcp npm install dsh plugin --profile web add link:<dsh-search-mcp 的绝对路径> dsh web `link:` 会让源码更新直接作用于 profile。修改或升级浏览器 bundle 后需要重启 DSH Web 并刷新页面。 如果 profile 中已有独立搜索 MCP 行，建议先移除重复入口，避免同时暴露 `mcp__...` 工具和本插件提供的 `web_search`。

## 🔗 链接

- [GitHub 仓库](https://github.com/gxpppp/dsh-search-mcp)
- [完整 README](https://github.com/gxpppp/dsh-search-mcp#readme)
- [返回dsh-search-mcp所在分类](../integrations.md)
