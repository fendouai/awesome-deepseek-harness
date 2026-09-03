---
title: "dsh-cubox"
description: "DeepSeek Harness 的 Cubox 收藏同步插件：定时同步收藏，按你的 prompt 用 LLM 生成今日收藏简报直接写入 Obsidian，并可导出每张收藏为 Markdown。"
keywords: "dsh-cubox, ui, plugin, automation, deepseek harness, dsh"
---
# dsh-cubox

> ⭐ **1** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 1 | 状态 | ✅ 活跃 |
| 作者 | [zhengjy01](https://github.com/zhengjy01) | 更新时间 | — |
| 子分类 | 💡 生成式界面 | 能力 | automation |

## 一句话介绍

> DeepSeek Harness 的 Cubox 收藏同步插件：定时同步收藏，按你的 prompt 用 LLM 生成今日收藏简报直接写入 Obsidian，并可导出每张收藏为 Markdown。

## 详细介绍

Cubox sync for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness): scheduled sync of your Cubox collection, with an **AI daily brief** generated from your own prompt template and written straight into Obsidian — via the same `/c/api/cli` endpoints the official cubox-cli uses. Agent tools plus a web settings panel.

## ✨ 核心特性

- **Scheduled sync** — a timer pulls your latest bookmarks into a local cache (`~/.dsh/dsh-cubox-cache.json`) every N minutes (default 60, configurable; 0 disable
- **AI daily brief** — write your own prompt template (e.g. "今日收藏简报", `{collection}` is replaced with the formatted collection for the sync window: title / source
- **Markdown export** — set `outputDir` and optionally keep one markdown file per card (frontmatter + title + description + Cubox/original links + annotations, sa
- **Query** — `cubox_cards` filters by keyword, time window, annotated/starred/read status.
- **Config & status** — `cubox_config` / `cubox_status`; credentials persist to `~/.dsh/dsh-cubox.json` (mode 0600), secrets never echoed.
- **Settings panel** — Settings → Cubox: paste the API-extension link, set the sync interval, pick the local export folder (OS folder chooser), toggle per-card ex

## 📦 安装

```bash
# after publishing to GitHub (repo tagged with the `dsh-plugin` topic)
dsh plugin --profile web add github:zhengjy01/dsh-cubox

# local development
dsh plugin --profile web add link:/path/to/dsh-cubox
```

## 🚀 快速开始

```bash
帮我配置 Cubox，API 链接是 https://cubox.pro/c/api/save/abcd12345
```

## 📚 更多信息

**Configure**

1. Open Cubox preferences → Extensions & Automation → API Extension → enable it and copy your unique link (e.g. `https://cubox.pro/c/api/save/abcd12345`). 2. Give the link to the plugin — either in the settings panel (Settings → Cubox), or just ask the agent: ```text 帮我配置 Cubox，API 链接是 https://cubox.pro/c/api/save/abcd12345 ``` The agent calls `cubox_config` to persist it. `cubox.pro` is the defau

## 🔗 链接

- [GitHub 仓库](https://github.com/zhengjy01/dsh-cubox)
- [完整 README](https://github.com/zhengjy01/dsh-cubox#readme)
- [返回dsh-cubox所在分类](../plugins.md)
