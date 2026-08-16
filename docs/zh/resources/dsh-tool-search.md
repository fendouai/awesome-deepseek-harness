---
title: "dsh-tool-search"
description: "按 Agent 按需工具发现与渐进式 schema 披露。"
keywords: "dsh-tool-search, developer, plugin, coding, context, deepseek harness, dsh"
---
# dsh-tool-search

> ⭐ 2 · ✅ 活跃 · 插件

## 一句话介绍

按 Agent 按需工具发现与渐进式 schema 披露。

## 详细介绍

An experimental external Native Tool Mode plugin for per-agent tool discovery and progressive schema disclosure. Each live agent sees one scope-local `tool_search` tool plus the global tools matched by `alwaysVisible`; other eligible global tools stay executable only after `tool_search` selects them. The plugin uses the existing `ctx.tools.restrict()` seam and does not change `agent-loop`. This private repository is the plugin's source of truth. The package is unreleased and carries no compatibi

## 作者
**[vibeinging](https://github.com/vibeinging)**

## 链接

- [GitHub 仓库](https://github.com/vibeinging/dsh-tool-search)
- [完整 README](https://github.com/vibeinging/dsh-tool-search#readme)
- [返回dsh-tool-search所在分类](../plugins.md)
