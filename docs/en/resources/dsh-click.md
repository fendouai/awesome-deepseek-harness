---
title: "dsh-click"
description: "Cross-platform native desktop control (Windows first): screenshot, screen read, click/type/scroll/key, app list and launch."
keywords: "dsh-click, automation, plugin, deepseek harness, dsh"
---
# dsh-click

> ⭐ **4** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Automation |
| Stars | ⭐ 4 | Status | ✅ active |
| Author | [PerryLink](https://github.com/PerryLink) | Updated | — |

## One-liner

> Cross-platform native desktop control (Windows first): screenshot, screen read, click/type/scroll/key, app list and launch.

## About

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-click` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **Cross-platform native desktop control for DeepSeek Harness — Windows first.** *Look at the screen, then act — every click gated, every action audited.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ Key Features

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-click` (counts toward the [deepseek1024.com](https://deepseek1024.co

## 📦 Install

```bash
# 1. install the bundle into your profile
dsh plugin --profile web add "github:PerryLink/dsh-click#main"

# or from npm (published releases)
dsh plugin --profile web add dsh-click

# 2. restart and verify the row
dsh --profile web --dump-config | grep -A2 'id: dsh-click'
```

## 🚀 Quick Start

```bash
> Open Notepad, type "hello", then read back what is on screen.
```

## 📚 Learn more

**Install & uninstall**

> If pnpm reports `ERR_PNPM_IGNORED_BUILDS` for this package (esbuild's harmless platform-binary validation), add `allowBuilds: { esbuild: true }` to your `pnpm-workspace.yaml` — the `dsh` CLI prints the exact snippet.

**Configuration**

All tunables are Schemastery `Config` fields (changeable from cordis.yml). An id-targeted override replaces the whole row — restate every key you need. `cordis.patch.yml` documents each key inline. Example override in your profile patch: - id: dsh-click name: dsh-click config: requireApproval: true autoApproveWindows: ['^Notepad'] focusFallback: never

## 🔗 Links

- [GitHub Repository](https://github.com/PerryLink/dsh-click)
- [Full README](https://github.com/PerryLink/dsh-click#readme)
- [Back to the Plugins list](../plugins.md)
