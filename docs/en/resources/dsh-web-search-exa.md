---
title: "dsh-web-search-exa"
description: "Zero-config Exa web search provider: keyless anonymous MCP fallback plus keyed REST search."
keywords: "dsh-web-search-exa, search, plugin, deepseek harness, dsh"
---
# dsh-web-search-exa

> ⭐ **6** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 6 | Status | ✅ active |
| Author | [TonyDua](https://github.com/TonyDua) | Updated | 2026-08-14 |
| Subcategory | 🌐 Web search | Capabilities | search |

## One-liner

> Zero-config Exa web search provider: keyless anonymous MCP fallback plus keyed REST search.

## About

Built with [deepseek-v4-flash](https://api-docs.deepseek.com) inside DeepSeek Harness (dsh).

## ✨ Key Features

- 🆓 **Zero-config, keyless by default** — searches route through Exa's hosted MCP
- 🔑 **Keyed REST upgrade** — set `EXA_API_KEY` and it automatically switches to
- 🔌 **Drop-in provider** — registers into the dsh `ctx.web` seam; the existing
- 🎛️ **`providerId` switch** — can coexist with the official
- 📦 **npm-publishable** — MIT, ESM, bundled types, `files` limited to `lib/`.

## 📦 Install

```bash
dsh plugin --profile web add @tonydua/dsh-web-search-exa
```

## 🚀 Quick Start

```bash
- id: web
  name: '@deepseek-ai/dsh-web'
  config:
    searchProvider: exa
```

## 📚 Learn more

**Installation (into a dsh profile)**

**One command from npm** (v0.1.3+ ships the `dsh.bundle` manifest — the bundle patch inserts the provider row, so no manual patch editing is needed): dsh plugin --profile web add @tonydua/dsh-web-search-exa Restart `dsh web`. **Without an API key** the official DeepSeek search provider is unavailable, so the seam auto-selects this provider — fully zero-config. **With a key configured**, select Exa

**FAQ**

**Q: Do I need an Exa API key?** No. Without a key the provider uses Exa's free anonymous hosted MCP. With a key it uses the REST API for higher limits. **Q: I got HTTP 429 / rate limited.** That's Exa's anonymous-MCP rate limit. Configure `EXA_API_KEY` (or the `apiKey` field) and the provider switches to the REST path automatically. **Q: Can I run this alongside the official Exa provider?** Yes —

## 🔗 Links

- [GitHub Repository](https://github.com/TonyDua/dsh-web-search-exa)
- [Full README](https://github.com/TonyDua/dsh-web-search-exa#readme)
- [Back to the Plugins list](../plugins.md)
