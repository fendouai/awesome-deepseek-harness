---
title: "dsh-notebooks"
description: "Notebooks plugin (cordis)."
keywords: "dsh-notebooks, discovery, plugin, coding, deepseek harness, dsh"
---
# dsh-notebooks

> ⭐ **4** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 插件发现 |
| 星数 | ⭐ 4 | 状态 | ✅ 活跃 |
| 作者 | [havingautism](https://github.com/havingautism) | 更新时间 | 2026-08-15 |

## 一句话介绍

> Notebooks plugin (cordis).

## 详细介绍

[English](README.en.md) | 中文 `@deepseek-ai/dsh-notebooks` 把 Codemini 风格的持久随手记带到 DSH。它提供 SQLite 存储、模型工具、生成的 `notebooks` Remote namespace，以及侧栏打开的全局「随手记」工作区。

## ✨ 核心特性

- 🗂️ 在 `#notes` 资料库中用网格或列表浏览支持搜索、筛选和排序的笔记。
- 📝 创建混合来源笔记：手写内容、网页链接、TXT/Markdown 文档。
- 🌐 自动抓取未读网页，来源变更后清空总结和 Studio 产物并重新总结。
- ✅ 精确选择参与综合总结和 Studio 产物的来源。
- 🧠 由宿主私有 Agent 生成综合总结、Mermaid 思维导图和 Markdown 报告。
- 💬 对话输入框用笔记本图标打开弹出框，或 `@` 引用**一篇**笔记追问；消息气泡下显示可点击的笔记徽章并跳转到 `#notes/<id>`。
- 🗑️ 删除前确认；工作区可查看来源原文并跳转原链接。

## 📦 安装

```bash
dsh plugin --profile web add github:havingautism/dsh-notebooks
dsh web
```

## 🔗 链接

- [GitHub 仓库](https://github.com/havingautism/dsh-notebooks)
- [完整 README](https://github.com/havingautism/dsh-notebooks#readme)
- [返回dsh-notebooks所在分类](../plugins.md)
