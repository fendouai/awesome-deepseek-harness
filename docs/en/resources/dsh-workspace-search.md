---
title: "dsh-workspace-search"
description: "VS Code-style workspace keyword search: a Search tab for the Better Sidebar ecosystem."
keywords: "dsh-workspace-search, ui, plugin, search, files, deepseek harness, dsh"
---
# dsh-workspace-search

> ⭐ **4** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 4 | Status | ✅ active |
| Author | [tsonglew](https://github.com/tsonglew) | Updated | 2026-08-14 |
| Subcategory | 🖥️ Sidebars & panels | Capabilities | ui, search, files |

## One-liner

> VS Code-style workspace keyword search: a Search tab for the Better Sidebar ecosystem.

## About

VS Code-style workspace keyword search for the DeepSeek Harness (dsh) web GUI, registered as a **Search tab** inside [dsh-better-sidebar](https://github.com/omdsh-dev/DSH-better-sidebar). - Keyword search across the session workspace: file **names** and file **contents**, grouped per file with line numbers - VS Code-style search rules: **files to include / files to exclude** glob patterns (comma-separated, supports `**`, `*`, `?`, `{a,b}`), regular expression queries (`.*` toggle), and case toggle (`Aa`) - Click a match to open the file in better-sidebar's built-in editor - VS Code default excludes: hidden files, `.git`, `node_modules`, `dist`, `build`, `.next`, `target` etc. are skipped; caps on files, matches, and line length are reported honestly as truncation

## ✨ Key Features

- Keyword search across the session workspace: file **names** and file
- VS Code-style search rules: **files to include / files to exclude** glob
- Click a match to open the file in better-sidebar's built-in editor
- VS Code default excludes: hidden files, `.git`, `node_modules`, `dist`,

## 📦 Install

```bash
dsh plugin --profile web add ./plugins/dsh-workspace-search
```

## 🚀 Quick Start

```bash
- id: workspace-search
  config:
    maxFiles: 5000       # hard cap on files scanned per search
    maxMatches: 300      # hard cap on total content matches
    maxLineLength: 300   # hard cap on one reported line
    maxFileBytes: 1048576  # files above this skip the content scan
```

## 📚 Learn more

**Install**

dsh plugin --profile web add ./plugins/dsh-workspace-search (Requires `dsh-better-sidebar` ≥ 0.4.0, which exposes `ctx.betterSidebar`.)

**Configuration**

All fields optional (profile patch layer): config: maxFiles: 5000 # hard cap on files scanned per search maxMatches: 300 # hard cap on total content matches maxLineLength: 300 # hard cap on one reported line maxFileBytes: 1048576 # files above this skip the content scan

## 🔗 Links

- [GitHub Repository](https://github.com/tsonglew/dsh-workspace-search)
- [Full README](https://github.com/tsonglew/dsh-workspace-search#readme)
- [Back to the Plugins list](../plugins.md)
