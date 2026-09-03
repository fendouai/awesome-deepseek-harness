---
title: "dsh-outline"
description: "DeepSeek Harness（DSH）Web GUI 的实时大纲插件，移植自 Ophel Atlas"
keywords: "dsh-outline, search, plugin, coding, ui, deepseek harness, dsh"
---
# dsh-outline

> ⭐ **18** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 搜索与研究 |
| 星数 | ⭐ 18 | 状态 | ✅ 活跃 |
| 作者 | [urzeye](https://github.com/urzeye) | 更新时间 | — |
| 子分类 | 🌐 网页搜索 | 能力 | coding, ui |

## 一句话介绍

> DeepSeek Harness（DSH）Web GUI 的实时大纲插件，移植自 Ophel Atlas

## 详细介绍

[DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)（DSH）Web GUI 的**实时大纲插件**：在会话页提供一棵"用户问题 + Markdown 标题（H1~H6）"的大纲树，流式生成时实时更新，点击节点即可定位正文并高亮当前阅读位置。

## ✨ 核心特性

- 大纲由会话事件流构建（用户问题为一级节点，助手回复中的 Markdown 标题挂在其下），不抓取 DOM
- 流式生成时随 token 实时更新；刷新、重连、历史分页由 DSH runtime 自动重建，无需自行处理
- 点击节点滚动定位正文，并高亮当前阅读位置
- 层级滑块控制展开深度（0~6 档），节点可单独展开/收起，支持一键展开/收起全部
- 关键词搜索（带匹配计数）、按会话收藏、"只看收藏"模式
- 一键复制大纲、回到顶部/底部

## 📦 安装

```bash
dsh plugin --profile web add dsh-outline@latest
```

## 🚀 快速开始

```bash
pnpm pack                                          # 产出 dsh-outline-<version>.tgz
dsh plugin --profile web add ./dsh-outline-0.1.6.tgz
```

## 🔗 链接

- [GitHub 仓库](https://github.com/urzeye/dsh-outline)
- [完整 README](https://github.com/urzeye/dsh-outline#readme)
- [返回dsh-outline所在分类](../plugins.md)
