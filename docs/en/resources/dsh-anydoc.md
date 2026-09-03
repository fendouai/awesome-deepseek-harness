---
title: "dsh-plugin-anydoc"
description: "Convert Word, PPT, Excel, PDF, EPUB and CSV documents to GitHub-Flavored Markdown via @firecrawl/anydoc."
keywords: "dsh-plugin-anydoc, developer, plugin, files, deepseek harness, dsh"
---
# dsh-plugin-anydoc

> ⭐ **6** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 6 | Status | ✅ active |
| Author | [beancookie](https://github.com/beancookie) | Updated | 2026-08-14 |
| Subcategory | 🧪 Code, tests & review | Capabilities | files |

## One-liner

> Convert Word, PPT, Excel, PDF, EPUB and CSV documents to GitHub-Flavored Markdown via @firecrawl/anydoc.

## About

一个 DeepSeek Harness (DSH) 插件，将 `@firecrawl/anydoc` 作为 `anydoc` 工具注册给 Agent，把多种文档格式转换为 GitHub-Flavored Markdown。 基于 [@firecrawl/anydoc](https://github.com/firecrawl/anydoc)（Rust 原生绑定，napi-rs），在 libuv 线程池中执行，不阻塞事件循环，无需任何外部进程或 Python 环境。

## 📦 Install

```bash
dsh plugin --profile web add github:beancookie/dsh-plugin-anydoc
```

## 🚀 Quick Start

```bash
dsh web
```

## 📚 Learn more

**安装**

dsh plugin --profile web add github:beancookie/dsh-plugin-anydoc 安装完成后直接启动： dsh web

**使用**

启动 DSH Web 后，向 Agent 发送类似指令： 请将 /path/to/report.docx 转换为 Markdown Agent 会调用 `anydoc` 工具，返回转换后的 Markdown 内容。

## 🔗 Links

- [GitHub Repository](https://github.com/beancookie/dsh-plugin-anydoc)
- [Full README](https://github.com/beancookie/dsh-plugin-anydoc#readme)
- [Back to the Plugins list](../plugins.md)
