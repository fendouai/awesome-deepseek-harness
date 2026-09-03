---
title: "dsh-tavily"
description: "为 DSH 新增 Tavily 搜索 API，作为其网页搜索服务提供商。Adds Tavily Search API as a web search provider for DSH."
keywords: "dsh-tavily, search, plugin, coding, deepseek harness, dsh"
---
# dsh-tavily

> ⭐ **4** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 搜索与研究 |
| 星数 | ⭐ 4 | 状态 | ✅ 活跃 |
| 作者 | [SZMY-haruhi](https://github.com/SZMY-haruhi) | 更新时间 | — |
| 子分类 | 🌐 网页搜索 | 能力 | coding, search |

## 一句话介绍

> 为 DSH 新增 Tavily 搜索 API，作为其网页搜索服务提供商。Adds Tavily Search API as a web search provider for DSH.

## 详细介绍

Tavily web search for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (DSH) as an **opt-in extra search tool** — with **multiple API keys**, **rotation/failover**, **live usage gauge**, **direct `extract` / `map` / `crawl` tools**, and a settings card in the Plugins configuration tab. The built-in `web_search` tool is **never replaced**: Tavily is an *option* on top of the native search, not a swap-in for it. This plugin registers no web-search provider and never rewrites `web.searchProvider`.

## ✨ 核心特性

- 🔑 **Multiple Tavily API keys** — manage a flat key list from the DSH settings UI.
- 🔁 **Key rotation & failover** — round-robin across keys; automatically retries on HTTP 401/429.
- 📊 **Live usage gauge** — per-key Tavily usage and totals, fetched server-side without exposing keys.
- ⚡ **Direct Tavily tools** — `tavily_extract` reads a known URL's content, `tavily_map` discovers a site's links, and `tavily_crawl` pulls an entire site, all un

## 📦 安装

```bash
# from the repository — always the latest source
dsh plugin --profile web add github:moguiyu/dsh-tavily

# from the npm release — the stable, marketplace-counted version
dsh plugin --profile web add @moguiyu/dsh-tavily
```

## 🚀 快速开始

```bash
pnpm install
pnpm test
pnpm build
```

## 📚 更多信息

**Install**

Either of these installs the `dsh-tavily` row (both resolve to the same plugin, but install with `--profile <name>`):

## 🔗 链接

- [GitHub 仓库](https://github.com/SZMY-haruhi/dsh-tavily)
- [完整 README](https://github.com/SZMY-haruhi/dsh-tavily#readme)
- [返回dsh-tavily所在分类](../plugins.md)
