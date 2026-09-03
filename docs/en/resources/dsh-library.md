---
title: "dsh-library"
description: "Local document knowledge base for DeepSeek Harness: library_add/remove/list, hybrid semantic+keyword library_search with diversity re-ranking, relevance filtering and lost-in-the-middle avoidance, citation-aware injection, library_cite_check and library_diagnose — SQLite-backed index via the storage domain, local embedding, zero model downloads."
keywords: "dsh-library, search, plugin, coding, deepseek harness, dsh"
---
# dsh-library

> ⭐ **4** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 4 | Status | ✅ active |
| Author | [PerryLink](https://github.com/PerryLink) | Updated | — |
| Subcategory | 🌐 Web search | Capabilities | coding, search |

## One-liner

> Local document knowledge base for DeepSeek Harness: library_add/remove/list, hybrid semantic+keyword library_search with diversity re-ranking, relevance filtering and lost-in-the-middle avoidance, citation-aware injection, library_cite_check and library_diagnose — SQLite-backed index via the storage domain, local embedding, zero model downloads.

## About

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-library` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **Local document knowledge base for DeepSeek Harness.** *Import, retrieve, verify — hybrid search with citations your agent can check.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ Key Features

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-library` (counts toward the [deepseek1024.com](https://deepseek1024.

## 📦 Install

```bash
# 1. install the bundle into your profile
dsh plugin --profile web add "github:PerryLink/dsh-library#main"

# or from npm (published releases)
dsh plugin --profile web add dsh-library

# 2. restart and verify the row
dsh --profile web --dump-config | grep -A2 'id: dsh-library'
```

## 🚀 Quick Start

```bash
> Add ./docs/spec.md to library docs, then answer: what does the spec say about retries? Cite [n] markers.
```

## 📚 Learn more

**Install & uninstall**

> If pnpm reports `ERR_PNPM_IGNORED_BUILDS` for this package (esbuild's harmless platform-binary validation), add `allowBuilds: { esbuild: true }` to your `pnpm-workspace.yaml` — the `dsh` CLI prints the exact snippet.

**Configuration**

All tunables are Schemastery `Config` fields (changeable from cordis.yml). An id-targeted override replaces the whole row — restate every key you need. `cordis.patch.yml` documents each key inline.

## 🔗 Links

- [GitHub Repository](https://github.com/PerryLink/dsh-library)
- [Full README](https://github.com/PerryLink/dsh-library#readme)
- [Back to the Plugins list](../plugins.md)
