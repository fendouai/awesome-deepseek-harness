---
title: "dsh-neo-skin"
description: "Neo-brutalism skin for the DeepSeek Harness Web UI — hard borders, high contrast, two switchable schemes (Blue Command / Aged Newspaper), works in light and dark themes."
keywords: "dsh-neo-skin, search, plugin, coding, ui, deepseek harness, dsh"
---
# dsh-neo-skin

> ⭐ **4** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 4 | Status | ✅ active |
| Author | [0nt-one](https://github.com/0nt-one) | Updated | — |
| Subcategory | 🌐 Web search | Capabilities | coding, search, ui |

## One-liner

> Neo-brutalism skin for the DeepSeek Harness Web UI — hard borders, high contrast, two switchable schemes (Blue Command / Aged Newspaper), works in light and dark themes.

## About

A zero-dependency **client skin plugin** for the DeepSeek Harness Web UI. It stacks a neo-brutalism palette and structure over the built-in light/dark themes via the official `theme` service — **it never replaces the built-in theme**, so the Appearance row (light / dark / system) keeps working and your skin applies to both palettes.

## ✨ Key Features

- 🎨 **Two built-in schemes**, switchable live from Settings → General → *Neo 皮肤*
- 🧱 **Structure layer** — hard offset shadows (theme-aware black/white), sharp corners,
- 🎛️ **On/off toggle** + scheme picker in the settings row
- 🎙️ **Adapts `dsh-voice-input`** UI (popover, pills, states) to the skin
- 🌗 Fully theme-aware: light/dark/system all work

## 📦 Install

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

## 🚀 Quick Start

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

## 📚 Learn more

**Screenshots / 预览**

> 截图放 `screenshots/` 目录，文件名对应上表；开发期也可打开仓库里的 `preview.html` > 交互对比两套方案 × 浅/深色。 ---

**安装（离线开发）**

cd <path\to\dsh-neo-skin> npm run build dsh plugin --profile web add <path\to\dsh-neo-skin>

## 🔗 Links

- [GitHub Repository](https://github.com/0nt-one/dsh-neo-skin)
- [Full README](https://github.com/0nt-one/dsh-neo-skin#readme)
- [Back to the Plugins list](../plugins.md)
