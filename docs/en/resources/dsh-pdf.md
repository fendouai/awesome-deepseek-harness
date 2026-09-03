---
title: "dsh-pdf"
description: "PDF toolbox: extract text, metadata and page ranges via pdfjs-dist, local with no API key."
keywords: "dsh-pdf, developer, plugin, files, deepseek harness, dsh"
---
# dsh-pdf

> ⭐ **7** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 7 | Status | ✅ active |
| Author | [sunshine-lang](https://github.com/sunshine-lang) | Updated | 2026-08-14 |
| Subcategory | 📁 Files & import | Capabilities | files |

## One-liner

> PDF toolbox: extract text, metadata and page ranges via pdfjs-dist, local with no API key.

## About

[English](README.en.md) | 中文 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) PDF 工具箱：从 PDF 文件中提取文本、元数据与页码范围。本地解析（基于 [PDF.js](https://mozilla.github.io/pdf.js/) / pdfjs-dist）——无需 API key、无需网络。

## ✨ Key Features

- `pdf_read` 工具：逐页提取文本，带页码标记。
- 页码选择：`"1-3,5"` 或 `"all"`——大文档可分块读取。
- 文档元数据（标题）与总页数。
- 内置边界控制：文件字节上限、单次解析页数上限、单次调用字符上限——截断行为明确，并提示模型如何继续。
- 通过 harness 文件系统接缝（`ctx.fs`）读取，部署的权限与沙箱策略自动生效。

## 📦 Install

```bash
dsh plugin --profile web add "github:sunshine-lang/dsh-pdf"
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add dsh-pdf
```

## 📚 Learn more

**从 GitHub 安装**

dsh plugin --profile web add "github:sunshine-lang/dsh-pdf" 然后重启 `dsh --profile web`。`lib/` 已预构建并提交，安装无需构建权限。

**从本地源码安装（开发）**

dsh plugin --profile web add ./dsh-pdf > 注意：pnpm 对 `link:` 方式的本地依赖不会自动安装其依赖，需要手动添加到 profile（通过 registry 或 GitHub 安装则会自动处理）： > > ```sh > dsh plugin --profile web add @deepseek-ai/dsh-tools @deepseek-ai/cordis @deepseek-ai/schemastery pdfjs-dist > ```

**使用方法**

启动 Web UI 后，向模型提问，例如： > 读取 `paper.pdf` 的前 3 页并总结。 > > `contract.pdf` 第 7 页写了什么？ 模型会调用 `pdf_read`：参数 `path`（必填），可选 `pages`（`"1-3,5"` 或 `"all"`）。输出达到上限时会在页边界截断并给出提示，模型会用页码范围继续读取。

**配置**

可通过 `cordis.patch.yml` 或 profile 的 patch 层覆盖任意配置项： - id: dsh-pdf config: maxFileBytes: 52428800 maxPages: 200 maxCharsPerCall: 20000 配置无效时插件加载会直接失败，并给出可操作的错误信息。

## 🔗 Links

- [GitHub Repository](https://github.com/sunshine-lang/dsh-pdf)
- [Full README](https://github.com/sunshine-lang/dsh-pdf#readme)
- [Back to the Plugins list](../plugins.md)
