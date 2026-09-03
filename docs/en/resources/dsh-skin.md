---
title: "dsh-skin"
description: "Codex-style skin switcher plus custom translucent wallpaper with opacity/blur controls."
keywords: "dsh-skin, ui, plugin, deepseek harness, dsh"
---
# dsh-skin

> ⭐ **19** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 19 | Status | ✅ active |
| Author | [KinGao294](https://github.com/KinGao294) | Updated | 2026-08-18 |
| Subcategory | 🎨 Skins & themes | Capabilities | ui |

## One-liner

> Codex-style skin switcher plus custom translucent wallpaper with opacity/blur controls.

## About

Skin switcher + custom wallpaper + **奶龙桌宠（desktop pet with sticker pack）** for DeepSeek Harness — a "change the skin" feature in the spirit of Codex themes. It registers a curated catalog of palettes into DSH's built-in theme runtime and adds three rows to **Settings → General** (below the built-in Appearance row): - **皮肤 / Skins** — pick one of 7 curated palettes (or **默认 / Default** to follow the built-in appearance). - **背景图片 / Wallpaper** — local image, or paste an image/video URL; opacity, blur, and fit (cover / contain / stretch / tile). - **奶龙桌宠 / Pet** — a floating, draggable yellow-dragon desktop pet with an 8-mood sticker pack (表情包). It follows the agent's running state (idle → thinking → working → done → sleeping), blinks while idle, falls asleep when idle too long, can be dragg

## ✨ Key Features

- **皮肤 / Skins** — pick one of 7 curated palettes (or **默认 / Default** to
- **背景图片 / Wallpaper** — local image, or paste an image/video URL; opacity,
- **奶龙桌宠 / Pet** — a floating, draggable yellow-dragon desktop pet with an

## 📦 Install

```bash
dsh plugin --profile web add -w /path/to/dsh-skin
```

## 🚀 Quick Start

```bash
# stop the running instance, then:
dsh web
```

## 📚 Learn more

**Install**

From anywhere, add the package to the `web` profile: dsh plugin --profile web add -w /path/to/dsh-skin > The `-w` flag is required: every profile ships a `pnpm-workspace.yaml`, so > pnpm 9 treats the profile directory as a workspace root and refuses a bare > `add` with `ERR_PNPM_ADDING_TO_ROOT`. This runs pnpm in `~/.dsh/profiles/web`, installs the package, and appends it to `dsh.profile.bundles` 

## 🔗 Links

- [GitHub Repository](https://github.com/KinGao294/dsh-skin)
- [Full README](https://github.com/KinGao294/dsh-skin#readme)
- [Back to the Plugins list](../plugins.md)
