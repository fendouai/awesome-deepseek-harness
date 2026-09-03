---
title: "dsh-code-intel"
description: "Symbol-aware code indexing and hybrid search for DeepSeek Harness."
keywords: "dsh-code-intel, search, plugin, coding, deepseek harness, dsh"
---
# dsh-code-intel

> ⭐ **1** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 1 | Status | ✅ active |
| Author | [lonelymoon87](https://github.com/lonelymoon87) | Updated | — |
| Subcategory | 🌐 Web search | Capabilities | coding, search |

## One-liner

> Symbol-aware code indexing and hybrid search for DeepSeek Harness.

## About

Symbol-aware code outline, persistent workspace indexing, and explicit lexical or embedding-assisted search for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness). The v0.1.3 release is tested with DSH 0.1.0-rc.8 and 0.1.1-rc.1 while retaining the rc.6-compatible peer range. Prebuilt packages are distributed through GitHub Releases; npm publication is prepared but not yet live. [简体中文](./README.zh-CN.md)

## ✨ Key Features

- `code_search` ranks AST symbol chunks and bounded module windows, returning `path:line`, symbol metadata, snippets, scores, and the active retrieval mode.
- `code_outline` parses one file immediately or projects a directory from the persistent index.
- The first workspace search starts a cancellable `code-index` background job instead of blocking the agent turn.
- SQLite persistence under `.dsh/code-index/` uses DSH filesystem versions for incremental rebuilds.
- `fs/observed` marks successful DSH file operations dirty; a Chokidar watcher covers local shell, IDE, and external changes.
- TypeScript, TSX, JavaScript, JSX, Python, Go, Rust, and Java use the install-script-free Tree-sitter WASM grammars published for VS Code.

## 📦 Install

```bash
dsh plugin --profile web add https://github.com/lonelymoon87/dsh-code-intel/releases/download/v0.1.3/dsh-code-intel-0.1.3.tgz
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add github:lonelymoon87/dsh-code-intel#v0.1.3
```

## 📚 Learn more

**Install**

The package supports DSH `>=0.1.0-rc.6 <0.2.0` plugin APIs and Node.js `^22.19 || >=24`. dsh plugin --profile web add https://github.com/lonelymoon87/dsh-code-intel/releases/download/v0.1.3/dsh-code-intel-0.1.3.tgz The release tarball is prebuilt and needs no build allowance. A pinned source install is also supported: dsh plugin --profile web add github:lonelymoon87/dsh-code-intel#v0.1.3 The sourc

**Configuration**

Lexical mode needs no provider configuration: name: dsh-code-intel config: indexDir: .dsh/code-index include: [.ts, .tsx, .js, .jsx, .py, .go, .rs, .java] exclude: [.dsh, .git, node_modules, dist, build, coverage, vendor] maxFileSize: 1000000 maxChunkChars: 12000 maxResults: 20 watch: true embedding: false Hybrid mode uses a complete OpenAI-compatible embeddings URL: embedding: provider: openai-co

## 🔗 Links

- [GitHub Repository](https://github.com/lonelymoon87/dsh-code-intel)
- [Full README](https://github.com/lonelymoon87/dsh-code-intel#readme)
- [Back to the Plugins list](../plugins.md)
