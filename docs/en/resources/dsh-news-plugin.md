---
title: "dsh-news-plugin"
description: "RSS/news ingestion returning structured title/link/source/date/summary for downstream model ranking and briefing."
keywords: "dsh-news-plugin, search, plugin, research, deepseek harness, dsh"
---
# dsh-news-plugin

> ⭐ **1** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 1 | Status | ✅ active |
| Author | [canghai666x](https://github.com/canghai666x) | Updated | 2026-08-14 |
| Subcategory | 📰 News & RSS | Capabilities | search, research |

## One-liner

> RSS/news ingestion returning structured title/link/source/date/summary for downstream model ranking and briefing.

## About

DeepSeek Harness 新闻采集工具插件。注册一个 `news_fetch` 工具：抓取 RSS 新闻源并解析为结构化条目，供模型做五维评分筛选与简报编排。 **设计原则：采集与解析是确定性工作交给插件，评分/筛选/写作交给模型。** 不依赖第三方包（Node 原生 fetch + 正则解析）。

## 🚀 Quick Start

```bash
plugins:
  - name: '@deepseek-ai/dsh-system-prompt'
  - name: '@deepseek-ai/dsh-tools'
  - name: './index.ts'          # 本插件
```

## 📚 Learn more

**安装（一句话版，推荐）**

在 DSH 对话里直接说： > 安装 https://github.com/canghai666x/dsh-news-plugin 这个插件 Agent 安装时会读取仓库内的 `AGENT_INSTALL.md`（给 AI 看的精确安装说明书），按步骤执行并验证。 Agent 会自动完成：clone 仓库 → 放入 plugins 目录 → 在 `cordis.yml` 注册 → 重启 dsh。全程不用手动敲命令。 **手动安装（备选）：** 将插件放入 Harness 项目，并在 `cordis.yml` 组合中声明（参考官方教程第 7 章）： plugins: - name: '@deepseek-ai/dsh-system-prompt' - name: '@deepseek-ai/dsh-tools' - name: './index.ts' # 本插件 运行： node --im

## 🔗 Links

- [GitHub Repository](https://github.com/canghai666x/dsh-news-plugin)
- [Full README](https://github.com/canghai666x/dsh-news-plugin#readme)
- [Back to the Plugins list](../plugins.md)
