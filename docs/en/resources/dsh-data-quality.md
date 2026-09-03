---
title: "dsh-data-quality"
description: "Deterministic data profiling, cleaning and verification with data_profile, data_clean and data_verify tools."
keywords: "dsh-data-quality, developer, plugin, workflow, deepseek harness, dsh"
---
# dsh-data-quality

> ⭐ **11** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 11 | Status | ✅ active |
| Author | [PerryLink](https://github.com/PerryLink) | Updated | — |
| Subcategory | 📁 Files & import | Capabilities | workflow |

## One-liner

> Deterministic data profiling, cleaning and verification with data_profile, data_clean and data_verify tools.

## About

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-data-quality` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **Deterministic data profiling, cleaning, and verification for DeepSeek Harness.** All computation is plain TypeScript in the harness process — the model never does the math. A `ctx.dataQuality` capability seam (Service Definition / local Provider / tool Consumers) exposes three model tools plus a frozen cross-plugin citation-checking contract. [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md)

## ✨ Key Features

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-data-quality` (counts toward the [deepseek1024.com](https://deepseek

## 📦 Install

```bash
dsh plugin --profile web add dsh-data-quality
```

## 🚀 Quick Start

```bash
pnpm pack                                  # produces dsh-data-quality-<version>.tgz
dsh plugin --profile web add ./dsh-data-quality-<version>.tgz
```

## 📚 Learn more

**Install & uninstall**

dsh plugin --profile web add dsh-data-quality # install (npm) — or the forms above dsh plugin --profile web remove dsh-data-quality # uninstall

**Configuration**

All keys are optional (defaults shown); invalid values fail loudly at load. Every key is settable from `cordis.yml` (the bundle ships `cordis.patch.yml` with the same defaults).

## 🔗 Links

- [GitHub Repository](https://github.com/PerryLink/dsh-data-quality)
- [Full README](https://github.com/PerryLink/dsh-data-quality#readme)
- [Back to the Plugins list](../plugins.md)
