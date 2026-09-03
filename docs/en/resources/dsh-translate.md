---
title: "dsh-translate"
description: "Vendor parameter translation and deterministic JSON repair for DeepSeek Harness: /translate maps temperature/top_p/max_tokens/stop/system across 11 vendors, and the post-execute repair layer (plus fix_json) fixes broken JSON tool output without ever fabricating data"
keywords: "dsh-translate, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-translate

> ⭐ **2** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 2 | Status | ✅ active |
| Author | [PerryLink](https://github.com/PerryLink) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> Vendor parameter translation and deterministic JSON repair for DeepSeek Harness: /translate maps temperature/top_p/max_tokens/stop/system across 11 vendors, and the post-execute repair layer (plus fix_json) fixes broken JSON tool output without ever fabricating data

## About

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-translate` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **Vendor parameter translation and deterministic JSON repair for DeepSeek Harness.** *Same request, every vendor. Broken JSON, fixed without inventing data.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ Key Features

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-translate` (counts toward the [deepseek1024.com](https://deepseek102

## 📦 Install

```bash
# 1. install the bundle into your profile
dsh plugin --profile web add "github:PerryLink/dsh-translate#main"

# or from npm (published releases)
dsh plugin --profile web add dsh-translate

# 2. restart and verify the row
dsh --profile web --dump-config | grep -A2 'id: dsh-translate'
```

## 🚀 Quick Start

```bash
> /translate openai ernie max_tokens
> Use fix_json to repair: {"a": 1,} against {"type":"object","properties":{"a":{"type":"integer"}},"required":["a"]}
```

## 📚 Learn more

**Configuration**

All tunables are Schemastery `Config` fields (changeable from cordis.yml). An id-targeted override replaces the whole row — restate every key you need. `cordis.patch.yml` documents each key inline. Example override in your profile patch: - id: dsh-translate name: dsh-translate config: enabled: true repair: enabled: true toolNames: ['emit-json'] strategies: escapeRepair: true trailingComma: true tr

## 🔗 Links

- [GitHub Repository](https://github.com/PerryLink/dsh-translate)
- [Full README](https://github.com/PerryLink/dsh-translate#readme)
- [Back to the Plugins list](../plugins.md)
