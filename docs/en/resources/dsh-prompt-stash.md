---
title: "dsh-prompt-stash"
description: "Local, per-session prompt stash for DeepSeek Harness Web | 本地、分对话的提示词输入暂存工具。写了一半的长提示词，临时需要先问一个短问题？ 同时准备多个方案，但尚未决定发哪一个？将未完成的想法放入草稿架中，准备好后再继续完成"
keywords: "dsh-prompt-stash, search, plugin, coding, deepseek harness, dsh"
---
# dsh-prompt-stash

> ⭐ **3** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 3 | Status | ✅ active |
| Author | [Wine-Red](https://github.com/Wine-Red) | Updated | 2026-08-19 |
| Subcategory | 🌐 Web search | Capabilities | coding |

## One-liner

> Local, per-session prompt stash for DeepSeek Harness Web | 本地、分对话的提示词输入暂存工具。写了一半的长提示词，临时需要先问一个短问题？ 同时准备多个方案，但尚未决定发哪一个？将未完成的想法放入草稿架中，准备好后再继续完成

## About

[简体中文](README.md) | [English](README.en.md) DeepSeek Harness Web 的本地输入暂存插件。把尚未发送的纯文本压入当前会话的 LIFO 暂存栈，先处理临时问题，之后再安全恢复原输入。

## ✨ Key Features

- 每个 DSH 会话独立保存，最新内容优先，最多保留 10 条。
- 暂存后立即在输入框上方显示折叠栏，可展开预览、恢复、删除或清空。
- 当前输入非空时不会直接覆盖；恢复前必须确认先暂存当前内容。
- 使用 DSH 官方 `inputActions.setDraft()` 清空和恢复，不操作 `textarea` 或内部 Store。
- 暂存内容只保存在当前浏览器的 `localStorage`；快捷键配置通过 DSH Host settings 保存，可跨刷新和浏览器生效。
- 支持中英文、深浅主题、键盘操作和 DSH 原生队列组合布局。
- 可在“设置 → 插件 → 插件配置”中录入单键或组合键快捷键，默认使用 `Ctrl+S`。

## 📦 Install

```bash
dsh plugin --profile web add dsh-prompt-stash
```

## 🚀 Quick Start

```bash
dsh plugin --profile web update dsh-prompt-stash
```

## 📚 Learn more

**使用**

1. 在输入框中编写一段纯文本。 2. 点击工具栏中的“暂存”，或在消息输入框内按下暂存快捷键。输入框会被清空，上方立即出现折叠的暂存消息栏。 3. 输入并发送临时问题。 4. 展开暂存消息，点击目标内容恢复。 5. 如果输入框已有内容，选择“暂存当前内容并恢复此条”，或取消操作。 添加或删除成功时不会弹出通知；只有存储或输入更新失败时才会显示错误提示。 消息输入框为空时按下快捷键，会恢复并弹出最新一条暂存。恢复后若内容保持不变，继续按同一快捷键会按“最新 → 较早”的顺序轮换其他暂存，当前显示的内容会安全放到轮换队尾，循环一周后再次出现。只要修改了恢复内容、清空后重写或输入了新消息，再按快捷键就会退出轮换，将当前内容新增到暂存并清空输入框，因此仍可连续加入多条暂存。只有一条内容可轮换时，再按一次也按普通暂存处理。快捷键不会覆盖空白字符、图片或文件引用等当前输入。

**配置快捷键**

打开“设置 → 插件 → 插件配置 → 输入暂存”，点击快捷键输入框后直接按下一个按键或组合键，再保存即可立即生效。默认快捷键为 `Ctrl+S`，也可以配置为 `F8` 等单键。输入非空时快捷键执行暂存，输入为空时恢复最新一条；进入恢复状态后，重复按键可循环轮换其余暂存。快捷键只在消息输入框内生效；使用单个可打印字符会占用该字符原本的输入行为。

## 🔗 Links

- [GitHub Repository](https://github.com/Wine-Red/dsh-prompt-stash)
- [Full README](https://github.com/Wine-Red/dsh-prompt-stash#readme)
- [Back to the Plugins list](../plugins.md)
