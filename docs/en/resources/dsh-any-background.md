---
title: "dsh-any-background"
description: "Deepseek Harness 自定义主题插件，支持自定义图片/视频壁纸，对话框，侧边栏等透明度模糊度调整，全局主题色的色轮调整插件"
keywords: "dsh-any-background, ui, plugin, coding, deepseek harness, dsh"
---
# dsh-any-background

> ⭐ **20** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 20 | Status | ✅ active |
| Author | [Tkingxiao](https://github.com/Tkingxiao) | Updated | — |
| Subcategory | 🎨 Skins & themes | Capabilities | coding |

## One-liner

> Deepseek Harness 自定义主题插件，支持自定义图片/视频壁纸，对话框，侧边栏等透明度模糊度调整，全局主题色的色轮调整插件

## About

A **DeepSeek Harness** appearance plugin that lets you fully customize the Web UI — custom theme color, background wallpaper, and fine-grained per-part opacity & blur controls. ---

## ✨ Key Features

- **PS-style Color Wheel** — Pick hue on the ring, adjust saturation & lightness in the inscribed square. Generates 30+ CSS design tokens in real time.
- **Precise HSL / RGB Input** — Enter exact color values numerically with instant bidirectional sync to the wheel.
- **Smart Color Extraction** — One click derives a theme color from your wallpaper by sampling the visible region, quantizing, and filtering out gray / near-black
- **Eyedropper** — Hover the wallpaper to preview a color and click to pick it as the theme color.
- **Background Wallpaper** — Upload any image as your wallpaper. Drag to pan and scroll to zoom inside a viewport-proportional editor.
- **Video Wallpaper** — Use a video as a live wallpaper: muted looping playback that survives refreshes (file persistence + HTTP streaming with Range seek), with 
- **Position Editor** — One shared editor for images and videos: drag to pan, scroll to zoom, one-click reset. Image and video placements are stored separately an
- **Layout Modes** — Fit / Fill / Stretch / Tile / Center for both images and videos; in Fit mode the editor-committed framing stays consistent across window resi

## 📦 Install

```bash
dsh plugin --profile web add github:Tkingxiao/dsh-any-background
# or, if published to the registry:
dsh plugin --profile web add dsh-any-background
```

## 🚀 Quick Start

```bash
dsh web
```

## 📚 Learn more

**Screenshots**

<p align="center">  <br/> <em>Custom homepage · wallpaper + theme color applied</em> </p> <p align="center">  <br/> <em>Theme color picker · PS-style wheel + precise HSL/RGB inputs</em> </p> <p align="center">  <br/> <em>Per-part opacity and blur · main background, sidebar, cards, settings</em> </p> <p align="center">  <br/> <em>Background editor · image/video wallpapers support drag-to-pan and sc

**Method 2: npx (No Global Install)**

npx @deepseek-ai/dsh plugin --profile web add github:Tkingxiao/dsh-any-background npx @deepseek-ai/dsh web

## 🔗 Links

- [GitHub Repository](https://github.com/Tkingxiao/dsh-any-background)
- [Full README](https://github.com/Tkingxiao/dsh-any-background#readme)
- [Back to the Plugins list](../plugins.md)
