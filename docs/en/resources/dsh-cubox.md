---
title: "dsh-cubox"
description: "Cubox sync plugin for DeepSeek Harness: scheduled sync of your bookmarks, an AI daily brief generated from your own prompt template straight into Obsidian, and per-card markdown export — via the /c/api/cli endpoints."
keywords: "dsh-cubox, ui, plugin, automation, deepseek harness, dsh"
---
# dsh-cubox

> ⭐ **1** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 1 | Status | ✅ active |
| Author | [zhengjy01](https://github.com/zhengjy01) | Updated | — |
| Subcategory | 💡 Generative UI | Capabilities | automation |

## One-liner

> Cubox sync plugin for DeepSeek Harness: scheduled sync of your bookmarks, an AI daily brief generated from your own prompt template straight into Obsidian, and per-card markdown export — via the /c/api/cli endpoints.

## About

Cubox sync for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness): scheduled sync of your Cubox collection, with an **AI daily brief** generated from your own prompt template and written straight into Obsidian — via the same `/c/api/cli` endpoints the official cubox-cli uses. Agent tools plus a web settings panel.

## ✨ Key Features

- **Scheduled sync** — a timer pulls your latest bookmarks into a local cache (`~/.dsh/dsh-cubox-cache.json`) every N minutes (default 60, configurable; 0 disable
- **AI daily brief** — write your own prompt template (e.g. "今日收藏简报", `{collection}` is replaced with the formatted collection for the sync window: title / source
- **Markdown export** — set `outputDir` and optionally keep one markdown file per card (frontmatter + title + description + Cubox/original links + annotations, sa
- **Query** — `cubox_cards` filters by keyword, time window, annotated/starred/read status.
- **Config & status** — `cubox_config` / `cubox_status`; credentials persist to `~/.dsh/dsh-cubox.json` (mode 0600), secrets never echoed.
- **Settings panel** — Settings → Cubox: paste the API-extension link, set the sync interval, pick the local export folder (OS folder chooser), toggle per-card ex

## 📦 Install

```bash
# after publishing to GitHub (repo tagged with the `dsh-plugin` topic)
dsh plugin --profile web add github:zhengjy01/dsh-cubox

# local development
dsh plugin --profile web add link:/path/to/dsh-cubox
```

## 🚀 Quick Start

```bash
帮我配置 Cubox，API 链接是 https://cubox.pro/c/api/save/abcd12345
```

## 📚 Learn more

**Configure**

1. Open Cubox preferences → Extensions & Automation → API Extension → enable it and copy your unique link (e.g. `https://cubox.pro/c/api/save/abcd12345`). 2. Give the link to the plugin — either in the settings panel (Settings → Cubox), or just ask the agent: ```text 帮我配置 Cubox，API 链接是 https://cubox.pro/c/api/save/abcd12345 ``` The agent calls `cubox_config` to persist it. `cubox.pro` is the defau

## 🔗 Links

- [GitHub Repository](https://github.com/zhengjy01/dsh-cubox)
- [Full README](https://github.com/zhengjy01/dsh-cubox#readme)
- [Back to the Plugins list](../plugins.md)
