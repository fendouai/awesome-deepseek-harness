---
title: "dsh-session-pin"
description: "Pin sessions and workspaces to the top of the DeepSeek Harness sidebar with per-pin row colors - a dual-face (host + client) dsh plugin."
keywords: "dsh-session-pin, ui, plugin, coding, deepseek harness, dsh"
---
# dsh-session-pin

> ⭐ **3** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 3 | 状态 | ✅ 活跃 |
| 作者 | [PerryLink](https://github.com/PerryLink) | 更新时间 | — |
| 子分类 | 🖥️ 侧边栏与面板 | 能力 | coding, ui |

## 一句话介绍

> Pin sessions and workspaces to the top of the DeepSeek Harness sidebar with per-pin row colors - a dual-face (host + client) dsh plugin.

## 详细介绍

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-session-pin` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **Pin sessions and workspaces to the top of the DeepSeek Harness sidebar with per-pin row colors.** *A dual-face (host + browser) plugin: two pin levels, an 8-color swatch per pin, and a navigation organizer — boards, tags, saved views, health summaries, and `/goto`.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ 核心特性

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-session-pin` (counts toward the [deepseek1024.com](https://deepseek1

## 📦 安装

```bash
# 1. install the bundle into your profile
dsh plugin --profile web add "github:PerryLink/dsh-session-pin#main"

# or from npm (published releases)
dsh plugin --profile web add dsh-session-pin

# 2. restart and verify the row
dsh --profile web --dump-config | grep -A3 'id: session-pin'
```

## 🚀 快速开始

```bash
pnpm install                    # install dependencies
pnpm run typecheck              # tsc --noEmit
pnpm test                       # vitest unit tests
pnpm run build                  # dual-half build + client-bundle purity check
node scripts/verify-live.mjs    # live check against a running `dsh web` (DSH_CHECKOUT env)
```

## 📚 更多信息

**Configuration**

All tunables are Schemastery `Config` fields (changeable from cordis.yml). `cordis.patch.yml` mounts the bundle with the defaults below.

## 🔗 链接

- [GitHub 仓库](https://github.com/PerryLink/dsh-session-pin)
- [完整 README](https://github.com/PerryLink/dsh-session-pin#readme)
- [返回dsh-session-pin所在分类](../plugins.md)
