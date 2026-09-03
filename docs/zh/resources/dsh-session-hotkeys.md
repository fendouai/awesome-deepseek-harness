---
title: "dsh-session-hotkeys"
description: "会话热键：像切浏览器标签页一样用键盘管理 DSH Web 会话（Alt+1-9 顺序切换、固定槽位、上/下一个、新建/归档/重命名、键盘模型切换与备用发送），键位可在面板录制重绑，Windows/macOS 双预设。"
keywords: "dsh-session-hotkeys, ui, plugin, deepseek harness, dsh"
---
# dsh-session-hotkeys

> ⭐ **3** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 3 | 状态 | ✅ 活跃 |
| 作者 | [YEYEYEYESHIFU](https://github.com/YEYEYEYESHIFU) | 更新时间 | — |
| 子分类 | 🖥️ 侧边栏与面板 | 能力 | ui |

## 一句话介绍

> 会话热键：像切浏览器标签页一样用键盘管理 DSH Web 会话（Alt+1-9 顺序切换、固定槽位、上/下一个、新建/归档/重命名、键盘模型切换与备用发送），键位可在面板录制重绑，Windows/macOS 双预设。

## 详细介绍

Session hotkeys for DeepSeek Harness Web · 给 DeepSeek Harness Web 的会话快捷键插件 Switch sessions from the keyboard the way you switch browser tabs. 像切换浏览器标签页一样用键盘管理会话。 ---

## 📦 安装

```bash
dsh plugin --profile web add "dsh-session-hotkeys"
```

## 🚀 快速开始

```bash
git clone https://github.com/YEYEYEYESHIFU/dsh-session-hotkeys.git
cd dsh-session-hotkeys
npm run verify     # self-check: package structure, parseable client bundle, no external imports
```

## 📚 更多信息

**Install**

dsh plugin --profile web add "dsh-session-hotkeys" Then restart DSH Web. 然后重启 DSH Web 即可。 > [English](#english) · [简体中文](#简体中文)

**说明**

<details> <summary><b>macOS 预设为什么长这样</b></summary> Chrome 里 ⌘+1-9 和 ⌃+1-9 都会切换标签页（Safari 只有 ⌘），所以顺序切换用 ⌃⇧1-9。⌥ 单独按会打出特殊字符，因此从不当主修饰键。⌃+↑/↓ 是调度中心，⌃+N/P/F/B/A/E/K/D 是文本框的 Emacs 行编辑键，故相关组合都补了 ⌥。⌃/⌘+Enter 是输入框自带的发送快捷键，Enter 系列因此加 ⌥。全部组合已在 macOS Chrome 与 Safari 中逐项筛查无冲突。macOS 上键位一律用原生符号显示（⌃ ⌥ ⇧ ⌘）。 </details> <details> <summary><b>兼容性与已知限制</b></summary> </details> <details> <summary><b>旧版 CLI 没有 dsh plu

## 🔗 链接

- [GitHub 仓库](https://github.com/YEYEYEYESHIFU/dsh-session-hotkeys)
- [完整 README](https://github.com/YEYEYEYESHIFU/dsh-session-hotkeys#readme)
- [返回dsh-session-hotkeys所在分类](../plugins.md)
