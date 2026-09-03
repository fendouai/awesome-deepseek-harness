---
title: "dsh-data-quality"
description: "确定性数据画像、清洗与核验，提供 data_profile/data_clean/data_verify 工具。"
keywords: "dsh-data-quality, developer, plugin, workflow, deepseek harness, dsh"
---
# dsh-data-quality

> ⭐ **11** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 11 | 状态 | ✅ 活跃 |
| 作者 | [PerryLink](https://github.com/PerryLink) | 更新时间 | — |
| 子分类 | 📁 文件与导入 | 能力 | workflow |

## 一句话介绍

> 确定性数据画像、清洗与核验，提供 data_profile/data_clean/data_verify 工具。

## 详细介绍

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-data-quality` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **Deterministic data profiling, cleaning, and verification for DeepSeek Harness.** All computation is plain TypeScript in the harness process — the model never does the math. A `ctx.dataQuality` capability seam (Service Definition / local Provider / tool Consumers) exposes three model tools plus a frozen cross-plugin citation-checking contract. [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md)

## ✨ 核心特性

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-data-quality` (counts toward the [deepseek1024.com](https://deepseek

## 📦 安装

```bash
dsh plugin --profile web add dsh-data-quality
```

## 🚀 快速开始

```bash
pnpm pack                                  # produces dsh-data-quality-<version>.tgz
dsh plugin --profile web add ./dsh-data-quality-<version>.tgz
```

## 📚 更多信息

**Install & uninstall**

dsh plugin --profile web add dsh-data-quality # install (npm) — or the forms above dsh plugin --profile web remove dsh-data-quality # uninstall

**Configuration**

All keys are optional (defaults shown); invalid values fail loudly at load. Every key is settable from `cordis.yml` (the bundle ships `cordis.patch.yml` with the same defaults).

## 🔗 链接

- [GitHub 仓库](https://github.com/PerryLink/dsh-data-quality)
- [完整 README](https://github.com/PerryLink/dsh-data-quality#readme)
- [返回dsh-data-quality所在分类](../plugins.md)
