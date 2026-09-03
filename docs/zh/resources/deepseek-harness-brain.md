---
title: "DeepSeek Harness Brain"
description: "带来源引用的 Obsidian 知识库，包含浅显指南、架构笔记、可安装助手技能，以及 DeepSeek Harness 可移植性指南。"
keywords: "DeepSeek Harness Brain, learning, tutorial, research, memory, deepseek harness, dsh"
---
# DeepSeek Harness Brain

> ⭐ **0** · ✅ 活跃 · 教程

| | | | |
|---|---|---|---|
| 类型 | 教程 | 分类 | 学习 |
| 星数 | ⭐ 0 | 状态 | ✅ 活跃 |
| 作者 | [AgriciDaniel](https://github.com/AgriciDaniel) | 更新时间 | — |

## 一句话介绍

> 带来源引用的 Obsidian 知识库，包含浅显指南、架构笔记、可安装助手技能，以及 DeepSeek Harness 可移植性指南。

## 详细介绍

DeepSeek Harness Brain 0.2.0 is an independent, evidence-gated Obsidian knowledge base for understanding, reviewing, extending, and selectively porting ideas from [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness). This community release was validated against a pinned upstream snapshot with deterministic importer, vault, pipeline, and packaging checks. Browser, live-provider, native, cross-platform, comprehensive security-audit, and production-scale behavior remain outside the verified release evidence. This project is not affiliated with or endorsed by DeepSeek.

## ✨ 核心特性

- A plain-language map of how the harness fits together.
- Source-cited notes about sessions, tools, permissions, persistence, plugins,
- A portability matrix that separates reusable patterns from framework-specific
- A deterministic sample vault and an allowlisted checkout importer.
- A grounded secretary and four curator agents for evidence-based review.
- Explicit confidence labels, open risks, and verification limits.

## 📦 安装

```bash
python -m pip install -e .
deepseek-harness-brain demo
deepseek-harness-brain lint --vault examples/sample-vault
deepseek-harness-brain report --vault examples/sample-vault --html-only
```

## 🚀 快速开始

```bash
deepseek-harness-brain import-checkout \
  --checkout /path/to/deepseek-harness \
  --vault examples/sample-vault \
  --expected-commit b150a551b8d465e31e418e1b2eaf5e79bbb7d28e \
  --as-of 2026-08-21
```

## 📚 更多信息

**Quick start**

Requires Python 3.11 or newer. python -m pip install -e . deepseek-harness-brain demo deepseek-harness-brain lint --vault examples/sample-vault deepseek-harness-brain report --vault examples/sample-vault --html-only To compare a local DeepSeek Harness checkout against the reviewed evidence: deepseek-harness-brain import-checkout \ --checkout /path/to/deepseek-harness \ --vault examples/sample-vaul

## 🔗 链接

- [GitHub 仓库](https://github.com/AgriciDaniel/deepseek-harness-brain)
- [完整 README](https://github.com/AgriciDaniel/deepseek-harness-brain#readme)
- [返回DeepSeek Harness Brain所在分类](../tutorials.md)
