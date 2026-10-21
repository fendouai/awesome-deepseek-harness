---
title: "dsh-serper-search"
description: "DeepSeek Search API（官方自研搜索引擎）+ serper.dev（Google 搜索）双擎互补的搜索插件，接入 DeepSeek Harness 的 web 能力缝（ctx.web）。安装后，DSH 内置的 web_search 每次只发两次直连检索请求（native:true 且两路可用时；单路缺 key 或 native:false 时只发一次，无辅助模型调用），结果按 URL 去重后以 固定比例交错（默认 2:1）合并，让模型同时拿到 DeepSeek 自有索引与 Google 索引。"
keywords: "dsh-serper-search, search, plugin, coding, deepseek harness, dsh"
---
# dsh-serper-search

> ⭐ **1** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 1 | Status | ✅ active |
| Author | [Minokun](https://github.com/Minokun) | Updated | — |

## One-liner

> DeepSeek Search API（官方自研搜索引擎）+ serper.dev（Google 搜索）双擎互补的搜索插件，接入 DeepSeek Harness 的 web 能力缝（ctx.web）。安装后，DSH 内置的 web_search 每次只发两次直连检索请求（native:true 且两路可用时；单路缺 key 或 native:false 时只发一次，无辅助模型调用），结果按 URL 去重后以 固定比例交错（默认 2:1）合并，让模型同时拿到 DeepSeek 自有索引与 Google 索引。

## About

DeepSeek Search API（官方自研搜索引擎）+ serper.dev（Google 搜索）双擎互补的搜索插件，接入 DeepSeek Harness 的 web 能力缝（ctx.web）。安装后，DSH 内置的 web_search 每次只发两次直连检索请求（native:true 且两路可用时；单路缺 key 或 native:false 时只发一次，无辅助模型调用），结果按 URL 去重后以 固定比例交错（默认 2:1）合并，让模型同时拿到 DeepSeek 自有索引与 Google 索引。

## 🔗 Links

- [GitHub Repository](https://github.com/Minokun/dsh-serper-search)
- [Full README](https://github.com/Minokun/dsh-serper-search#readme)
- [Back to the Plugins list](../plugins.md)
