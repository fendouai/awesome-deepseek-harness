---
title: "dsh-plugin-mineru"
description: "Expose MinerU document parsing to the model: PDF/images/DOCX/PPTX/XLSX to structured Markdown/JSON."
keywords: "dsh-plugin-mineru, developer, plugin, files, multimodal, deepseek harness, dsh"
---
# dsh-plugin-mineru

> ⭐ **38** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 38 | Status | ✅ active |
| Author | [HuanLinOTO](https://github.com/HuanLinOTO) | Updated | 2026-08-15 |
| Subcategory | 📁 Files & import | Capabilities | files, multimodal |

## One-liner

> Expose MinerU document parsing to the model: PDF/images/DOCX/PPTX/XLSX to structured Markdown/JSON.

## About

DSH 插件：向模型暴露 [MinerU](https://github.com/opendatalab/MinerU) 文档解析工具。MinerU 可将 PDF、图片、DOCX、PPTX、XLSX 等文件转换为结构化的 Markdown / JSON。

## 📦 Install

```bash
# 从 npm 安装（推荐）：
dsh plugin --profile web add @huanlin/dsh-plugin-mineru

# 从本地 checkout 开发安装：
dsh plugin --profile web add link:D:\Projects\deepseek-harness\dsh-mineru
```

## 🚀 Quick Start

```bash
allowBuilds:
  '@huanlin/dsh-plugin-mineru': true
```

## 📚 Learn more

**从本地 checkout 开发安装：**

dsh plugin --profile web add link:D:\Projects\deepseek-harness\dsh-mineru 若从 git 安装（pnpm ≥10），需在 profile 的 `pnpm-workspace.yaml` 中允许构建： allowBuilds: '@huanlin/dsh-plugin-mineru': true

## 🔗 Links

- [GitHub Repository](https://github.com/HuanLinOTO/dsh-plugin-mineru)
- [Full README](https://github.com/HuanLinOTO/dsh-plugin-mineru#readme)
- [Back to the Plugins list](../plugins.md)
