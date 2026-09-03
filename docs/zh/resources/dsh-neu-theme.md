---
title: "dsh-neu-theme"
description: "DeepSeek Harness Web 的轻拟物与磨砂玻璃主题插件，提供浅色/深色主题、环境光、材质纹理和细腻微交互。Neumorphism + glassmorphism theme plugin for DeepSeek Harness Web with warm light/dark palettes, ambient lighting, grain texture, and subtle micro-interactions."
keywords: "dsh-neu-theme, search, plugin, coding, ui, deepseek harness, dsh"
---
# dsh-neu-theme

> ⭐ **6** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 搜索与研究 |
| 星数 | ⭐ 6 | 状态 | ✅ 活跃 |
| 作者 | [Lhy723](https://github.com/Lhy723) | 更新时间 | — |
| 子分类 | 🌐 网页搜索 | 能力 | coding, ui |

## 一句话介绍

> DeepSeek Harness Web 的轻拟物与磨砂玻璃主题插件，提供浅色/深色主题、环境光、材质纹理和细腻微交互。Neumorphism + glassmorphism theme plugin for DeepSeek Harness Web with warm light/dark palettes, ambient lighting, grain texture, and subtle micro-interactions.

## 详细介绍

A Neumorphism (soft-UI) theme plugin for **DeepSeek Harness web** — gentle raised-and-recessed surfaces in a cream light palette and an ink-dark palette, complete with ambient lighting, material gloss, grain texture, glassmorphism and micro-interactions. 中文说明见 [README.zh.md](README.zh.md)。

## ✨ 核心特性

- **Two themes** registered into the built-in ThemeRuntime:
- **Lighting** — ambient top glow + corner fill painted on the visible
- **Material** — three-layer shadows (contact + cast + top-edge highlight),
- **Texture** — fine grayscale grain (inline SVG feTurbulence) over the
- **Glassmorphism** — the composer capsule and its popovers (permission
- **Micro-interactions** — conversation nodes fade in on mount, bubbles
- **Settings row** — Settings → General gains a Neumorphism picker
- **Default is pristine** — selecting Default (or having no saved skin)

## 📦 安装

```bash
dsh plugin --profile web add dsh-neu-theme
# or install manually in the web profile:
cd ~/.dsh/profiles/web
pnpm add dsh-neu-theme
```

## 🚀 快速开始

```bash
npm run build   # regenerates lib/client.js from src/client.tpl.js + themes/*.json
npm run check   # syntax-checks the built bundles
```

## 📚 更多信息

**Install**

Install the published package into a dsh profile (works with the `web` profile): dsh plugin --profile web add dsh-neu-theme

**or install manually in the web profile:**

cd ~/.dsh/profiles/web pnpm add dsh-neu-theme The package is also available on [npm](https://www.npmjs.com/package/dsh-neu-theme). Then add `"dsh-neu-theme"` to `dsh.profile.bundles` in the profile's `package.json`, and restart `dsh web`. Once running: **Settings → General → Neumorphism theme** → pick **Default / Neu Light / Neu Dark**. The choice is stored in the Host settings namespace `dsh-neu-

## 🔗 链接

- [GitHub 仓库](https://github.com/Lhy723/dsh-neu-theme)
- [完整 README](https://github.com/Lhy723/dsh-neu-theme#readme)
- [返回dsh-neu-theme所在分类](../plugins.md)
