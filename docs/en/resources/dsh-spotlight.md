---
title: "dsh-spotlight"
description: "Keyboard-first command palette for DeepSeek Harness Web."
keywords: "dsh-spotlight, ui, plugin, deepseek harness, dsh"
---
# dsh-spotlight

> ⭐ **9** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 9 | Status | ✅ active |
| Author | [0xsline](https://github.com/0xsline) | Updated | 2026-08-14 |
| Subcategory | 🖥️ Sidebars & panels | Capabilities | ui |

## One-liner

> Keyboard-first command palette for DeepSeek Harness Web.

## About

[简体中文](README.zh.md) | English A keyboard-first command palette for DeepSeek Harness Web. Open one palette to find native slash commands, recent sessions, visible UI actions, and installed plugin settings—without leaving the keyboard.

## ✨ Key Features

- **One shortcut:** `⌘K` on macOS, `Ctrl+K` on other platforms.
- **Customizable:** click the shortcut control in the footer, then press a new
- **Native actions:** discovers and triggers the actions already provided by
- **Fast search:** deterministic fuzzy matching across slash commands, recent
- **Keyboard navigation:** Arrow Up/Down to select, Enter to run, Escape to
- **Clean lifecycle:** removes its event listeners, styles, and DOM nodes when

## 📦 Install

```bash
dsh plugin --profile web add "@0xsline/dsh-spotlight"
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add "github:0xsline/dsh-spotlight#main"
```

## 📚 Learn more

**Install**

Install the bundle into your DSH Web profile. From npm: dsh plugin --profile web add "@0xsline/dsh-spotlight" Or from the Git source: dsh plugin --profile web add "github:0xsline/dsh-spotlight#main" The Git install runs the package's `prepare` lifecycle because generated `lib/` files are not committed. It deletes and recreates only this package's `lib/` directory with the repository-local TypeScri

**Usage**

1. Open Spotlight with the global shortcut, or type `/spotlight` in the DSH Web composer and pick the entry from the slash menu. 2. Type to filter commands and actions. 3. Use Arrow Up/Down and Enter, or click a result. 4. Click **Shortcut** in the footer to record a different key combination. 5. Click **Reset** to restore the platform default. Shortcut preferences are local to the current browser

## 🔗 Links

- [GitHub Repository](https://github.com/0xsline/dsh-spotlight)
- [Full README](https://github.com/0xsline/dsh-spotlight#readme)
- [Back to the Plugins list](../plugins.md)
