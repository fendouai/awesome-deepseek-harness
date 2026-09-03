---
title: "dsh-plugin-radar"
description: "Userscript: marks DeepSeek Harness plugins on GitHub and npm, with the install command that actually works"
keywords: "dsh-plugin-radar, vision, plugin, coding, git, deepseek harness, dsh"
---
# dsh-plugin-radar

> ⭐ **1** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 1 | Status | ✅ active |
| Author | [DshMarketPlace](https://github.com/DshMarketPlace) | Updated | 2026-08-20 |
| Subcategory | 👁️ Vision tools | Capabilities | coding, git |

## One-liner

> Userscript: marks DeepSeek Harness plugins on GitHub and npm, with the install command that actually works

## About

`dsh plugin add` is a thin forward to pnpm inside a profile directory, so `--profile` is **mandatory**: $ dsh plugin add some-plugin error: required option '--profile ' not specified Plenty of READMEs print the short form anyway. This script reads the command from the [DSH Marketplace](https://dshmarketplace.dev) catalogue, where every listing carries the flag, and drops it on the page you are already looking at.

## 📦 Install

```bash
$ dsh plugin add some-plugin
error: required option '--profile <name>' not specified
```

## 🚀 Quick Start

```bash
{
  "fields": ["fullName", "category", "install", "path", "npm"],
  "plugins": [
    ["liustack/modlens", "vision", "dsh plugin --profile web add @liustack/modlens", "/plugins/liustack-modlens", "@liustack/modlens"]
  ]
}
```

## 📚 Learn more

**Install**

1. Install a userscript manager — [Tampermonkey](https://www.tampermonkey.net/), [Violentmonkey](https://violentmonkey.github.io/) or [Userscripts](https://apps.apple.com/app/userscripts/id1463298887) for Safari. 2. **[Install from Greasy Fork](https://greasyfork.org/scripts/591735-dsh-plugin-radar)**, or open [`dsh-plugin-radar.user.js`](dsh-plugin-radar.user.js) raw and your manager will offer t

## 🔗 Links

- [GitHub Repository](https://github.com/DshMarketPlace/dsh-plugin-radar)
- [Full README](https://github.com/DshMarketPlace/dsh-plugin-radar#readme)
- [Back to the Plugins list](../plugins.md)
