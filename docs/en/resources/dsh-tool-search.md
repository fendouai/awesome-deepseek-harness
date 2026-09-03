---
title: "dsh-tool-search"
description: "Tool search & slimming for DeepSeek Harness: Hermes-style progressive disclosure — search, describe, and call long-tail tools on demand"
keywords: "dsh-tool-search, search, plugin, coding, deepseek harness, dsh"
---
# dsh-tool-search

> ⭐ **6** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 6 | Status | ✅ active |
| Author | [Letter2025](https://github.com/Letter2025) | Updated | — |
| Subcategory | 🌐 Web search | Capabilities | coding, search |

## One-liner

> Tool search & slimming for DeepSeek Harness: Hermes-style progressive disclosure — search, describe, and call long-tail tools on demand

## About

An experimental external Native Tool Mode plugin for per-agent tool discovery and progressive schema disclosure. Each live agent sees one scope-local `tool_search` tool plus the global tools matched by `alwaysVisible`; other eligible global tools stay executable only after `tool_search` selects them. The plugin uses the existing `ctx.tools.restrict()` seam and does not change `agent-loop`. This private repository is the plugin's source of truth. The package is unreleased and carries no compatibility promise. See the [scale benchmark report](docs/reports/2026-08-11-tool-search-benchmark.md) for keyless 10/30/50/100-tool results and the [design record](docs/design/2026-08-11-tool-search-progressive-disclosure.md) for the decision and trade-offs.

## ✨ Key Features

- id: tool-search

## 📦 Install

```bash
dsh plugin --profile headless add -w github:dsh-external/dsh-tool-search#<reviewed-commit>
dsh plugin --profile web add -w github:dsh-external/dsh-tool-search#<reviewed-commit>
dsh --profile web --dump-config
```

## 🚀 Quick Start

```bash
- id: tool-search
  name: '@deepseek-ai/dsh-tool-search'
  config:
    alwaysVisible: [read_file, todo_*]
    maxResults: 5
    maxQueryChars: 512
```

## 📚 Learn more

**Installation**

The repository is private and the package is not published to an npm registry. Install a reviewed commit directly from GitHub with Git credentials and pnpm `11.7.0`; install it separately into every profile that should use tool search. The `-w` flag is required because a DSH profile is a pnpm workspace root: dsh plugin --profile headless add -w github:dsh-external/dsh-tool-search#<reviewed-commit>

**Config**

name: '@deepseek-ai/dsh-tool-search' config: alwaysVisible: [read_file, todo_*] maxResults: 5 maxQueryChars: 512 Invalid positive-integer bounds, empty or whitespace-padded patterns, and repeated patterns fail at plugin load. A model may request a smaller `limit`, from `1` through `maxResults`; it cannot raise the deployment bound.

## 🔗 Links

- [GitHub Repository](https://github.com/Letter2025/dsh-tool-search)
- [Full README](https://github.com/Letter2025/dsh-tool-search#readme)
- [Back to the Plugins list](../plugins.md)
