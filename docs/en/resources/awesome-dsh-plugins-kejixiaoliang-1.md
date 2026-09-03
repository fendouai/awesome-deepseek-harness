---
title: "awesome-dsh-plugins (kejixiaoliang)"
description: "Curated DSH plugin catalog: 14 categories, 280+ community plugins covering MCP/Skill/TUI/multi-agent/context memory/UI skins."
keywords: "awesome-dsh-plugins (kejixiaoliang), registry, awesome-list, search, deepseek harness, dsh"
---
# awesome-dsh-plugins (kejixiaoliang)

> ⭐ **22** · ✅ active · awesome-list

| | | | |
|---|---|---|---|
| Type | awesome-list | Category | Registries |
| Stars | ⭐ 22 | Status | ✅ active |
| Author | [kejixiaoliang](https://github.com/kejixiaoliang) | Updated | 2026-08-21 |

## One-liner

> Curated DSH plugin catalog: 14 categories, 280+ community plugins covering MCP/Skill/TUI/multi-agent/context memory/UI skins.

## About

**A curated directory of 306+ [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`) plugins across 14 categories — every entry with ⭐ stars and a `dsh plugin add` command. Bilingual (EN + 中文), machine-readable data, auto-sync CI.** **English** · [中文版](README.zh.md) [Quick Start](#quick-start) · [Hot Plugins](#hot-plugins) · [Categories](#categories) · [Browse All](#browse-all-plugins) · [Full Index](INDEX.md) · [Contributing](CONTRIBUTING.md) ---

## ✨ Key Features

- ✅ Official install: `dsh plugin --profile <name> add <pkg>` (forwards to pnpm; npm / git / tarball)
- ✅ Official discovery: npm + the GitHub [`dsh-plugin`](https://github.com/topics/dsh-plugin) topic (**no built-in marketplace**)

## 📦 Install

```bash
# Install a plugin (forwards to pnpm; npm / git / tarball all supported)
dsh plugin --profile <name> add <pkg>

# Example
dsh plugin add dsh-cc-tui
```

## 🚀 Quick Start

```bash
import type { Context } from '@deepseek-ai/cordis'
export const name = 'hello-plugin'
export function apply(ctx: Context) {
  // register a tool, a command, a UI node, ...
}
```

## 📚 Learn more

**⚡ Quick Start**

Three ways to use this directory: 1. **Browse** — expand any category below (or jump into a category file); each entry links straight to its GitHub repo. 2. **Search** — press `t` (or `Ctrl+F`) on the repo page and search keywords like `mcp`, `memory`, `TUI`, `multi-agent`. 3. **Consume programmatically** — read [`web/data.js`](web/data.js) (generated from the category files; see [web/README.md](w

**Example**

dsh plugin add dsh-cc-tui Each enriched entry above shows its install command, e.g. `` `dsh plugin add <npm-package>` ``.

## 🔗 Links

- [GitHub Repository](https://github.com/kejixiaoliang/awesome-dsh-plugins)
- [Full README](https://github.com/kejixiaoliang/awesome-dsh-plugins#readme)
- [Back to the Awesome Lists & Registries list](../awesome-lists.md)
