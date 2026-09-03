---
title: "dsh-usage-plugin"
description: "DeepSeek Harness 用量与消耗插件（dsh-usage）—— 每次调用的 token 用量/缓存命中统计、峰谷计费、余额查询、CSV/JSON/PNG 导出，可经桌面端一键安装或命令行 dsh plugin add 安装。"
keywords: "dsh-usage-plugin, desktop, client, coding, deepseek harness, dsh"
---
# dsh-usage-plugin

> ⭐ **33** · ✅ 活跃 · 客户端 · 近期 ⬆️ +3

| | | | |
|---|---|---|---|
| 类型 | 客户端 | 分类 | 桌面端 |
| 星数 | ⭐ 33 | 状态 | ✅ 活跃 |
| 作者 | [feiyang-dev](https://github.com/feiyang-dev) | 更新时间 | 2026-08-20 |

## 一句话介绍

> DeepSeek Harness 用量与消耗插件（dsh-usage）—— 每次调用的 token 用量/缓存命中统计、峰谷计费、余额查询、CSV/JSON/PNG 导出，可经桌面端一键安装或命令行 dsh plugin add 安装。

## 详细介绍

**English** · [简体中文](./README.zh.md) [GitHub](https://github.com/feiyang-dev/dsh-usage-plugin) · [npm](https://www.npmjs.com/package/@feiyang666/dsh-usage-plugin) · MIT License **A community plugin for DeepSeek Harness** — records token usage and cost for every model call, with peak/off-peak billing, balance query, a calendar heatmap, and CSV / JSON / PNG export. --- ---

## ✨ 核心特性

- **Usage & Cost**: records each model call's token usage and cache hits (input miss / cache hit / cache write / output / reasoning / finish reason), and computes
- **Usage Calendar**: a monthly daily-usage heatmap (colored by cost or call count), hover for details including the peak/off-peak cost split, click a day for its
- **Cache Hit List**: newest-first, fully scrollable, with quick filters (Today / 7 days / 30 days / All) and custom date ranges; the summary line and footer tota
- **Interrupted calls shown truthfully**: calls that were aborted / errored / timed out (e.g. manually stopped generation, stream interruption) are shown with a r
- **Local stats vs official console**: a fixed notice banner at the top of the panel explains that this panel reflects calls captured locally by the plugin (offic
- **Price Table**: the official DeepSeek API price table (covering `deepseek-v4-flash` / `deepseek-v4-flash-vision-exp` / `deepseek-v4-pro`) — base and peak/valle

## 📦 安装

```bash
# Prerequisite: install dsh (npm install -g @deepseek-ai/dsh)
dsh plugin --profile web add @feiyang666/dsh-usage-plugin
```

## 🚀 快速开始

```bash
dsh plugin --profile web add @feiyang666/dsh-usage-plugin
dsh plugin --profile headless add @feiyang666/dsh-usage-plugin
```

## 📚 更多信息

**DeepSeek Harness Usage & Cost Tracker (dsh-usage-plugin)**

**English** · [简体中文](./README.zh.md) [GitHub](https://github.com/feiyang-dev/dsh-usage-plugin) · [npm](https://www.npmjs.com/package/@feiyang666/dsh-usage-plugin) · MIT License **A community plugin for DeepSeek Harness** — records token usage and cost for every model call, with peak/off-peak billing, balance query, a calendar heatmap, and CSV / JSON / PNG export. </div> --- > ## 🔔 Important Notice

**Recommended Installation**

> Either method works and is equivalent. **We recommend the desktop app** — fully graphical, no command line needed.

**Prerequisite: install dsh (npm install -g @deepseek-ai/dsh)**

dsh plugin --profile web add @feiyang666/dsh-usage-plugin Or install to another profile: dsh plugin --profile web add @feiyang666/dsh-usage-plugin dsh plugin --profile headless add @feiyang666/dsh-usage-plugin Restart the dsh web service after installation. Detailed manual install / wiring / uninstall / troubleshooting follows below. ---

**2. Method B: manual install (no pnpm / no `dsh plugin`)**

Only for when you have no pnpm or want full manual control. **Do not `npm install` directly at `~/.dsh/profiles`** (that dir has no package.json; npm would treat the whole node_modules as residue and wipe it). **B1. Use pnpm but not `dsh plugin`:** cd ~/.dsh/profiles/web pnpm add @feiyang666/dsh-usage-plugin

## 🔗 链接

- [GitHub 仓库](https://github.com/feiyang-dev/dsh-usage-plugin)
- [完整 README](https://github.com/feiyang-dev/dsh-usage-plugin#readme)
- [返回dsh-usage-plugin所在分类](../clients.md)
