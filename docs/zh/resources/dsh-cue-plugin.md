---
title: "dsh-cue-plugin"
description: "DeepSeek Harness 的跨会话引用(cue)插件"
keywords: "dsh-cue-plugin, memory, plugin, coding, deepseek harness, dsh"
---
# dsh-cue-plugin

> ⭐ **6** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 记忆与上下文 |
| 星数 | ⭐ 6 | 状态 | ✅ 活跃 |
| 作者 | [unnnnoooo](https://github.com/unnnnoooo) | 更新时间 | 2026-08-13 |
| 子分类 | 🔍 上下文审计 | 能力 | coding |

## 一句话介绍

> DeepSeek Harness 的跨会话引用(cue)插件

## 详细介绍

跨会话结点引用（cue）插件 / Cross-session node reference plugin for DeepSeek Harness. ---

## 📦 安装

```bash
dsh plugin add github:unnnnoooo/dsh-cue-plugin
```

## 🚀 快速开始

```bash
## Cued nodes from <title>

   用户 cue 引用了以下结点，请把它们作为跨会话参考上下文阅读：
   ...
```

## 📚 更多信息

**安装**

dsh plugin add github:unnnnoooo/dsh-cue-plugin （本地路径同样支持：`dsh plugin add ./path/to/dsh-cue-plugin`。）

**设计要点**

从不重读源会话，模型也从不自己做提取。 相邻选区的窗口自动合并，连续结点的上下文绝不重复。 是浏览器半（工具条按钮、选择器、chips），通过 `dsh.client` 清单和 `window.__ModuleLoader__.load` 注册。

**Install**

dsh plugin add github:unnnnoooo/dsh-cue-plugin (Local checkout works too: `dsh plugin add ./path/to/dsh-cue-plugin`.)

**Usage**

1. In the composer's tool row, click the **cue** button. 2. Pick a target session by title, then select its user nodes — click to toggle, drag to box-select, or **全选 / 清空** for batch. Agent replies are shown collapsed and are never selectable; only user messages become nodes. 3. Confirm (**cue 这些结点**): the selection becomes chips in the composer, captured **at cue time** — the context snapshot is 

## 🔗 链接

- [GitHub 仓库](https://github.com/unnnnoooo/dsh-cue-plugin)
- [完整 README](https://github.com/unnnnoooo/dsh-cue-plugin#readme)
- [返回dsh-cue-plugin所在分类](../plugins.md)
