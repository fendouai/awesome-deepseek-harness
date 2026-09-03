---
title: "dsh-plugin-cc"
description: "Bridge DeepSeek Harness into Claude Code for review, critique, delegation and session import."
keywords: "dsh-plugin-cc, multi-agent, agent, coding, deepseek harness, dsh"
---
# dsh-plugin-cc

> ⭐ **29** · ✅ active · agent · ⬆️ +10 recently

| | | | |
|---|---|---|---|
| Type | agent | Category | Multi-agent |
| Stars | ⭐ 29 | Status | ✅ active |
| Author | [cpj-dev](https://github.com/cpj-dev) | Updated | 2026-08-18 |

## One-liner

> Bridge DeepSeek Harness into Claude Code for review, critique, delegation and session import.

## About

[English](README.md) | [简体中文](README.zh-CN.md) Claude Code plugin that runs **DeepSeek Harness** (`dsh`) from slash commands: review, critique, one-shot tasks, and resumable multi-turn sessions. Pin: [`@deepseek-ai/dsh@0.1.1-rc.2`](https://www.npmjs.com/package/@deepseek-ai/dsh). After upgrading the plugin, rerun `/dsh:setup`. Re-verify [docs/dsh-compat.md](docs/dsh-compat.md) on every dsh upgrade.

## ✨ Key Features

- this run: `/dsh:run --mode minimal …` or `--mode anchored-standard`
- this shell: `DSH_CC_MODE=minimal`
- this machine: `/dsh:setup --mode minimal`

## 🚀 Quick Start

```bash
/plugin marketplace add cpj-dev/dsh-plugin-cc
/plugin install dsh@deepseek-dsh
/dsh:setup
/dsh:review
```

## 📚 Learn more

**Quick start**

Needs Node >= 20 and a `DEEPSEEK_API_KEY`. `/dsh:setup` also needs Node >= 22.19, `npm`, and `pnpm` (`corepack enable`). /plugin marketplace add cpj-dev/dsh-plugin-cc /plugin install dsh@deepseek-dsh /dsh:setup /dsh:review Already have a built [deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) checkout? `/dsh:setup --harness <path>`. Already have a `dsh` binary? set `DSH_BINARY`. 

## 🔗 Links

- [GitHub Repository](https://github.com/cpj-dev/dsh-plugin-cc)
- [Full README](https://github.com/cpj-dev/dsh-plugin-cc#readme)
- [Back to the Agents & Multi-Agent list](../agents.md)
