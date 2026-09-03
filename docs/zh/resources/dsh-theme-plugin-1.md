---
title: "dsh-theme-plugin"
description: "DSH Web GUI theme studio: presets + per-mode customization (accent, background, foreground, fonts, translucent sidebar, contrast) via the official webServer.tapIndex seam"
keywords: "dsh-theme-plugin, search, plugin, coding, ui, deepseek harness, dsh"
---
# dsh-theme-plugin

> ⭐ **3** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 搜索与研究 |
| 星数 | ⭐ 3 | 状态 | ✅ 活跃 |
| 作者 | [BeiZi6](https://github.com/BeiZi6) | 更新时间 | — |
| 子分类 | 🌐 网页搜索 | 能力 | coding, ui |

## 一句话介绍

> DSH Web GUI theme studio: presets + per-mode customization (accent, background, foreground, fonts, translucent sidebar, contrast) via the official webServer.tapIndex seam

## 详细介绍

**[English](README.md) · [简体中文](README.zh-CN.md)** Theme studio for the DeepSeek Harness (DSH) Web GUI: five built-in presets plus fully customizable light/dark palettes — accent, background, foreground, UI and code fonts, translucent sidebar and contrast — applied instantly, with no page refresh.

## ✨ 核心特性

- 🎨 **5 built-in presets** — `codex-warm`, `nord`, `solarized`, `graphite`, plus the stock DeepSeek theme
- 🖌️ **Full customization** — per-mode (`light.*` / `dark.*`) accent, background, foreground, UI font, code font, translucent sidebar and contrast; `custom` mode 
- ⚡ **Instant hot-swap** — a Settings GUI ("Theme Studio") applies changes immediately through the official `ctx.theme.overrideTokens` API; light/dark follow the 
- 💾 **Persistent** — the selection is saved in browser `localStorage` and survives reloads
- 🧮 **70+ derived tokens** — three colors plus a contrast value expand into the whole semantic token set (borders, layers, scrollbar, tooltip, code blocks, bubble
- 🪟 **Translucent sidebar** — real frosted sidebar via the `--dsw-specific-sidebar-fill` variable
- 🔌 **Official seams only** — host-side injection through `webServer.tapIndex`, no patched vendor files

## 📦 安装

```bash
dsh plugin --profile web add github:BeiZi6/dsh-theme-plugin
```

## 🚀 快速开始

```bash
dsh plugin --profile web remove dsh-theme-plugin
```

## 📚 更多信息

**Installation**

Requires DeepSeek Harness with the web profile enabled. Install from the official registry: dsh plugin --profile web add github:BeiZi6/dsh-theme-plugin Restart `dsh web` for the plugin to take effect. To remove: dsh plugin --profile web remove dsh-theme-plugin

**Settings GUI (recommended)**

After a restart, open **Settings → Theme Studio**: Every change applies instantly and persists locally; GUI selections take priority over host config. > The `stock` preset derives no palette: color controls are disabled and only fonts can be overridden.

**Config reference**

Empty strings mean "keep the preset value"; unset fields are not overridden at all. Example — merge into the web profile patch (`$DSH_HOME/profiles/web/cordis.patch.yml`): config: preset: codex-warm light: accent: '#FF6B35' background: '#FFFAF0' foreground: '#1A1A1A' uiFont: '"Inter", "PingFang SC", sans-serif' codeFont: '"JetBrains Mono", Consolas, monospace' translucentSidebar: off contrast: 70 

## 🔗 链接

- [GitHub 仓库](https://github.com/BeiZi6/dsh-theme-plugin)
- [完整 README](https://github.com/BeiZi6/dsh-theme-plugin#readme)
- [返回dsh-theme-plugin所在分类](../plugins.md)
