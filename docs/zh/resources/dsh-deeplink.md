---
title: "dsh-deeplink"
description: "DSH WebUI 深链插件：?session=/?workspace= 直接打开指定项目对话"
keywords: "dsh-deeplink, search, plugin, coding, ui, deepseek harness, dsh"
---
# dsh-deeplink

> ⭐ **4** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 搜索与研究 |
| 星数 | ⭐ 4 | 状态 | ✅ 活跃 |
| 作者 | [qyw233](https://github.com/qyw233) | 更新时间 | — |
| 子分类 | 🌐 网页搜索 | 能力 | coding, ui |

## 一句话介绍

> DSH WebUI 深链插件：?session=/?workspace= 直接打开指定项目对话

## 详细介绍

A DeepSeek Harness Web UI plugin that opens a **specific project conversation** directly from a URL query parameter, instead of always returning to the last session. - `?session=` → open that conversation - `?workspace=` → open that project's latest/blank conversation - Persistent links: the address bar follows the current conversation, so you can copy/bookmark/share the link at any time - Settings toggles to enable/disable jumping and address-bar following independently - Ships a model prompt section so the model surfaces clickable deep links when a reply refers to another conversation or project License: MIT

## ✨ 核心特性

- Reads `?session=` / `?workspace=` from the page URL and switches once the session/workspace list baseline is ready
- `session` wins when both parameters are present
- When the target session/workspace does not exist (or is archived/hidden), it silently falls back to the default behavior (restore the last session) — no errors,
- Persistent links: whenever the current session changes (deep-link switch or a manual switch in the UI), the address bar is rewritten to `?session=<current-sessi
- Settings toggles: two independent switches (设置 → 插件 → 插件配置, shown as a card via the official `settings.plugin.item` slot, keyed by the `dsh-deeplink` settings n
- The node half registers a global prompt section so the model knows deep links exist and can attach links when a reply refers to other conversations/projects
- Pure browser half + a lightweight node half; no cordis import, no peerDependencies

## 📦 安装

```bash
# Official profile (ships dsh-base + dsh-web-app, which provide the systemPrompt/webServer services):
dsh plugin --profile web add github:qyw233/dsh-deeplink
# Or a local checkout:
dsh plugin --profile web add /path/to/dsh-deeplink
```

## 📚 更多信息

**Install**

The plugin is installed into a profile via the standard `dsh plugin` mechanism — **no DSH source changes required**.

**Usage**

Append query parameters to the WebUI URL: New window/tab behavior: Persistent links:

**Settings**

The plugin registers a **深链** card in the 插件配置 tab (设置 → 插件 → 插件配置, via the official `settings.plugin.item` slot, keyed by the `dsh-deeplink` settings namespace registered on the host) with two independent toggles (both default on, persisted in `localStorage`):

## 🔗 链接

- [GitHub 仓库](https://github.com/qyw233/dsh-deeplink)
- [完整 README](https://github.com/qyw233/dsh-deeplink#readme)
- [返回dsh-deeplink所在分类](../plugins.md)
