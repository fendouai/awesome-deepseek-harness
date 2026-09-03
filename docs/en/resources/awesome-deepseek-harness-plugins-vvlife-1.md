---
title: "awesome-deepseek-harness-plugins"
description: "A curated list of plugins, tools, skins, and extensions for DeepSeek Harness (DSH)."
keywords: "awesome-deepseek-harness-plugins, registry, awesome-list, search, deepseek harness, dsh"
---
# awesome-deepseek-harness-plugins

> ⭐ **10** · ✅ active · awesome-list · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | awesome-list | Category | Registries |
| Stars | ⭐ 10 | Status | ✅ active |
| Author | [vvlife](https://github.com/vvlife) | Updated | 2026-08-21 |

## One-liner

> A curated list of plugins, tools, skins, and extensions for DeepSeek Harness (DSH).

## About

A curated list of plugins, tools, skins, bridges, and extensions for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (DSH) — the open-source agent framework from DeepSeek, built on the motto **"Everything is a Plugin."** DSH launched its developer preview on **2026-08-13** (MIT license, Cordis-based). Within a day the community shipped a wave of plugins; this list tracks the notable ones and points to the rest.

## ✨ Key Features

- [How to install a plugin](#how-to-install-a-plugin)
- [Official built-in plugins](#official-built-in-plugins)
- [Community plugins](#community-plugins)
- [Hands-on Notes](#hands-on-notes)
- [Other awesome lists (meta)](#other-awesome-lists-meta)
- [Contributing](#contributing)

## 📦 Install

```bash
# npm-scoped plugin (recommended)
dsh plugin add <npm-package>

# repo-hosted plugin (the .dsh-plugin format)
# add to your profile's cordis.yml, or via the CLI patch layer:
# github:<owner>/<repo>#<ref>&path:/.dsh-plugin
```

## 🚀 Quick Start

```bash
dsh web            # http://127.0.0.1:3080
```

## 📚 Learn more

**How to install a plugin**

**中文**：DSH 把插件当作 [Cordis](https://github.com/cordiverse/cordis) bundle 加载，最常用的两条路：npm 包用 `dsh plugin add <npm-package>`，仓库托管（`.dsh-plugin` 形态）用 `github:<owner>/<repo>` 形式。 DSH loads plugins as [Cordis](https://github.com/cordiverse/cordis) bundles. Two common paths:

## 🔗 Links

- [GitHub Repository](https://github.com/vvlife/awesome-deepseek-harness-plugins)
- [Full README](https://github.com/vvlife/awesome-deepseek-harness-plugins#readme)
- [Back to the Awesome Lists & Registries list](../awesome-lists.md)
