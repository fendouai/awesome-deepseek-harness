---
title: "dsh-lsp-actions"
description: "LSP action surface for DeepSeek Harness: diagnostics, formatting, completion, code actions, symbols, signature help, inlay hints, and rename tools over language servers"
keywords: "dsh-lsp-actions, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-lsp-actions

> ⭐ **11** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 11 | 状态 | ✅ 活跃 |
| 作者 | [PerryLink](https://github.com/PerryLink) | 更新时间 | — |
| 子分类 | 👁️ 视觉工具 | 能力 | coding |

## 一句话介绍

> LSP action surface for DeepSeek Harness: diagnostics, formatting, completion, code actions, symbols, signature help, inlay hints, and rename tools over language servers

## 详细介绍

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-lsp-actions` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **The LSP action surface for DeepSeek Harness — real language servers, real feedback, and the IDE integration backend for editors.** *Diagnostics, formatting, completion, code actions, symbols, signature help, inlay hints, and rename for your agent's editor loop — plus the stable editor action protocol (`lsp.actions.*`) that lets any editor consume them directly.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ 核心特性

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-lsp-actions` (counts toward the [deepseek1024.com](https://deepseek1

## 📦 安装

```bash
# 1. install the bundle into your profile
dsh plugin --profile web add "github:PerryLink/dsh-lsp-actions#main"

# or from npm (published releases)
dsh plugin --profile web add dsh-lsp-actions

# 2. restart and verify the row
dsh --profile web --dump-config | grep -A3 'id: lsp-actions'
```

## 🚀 快速开始

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

## 📚 更多信息

**Configuration**

All tunables are Schemastery `Config` fields (changeable from cordis.yml). An id-targeted override replaces the whole row — restate every key you need. `cordis.patch.yml` documents each key inline. Each `servers` entry is an `LspServerEntry`: `command` (executable resolved on PATH at load) and `extensionToLanguage` (`".ts"` → `typescript`) are required; optional `fileGlobs`, `args`, `env`, `initia

**Architecture**

Actions run **official-seam-first** and fall back to the plugin's own minimal stdio client: lsp_diagnostics / lsp_format / lsp_completion / lsp_code_action / lsp_symbols / lsp_signature / lsp_inlay_hints / lsp_rename │ ▼ ctx.lsp seam (extended: diagnostics / formatDocument / completion) │ absent · legacy · no provider for this file ▼ built-in stdio client ← servers table (ctx.subprocess.spawn + JS

## 🔗 链接

- [GitHub 仓库](https://github.com/PerryLink/dsh-lsp-actions)
- [完整 README](https://github.com/PerryLink/dsh-lsp-actions#readme)
- [返回dsh-lsp-actions所在分类](../plugins.md)
