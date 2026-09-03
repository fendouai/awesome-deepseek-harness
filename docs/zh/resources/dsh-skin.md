---
title: "dsh-skin"
description: "Codex 风格皮肤切换器 + 自定义半透明壁纸，支持透明度/模糊控制。"
keywords: "dsh-skin, ui, plugin, deepseek harness, dsh"
---
# dsh-skin

> ⭐ **19** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 19 | 状态 | ✅ 活跃 |
| 作者 | [KinGao294](https://github.com/KinGao294) | 更新时间 | 2026-08-18 |
| 子分类 | 🎨 皮肤与主题 | 能力 | ui |

## 一句话介绍

> Codex 风格皮肤切换器 + 自定义半透明壁纸，支持透明度/模糊控制。

## 详细介绍

Skin switcher + custom wallpaper + **奶龙桌宠（desktop pet with sticker pack）** for DeepSeek Harness — a "change the skin" feature in the spirit of Codex themes. It registers a curated catalog of palettes into DSH's built-in theme runtime and adds three rows to **Settings → General** (below the built-in Appearance row): - **皮肤 / Skins** — pick one of 7 curated palettes (or **默认 / Default** to follow the built-in appearance). - **背景图片 / Wallpaper** — local image, or paste an image/video URL; opacity, blur, and fit (cover / contain / stretch / tile). - **奶龙桌宠 / Pet** — a floating, draggable yellow-dragon desktop pet with an 8-mood sticker pack (表情包). It follows the agent's running state (idle → thinking → working → done → sleeping), blinks while idle, falls asleep when idle too long, can be dragg

## ✨ 核心特性

- **皮肤 / Skins** — pick one of 7 curated palettes (or **默认 / Default** to
- **背景图片 / Wallpaper** — local image, or paste an image/video URL; opacity,
- **奶龙桌宠 / Pet** — a floating, draggable yellow-dragon desktop pet with an

## 📦 安装

```bash
dsh plugin --profile web add -w /path/to/dsh-skin
```

## 🚀 快速开始

```bash
# stop the running instance, then:
dsh web
```

## 📚 更多信息

**Install**

From anywhere, add the package to the `web` profile: dsh plugin --profile web add -w /path/to/dsh-skin > The `-w` flag is required: every profile ships a `pnpm-workspace.yaml`, so > pnpm 9 treats the profile directory as a workspace root and refuses a bare > `add` with `ERR_PNPM_ADDING_TO_ROOT`. This runs pnpm in `~/.dsh/profiles/web`, installs the package, and appends it to `dsh.profile.bundles` 

## 🔗 链接

- [GitHub 仓库](https://github.com/KinGao294/dsh-skin)
- [完整 README](https://github.com/KinGao294/dsh-skin#readme)
- [返回dsh-skin所在分类](../plugins.md)
