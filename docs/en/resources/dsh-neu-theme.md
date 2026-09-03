---
title: "dsh-neu-theme"
description: "DeepSeek Harness Web 的轻拟物与磨砂玻璃主题插件，提供浅色/深色主题、环境光、材质纹理和细腻微交互。Neumorphism + glassmorphism theme plugin for DeepSeek Harness Web with warm light/dark palettes, ambient lighting, grain texture, and subtle micro-interactions."
keywords: "dsh-neu-theme, search, plugin, coding, ui, deepseek harness, dsh"
---
# dsh-neu-theme

> ⭐ **6** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 6 | Status | ✅ active |
| Author | [Lhy723](https://github.com/Lhy723) | Updated | — |
| Subcategory | 🌐 Web search | Capabilities | coding, ui |

## One-liner

> DeepSeek Harness Web 的轻拟物与磨砂玻璃主题插件，提供浅色/深色主题、环境光、材质纹理和细腻微交互。Neumorphism + glassmorphism theme plugin for DeepSeek Harness Web with warm light/dark palettes, ambient lighting, grain texture, and subtle micro-interactions.

## About

A Neumorphism (soft-UI) theme plugin for **DeepSeek Harness web** — gentle raised-and-recessed surfaces in a cream light palette and an ink-dark palette, complete with ambient lighting, material gloss, grain texture, glassmorphism and micro-interactions. 中文说明见 [README.zh.md](README.zh.md)。

## ✨ Key Features

- **Two themes** registered into the built-in ThemeRuntime:
- **Lighting** — ambient top glow + corner fill painted on the visible
- **Material** — three-layer shadows (contact + cast + top-edge highlight),
- **Texture** — fine grayscale grain (inline SVG feTurbulence) over the
- **Glassmorphism** — the composer capsule and its popovers (permission
- **Micro-interactions** — conversation nodes fade in on mount, bubbles
- **Settings row** — Settings → General gains a Neumorphism picker
- **Default is pristine** — selecting Default (or having no saved skin)

## 📦 Install

```bash
dsh plugin --profile web add dsh-neu-theme
# or install manually in the web profile:
cd ~/.dsh/profiles/web
pnpm add dsh-neu-theme
```

## 🚀 Quick Start

```bash
npm run build   # regenerates lib/client.js from src/client.tpl.js + themes/*.json
npm run check   # syntax-checks the built bundles
```

## 📚 Learn more

**Install**

Install the published package into a dsh profile (works with the `web` profile): dsh plugin --profile web add dsh-neu-theme

**or install manually in the web profile:**

cd ~/.dsh/profiles/web pnpm add dsh-neu-theme The package is also available on [npm](https://www.npmjs.com/package/dsh-neu-theme). Then add `"dsh-neu-theme"` to `dsh.profile.bundles` in the profile's `package.json`, and restart `dsh web`. Once running: **Settings → General → Neumorphism theme** → pick **Default / Neu Light / Neu Dark**. The choice is stored in the Host settings namespace `dsh-neu-

## 🔗 Links

- [GitHub Repository](https://github.com/Lhy723/dsh-neu-theme)
- [Full README](https://github.com/Lhy723/dsh-neu-theme#readme)
- [Back to the Plugins list](../plugins.md)
