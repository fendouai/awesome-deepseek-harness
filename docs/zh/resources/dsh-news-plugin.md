---
title: "dsh-news-plugin"
description: "RSS/新闻摄入插件：返回结构化的标题/链接/来源/日期/摘要，供模型排序与简报。"
keywords: "dsh-news-plugin, search, plugin, research, deepseek harness, dsh"
---
# dsh-news-plugin

> ⭐ **1** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 搜索与研究 |
| 星数 | ⭐ 1 | 状态 | ✅ 活跃 |
| 作者 | [canghai666x](https://github.com/canghai666x) | 更新时间 | 2026-08-14 |
| 子分类 | 📰 新闻与资讯 | 能力 | search, research |

## 一句话介绍

> RSS/新闻摄入插件：返回结构化的标题/链接/来源/日期/摘要，供模型排序与简报。

## 详细介绍

DeepSeek Harness 新闻采集工具插件。注册一个 `news_fetch` 工具：抓取 RSS 新闻源并解析为结构化条目，供模型做五维评分筛选与简报编排。 **设计原则：采集与解析是确定性工作交给插件，评分/筛选/写作交给模型。** 不依赖第三方包（Node 原生 fetch + 正则解析）。

## 🚀 快速开始

```bash
plugins:
  - name: '@deepseek-ai/dsh-system-prompt'
  - name: '@deepseek-ai/dsh-tools'
  - name: './index.ts'          # 本插件
```

## 📚 更多信息

**安装（一句话版，推荐）**

在 DSH 对话里直接说： > 安装 https://github.com/canghai666x/dsh-news-plugin 这个插件 Agent 安装时会读取仓库内的 `AGENT_INSTALL.md`（给 AI 看的精确安装说明书），按步骤执行并验证。 Agent 会自动完成：clone 仓库 → 放入 plugins 目录 → 在 `cordis.yml` 注册 → 重启 dsh。全程不用手动敲命令。 **手动安装（备选）：** 将插件放入 Harness 项目，并在 `cordis.yml` 组合中声明（参考官方教程第 7 章）： plugins: - name: '@deepseek-ai/dsh-system-prompt' - name: '@deepseek-ai/dsh-tools' - name: './index.ts' # 本插件 运行： node --im

## 🔗 链接

- [GitHub 仓库](https://github.com/canghai666x/dsh-news-plugin)
- [完整 README](https://github.com/canghai666x/dsh-news-plugin#readme)
- [返回dsh-news-plugin所在分类](../plugins.md)
