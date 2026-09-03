---
title: "dsh-plugin-hub"
description: "插件管理面板：一键启停已装插件 + GitHub dsh-plugin 市场，带详情与一键安装。"
keywords: "dsh-plugin-hub, discovery, plugin, ui, workflow, deepseek harness, dsh"
---
# dsh-plugin-hub

> ⭐ **64** · ✅ 活跃 · 插件 · 近期 ⬆️ +2

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 插件发现 |
| 星数 | ⭐ 64 | 状态 | ✅ 活跃 |
| 作者 | [Noob-stupid](https://github.com/Noob-stupid) | 更新时间 | 2026-08-21 |

## 一句话介绍

> 插件管理面板：一键启停已装插件 + GitHub dsh-plugin 市场，带详情与一键安装。

## 详细介绍

A **plugin management panel** for the DeepSeek Harness (DSH) Web GUI: one-click enable/disable of installed plugins, a **multi-source plugin marketplace** (GitHub / Gitee / custom sources) with one-click install, an **auto-collected static plugin & skill index** refreshed by CI every 6 hours, skill install/disable, suite one-click assembly, and **one-click framework upgrade** (online install with auto-rollback). - [Highlights](#highlights) - [One-click install](#one-click-install) - [Usage](#usage) - [Features](#features) - [How it works](#how-it-works) - [Compatibility](#compatibility) - [Project layout](#project-layout) - [HTTP endpoints](#http-endpoints) - [Local AI fallback & consent dialog](#local-ai-fallback--consent-dialog) - [Framework patch (cordis.patch.yml parse tolerance)](#fra

## ✨ 核心特性

- [Highlights](#highlights)
- [One-click install](#one-click-install)
- [Usage](#usage)
- [Features](#features)
- [How it works](#how-it-works)
- [Compatibility](#compatibility)

## 📦 安装

```bash
> npm i -g @noob-stupid/dsh-plugin-console
> # or in DSH: dsh plugin --profile web add @noob-stupid/dsh-plugin-console
>
```

## 🚀 快速开始

```bash
{ "vlm": { "provider": "openai", "api_base": "https://api.deepseek.com", "model": "deepseek-v4-flash-vision-exp" }, "api_key": "sk-..." }
```

## 📚 更多信息

**or install from GitHub source (needs git; allowBuilds author**

dsh plugin --profile web add github:Noob-stupid/dsh-plugin-hub Uninstall / reinstall (update): dsh plugin --profile web remove @noob-stupid/dsh-plugin-console dsh plugin --profile web add @noob-stupid/dsh-plugin-console Then restart the dsh service → refresh the page → Settings → Plugins → Plugin Console.

**Usage**

1. Restart DSH → open the Web GUI → **Settings → Plugins → Plugin Console**. 2. **Installed list**: toggle plugins on/off (HMR applies within ~1s), search by name/id, expand details (version, repository, README summary). 3. **Marketplace**: empty query on the GitHub source opens the static index (instant); type a query to search live. Switch sources via the login pill (GitHub / Gitee / custom); `⊞

**Installed plugins (one-click toggle + details)**

"Third-party" with a delete entry; click "All" to see the full list (1.5s flash feedback); `disabled: false`; (70+ rows) are marked "Protected" and cannot be toggled — disabling them would break HMR; node networking is blocked) and warns about subpackages that need syncing (depsOutdated).

**Install chain**

configured registries (primary→backup, default npmmirror → npmjs) → curl manual install (node networking blocked: tarball into node_modules) → git channel (GitHub via proxy+direct, Gitee via its platform) → EPERM stale-dir cleanup retry → repository subpackage expansion (aggregate packages first) → local AI fallback (behind an explicit cost-consent modal) Skills install directly by `git clone --de

## 🔗 链接

- [GitHub 仓库](https://github.com/Noob-stupid/dsh-plugin-hub)
- [完整 README](https://github.com/Noob-stupid/dsh-plugin-hub#readme)
- [返回dsh-plugin-hub所在分类](../plugins.md)
