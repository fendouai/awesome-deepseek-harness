---
title: "dsh-agy"
description: "Google Antigravity (agy) OAuth auth + model access plugin for DeepSeek Harness: multi-account pool, 429 rotation, device fingerprinting, CLI and web login."
keywords: "dsh-agy, search, plugin, coding, deepseek harness, dsh"
---
# dsh-agy

> ⭐ **19** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 19 | Status | ✅ active |
| Author | [chaos-03x](https://github.com/chaos-03x) | Updated | 2026-08-19 |
| Subcategory | 🌐 Web search | Capabilities | coding |

## One-liner

> Google Antigravity (agy) OAuth auth + model access plugin for DeepSeek Harness: multi-account pool, 429 rotation, device fingerprinting, CLI and web login.

## About

Google Antigravity (agy) access for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness): OAuth authentication, a multi-account pool with automatic 429 rotation, device fingerprinting, and both CLI and web management.

## ✨ Key Features

- **OAuth login**: one-click sign-in via browser OAuth callback, with headless
- **Two management surfaces**: web and CLI, either one works, core features are
- **Multi-account pool**: encrypted account store, usage-aware account
- **Quota dashboard**: only active when DSH Web is running; append `/agy` to
- **CLI**: `dsh-agy login|status|import|verify|logout` works standalone, with or

## 📦 Install

```bash
# 1. Install plugin into DSH web profile (via dsh CLI, or pnpx/npx if dsh is not in PATH)
dsh plugin --profile web add dsh-agy
# or: npx @deepseek-ai/dsh plugin --profile web add dsh-agy

# 2. Launch DSH Web
dsh web

# 3. Open dashboard at http://127.0.0.1:3080/agy
# Click "Login with Google", complete OAuth authorization, and start using the agy provider
```

## 🚀 Quick Start

```bash
git clone https://github.com/chaos-03x/dsh-agy.git
cd dsh-agy && pnpm install && pnpm run build
dsh plugin --profile web link .
```

## 📚 Learn more

**Screenshots**

The `/agy` dashboard inside DSH Web — account cards, per-model quota bars, and one-shot model tests:

**Or install globally**

npm install -g dsh-agy dsh-agy login # interactive OAuth (browser, --headless paste, or --blob) dsh-agy status # list accounts + quota summary dsh-agy verify # refresh + health check dsh-agy health # batch health check (optionally on an interval) dsh-agy import <file> # import agy auth.json or credential blob (--blob) dsh-agy logout # remove account

## 🔗 Links

- [GitHub Repository](https://github.com/chaos-03x/dsh-agy)
- [Full README](https://github.com/chaos-03x/dsh-agy#readme)
- [Back to the Plugins list](../plugins.md)
