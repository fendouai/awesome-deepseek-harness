---
title: "dsh-local-ai"
description: "Local-model (Ollama) integration for DeepSeek Harness: discover, pull, remove, and inspect local models, route requests to them by task type or keyword with automatic fallback to the cloud, and get a one-shot status overview via /ollama."
keywords: "dsh-local-ai, learning, skill, coding, deepseek harness, dsh"
---
# dsh-local-ai

> ⭐ **3** · ✅ 活跃 · 技能

| | | | |
|---|---|---|---|
| 类型 | 技能 | 分类 | 学习 |
| 星数 | ⭐ 3 | 状态 | ✅ 活跃 |
| 作者 | [PerryLink](https://github.com/PerryLink) | 更新时间 | — |

## 一句话介绍

> Local-model (Ollama) integration for DeepSeek Harness: discover, pull, remove, and inspect local models, route requests to them by task type or keyword with automatic fallback to the cloud, and get a one-shot status overview via /ollama.

## 详细介绍

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-local-ai` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **Local-model (Ollama) integration for DeepSeek Harness.** *Discover, pull, remove, and inspect local models, route requests to them by task type or keyword with automatic fallback to the cloud, and get a one-shot status overview via `/ollama`.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ 核心特性

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-local-ai` (counts toward the [deepseek1024.com](https://deepseek1024

## 📦 安装

```bash
# 1. install the bundle into your profile
dsh plugin --profile web add "github:PerryLink/dsh-local-ai#main"

# or from npm (published releases)
dsh plugin --profile web add dsh-local-ai

# 2. configure routing in your profile patch (cordis.yml) and restart
dsh --profile web
```

## 🚀 快速开始

```bash
- insert:
    - id: dsh-local-ai
      name: dsh-local-ai
      config:
        route:
          - model: llama3.2
            keywords: ["confidential", "offline"]
```

## 📚 更多信息

**2. configure routing in your profile patch (cordis.yml) and **

dsh --profile web Minimal routing configuration (the rule ships commented out in `cordis.patch.yml`): - id: dsh-local-ai name: dsh-local-ai config: route: - model: llama3.2 keywords: ["confidential", "offline"] Then verify the row mounts: dsh --profile web --dump-config | grep -A2 'id: dsh-local-ai'

**Install & uninstall**

> If pnpm reports `ERR_PNPM_IGNORED_BUILDS` for this package, add `allowBuilds: { esbuild: true }` to your `pnpm-workspace.yaml` — the `dsh` CLI prints the exact snippet.

**Configuration**

All tunables are Schemastery `Config` fields (changeable from cordis.yml). An id-targeted override replaces the whole row — restate every key you need. `cordis.patch.yml` documents each key inline.

## 🔗 链接

- [GitHub 仓库](https://github.com/PerryLink/dsh-local-ai)
- [完整 README](https://github.com/PerryLink/dsh-local-ai#readme)
- [返回dsh-local-ai所在分类](../skills.md)
