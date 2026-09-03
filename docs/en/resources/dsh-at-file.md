---
title: "dsh-at-file"
description: "Codex-style @file mentions for DeepSeek Harness: search workspace files in the composer and attach their path to prompts."
keywords: "dsh-at-file, search, plugin, coding, deepseek harness, dsh"
---
# dsh-at-file

> ⭐ **505** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 505 | Status | ✅ active |
| Author | [FSMargoo](https://github.com/FSMargoo) | Updated | — |
| Subcategory | 🌐 Web search | Capabilities | coding, search |

## One-liner

> Codex-style @file mentions for DeepSeek Harness: search workspace files in the composer and attach their path to prompts.

## About

Workspace path references for the DeepSeek Harness web interface. Type `@` in the composer to search the current workspace and insert a file or directory path.

## 📦 Install

```bash
dsh plugin --profile web add https://github.com/omdsh-dev/dsh-at-file/archive/refs/tags/v0.7.0.tar.gz
```

## 🚀 Quick Start

```bash
- id: dsh-at-file
  config:
    maxIndexedFiles: 10000
```

## 📚 Learn more

**Usage**

Choose a result from the `@` menu. The selected path remains visible in the draft and can be opened or removed from the reference bar. Review @docs/spec.pdf Before the agent starts a step, the plugin confirms that the path exists inside the active workspace. It then adds a short reference message: <workspace-reference path="docs/spec.pdf" kind="file" /> The reference contains the workspace-relativ

**Install or Update**

dsh plugin --profile web add https://github.com/omdsh-dev/dsh-at-file/archive/refs/tags/v0.7.0.tar.gz Use the same command to update an existing installation. Restart `dsh web` after installation so the Host and browser client load version `0.7.0`. Version `0.7.0` supports both the 0.1.1 and 0.1.2 Harness client package layouts. It also restores the default file ignores for installations that pers

**Configuration**

The available options apply to the path picker index: Add the complete configuration to the selected profile's `cordis.patch.yml`. The usual path is `~/.dsh/profiles/web/cordis.patch.yml`. config: maxIndexedFiles: 10000 Omitting `ignoreDirs` keeps the built-in list. When you provide it, include every directory name you want excluded.

## 🔗 Links

- [GitHub Repository](https://github.com/FSMargoo/dsh-at-file)
- [Full README](https://github.com/FSMargoo/dsh-at-file#readme)
- [Back to the Plugins list](../plugins.md)
