---
title: "dsh-defend"
description: "Prompt-injection, jailbreak, and secret-leak defense for DeepSeek Harness: Aho-Corasick detection with allow/ask/block interception and sanitized audit events"
keywords: "dsh-defend, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-defend

> ⭐ **5** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 5 | Status | ✅ active |
| Author | [PerryLink](https://github.com/PerryLink) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> Prompt-injection, jailbreak, and secret-leak defense for DeepSeek Harness: Aho-Corasick detection with allow/ask/block interception and sanitized audit events

## About

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-defend` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **Prompt-injection, jailbreak, and secret-leak defense for DeepSeek Harness.** *Rules decide the known. Interception decides the rest — and everything is audited.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ Key Features

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-defend` (counts toward the [deepseek1024.com](https://deepseek1024.c

## 📦 Install

```bash
# 1. install the bundle into your profile
dsh plugin --profile web add "github:PerryLink/dsh-defend#main"

# or from npm (published releases)
dsh plugin --profile web add dsh-defend

# 2. restart and verify the row
dsh --profile web --dump-config | grep -A3 'id: dsh-defend'
```

## 🚀 Quick Start

```bash
inbound message ── agent/pre-step ── scan ── clean → next()/enter
tool arguments ── tools/pre-execute ── scan ── allow → next()
tool results   ── tools/post-execute ── scan ── block → feedback
                                  │
                                  └─ defend/detection audit (rule id, family,
                                     severity, decision — never matched text)
```

## 📚 Learn more

**Configuration**

All tunables are Schemastery `Config` fields (changeable from cordis.yml). An id-targeted override replaces the whole row — restate every key you need. `cordis.patch.yml` documents each key inline.

## 🔗 Links

- [GitHub Repository](https://github.com/PerryLink/dsh-defend)
- [Full README](https://github.com/PerryLink/dsh-defend#readme)
- [Back to the Plugins list](../plugins.md)
