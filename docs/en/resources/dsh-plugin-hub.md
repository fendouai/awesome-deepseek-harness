---
title: "dsh-plugin-hub"
description: "Plugin management panel: enable/disable installed plugins plus a GitHub dsh-plugin marketplace with one-click install."
keywords: "dsh-plugin-hub, discovery, plugin, ui, workflow, deepseek harness, dsh"
---
# dsh-plugin-hub

> ⭐ **64** · ✅ active · plugin · ⬆️ +2 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Plugin discovery |
| Stars | ⭐ 64 | Status | ✅ active |
| Author | [Noob-stupid](https://github.com/Noob-stupid) | Updated | 2026-08-21 |

## One-liner

> Plugin management panel: enable/disable installed plugins plus a GitHub dsh-plugin marketplace with one-click install.

## About

A **plugin management panel** for the DeepSeek Harness (DSH) Web GUI: one-click enable/disable of installed plugins, a **multi-source plugin marketplace** (GitHub / Gitee / custom sources) with one-click install, an **auto-collected static plugin & skill index** refreshed by CI every 6 hours, skill install/disable, suite one-click assembly, and **one-click framework upgrade** (online install with auto-rollback). - [Highlights](#highlights) - [One-click install](#one-click-install) - [Usage](#usage) - [Features](#features) - [How it works](#how-it-works) - [Compatibility](#compatibility) - [Project layout](#project-layout) - [HTTP endpoints](#http-endpoints) - [Local AI fallback & consent dialog](#local-ai-fallback--consent-dialog) - [Framework patch (cordis.patch.yml parse tolerance)](#fra

## ✨ Key Features

- [Highlights](#highlights)
- [One-click install](#one-click-install)
- [Usage](#usage)
- [Features](#features)
- [How it works](#how-it-works)
- [Compatibility](#compatibility)

## 📦 Install

```bash
> npm i -g @noob-stupid/dsh-plugin-console
> # or in DSH: dsh plugin --profile web add @noob-stupid/dsh-plugin-console
>
```

## 🚀 Quick Start

```bash
{ "vlm": { "provider": "openai", "api_base": "https://api.deepseek.com", "model": "deepseek-v4-flash-vision-exp" }, "api_key": "sk-..." }
```

## 📚 Learn more

**or install from GitHub source (needs git; allowBuilds author**

dsh plugin --profile web add github:Noob-stupid/dsh-plugin-hub Uninstall / reinstall (update): dsh plugin --profile web remove @noob-stupid/dsh-plugin-console dsh plugin --profile web add @noob-stupid/dsh-plugin-console Then restart the dsh service → refresh the page → Settings → Plugins → Plugin Console.

**Usage**

1. Restart DSH → open the Web GUI → **Settings → Plugins → Plugin Console**. 2. **Installed list**: toggle plugins on/off (HMR applies within ~1s), search by name/id, expand details (version, repository, README summary). 3. **Marketplace**: empty query on the GitHub source opens the static index (instant); type a query to search live. Switch sources via the login pill (GitHub / Gitee / custom); `⊞

**Installed plugins (one-click toggle + details)**

"Third-party" with a delete entry; click "All" to see the full list (1.5s flash feedback); `disabled: false`; (70+ rows) are marked "Protected" and cannot be toggled — disabling them would break HMR; node networking is blocked) and warns about subpackages that need syncing (depsOutdated).

**Install chain**

configured registries (primary→backup, default npmmirror → npmjs) → curl manual install (node networking blocked: tarball into node_modules) → git channel (GitHub via proxy+direct, Gitee via its platform) → EPERM stale-dir cleanup retry → repository subpackage expansion (aggregate packages first) → local AI fallback (behind an explicit cost-consent modal) Skills install directly by `git clone --de

## 🔗 Links

- [GitHub Repository](https://github.com/Noob-stupid/dsh-plugin-hub)
- [Full README](https://github.com/Noob-stupid/dsh-plugin-hub#readme)
- [Back to the Plugins list](../plugins.md)
