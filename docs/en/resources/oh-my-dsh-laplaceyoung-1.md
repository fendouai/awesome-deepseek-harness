---
title: "oh-my-dsh"
description: "Plugin ecosystem for DSH: 700+ plugins registered only through extension seams, without modifying the agent-loop skeleton."
keywords: "oh-my-dsh, registry, awesome-list, search, deepseek harness, dsh"
---
# oh-my-dsh

> ⭐ **51** · ✅ active · awesome-list · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | awesome-list | Category | Registries |
| Stars | ⭐ 51 | Status | ✅ active |
| Author | [LaplaceYoung](https://github.com/LaplaceYoung) | Updated | 2026-08-15 |

## One-liner

> Plugin ecosystem for DSH: 700+ plugins registered only through extension seams, without modifying the agent-loop skeleton.

## About

`deep-research` decomposes a compound question into sub-questions, searches and fetches sources in parallel through DSH's portable web seam, and synthesizes a cited report. Configure a `provider` + `model` and synthesis runs through the LLM; leave them unset and a deterministic template report still lands — every path degrades gracefully, none require a real key to test.

## 📦 Install

```bash
git clone https://github.com/LaplaceYoung/oh-my-dsh.git
cd oh-my-dsh
pnpm install
```

## 🚀 Quick Start

```bash
- id: omd-deep-research
  name: '@oh-my-dsh/deep-research'
  config:
    provider: deepseek-official
    model: deepseek-v4-flash
```

## 📚 Learn more

**Install**

git clone https://github.com/LaplaceYoung/oh-my-dsh.git cd oh-my-dsh pnpm install Plugins are ESM packages under `plugins/<name>` (`@oh-my-dsh/<name>`). Mount them in a DSH `cordis.yml` composition: name: '@oh-my-dsh/deep-research' config: provider: deepseek-official model: deepseek-v4-flash

**Architecture**

DSH is an all-plugin harness: the agent loop itself is a plugin, and new behavior lands through documented seams — never by editing the skeleton.

## 🔗 Links

- [GitHub Repository](https://github.com/LaplaceYoung/oh-my-dsh)
- [Full README](https://github.com/LaplaceYoung/oh-my-dsh#readme)
- [Back to the Awesome Lists & Registries list](../awesome-lists.md)
