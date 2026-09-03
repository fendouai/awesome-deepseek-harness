---
title: "dsh-session-search"
description: "Index-free cross-agent session search for DeepSeek Harness."
keywords: "dsh-session-search, developer, plugin, search, files, deepseek harness, dsh"
---
# dsh-session-search

> ⭐ **2** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 2 | Status | ✅ active |
| Author | [Tieboyh](https://github.com/Tieboyh) | Updated | 2026-08-13 |

## One-liner

> Index-free cross-agent session search for DeepSeek Harness.

## About

Cross-agent session search plugin for DeepSeek Harness — directly scan past conversations from dsh, Codex, Claude Code, pi, and OpenCode without creating a derived database. [中文](README.zh-CN.md)

## 📦 Install

```bash
git clone https://github.com/dsh-external/dsh-session-search.git
dshx install dsh-session-search ./dsh-session-search
```

## 🚀 Quick Start

```bash
# ~/.dsh/config.yaml
- insert:
    - id: dsh-session-search
      name: '/absolute/path/to/dsh-session-search/lib/index.js'
      config:
        sources: { dsh: true, codex: true, claude: true, pi: true, opencode: true }
        maxResults: 10
        readWindow: 10
```

## 📚 Learn more

**Install (marisa / dshx)**

git clone https://github.com/dsh-external/dsh-session-search.git dshx install dsh-session-search ./dsh-session-search Or install directly from a git URL. The plugin is mounted into `~/.dsh/config.yaml` and takes effect on the next `dsh web`/TUI start (hot with Web HMR).

**~/.dsh/config.yaml**

- id: dsh-session-search name: '/absolute/path/to/dsh-session-search/lib/index.js' config: sources: { dsh: true, codex: true, claude: true, pi: true, opencode: true } maxResults: 10 readWindow: 10

## 🔗 Links

- [GitHub Repository](https://github.com/Tieboyh/dsh-session-search)
- [Full README](https://github.com/Tieboyh/dsh-session-search#readme)
- [Back to the Plugins list](../plugins.md)
