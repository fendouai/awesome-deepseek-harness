---
title: "dsh-plugin-anydoc"
description: "基于 @firecrawl/anydoc 将 Word/PPT/Excel/PDF/EPUB/CSV 等文档转换为 GFM Markdown。"
keywords: "dsh-plugin-anydoc, developer, plugin, files, deepseek harness, dsh"
---
# dsh-plugin-anydoc

> ⭐ **6** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 6 | 状态 | ✅ 活跃 |
| 作者 | [beancookie](https://github.com/beancookie) | 更新时间 | 2026-08-14 |
| 子分类 | 🧪 代码·测试·审查 | 能力 | files |

## 一句话介绍

> 基于 @firecrawl/anydoc 将 Word/PPT/Excel/PDF/EPUB/CSV 等文档转换为 GFM Markdown。

## 详细介绍

一个 DeepSeek Harness (DSH) 插件，将 `@firecrawl/anydoc` 作为 `anydoc` 工具注册给 Agent，把多种文档格式转换为 GitHub-Flavored Markdown。 基于 [@firecrawl/anydoc](https://github.com/firecrawl/anydoc)（Rust 原生绑定，napi-rs），在 libuv 线程池中执行，不阻塞事件循环，无需任何外部进程或 Python 环境。

## 📦 安装

```bash
dsh plugin --profile web add github:beancookie/dsh-plugin-anydoc
```

## 🚀 快速开始

```bash
dsh web
```

## 📚 更多信息

**安装**

dsh plugin --profile web add github:beancookie/dsh-plugin-anydoc 安装完成后直接启动： dsh web

**使用**

启动 DSH Web 后，向 Agent 发送类似指令： 请将 /path/to/report.docx 转换为 Markdown Agent 会调用 `anydoc` 工具，返回转换后的 Markdown 内容。

## 🔗 链接

- [GitHub 仓库](https://github.com/beancookie/dsh-plugin-anydoc)
- [完整 README](https://github.com/beancookie/dsh-plugin-anydoc#readme)
- [返回dsh-plugin-anydoc所在分类](../plugins.md)
