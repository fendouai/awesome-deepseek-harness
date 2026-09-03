---
title: "dsh-lsp-actions"
description: "LSP action surface for DeepSeek Harness: diagnostics, formatting, completion, code actions, symbols, signature help, inlay hints, and rename tools over language servers"
keywords: "dsh-lsp-actions, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-lsp-actions

> ⭐ **11** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 11 | Status | ✅ active |
| Author | [PerryLink](https://github.com/PerryLink) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> LSP action surface for DeepSeek Harness: diagnostics, formatting, completion, code actions, symbols, signature help, inlay hints, and rename tools over language servers

## About

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-lsp-actions` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **The LSP action surface for DeepSeek Harness — real language servers, real feedback, and the IDE integration backend for editors.** *Diagnostics, formatting, completion, code actions, symbols, signature help, inlay hints, and rename for your agent's editor loop — plus the stable editor action protocol (`lsp.actions.*`) that lets any editor consume them directly.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ Key Features

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-lsp-actions` (counts toward the [deepseek1024.com](https://deepseek1

## 📦 Install

```bash
# 1. install the bundle into your profile
dsh plugin --profile web add "github:PerryLink/dsh-lsp-actions#main"

# or from npm (published releases)
dsh plugin --profile web add dsh-lsp-actions

# 2. restart and verify the row
dsh --profile web --dump-config | grep -A3 'id: lsp-actions'
```

## 🚀 Quick Start

```bash
lsp_diagnostics / lsp_format / lsp_completion / lsp_code_action /
lsp_symbols / lsp_signature / lsp_inlay_hints / lsp_rename
        │
        ▼
   ctx.lsp seam (extended: diagnostics / formatDocument / completion)
        │  absent · legacy · no provider for this file
        ▼
   built-in stdio client  ←  servers table (ctx.subprocess.spawn + JSON-RPC)
```

## 📚 Learn more

**Configuration**

All tunables are Schemastery `Config` fields (changeable from cordis.yml). An id-targeted override replaces the whole row — restate every key you need. `cordis.patch.yml` documents each key inline. Each `servers` entry is an `LspServerEntry`: `command` (executable resolved on PATH at load) and `extensionToLanguage` (`".ts"` → `typescript`) are required; optional `fileGlobs`, `args`, `env`, `initia

**Architecture**

Actions run **official-seam-first** and fall back to the plugin's own minimal stdio client: lsp_diagnostics / lsp_format / lsp_completion / lsp_code_action / lsp_symbols / lsp_signature / lsp_inlay_hints / lsp_rename │ ▼ ctx.lsp seam (extended: diagnostics / formatDocument / completion) │ absent · legacy · no provider for this file ▼ built-in stdio client ← servers table (ctx.subprocess.spawn + JS

## 🔗 Links

- [GitHub Repository](https://github.com/PerryLink/dsh-lsp-actions)
- [Full README](https://github.com/PerryLink/dsh-lsp-actions#readme)
- [Back to the Plugins list](../plugins.md)
