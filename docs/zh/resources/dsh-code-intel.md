---
title: "dsh-code-intel"
description: "Symbol-aware code indexing and hybrid search for DeepSeek Harness."
keywords: "dsh-code-intel, search, plugin, coding, deepseek harness, dsh"
---
# dsh-code-intel

> ⭐ **1** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 搜索与研究 |
| 星数 | ⭐ 1 | 状态 | ✅ 活跃 |
| 作者 | [lonelymoon87](https://github.com/lonelymoon87) | 更新时间 | — |
| 子分类 | 🌐 网页搜索 | 能力 | coding, search |

## 一句话介绍

> Symbol-aware code indexing and hybrid search for DeepSeek Harness.

## 详细介绍

Symbol-aware code outline, persistent workspace indexing, and explicit lexical or embedding-assisted search for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness). The v0.1.3 release is tested with DSH 0.1.0-rc.8 and 0.1.1-rc.1 while retaining the rc.6-compatible peer range. Prebuilt packages are distributed through GitHub Releases; npm publication is prepared but not yet live. [简体中文](./README.zh-CN.md)

## ✨ 核心特性

- `code_search` ranks AST symbol chunks and bounded module windows, returning `path:line`, symbol metadata, snippets, scores, and the active retrieval mode.
- `code_outline` parses one file immediately or projects a directory from the persistent index.
- The first workspace search starts a cancellable `code-index` background job instead of blocking the agent turn.
- SQLite persistence under `.dsh/code-index/` uses DSH filesystem versions for incremental rebuilds.
- `fs/observed` marks successful DSH file operations dirty; a Chokidar watcher covers local shell, IDE, and external changes.
- TypeScript, TSX, JavaScript, JSX, Python, Go, Rust, and Java use the install-script-free Tree-sitter WASM grammars published for VS Code.

## 📦 安装

```bash
dsh plugin --profile web add https://github.com/lonelymoon87/dsh-code-intel/releases/download/v0.1.3/dsh-code-intel-0.1.3.tgz
```

## 🚀 快速开始

```bash
dsh plugin --profile web add github:lonelymoon87/dsh-code-intel#v0.1.3
```

## 📚 更多信息

**Install**

The package supports DSH `>=0.1.0-rc.6 <0.2.0` plugin APIs and Node.js `^22.19 || >=24`. dsh plugin --profile web add https://github.com/lonelymoon87/dsh-code-intel/releases/download/v0.1.3/dsh-code-intel-0.1.3.tgz The release tarball is prebuilt and needs no build allowance. A pinned source install is also supported: dsh plugin --profile web add github:lonelymoon87/dsh-code-intel#v0.1.3 The sourc

**Configuration**

Lexical mode needs no provider configuration: name: dsh-code-intel config: indexDir: .dsh/code-index include: [.ts, .tsx, .js, .jsx, .py, .go, .rs, .java] exclude: [.dsh, .git, node_modules, dist, build, coverage, vendor] maxFileSize: 1000000 maxChunkChars: 12000 maxResults: 20 watch: true embedding: false Hybrid mode uses a complete OpenAI-compatible embeddings URL: embedding: provider: openai-co

## 🔗 链接

- [GitHub 仓库](https://github.com/lonelymoon87/dsh-code-intel)
- [完整 README](https://github.com/lonelymoon87/dsh-code-intel#readme)
- [返回dsh-code-intel所在分类](../plugins.md)
