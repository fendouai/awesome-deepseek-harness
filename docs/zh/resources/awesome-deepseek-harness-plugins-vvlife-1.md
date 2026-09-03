---
title: "awesome-deepseek-harness-plugins"
description: "DeepSeek Harness 插件目录"
keywords: "awesome-deepseek-harness-plugins, registry, awesome-list, search, deepseek harness, dsh"
---
# awesome-deepseek-harness-plugins

> ⭐ **10** · ✅ 活跃 · 精选列表 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 精选列表 | 分类 | 注册表 |
| 星数 | ⭐ 10 | 状态 | ✅ 活跃 |
| 作者 | [vvlife](https://github.com/vvlife) | 更新时间 | 2026-08-21 |

## 一句话介绍

> DeepSeek Harness 插件目录

## 详细介绍

A curated list of plugins, tools, skins, bridges, and extensions for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (DSH) — the open-source agent framework from DeepSeek, built on the motto **"Everything is a Plugin."** DSH launched its developer preview on **2026-08-13** (MIT license, Cordis-based). Within a day the community shipped a wave of plugins; this list tracks the notable ones and points to the rest.

## ✨ 核心特性

- [How to install a plugin](#how-to-install-a-plugin)
- [Official built-in plugins](#official-built-in-plugins)
- [Community plugins](#community-plugins)
- [Hands-on Notes](#hands-on-notes)
- [Other awesome lists (meta)](#other-awesome-lists-meta)
- [Contributing](#contributing)

## 📦 安装

```bash
# npm-scoped plugin (recommended)
dsh plugin add <npm-package>

# repo-hosted plugin (the .dsh-plugin format)
# add to your profile's cordis.yml, or via the CLI patch layer:
# github:<owner>/<repo>#<ref>&path:/.dsh-plugin
```

## 🚀 快速开始

```bash
dsh web            # http://127.0.0.1:3080
```

## 📚 更多信息

**How to install a plugin**

**中文**：DSH 把插件当作 [Cordis](https://github.com/cordiverse/cordis) bundle 加载，最常用的两条路：npm 包用 `dsh plugin add <npm-package>`，仓库托管（`.dsh-plugin` 形态）用 `github:<owner>/<repo>` 形式。 DSH loads plugins as [Cordis](https://github.com/cordiverse/cordis) bundles. Two common paths:

## 🔗 链接

- [GitHub 仓库](https://github.com/vvlife/awesome-deepseek-harness-plugins)
- [完整 README](https://github.com/vvlife/awesome-deepseek-harness-plugins#readme)
- [返回awesome-deepseek-harness-plugins所在分类](../awesome-lists.md)
