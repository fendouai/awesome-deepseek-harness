---
title: "dsh-tool-search"
description: "Per-agent on-demand tool discovery and progressive schema disclosure."
keywords: "dsh-tool-search, developer, plugin, coding, context, deepseek harness, dsh"
---
# dsh-tool-search

> ⭐ 2 · ✅ active · plugin

## One-liner

Per-agent on-demand tool discovery and progressive schema disclosure.

## About

An experimental external Native Tool Mode plugin for per-agent tool discovery and progressive schema disclosure. Each live agent sees one scope-local `tool_search` tool plus the global tools matched by `alwaysVisible`; other eligible global tools stay executable only after `tool_search` selects them. The plugin uses the existing `ctx.tools.restrict()` seam and does not change `agent-loop`. This private repository is the plugin's source of truth. The package is unreleased and carries no compatibi

## Author
**[vibeinging](https://github.com/vibeinging)**

## Links

- [GitHub Repository](https://github.com/vibeinging/dsh-tool-search)
- [Full README](https://github.com/vibeinging/dsh-tool-search#readme)
- [Back to the Plugins list](../plugins.md)
