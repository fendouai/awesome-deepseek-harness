---
title: "dsh-fork-to-preset"
description: "在会话 Header 上一键把当前会话分叉到任意 agent preset：选择 preset 后创建挂载到该 preset 的新子会话，并继承源会话的已完成轮次。"
keywords: "dsh-fork-to-preset, ui, plugin, deepseek harness, dsh"
---
# dsh-fork-to-preset

> ⭐ **0** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 0 | 状态 | ✅ 活跃 |
| 作者 | [bpc-oss](https://github.com/bpc-oss) | 更新时间 | 2026-08-21 |
| 子分类 | 🧭 导航与跳转 | 能力 | ui |

## 一句话介绍

> 在会话 Header 上一键把当前会话分叉到任意 agent preset：选择 preset 后创建挂载到该 preset 的新子会话，并继承源会话的已完成轮次。

## 详细介绍

A [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) plugin that adds a **"Fork to preset"** button to every conversation's header. Pick any agent preset from the roster and fork the current session into a fresh independent child session running under that preset — inheriting the parent's completed turns.

## ✨ 核心特性

- Click the **↴ Fork to preset** dropdown in the conversation header
- Select a target agent preset from the roster
- Click the button → a new session opens, mounted on the chosen preset, with the parent's completed-turn history

## 🚀 快速开始

```bash
:: Windows
mklink /J "<plugin-dir>\node_modules" "<harness>\resources\host\node_modules"
```

## 📚 更多信息

**1. Link the package into the harness install**

:: Windows mklink /J "<plugin-dir>\node_modules" "<harness>\resources\host\node_modules"

## 🔗 链接

- [GitHub 仓库](https://github.com/bpc-oss/dsh-fork-to-preset)
- [完整 README](https://github.com/bpc-oss/dsh-fork-to-preset#readme)
- [返回dsh-fork-to-preset所在分类](../plugins.md)
