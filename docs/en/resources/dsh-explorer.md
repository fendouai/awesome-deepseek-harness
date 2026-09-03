---
title: "dsh-explorer"
description: "DSH plugin: VS Code-style file-tree explorer (git decorations, preview, diff, drag-to-reference); install via dsh plugin --profile web add."
keywords: "dsh-explorer, search, plugin, coding, git, deepseek harness, dsh"
---
# dsh-explorer

> ⭐ **9** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 9 | Status | ✅ active |
| Author | [No-PRM](https://github.com/No-PRM) | Updated | — |
| Subcategory | 🌐 Web search | Capabilities | coding, git |

## One-liner

> DSH plugin: VS Code-style file-tree explorer (git decorations, preview, diff, drag-to-reference); install via dsh plugin --profile web add.

## About

A file-tree sidebar for the DeepSeek Harness web UI. A blue round button on the right edge opens a drawer with the current workspace's files — lazy-loaded and virtualized, so even big directories stay responsive. The plugins only add UI and a few read-only routes. Nothing in the shipped dsh packages is touched, so dsh updates shouldn't break anything.

## 📦 Install

```bash
dsh plugin --profile web add "github:No-PRM/dsh-explorer#main&path:/dsh-plugins/dsh-explorer"
dsh plugin --profile web add "github:No-PRM/dsh-explorer#main&path:/dsh-plugins/dsh-client-ui-explorer"
# restart dsh
```

## 🚀 Quick Start

```bash
- insert:
    - id: filetree
      name: dsh-explorer-v1
    - id: ui-filetree
      name: dsh-client-ui-explorer
```

## 📚 Learn more

**Install (two commands — monorepo)**

dsh plugin --profile web add "github:No-PRM/dsh-explorer#main&path:/dsh-plugins/dsh-explorer" dsh plugin --profile web add "github:No-PRM/dsh-explorer#main&path:/dsh-plugins/dsh-client-ui-explorer"

**Install**

You need both halves. Bundle install (monorepo — one command per package): dsh plugin --profile web add "github:No-PRM/dsh-explorer#main&path:/dsh-plugins/dsh-explorer" dsh plugin --profile web add "github:No-PRM/dsh-explorer#main&path:/dsh-plugins/dsh-client-ui-explorer"

## 🔗 Links

- [GitHub Repository](https://github.com/No-PRM/dsh-explorer)
- [Full README](https://github.com/No-PRM/dsh-explorer#readme)
- [Back to the Plugins list](../plugins.md)
