---
title: "dsh-hud"
description: "HUD status panel: git status, MCP servers, skills, model and token usage in a floating side panel."
keywords: "dsh-hud, developer, plugin, ui, observability, git, deepseek harness, dsh"
---
# dsh-hud

> ⭐ **9** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 9 | Status | ✅ active |
| Author | [a903067276-rgb](https://github.com/a903067276-rgb) | Updated | 2026-08-21 |
| Subcategory | 💰 Cost & billing | Capabilities | ui, observability, git |

## One-liner

> HUD status panel: git status, MCP servers, skills, model and token usage in a floating side panel.

## About

[English](README.md) | [简体中文](README.zh-CN.md) A **HUD status panel** plugin for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`) web: one button in the input toolbar opens a floating panel with git status, MCP servers, skills, official usage info and balance. *Unofficial project: independently developed and maintained by a community member, not an official DeepSeek product.*

## ✨ Key Features

- **Git** — branch, ahead/behind, unstaged / staged / untracked files (collapsible groups),
- **MCP** — connected MCP servers (derived from `mcp__<server>__<tool>` tool names)
- **Skills** — skills available to the current agent
- **Official info** — current model + reasoning effort, plan mode state, token usage
- **Balance** — official DeepSeek account balance, auto-fetched from
- **Per-model usage** — current session's token buckets broken down by model

## 📦 Install

```bash
dsh plugin --profile web add "github:a903067276-rgb/dsh-hud#main"
```

## 🚀 Quick Start

```bash
lib/index.js        host half — data routes (git / mcp / skills / model)
lib/client.js       client half — UI (button + panel), final bundle, no build step
cordis.patch.yml    bundle patch — single package-name mount (official bundle flow)
docs/               install guide & architecture notes
examples/           manual double-mount example (fallback install path)
```

## 📚 Learn more

**Screenshot**

The gauge button in the input toolbar opens the floating panel showing git status, commit history, MCP servers, skills and official usage info (tokens, cache hit rate, turns/steps, LLM & tool time, context usage).

**Install**

This repository is an official **bundle plugin** (`dsh.bundle` + `dsh.client` in the root `package.json`), installed through the official profile manager: dsh plugin --profile web add "github:a903067276-rgb/dsh-hud#main" Then **restart `dsh web`** (bundle layers are composed at startup; HMR does not apply). Requires `pnpm` on PATH (`dsh plugin` forwards to pnpm). Manual mount fallback: see [docs/i

**Usage**

Click the **gauge icon** in the input toolbar (official DSH design tokens, follows dark/light theme). The panel opens on the left side by default (240px wide), clear of the official right-edge turn navigator; **drag its title bar to move it anywhere** (position remembered in `localStorage`, restored on reopen); drag its left edge to resize (200–480px, remembered in `localStorage`). Section headers

## 🔗 Links

- [GitHub Repository](https://github.com/a903067276-rgb/dsh-hud)
- [Full README](https://github.com/a903067276-rgb/dsh-hud#readme)
- [Back to the Plugins list](../plugins.md)
