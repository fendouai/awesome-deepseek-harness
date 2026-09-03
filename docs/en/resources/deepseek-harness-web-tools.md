---
title: "DeepSeek-Harness-Web-Tools"
description: "Free, keyless web_search and web_fetch for DSH, DuckDuckGo-backed with no signup."
keywords: "DeepSeek-Harness-Web-Tools, search, plugin, deepseek harness, dsh"
---
# DeepSeek-Harness-Web-Tools

> ⭐ **17** · ✅ active · plugin · ⬆️ +2 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 17 | Status | ✅ active |
| Author | [tonyd2wild](https://github.com/tonyd2wild) | Updated | 2026-08-13 |
| Subcategory | 🌐 Web search | Capabilities | search |

## One-liner

> Free, keyless web_search and web_fetch for DSH, DuckDuckGo-backed with no signup.

## About

**Free, keyless `web_search` and `web_fetch` for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`).** Out of the box, `dsh`'s `web_search` requires a paid API key and `web_fetch` ships disabled. If you run `dsh` against a local model, you probably wanted neither of those things. This repo gets you both, for free, with no signup: - **`web_search`** — a local shim backed by DuckDuckGo, plus a `dsh` plugin that registers it with the `ctx.web` seam. - **`web_fetch`** — configuration to enable the provider DeepSeek already publishes. Everything here is upgrade-safe: it lives in your profile patch layer and `$DSH_HOME`, not in shipped package files. ---

## ✨ Key Features

- **`web_search`** — a local shim backed by DuckDuckGo, plus a `dsh` plugin that registers it with the `ctx.web` seam.
- **`web_fetch`** — configuration to enable the provider DeepSeek already publishes.

## 📦 Install

```bash
plugin/    a dsh plugin registering a DuckDuckGo-backed WebSearchProvider
shim/      a small local HTTP service that queries DuckDuckGo
examples/  a cordis.patch.yml showing the wiring
```

## 🚀 Quick Start

```bash
cd shim
python -m venv venv

# Windows
venv\Scripts\python.exe -m pip install -r requirements.txt
venv\Scripts\python.exe server.py

# macOS / Linux
venv/bin/python -m pip install -r requirements.txt
venv/bin/python server.py
```

## 📚 Learn more

**Configuration**

The plugin takes one option: name: 'dsh-plugin-ddg-search' config: baseURL: http://127.0.0.1:8899 The shim takes `--host`, `--port`, and `--verbose`.

## 🔗 Links

- [GitHub Repository](https://github.com/tonyd2wild/DeepSeek-Harness-Web-Tools)
- [Full README](https://github.com/tonyd2wild/DeepSeek-Harness-Web-Tools#readme)
- [Back to the Plugins list](../plugins.md)
