---
title: "dsh-workspace-search"
description: "VS Code 风格工作区关键词搜索：Better Sidebar 生态的搜索 Tab。"
keywords: "dsh-workspace-search, ui, plugin, search, files, deepseek harness, dsh"
---
# dsh-workspace-search

> ⭐ **4** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 4 | 状态 | ✅ 活跃 |
| 作者 | [tsonglew](https://github.com/tsonglew) | 更新时间 | 2026-08-14 |
| 子分类 | 🖥️ 侧边栏与面板 | 能力 | ui, search, files |

## 一句话介绍

> VS Code 风格工作区关键词搜索：Better Sidebar 生态的搜索 Tab。

## 详细介绍

VS Code-style workspace keyword search for the DeepSeek Harness (dsh) web GUI, registered as a **Search tab** inside [dsh-better-sidebar](https://github.com/omdsh-dev/DSH-better-sidebar). - Keyword search across the session workspace: file **names** and file **contents**, grouped per file with line numbers - VS Code-style search rules: **files to include / files to exclude** glob patterns (comma-separated, supports `**`, `*`, `?`, `{a,b}`), regular expression queries (`.*` toggle), and case toggle (`Aa`) - Click a match to open the file in better-sidebar's built-in editor - VS Code default excludes: hidden files, `.git`, `node_modules`, `dist`, `build`, `.next`, `target` etc. are skipped; caps on files, matches, and line length are reported honestly as truncation

## ✨ 核心特性

- Keyword search across the session workspace: file **names** and file
- VS Code-style search rules: **files to include / files to exclude** glob
- Click a match to open the file in better-sidebar's built-in editor
- VS Code default excludes: hidden files, `.git`, `node_modules`, `dist`,

## 📦 安装

```bash
dsh plugin --profile web add ./plugins/dsh-workspace-search
```

## 🚀 快速开始

```bash
- id: workspace-search
  config:
    maxFiles: 5000       # hard cap on files scanned per search
    maxMatches: 300      # hard cap on total content matches
    maxLineLength: 300   # hard cap on one reported line
    maxFileBytes: 1048576  # files above this skip the content scan
```

## 📚 更多信息

**Install**

dsh plugin --profile web add ./plugins/dsh-workspace-search (Requires `dsh-better-sidebar` ≥ 0.4.0, which exposes `ctx.betterSidebar`.)

**Configuration**

All fields optional (profile patch layer): config: maxFiles: 5000 # hard cap on files scanned per search maxMatches: 300 # hard cap on total content matches maxLineLength: 300 # hard cap on one reported line maxFileBytes: 1048576 # files above this skip the content scan

## 🔗 链接

- [GitHub 仓库](https://github.com/tsonglew/dsh-workspace-search)
- [完整 README](https://github.com/tsonglew/dsh-workspace-search#readme)
- [返回dsh-workspace-search所在分类](../plugins.md)
