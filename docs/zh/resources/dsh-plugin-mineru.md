---
title: "dsh-plugin-mineru"
description: "向模型暴露 MinerU 文档解析：PDF/图片/DOCX/PPTX/XLSX 转结构化 Markdown/JSON。"
keywords: "dsh-plugin-mineru, developer, plugin, files, multimodal, deepseek harness, dsh"
---
# dsh-plugin-mineru

> ⭐ **38** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 38 | 状态 | ✅ 活跃 |
| 作者 | [HuanLinOTO](https://github.com/HuanLinOTO) | 更新时间 | 2026-08-15 |
| 子分类 | 📁 文件与导入 | 能力 | files, multimodal |

## 一句话介绍

> 向模型暴露 MinerU 文档解析：PDF/图片/DOCX/PPTX/XLSX 转结构化 Markdown/JSON。

## 详细介绍

DSH 插件：向模型暴露 [MinerU](https://github.com/opendatalab/MinerU) 文档解析工具。MinerU 可将 PDF、图片、DOCX、PPTX、XLSX 等文件转换为结构化的 Markdown / JSON。

## 📦 安装

```bash
# 从 npm 安装（推荐）：
dsh plugin --profile web add @huanlin/dsh-plugin-mineru

# 从本地 checkout 开发安装：
dsh plugin --profile web add link:D:\Projects\deepseek-harness\dsh-mineru
```

## 🚀 快速开始

```bash
allowBuilds:
  '@huanlin/dsh-plugin-mineru': true
```

## 📚 更多信息

**从本地 checkout 开发安装：**

dsh plugin --profile web add link:D:\Projects\deepseek-harness\dsh-mineru 若从 git 安装（pnpm ≥10），需在 profile 的 `pnpm-workspace.yaml` 中允许构建： allowBuilds: '@huanlin/dsh-plugin-mineru': true

## 🔗 链接

- [GitHub 仓库](https://github.com/HuanLinOTO/dsh-plugin-mineru)
- [完整 README](https://github.com/HuanLinOTO/dsh-plugin-mineru#readme)
- [返回dsh-plugin-mineru所在分类](../plugins.md)
