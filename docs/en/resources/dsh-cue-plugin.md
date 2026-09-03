---
title: "dsh-cue-plugin"
description: "DeepSeek Harness 的跨会话引用(cue)插件"
keywords: "dsh-cue-plugin, memory, plugin, coding, deepseek harness, dsh"
---
# dsh-cue-plugin

> ⭐ **6** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Memory & context |
| Stars | ⭐ 6 | Status | ✅ active |
| Author | [unnnnoooo](https://github.com/unnnnoooo) | Updated | 2026-08-13 |
| Subcategory | 🔍 Context audit | Capabilities | coding |

## One-liner

> DeepSeek Harness 的跨会话引用(cue)插件

## About

跨会话结点引用（cue）插件 / Cross-session node reference plugin for DeepSeek Harness. ---

## 📦 Install

```bash
dsh plugin add github:unnnnoooo/dsh-cue-plugin
```

## 🚀 Quick Start

```bash
## Cued nodes from <title>

   用户 cue 引用了以下结点，请把它们作为跨会话参考上下文阅读：
   ...
```

## 📚 Learn more

**安装**

dsh plugin add github:unnnnoooo/dsh-cue-plugin （本地路径同样支持：`dsh plugin add ./path/to/dsh-cue-plugin`。）

**设计要点**

从不重读源会话，模型也从不自己做提取。 相邻选区的窗口自动合并，连续结点的上下文绝不重复。 是浏览器半（工具条按钮、选择器、chips），通过 `dsh.client` 清单和 `window.__ModuleLoader__.load` 注册。

**Install**

dsh plugin add github:unnnnoooo/dsh-cue-plugin (Local checkout works too: `dsh plugin add ./path/to/dsh-cue-plugin`.)

**Usage**

1. In the composer's tool row, click the **cue** button. 2. Pick a target session by title, then select its user nodes — click to toggle, drag to box-select, or **全选 / 清空** for batch. Agent replies are shown collapsed and are never selectable; only user messages become nodes. 3. Confirm (**cue 这些结点**): the selection becomes chips in the composer, captured **at cue time** — the context snapshot is 

## 🔗 Links

- [GitHub Repository](https://github.com/unnnnoooo/dsh-cue-plugin)
- [Full README](https://github.com/unnnnoooo/dsh-cue-plugin#readme)
- [Back to the Plugins list](../plugins.md)
