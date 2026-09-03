---
title: "DSH Composer Layout"
description: "让 DSH Web 的长回答与正在撰写的详细提示词并排可见，边读边写。"
keywords: "DSH Composer Layout, ui, plugin, deepseek harness, dsh"
---
# DSH Composer Layout

> ⭐ **4** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 4 | 状态 | ✅ 活跃 |
| 作者 | [lavapapa](https://github.com/lavapapa) | 更新时间 | — |
| 子分类 | ⌨️ 输入增强 | 能力 | ui |

## 一句话介绍

> 让 DSH Web 的长回答与正在撰写的详细提示词并排可见，边读边写。

## 详细介绍

**English** · [简体中文](README.zh.md) [Overview](#dsh-composer-layout) · [Install](#install) · [Why side by side?](#why-a-side-by-side-composer) · [See it in DSH](#see-it-in-dsh) · [Switch and resize](#switch-and-resize) · [Features](#what-it-adds) · [Release checks](docs/RELEASE_CHECKS.md) · [Contributing](CONTRIBUTING.md) · [简体中文](README.zh.md) [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) Web plugin that lets the Composer stay at the bottom or dock in a right-side column. The chat and Composer keep their own space, while the normal DSH model, permission, quota, session, and tool behavior remains intact.

## 📦 安装

```bash
dsh plugin --profile web add dsh-composer-layout@latest
dsh web --profile web
```

## 🚀 快速开始

```bash
dsh plugin --profile web add "github:lavapapa/dsh-composer-layout#v0.1.12"
dsh web --profile web
```

## 📚 更多信息

**Install from npm**

The npm package already contains the prebuilt plugin bundle: dsh plugin --profile web add dsh-composer-layout@latest dsh web --profile web

**Install directly from GitHub**

DSH installs the plugin bundle directly from a GitHub repository; pinning the command to `v0.1.12` makes the installed source explicit and repeatable. dsh plugin --profile web add "github:lavapapa/dsh-composer-layout#v0.1.12" dsh web --profile web Then open **Settings → Plugins → Composer Layout** and select **Right side**. Restarting the Web profile is required because DSH does not hot-reload pro

## 🔗 链接

- [GitHub 仓库](https://github.com/lavapapa/dsh-composer-layout)
- [完整 README](https://github.com/lavapapa/dsh-composer-layout#readme)
- [返回DSH Composer Layout所在分类](../plugins.md)
