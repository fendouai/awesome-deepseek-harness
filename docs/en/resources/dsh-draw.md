---
title: "dsh-draw"
description: "Unified text-to-image router with config-driven OpenAI-compatible engine routing and health-aware fallback."
keywords: "dsh-draw, vision, plugin, deepseek harness, dsh"
---
# dsh-draw

> ⭐ **5** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 5 | Status | ✅ active |
| Author | [PerryLink](https://github.com/PerryLink) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | vision |

## One-liner

> Unified text-to-image router with config-driven OpenAI-compatible engine routing and health-aware fallback.

## About

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-draw` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **Unified static-image generation routing for DeepSeek Harness.** *One tool, many engines — health-aware fallback, durable results, counted usage.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ Key Features

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-draw` (counts toward the [deepseek1024.com](https://deepseek1024.com

## 🚀 Quick Start

```bash
model                           harness
  │ image_generate {prompt, ...} ──▶ validate ──▶ quota check ──▶ router
  │                                  openai ──(fail)──▶ cogview ──▶ images
  │ ◀── canonical JSON + image blocks (durable attachment refs)
  │                       └── draw/generated session event (quota + audit)
```

## 📚 Learn more

**Install & uninstall**

> If pnpm reports `ERR_PNPM_IGNORED_BUILDS` for this package (esbuild's harmless platform-binary validation), add `allowBuilds: { esbuild: true }` to your `pnpm-workspace.yaml` — the `dsh` CLI prints the exact snippet.

**Configuration**

All tunables are Schemastery `Config` fields (changeable from cordis.yml). An id-targeted override replaces the whole row — restate every key you need. `cordis.patch.yml` documents each key inline. Example override in your profile patch: - id: dsh-draw name: dsh-draw config: defaultEngine: cogview maxImagesPerCall: 2

## 🔗 Links

- [GitHub Repository](https://github.com/PerryLink/dsh-draw)
- [Full README](https://github.com/PerryLink/dsh-draw#readme)
- [Back to the Plugins list](../plugins.md)
