---
title: "dsh-plugin-guide"
description: "skill for Deepseek-Harness plugins development"
keywords: "dsh-plugin-guide, learning, skill, coding, deepseek harness, dsh"
---
# dsh-plugin-guide

> ⭐ **0** · ✅ active · skill

| | | | |
|---|---|---|---|
| Type | skill | Category | Learning |
| Stars | ⭐ 0 | Status | ✅ active |
| Author | [HarcoChen](https://github.com/HarcoChen) | Updated | — |

## One-liner

> skill for Deepseek-Harness plugins development

## About

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-plugin-guide` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **Everything you need to build [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) plugins.** *Official docs archive · Cordis primer · community deep-dives · battle-tested pitfalls · agent skill · CLI toolchain* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ Key Features

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-plugin-guide` (counts toward the [deepseek1024.com](https://deepseek

## 📦 Install

```bash
# 1. install the bundle into your profile
dsh plugin --profile web add "github:PerryLink/dsh-plugin-guide#main"

# or from npm (published releases)
dsh plugin --profile web add dsh-plugin-guide

# 2. restart and verify the row
dsh --profile web --dump-config | grep -A3 'id: dsh-plugin-guide'
```

## 🚀 Quick Start

```bash
npx dsh-plugin-guide new hello-plugin            # scaffold a TS plugin repo
npx dsh-plugin-guide check --json                # static-check it
npx dsh-plugin-guide verify                      # pack + clean-profile smoke
```

## 📚 Learn more

**Upstream roadmap**

`dsh-plugin-dev` is an upstream candidate for the official plugin-development CLI (planned item C12): the scaffolder/checker/verifier are the mechanical layers, while `SKILL.md` + `guide/` stay the cognitive layer.

**Configuration**

The skill bundle exposes no Schemastery `Config` — it registers the knowledge base as an agent skill with no tunable keys. The `dsh-plugin-dev` CLI reads its tunables from flags and `DSH_PLUGIN_DEV_*` environment variables (see [CLI toolchain](#cli-toolchain)).

## 🔗 Links

- [GitHub Repository](https://github.com/HarcoChen/dsh-plugin-guide)
- [Full README](https://github.com/HarcoChen/dsh-plugin-guide#readme)
- [Back to the Skills list](../skills.md)
