---
title: "dsh-opencodego-usage"
description: "DSH Web GUI plugin: OpenCodeGo quota breathing light + liquid-glass panel with rolling/weekly/monthly progress bars (作者 Xu Yuanshan)"
keywords: "dsh-opencodego-usage, search, plugin, coding, ui, deepseek harness, dsh"
---
# dsh-opencodego-usage

> ⭐ **8** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 搜索与研究 |
| 星数 | ⭐ 8 | 状态 | ✅ 活跃 |
| 作者 | [BeiZi6](https://github.com/BeiZi6) | 更新时间 | — |
| 子分类 | 🌐 网页搜索 | 能力 | coding, ui |

## 一句话介绍

> DSH Web GUI plugin: OpenCodeGo quota breathing light + liquid-glass panel with rolling/weekly/monthly progress bars (作者 Xu Yuanshan)

## 详细介绍

**[English](README.md) · [简体中文](README.zh-CN.md)** OpenCodeGo quota monitor for the DeepSeek Harness (DSH) Web GUI: a breathing indicator at the bottom-right of the input box shows your remaining quota at a glance; click it to open a liquid-glass panel with per-window progress bars and reset times.

## ✨ 核心特性

- 🟢🟡🔴 **Breathing indicator** — color-coded by remaining quota (>50% green, 20–50% yellow, <20% red) with a gentle 3.6 s breathing animation
- 📊 **Three-window progress panel** — `rolling` (≈ last 5 h), `weekly` (≈ last 7 d) and `monthly` (≈ last 30 d) bars with used · remaining amounts and a reset tim
- 🔑 **Zero-config key handling** — reads your API key from DSH credentials automatically (only when the provider is `opencode-go`); an in-panel override is availa
- 🪟 **Liquid-glass panel** — mouse-follow highlight, frosted blur and a window-style diagonal open animation
- ⏱ **Auto-refresh** — fetches fresh quota every 2 minutes

## 📦 安装

```bash
dsh plugin --profile web add github:BeiZi6/dsh-opencodego-usage
```

## 🚀 快速开始

```bash
dsh plugin --profile web remove dsh-opencodego-usage
```

## 📚 更多信息

**dsh-opencodego-usage**

**[English](README.md) · [简体中文](README.zh-CN.md)** OpenCodeGo quota monitor for the DeepSeek Harness (DSH) Web GUI: a breathing indicator at the bottom-right of the input box shows your remaining quota at a glance; click it to open a liquid-glass panel with per-window progress bars and reset times.

**Installation**

Requires DeepSeek Harness with the web profile enabled. Install from the official registry: dsh plugin --profile web add github:BeiZi6/dsh-opencodego-usage Restart `dsh web` for the plugin to take effect. To remove: dsh plugin --profile web remove dsh-opencodego-usage

**Usage**

| Remaining share | Color | |---|---| | > 50% | 🟢 green | | 20–50% | 🟡 yellow | | < 20% | 🔴 red | - `rolling` — quota used in roughly the last 5 hours - `weekly` — quota used in roughly the last 7 days - `monthly` — quota used in roughly the last 30 days

## 🔗 链接

- [GitHub 仓库](https://github.com/BeiZi6/dsh-opencodego-usage)
- [完整 README](https://github.com/BeiZi6/dsh-opencodego-usage#readme)
- [返回dsh-opencodego-usage所在分类](../plugins.md)
