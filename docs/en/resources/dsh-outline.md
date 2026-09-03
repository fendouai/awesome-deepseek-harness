---
title: "dsh-outline"
description: "DeepSeek Harness（DSH）Web GUI 的实时大纲插件，移植自 Ophel Atlas"
keywords: "dsh-outline, search, plugin, coding, ui, deepseek harness, dsh"
---
# dsh-outline

> ⭐ **18** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 18 | Status | ✅ active |
| Author | [urzeye](https://github.com/urzeye) | Updated | — |
| Subcategory | 🌐 Web search | Capabilities | coding, ui |

## One-liner

> DeepSeek Harness（DSH）Web GUI 的实时大纲插件，移植自 Ophel Atlas

## About

[DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)（DSH）Web GUI 的**实时大纲插件**：在会话页提供一棵"用户问题 + Markdown 标题（H1~H6）"的大纲树，流式生成时实时更新，点击节点即可定位正文并高亮当前阅读位置。

## ✨ Key Features

- 大纲由会话事件流构建（用户问题为一级节点，助手回复中的 Markdown 标题挂在其下），不抓取 DOM
- 流式生成时随 token 实时更新；刷新、重连、历史分页由 DSH runtime 自动重建，无需自行处理
- 点击节点滚动定位正文，并高亮当前阅读位置
- 层级滑块控制展开深度（0~6 档），节点可单独展开/收起，支持一键展开/收起全部
- 关键词搜索（带匹配计数）、按会话收藏、"只看收藏"模式
- 一键复制大纲、回到顶部/底部

## 📦 Install

```bash
dsh plugin --profile web add dsh-outline@latest
```

## 🚀 Quick Start

```bash
pnpm pack                                          # 产出 dsh-outline-<version>.tgz
dsh plugin --profile web add ./dsh-outline-0.1.6.tgz
```

## 🔗 Links

- [GitHub Repository](https://github.com/urzeye/dsh-outline)
- [Full README](https://github.com/urzeye/dsh-outline#readme)
- [Back to the Plugins list](../plugins.md)
