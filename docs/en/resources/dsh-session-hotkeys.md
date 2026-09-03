---
title: "dsh-session-hotkeys"
description: "Session hotkeys for the DSH Web GUI: switch sessions like browser tabs (positional Alt+1-9, pinned slots, previous/next), keyboard model switching, alternate send and archive confirmation, every binding rebindable with Windows/macOS presets."
keywords: "dsh-session-hotkeys, ui, plugin, deepseek harness, dsh"
---
# dsh-session-hotkeys

> ⭐ **3** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 3 | Status | ✅ active |
| Author | [YEYEYEYESHIFU](https://github.com/YEYEYEYESHIFU) | Updated | — |
| Subcategory | 🖥️ Sidebars & panels | Capabilities | ui |

## One-liner

> Session hotkeys for the DSH Web GUI: switch sessions like browser tabs (positional Alt+1-9, pinned slots, previous/next), keyboard model switching, alternate send and archive confirmation, every binding rebindable with Windows/macOS presets.

## About

Session hotkeys for DeepSeek Harness Web · 给 DeepSeek Harness Web 的会话快捷键插件 Switch sessions from the keyboard the way you switch browser tabs. 像切换浏览器标签页一样用键盘管理会话。 ---

## 📦 Install

```bash
dsh plugin --profile web add "dsh-session-hotkeys"
```

## 🚀 Quick Start

```bash
git clone https://github.com/YEYEYEYESHIFU/dsh-session-hotkeys.git
cd dsh-session-hotkeys
npm run verify     # self-check: package structure, parseable client bundle, no external imports
```

## 📚 Learn more

**Install**

dsh plugin --profile web add "dsh-session-hotkeys" Then restart DSH Web. 然后重启 DSH Web 即可。 > [English](#english) · [简体中文](#简体中文)

**说明**

<details> <summary><b>macOS 预设为什么长这样</b></summary> Chrome 里 ⌘+1-9 和 ⌃+1-9 都会切换标签页（Safari 只有 ⌘），所以顺序切换用 ⌃⇧1-9。⌥ 单独按会打出特殊字符，因此从不当主修饰键。⌃+↑/↓ 是调度中心，⌃+N/P/F/B/A/E/K/D 是文本框的 Emacs 行编辑键，故相关组合都补了 ⌥。⌃/⌘+Enter 是输入框自带的发送快捷键，Enter 系列因此加 ⌥。全部组合已在 macOS Chrome 与 Safari 中逐项筛查无冲突。macOS 上键位一律用原生符号显示（⌃ ⌥ ⇧ ⌘）。 </details> <details> <summary><b>兼容性与已知限制</b></summary> </details> <details> <summary><b>旧版 CLI 没有 dsh plu

## 🔗 Links

- [GitHub Repository](https://github.com/YEYEYEYESHIFU/dsh-session-hotkeys)
- [Full README](https://github.com/YEYEYEYESHIFU/dsh-session-hotkeys#readme)
- [Back to the Plugins list](../plugins.md)
