---
title: "DSH Composer Layout"
description: "Lets you read a long answer while drafting the next detailed prompt beside it in DSH Web."
keywords: "DSH Composer Layout, ui, plugin, deepseek harness, dsh"
---
# DSH Composer Layout

> ⭐ **4** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 4 | Status | ✅ active |
| Author | [lavapapa](https://github.com/lavapapa) | Updated | — |
| Subcategory | ⌨️ Input enhancement | Capabilities | ui |

## One-liner

> Lets you read a long answer while drafting the next detailed prompt beside it in DSH Web.

## About

**English** · [简体中文](README.zh.md) [Overview](#dsh-composer-layout) · [Install](#install) · [Why side by side?](#why-a-side-by-side-composer) · [See it in DSH](#see-it-in-dsh) · [Switch and resize](#switch-and-resize) · [Features](#what-it-adds) · [Release checks](docs/RELEASE_CHECKS.md) · [Contributing](CONTRIBUTING.md) · [简体中文](README.zh.md) [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) Web plugin that lets the Composer stay at the bottom or dock in a right-side column. The chat and Composer keep their own space, while the normal DSH model, permission, quota, session, and tool behavior remains intact.

## 📦 Install

```bash
dsh plugin --profile web add dsh-composer-layout@latest
dsh web --profile web
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add "github:lavapapa/dsh-composer-layout#v0.1.12"
dsh web --profile web
```

## 📚 Learn more

**Install from npm**

The npm package already contains the prebuilt plugin bundle: dsh plugin --profile web add dsh-composer-layout@latest dsh web --profile web

**Install directly from GitHub**

DSH installs the plugin bundle directly from a GitHub repository; pinning the command to `v0.1.12` makes the installed source explicit and repeatable. dsh plugin --profile web add "github:lavapapa/dsh-composer-layout#v0.1.12" dsh web --profile web Then open **Settings → Plugins → Composer Layout** and select **Right side**. Restarting the Web profile is required because DSH does not hot-reload pro

## 🔗 Links

- [GitHub Repository](https://github.com/lavapapa/dsh-composer-layout)
- [Full README](https://github.com/lavapapa/dsh-composer-layout#readme)
- [Back to the Plugins list](../plugins.md)
