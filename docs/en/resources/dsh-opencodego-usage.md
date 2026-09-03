---
title: "dsh-opencodego-usage"
description: "DSH Web GUI plugin: OpenCodeGo quota breathing light + liquid-glass panel with rolling/weekly/monthly progress bars (作者 Xu Yuanshan)"
keywords: "dsh-opencodego-usage, search, plugin, coding, ui, deepseek harness, dsh"
---
# dsh-opencodego-usage

> ⭐ **8** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 8 | Status | ✅ active |
| Author | [BeiZi6](https://github.com/BeiZi6) | Updated | — |
| Subcategory | 🌐 Web search | Capabilities | coding, ui |

## One-liner

> DSH Web GUI plugin: OpenCodeGo quota breathing light + liquid-glass panel with rolling/weekly/monthly progress bars (作者 Xu Yuanshan)

## About

**[English](README.md) · [简体中文](README.zh-CN.md)** OpenCodeGo quota monitor for the DeepSeek Harness (DSH) Web GUI: a breathing indicator at the bottom-right of the input box shows your remaining quota at a glance; click it to open a liquid-glass panel with per-window progress bars and reset times.

## ✨ Key Features

- 🟢🟡🔴 **Breathing indicator** — color-coded by remaining quota (>50% green, 20–50% yellow, <20% red) with a gentle 3.6 s breathing animation
- 📊 **Three-window progress panel** — `rolling` (≈ last 5 h), `weekly` (≈ last 7 d) and `monthly` (≈ last 30 d) bars with used · remaining amounts and a reset tim
- 🔑 **Zero-config key handling** — reads your API key from DSH credentials automatically (only when the provider is `opencode-go`); an in-panel override is availa
- 🪟 **Liquid-glass panel** — mouse-follow highlight, frosted blur and a window-style diagonal open animation
- ⏱ **Auto-refresh** — fetches fresh quota every 2 minutes

## 📦 Install

```bash
dsh plugin --profile web add github:BeiZi6/dsh-opencodego-usage
```

## 🚀 Quick Start

```bash
dsh plugin --profile web remove dsh-opencodego-usage
```

## 📚 Learn more

**dsh-opencodego-usage**

**[English](README.md) · [简体中文](README.zh-CN.md)** OpenCodeGo quota monitor for the DeepSeek Harness (DSH) Web GUI: a breathing indicator at the bottom-right of the input box shows your remaining quota at a glance; click it to open a liquid-glass panel with per-window progress bars and reset times.

**Installation**

Requires DeepSeek Harness with the web profile enabled. Install from the official registry: dsh plugin --profile web add github:BeiZi6/dsh-opencodego-usage Restart `dsh web` for the plugin to take effect. To remove: dsh plugin --profile web remove dsh-opencodego-usage

**Usage**

| Remaining share | Color | |---|---| | > 50% | 🟢 green | | 20–50% | 🟡 yellow | | < 20% | 🔴 red | - `rolling` — quota used in roughly the last 5 hours - `weekly` — quota used in roughly the last 7 days - `monthly` — quota used in roughly the last 30 days

## 🔗 Links

- [GitHub Repository](https://github.com/BeiZi6/dsh-opencodego-usage)
- [Full README](https://github.com/BeiZi6/dsh-opencodego-usage#readme)
- [Back to the Plugins list](../plugins.md)
