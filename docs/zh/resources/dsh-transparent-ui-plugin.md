---
title: "dsh-transparent-ui-plugin"
description: "是一层高自由度的玻璃质感主题，套在 DeepSeek Harness 网页端。顶栏、侧边栏、输入框、统计行、轨迹视图都成了磨砂玻璃片。玻璃模糊度、磨砂度、背景（流体或自定义壁纸，壁纸还能单独调模糊和磨砂）全都能在设置卡片里自由调节。关掉开关就回到原生界面，不改 DSH 任何一行源码。"
keywords: "dsh-transparent-ui-plugin, ui, plugin, coding, deepseek harness, dsh"
---
# dsh-transparent-ui-plugin

> ⭐ **355** · ✅ 活跃 · 插件 · 近期 ⬆️ +16

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 355 | 状态 | ✅ 活跃 |
| 作者 | [WYH66666666](https://github.com/WYH66666666) | 更新时间 | 2026-08-20 |
| 子分类 | 🎨 皮肤与主题 | 能力 | coding |

## 一句话介绍

> 是一层高自由度的玻璃质感主题，套在 DeepSeek Harness 网页端。顶栏、侧边栏、输入框、统计行、轨迹视图都成了磨砂玻璃片。玻璃模糊度、磨砂度、背景（流体或自定义壁纸，壁纸还能单独调模糊和磨砂）全都能在设置卡片里自由调节。关掉开关就回到原生界面，不改 DSH 任何一行源码。

## 详细介绍

Aqua is a highly customizable glassmorphism theme for the DeepSeek Harness web UI. The header, sidebar, composer, stats line, and trajectory view all become panes of frosted glass. you can put video for wallpaper and Switch it off and the stock UI comes back exactly, with no source changes to DSH itself.

## ✨ 核心特性

- **Two modes**: **Mica** restyles the layout into floating glass cards (blur and frost adjustable), while **Compatibility Mode** keeps the stock layout byte-for-
- **Free backdrop**: a living fluid board (hue adjustable) or your own wallpaper (fills the page, aspect preserved, with its own blur and frost); light wallpapers
- **Background brightness**: follows the resolved scheme — dark mode darkens (0–50), light mode brightens (50–100), 50 is unchanged
- **Particle whale**: the deepseek.com/harness centerpiece fish (a 2D port of the site's particle engine), centered in the chat area right of the sidebar — white 
- **Glossy "Harness" badge**: in dark mode the sidebar wordmark wears the official nameplate pill (135° gradient ring + soft glow); light mode keeps the stock pla
- **Edge fades**: 5px gradient blur bands pinned to the top and bottom of the page, above the chat content — scrolling content melts into the edges; faint white v
- One switch: off restores the stock UI exactly, and every effect is removed with the plugin

## 📦 安装

```bash
dsh plugin --profile web add dsh-client-ui-aqua
```

## 🚀 快速开始

```bash
powershell -ExecutionPolicy Bypass -Command "Invoke-WebRequest 'https://github.com/WYH66666666/DSH-Transparent-UI-Plugin/raw/main/install.ps1' -OutFile install.ps1; .\install.ps1"
```

## 📚 更多信息

**Notice ⚠️: As DSH has been updated, I am unable to promptly **

Aqua is a highly customizable glassmorphism theme for the DeepSeek Harness web UI. The header, sidebar, composer, stats line, and trajectory view all become panes of frosted glass. you can put video for wallpaper and Switch it off and the stock UI comes back exactly, with no source changes to DSH itself.

**Option 2: GitHub installer (fallback)**

No npm account and no git needed (falls back to a plain zip download). **Windows (one command):** powershell -ExecutionPolicy Bypass -Command "Invoke-WebRequest 'https://github.com/WYH66666666/DSH-Transparent-UI-Plugin/raw/main/install.ps1' -OutFile install.ps1; .\install.ps1" Installs the **latest release** by default. The script links the plugin into the profile's `node_modules` and registers `u

**Usage**

Reload the web UI. Aqua is **on by default**; the master switch lives in **Settings → Plugins → Glass theme** (same shape as the other plugin cards), and every other control sits directly under **Settings → General → Appearance** (no title of its own): mode, blur/frost (Mica mode), fluid color, background brightness, backdrop (fluid/wallpaper) with its wallpaper controls, and the particle-whale to

## 🔗 链接

- [GitHub 仓库](https://github.com/WYH66666666/DSH-Transparent-UI-Plugin)
- [完整 README](https://github.com/WYH66666666/DSH-Transparent-UI-Plugin#readme)
- [返回dsh-transparent-ui-plugin所在分类](../plugins.md)
