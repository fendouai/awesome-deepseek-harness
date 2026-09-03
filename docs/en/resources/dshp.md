---
title: "dshp"
description: "Manage DeepSeek Harness profiles — list, create, clone, diff, and share a whole dsh setup as one portable file."
keywords: "dshp, discovery, plugin, coding, deepseek harness, dsh"
---
# dshp

> ⭐ **1** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Plugin discovery |
| Stars | ⭐ 1 | Status | ✅ active |
| Author | [asdf17128](https://github.com/asdf17128) | Updated | 2026-08-16 |

## One-liner

> Manage DeepSeek Harness profiles — list, create, clone, diff, and share a whole dsh setup as one portable file.

## About

**Hand your whole dsh setup to someone as one file — and they get the exact same tree.** npx github:asdf17128/dshp ls Shows every profile on your machine in one line each. Read-only, zero dependencies. ---

## 📦 Install

```bash
dshp clone web web-试验田      # instant, keeps node_modules
dsh plugin --profile web-试验田 add some-experimental-plugin
dshp diff web web-试验田
```

## 🚀 Quick Start

```bash
web -> web-试验田

plugins
  + some-experimental-plugin@^0.2.0
```

## 📚 Learn more

**Install and uninstall**

As a CLI: `npx dshp ls` — nothing to install. As a plugin: dsh plugin --profile web add github:asdf17128/dshp # install dsh plugin --profile web remove dshp # uninstall Removing it drops the `list_profiles` and `export_profile` tools. Your profiles are untouched — the plugin only reads.

## 🔗 Links

- [GitHub Repository](https://github.com/asdf17128/dshp)
- [Full README](https://github.com/asdf17128/dshp#readme)
- [Back to the Plugins list](../plugins.md)
