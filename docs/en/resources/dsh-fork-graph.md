---
title: "dsh-fork-graph"
description: "See your DSH conversation's fork history as a git graph — coloured branch lanes in the session header, click to jump. A pure-derivation DeepSeek Harness Web plugin."
keywords: "dsh-fork-graph, search, plugin, coding, git, deepseek harness, dsh"
---
# dsh-fork-graph

> ⭐ **2** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 2 | Status | ✅ active |
| Author | [chouyong](https://github.com/chouyong) | Updated | — |
| Subcategory | 🌐 Web search | Capabilities | coding, git |

## One-liner

> See your DSH conversation's fork history as a git graph — coloured branch lanes in the session header, click to jump. A pure-derivation DeepSeek Harness Web plugin.

## About

**See your conversation's fork history as a git graph — right in the session header.** A [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (DSH) Web plugin. Fork a session in DSH and you get a child that inherits the parent's history — but the sidebar only shows a flat list with indentation. This plugin draws the actual branch topology: coloured lanes, curved fork lines, one row per session, click to jump. *The SVG above is rendered by the plugin's own layout code (`scripts/render-preview.ts`); the two PNGs are genuine captures from a running DSH Web session.*

## ✨ Key Features

- **Branch topology, not indentation.** Each branch gets its own coloured lane; forks are drawn as curves leaving the parent commit dot.
- **One row per session** with its title, plus the facts that change how you read it: `current`, `running`, `subagent`, `forks into N`.
- **Click to jump.** Any node navigates to that session.
- **Focused by default.** Shows the lineage family of the session you are in, not every session you ever had.
- **Appears only when it is useful.** No fork in this lineage → the control does not render at all.
- **English and Chinese**, following the page language.

## 📦 Install

```bash
dsh plugin --profile web add github:chouyong/dsh-fork-graph
dsh web
```

## 🚀 Quick Start

```bash
allowBuilds:
  dsh-fork-graph: true
```

## 📚 Learn more

**Install**

Requires DSH, Node.js `^22.19.0 || >=24.0.0`, and pnpm. dsh plugin --profile web add github:chouyong/dsh-fork-graph dsh web A git install builds from source, so pnpm ≥10 will refuse the package's `prepare` script until you allow it. The first `add` prints the exact key — put it in that profile's `pnpm-workspace.yaml`: allowBuilds: dsh-fork-graph: true then run the `add` again. Pin a commit (`githu

## 🔗 Links

- [GitHub Repository](https://github.com/chouyong/dsh-fork-graph)
- [Full README](https://github.com/chouyong/dsh-fork-graph#readme)
- [Back to the Plugins list](../plugins.md)
