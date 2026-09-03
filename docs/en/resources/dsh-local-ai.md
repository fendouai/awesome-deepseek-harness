---
title: "dsh-local-ai"
description: "Local-model (Ollama) integration for DeepSeek Harness: discover, pull, remove, and inspect local models, route requests to them by task type or keyword with automatic fallback to the cloud, and get a one-shot status overview via /ollama."
keywords: "dsh-local-ai, learning, skill, coding, deepseek harness, dsh"
---
# dsh-local-ai

> ⭐ **3** · ✅ active · skill

| | | | |
|---|---|---|---|
| Type | skill | Category | Learning |
| Stars | ⭐ 3 | Status | ✅ active |
| Author | [PerryLink](https://github.com/PerryLink) | Updated | — |

## One-liner

> Local-model (Ollama) integration for DeepSeek Harness: discover, pull, remove, and inspect local models, route requests to them by task type or keyword with automatic fallback to the cloud, and get a one-shot status overview via /ollama.

## About

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-local-ai` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **Local-model (Ollama) integration for DeepSeek Harness.** *Discover, pull, remove, and inspect local models, route requests to them by task type or keyword with automatic fallback to the cloud, and get a one-shot status overview via `/ollama`.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ Key Features

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-local-ai` (counts toward the [deepseek1024.com](https://deepseek1024

## 📦 Install

```bash
# 1. install the bundle into your profile
dsh plugin --profile web add "github:PerryLink/dsh-local-ai#main"

# or from npm (published releases)
dsh plugin --profile web add dsh-local-ai

# 2. configure routing in your profile patch (cordis.yml) and restart
dsh --profile web
```

## 🚀 Quick Start

```bash
- insert:
    - id: dsh-local-ai
      name: dsh-local-ai
      config:
        route:
          - model: llama3.2
            keywords: ["confidential", "offline"]
```

## 📚 Learn more

**2. configure routing in your profile patch (cordis.yml) and **

dsh --profile web Minimal routing configuration (the rule ships commented out in `cordis.patch.yml`): - id: dsh-local-ai name: dsh-local-ai config: route: - model: llama3.2 keywords: ["confidential", "offline"] Then verify the row mounts: dsh --profile web --dump-config | grep -A2 'id: dsh-local-ai'

**Install & uninstall**

> If pnpm reports `ERR_PNPM_IGNORED_BUILDS` for this package, add `allowBuilds: { esbuild: true }` to your `pnpm-workspace.yaml` — the `dsh` CLI prints the exact snippet.

**Configuration**

All tunables are Schemastery `Config` fields (changeable from cordis.yml). An id-targeted override replaces the whole row — restate every key you need. `cordis.patch.yml` documents each key inline.

## 🔗 Links

- [GitHub Repository](https://github.com/PerryLink/dsh-local-ai)
- [Full README](https://github.com/PerryLink/dsh-local-ai#readme)
- [Back to the Skills list](../skills.md)
