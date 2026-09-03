---
title: "dsh-library"
description: "Local document knowledge base for DeepSeek Harness: library_add/remove/list, hybrid semantic+keyword library_search with diversity re-ranking, relevance filtering and lost-in-the-middle avoidance, citation-aware injection, library_cite_check and library_diagnose — SQLite-backed index via the storage domain, local embedding, zero model downloads."
keywords: "dsh-library, search, plugin, coding, deepseek harness, dsh"
---
# dsh-library

> ⭐ **4** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 搜索与研究 |
| 星数 | ⭐ 4 | 状态 | ✅ 活跃 |
| 作者 | [PerryLink](https://github.com/PerryLink) | 更新时间 | — |
| 子分类 | 🌐 网页搜索 | 能力 | coding, search |

## 一句话介绍

> Local document knowledge base for DeepSeek Harness: library_add/remove/list, hybrid semantic+keyword library_search with diversity re-ranking, relevance filtering and lost-in-the-middle avoidance, citation-aware injection, library_cite_check and library_diagnose — SQLite-backed index via the storage domain, local embedding, zero model downloads.

## 详细介绍

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-library` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **Local document knowledge base for DeepSeek Harness.** *Import, retrieve, verify — hybrid search with citations your agent can check.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ 核心特性

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-library` (counts toward the [deepseek1024.com](https://deepseek1024.

## 📦 安装

```bash
# 1. install the bundle into your profile
dsh plugin --profile web add "github:PerryLink/dsh-library#main"

# or from npm (published releases)
dsh plugin --profile web add dsh-library

# 2. restart and verify the row
dsh --profile web --dump-config | grep -A2 'id: dsh-library'
```

## 🚀 快速开始

```bash
> Add ./docs/spec.md to library docs, then answer: what does the spec say about retries? Cite [n] markers.
```

## 📚 更多信息

**Install & uninstall**

> If pnpm reports `ERR_PNPM_IGNORED_BUILDS` for this package (esbuild's harmless platform-binary validation), add `allowBuilds: { esbuild: true }` to your `pnpm-workspace.yaml` — the `dsh` CLI prints the exact snippet.

**Configuration**

All tunables are Schemastery `Config` fields (changeable from cordis.yml). An id-targeted override replaces the whole row — restate every key you need. `cordis.patch.yml` documents each key inline.

## 🔗 链接

- [GitHub 仓库](https://github.com/PerryLink/dsh-library)
- [完整 README](https://github.com/PerryLink/dsh-library#readme)
- [返回dsh-library所在分类](../plugins.md)
