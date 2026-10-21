---
title: "dsh-serper-search"
description: "DeepSeek Search API（官方自研搜索引擎）+ serper.dev（Google 搜索）双擎互补的搜索插件，接入 DeepSeek Harness 的 web 能力缝（ctx.web）。安装后，DSH 内置的 web_search 每次只发两次直连检索请求（native:true 且两路可用时；单路缺 key 或 native:false 时只发一次，无辅助模型调用），结果按 URL 去重后以 固定比例交错（默认 2:1）合并，让模型同时拿到 DeepSeek 自有索引与 Google 索引。"
keywords: "dsh-serper-search, search, plugin, coding, deepseek harness, dsh"
---
# dsh-serper-search

> ⭐ **1** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 搜索与研究 |
| 星数 | ⭐ 1 | 状态 | ✅ 活跃 |
| 作者 | [Minokun](https://github.com/Minokun) | 更新时间 | — |

## 一句话介绍

> DeepSeek Search API（官方自研搜索引擎）+ serper.dev（Google 搜索）双擎互补的搜索插件，接入 DeepSeek Harness 的 web 能力缝（ctx.web）。安装后，DSH 内置的 web_search 每次只发两次直连检索请求（native:true 且两路可用时；单路缺 key 或 native:false 时只发一次，无辅助模型调用），结果按 URL 去重后以 固定比例交错（默认 2:1）合并，让模型同时拿到 DeepSeek 自有索引与 Google 索引。

## 详细介绍

DeepSeek Search API（官方自研搜索引擎）+ serper.dev（Google 搜索）双擎互补的搜索插件，接入 DeepSeek Harness 的 web 能力缝（ctx.web）。安装后，DSH 内置的 web_search 每次只发两次直连检索请求（native:true 且两路可用时；单路缺 key 或 native:false 时只发一次，无辅助模型调用），结果按 URL 去重后以 固定比例交错（默认 2:1）合并，让模型同时拿到 DeepSeek 自有索引与 Google 索引。

## 🔗 链接

- [GitHub 仓库](https://github.com/Minokun/dsh-serper-search)
- [完整 README](https://github.com/Minokun/dsh-serper-search#readme)
- [返回dsh-serper-search所在分类](../plugins.md)
