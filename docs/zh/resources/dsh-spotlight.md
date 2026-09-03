---
title: "dsh-spotlight"
description: "DSH Web 键盘优先命令面板。"
keywords: "dsh-spotlight, ui, plugin, deepseek harness, dsh"
---
# dsh-spotlight

> ⭐ **9** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 9 | 状态 | ✅ 活跃 |
| 作者 | [0xsline](https://github.com/0xsline) | 更新时间 | 2026-08-14 |
| 子分类 | 🖥️ 侧边栏与面板 | 能力 | ui |

## 一句话介绍

> DSH Web 键盘优先命令面板。

## 详细介绍

[简体中文](README.zh.md) | English A keyboard-first command palette for DeepSeek Harness Web. Open one palette to find native slash commands, recent sessions, visible UI actions, and installed plugin settings—without leaving the keyboard.

## ✨ 核心特性

- **One shortcut:** `⌘K` on macOS, `Ctrl+K` on other platforms.
- **Customizable:** click the shortcut control in the footer, then press a new
- **Native actions:** discovers and triggers the actions already provided by
- **Fast search:** deterministic fuzzy matching across slash commands, recent
- **Keyboard navigation:** Arrow Up/Down to select, Enter to run, Escape to
- **Clean lifecycle:** removes its event listeners, styles, and DOM nodes when

## 📦 安装

```bash
dsh plugin --profile web add "@0xsline/dsh-spotlight"
```

## 🚀 快速开始

```bash
dsh plugin --profile web add "github:0xsline/dsh-spotlight#main"
```

## 📚 更多信息

**Install**

Install the bundle into your DSH Web profile. From npm: dsh plugin --profile web add "@0xsline/dsh-spotlight" Or from the Git source: dsh plugin --profile web add "github:0xsline/dsh-spotlight#main" The Git install runs the package's `prepare` lifecycle because generated `lib/` files are not committed. It deletes and recreates only this package's `lib/` directory with the repository-local TypeScri

**Usage**

1. Open Spotlight with the global shortcut, or type `/spotlight` in the DSH Web composer and pick the entry from the slash menu. 2. Type to filter commands and actions. 3. Use Arrow Up/Down and Enter, or click a result. 4. Click **Shortcut** in the footer to record a different key combination. 5. Click **Reset** to restore the platform default. Shortcut preferences are local to the current browser

## 🔗 链接

- [GitHub 仓库](https://github.com/0xsline/dsh-spotlight)
- [完整 README](https://github.com/0xsline/dsh-spotlight#readme)
- [返回dsh-spotlight所在分类](../plugins.md)
