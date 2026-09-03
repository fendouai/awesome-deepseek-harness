---
title: "dsh-permission-rules"
description: "Claude Code-style declarative permission rules for DeepSeek Harness: ordered allow/deny/ask rules with tool-name, argument (glob/regex), and workspace-path matching on the tools/pre-execute waterfall, session-log audit, and HMR reload."
keywords: "dsh-permission-rules, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-permission-rules

> ⭐ **65** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 65 | Status | ✅ active |
| Author | [PerryLink](https://github.com/PerryLink) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> Claude Code-style declarative permission rules for DeepSeek Harness: ordered allow/deny/ask rules with tool-name, argument (glob/regex), and workspace-path matching on the tools/pre-execute waterfall, session-log audit, and HMR reload.

## About

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-permission-rules` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **Claude Code-style declarative permission rules for DeepSeek Harness.** *Rules decide what is known. A reviewer model decides what is not.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ Key Features

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-permission-rules` (counts toward the [deepseek1024.com](https://deep

## 📦 Install

```bash
# 1. install the bundle into your profile
dsh plugin --profile web add "github:PerryLink/dsh-permission-rules#main"

# or from npm (published releases)
dsh plugin --profile web add dsh-permission-rules

# 2. restart and verify the row
dsh --profile web --dump-config | grep -A4 'id: permission-rules'
```

## 🚀 Quick Start

```bash
node scripts/repair-session-logs.mjs scan [--home DIR]      # report foreign rows, change nothing
node scripts/repair-session-logs.mjs repair [--home DIR] [--dry-run]
```

## 📚 Learn more

**Configuration**

All tunables are Schemastery `Config` fields (changeable from cordis.yml). An id-targeted override replaces the whole row — restate every key you need.

## 🔗 Links

- [GitHub Repository](https://github.com/PerryLink/dsh-permission-rules)
- [Full README](https://github.com/PerryLink/dsh-permission-rules#readme)
- [Back to the Plugins list](../plugins.md)
