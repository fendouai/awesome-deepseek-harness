---
title: "dsh-web-lan-access"
description: "DeepSeek Harness (dsh) Web plugin"
keywords: "dsh-web-lan-access, search, plugin, coding, deepseek harness, dsh"
---
# dsh-web-lan-access

> ⭐ **26** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 26 | Status | ✅ active |
| Author | [AcidGr](https://github.com/AcidGr) | Updated | — |
| Subcategory | 🌐 Web search | Capabilities | coding |

## One-liner

> DeepSeek Harness (dsh) Web plugin

## About

LAN / remote access support for the [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) Web UI.

## ✨ Key Features

- No product source modified; fully reversible
- Version-independent (it only transforms the served `index.html`)
- Platform-independent (Linux / macOS / Windows / Android)

## 📦 Install

```bash
dsh plugin --profile web add dsh-web-lan-access
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add github:AcidGr/dsh-web-lan-access
```

## 📚 Learn more

**Bundle install (recommended)**

Installed from npm: dsh plugin --profile web add dsh-web-lan-access (No npm / local development — point pnpm at the repo instead: dsh plugin --profile web add github:AcidGr/dsh-web-lan-access ) Restart `dsh web`, then hard-refresh the browser.

**Manual install (no pnpm / offline)**

PROFILE="$DSH_HOME/profiles/web" # adjust DSH_HOME and profile name mkdir -p "$PROFILE/plugins" "$PROFILE/node_modules/@dsh-profile" cp -r dsh-web-lan-access "$PROFILE/plugins/lan-access" ln -sfn ../../plugins/lan-access "$PROFILE/node_modules/@dsh-profile/lan-access"

**Usage**

The plugin is **self-contained**: its bundle patch sets the webserver bind host to `0.0.0.0` directly (the CLI flag `--host 0.0.0.0` is hard-rejected for safety on newer harness versions, but the webserver config still accepts it — so **no source changes and no `--host` flag are needed**; the CLI `--port` flag still works). It also widens the `/api` trust fence automatically. 1. **Install the plug

## 🔗 Links

- [GitHub Repository](https://github.com/AcidGr/dsh-web-lan-access)
- [Full README](https://github.com/AcidGr/dsh-web-lan-access#readme)
- [Back to the Plugins list](../plugins.md)
