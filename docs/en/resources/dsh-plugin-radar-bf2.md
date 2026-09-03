---
title: "dsh-plugin-radar"
description: "Find DSH plugins by asking in plain language, then security-scan them before install"
keywords: "dsh-plugin-radar, ui, plugin, coding, deepseek harness, dsh"
---
# dsh-plugin-radar

> ⭐ **2** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 2 | Status | ✅ active |
| Author | [dshplugin-me](https://github.com/dshplugin-me) | Updated | 2026-08-16 |
| Subcategory | 🎨 Skins & themes | Capabilities | coding, ui |

## One-liner

> Find DSH plugins by asking in plain language, then security-scan them before install

## About

**Find · Vet · Install — DSH plugins, with a security scan before anything touches your profile.** Ask DSH *"is there a plugin that can…"* and this plugin searches the live [`dsh-plugin` GitHub topic](https://github.com/topics/dsh-plugin) with server-side keyword filtering, cross-checks candidates against two curated registries, then runs a **pre-install security scan** — lifecycle scripts, external domains, subprocesses, credential reads, prompt injection — reports findings either way, and only installs after you say go. It also works in reverse: already eyeing a plugin? Ask *"is XX safe to install?"* and it runs the same checklist and hands you the report.

## 📦 Install

```bash
dsh plugin --profile web add 'github:dshplugin-me/dsh-plugin-radar#v0.1.1'
```

## 🚀 Quick Start

```bash
dsh --profile web --dump-config   # shows a "# == dsh-plugin-radar" layer
dsh --profile web
```

## 🔗 Links

- [GitHub Repository](https://github.com/dshplugin-me/dsh-plugin-radar)
- [Full README](https://github.com/dshplugin-me/dsh-plugin-radar#readme)
- [Back to the Plugins list](../plugins.md)
