---
title: "dsh-neo-skin"
description: "Neo-brutalism skin for the DeepSeek Harness Web UI — hard borders, high contrast, two switchable schemes (Blue Command / Aged Newspaper), works in light and dark themes."
keywords: "dsh-neo-skin, search, plugin, coding, ui, deepseek harness, dsh"
---
# dsh-neo-skin

> ⭐ **4** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 搜索与研究 |
| 星数 | ⭐ 4 | 状态 | ✅ 活跃 |
| 作者 | [0nt-one](https://github.com/0nt-one) | 更新时间 | — |
| 子分类 | 🌐 网页搜索 | 能力 | coding, search, ui |

## 一句话介绍

> Neo-brutalism skin for the DeepSeek Harness Web UI — hard borders, high contrast, two switchable schemes (Blue Command / Aged Newspaper), works in light and dark themes.

## 详细介绍

A zero-dependency **client skin plugin** for the DeepSeek Harness Web UI. It stacks a neo-brutalism palette and structure over the built-in light/dark themes via the official `theme` service — **it never replaces the built-in theme**, so the Appearance row (light / dark / system) keeps working and your skin applies to both palettes.

## ✨ 核心特性

- 🎨 **Two built-in schemes**, switchable live from Settings → General → *Neo 皮肤*
- 🧱 **Structure layer** — hard offset shadows (theme-aware black/white), sharp corners,
- 🎛️ **On/off toggle** + scheme picker in the settings row
- 🎙️ **Adapts `dsh-voice-input`** UI (popover, pills, states) to the skin
- 🌗 Fully theme-aware: light/dark/system all work

## 📦 安装

```bash
# 1. build the bundle (zero deps, no npm install)
npm run build

# 2. install into the web profile
dsh plugin --profile web add <path\to\dsh-neo-skin>

# 3. register the roster row in .dsh/profiles/web/cordis.patch.yml:
#    - insert:
#        - id: dsh-neo-skin
#          name: 'dsh-neo-skin'

# 4. restart `dsh --profile web`
```

## 🚀 快速开始

```bash
cd <path\to\dsh-neo-skin>
npm run build
dsh plugin --profile web add <path\to\dsh-neo-skin>
# 然后在 .dsh/profiles/web/cordis.patch.yml 注册：
#   - insert:
#       - id: dsh-neo-skin
#         name: 'dsh-neo-skin'
# 重启 dsh --profile web
```

## 📚 更多信息

**Screenshots / 预览**

> 截图放 `screenshots/` 目录，文件名对应上表；开发期也可打开仓库里的 `preview.html` > 交互对比两套方案 × 浅/深色。 ---

**安装（离线开发）**

cd <path\to\dsh-neo-skin> npm run build dsh plugin --profile web add <path\to\dsh-neo-skin>

## 🔗 链接

- [GitHub 仓库](https://github.com/0nt-one/dsh-neo-skin)
- [完整 README](https://github.com/0nt-one/dsh-neo-skin#readme)
- [返回dsh-neo-skin所在分类](../plugins.md)
