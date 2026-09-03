---
title: "dsh-movein"
description: "Migrate Claude Code setup into DeepSeek Harness. Import skills, commands, agents, hooks, permission rules, and MCP config. Codex and OpenCode supported."
keywords: "dsh-movein, mcp, integration, coding, multi-agent, deepseek harness, dsh"
---
# dsh-movein

> ⭐ **15** · ✅ active · integration

| | | | |
|---|---|---|---|
| Type | integration | Category | MCP |
| Stars | ⭐ 15 | Status | ✅ active |
| Author | [sjh9714](https://github.com/sjh9714) | Updated | — |

## One-liner

> Migrate Claude Code setup into DeepSeek Harness. Import skills, commands, agents, hooks, permission rules, and MCP config. Codex and OpenCode supported.

## About

[中文](./docs/README.zh.md) Migrate your Claude Code setup into [DeepSeek Harness (DSH)](https://github.com/deepseek-ai/deepseek-harness) without rebuilding it by hand. Preview instructions, skills, commands, agents, hooks, permission rules, and MCP servers before DSH writes anything. Existing destinations stay untouched. This GIF uses two screenshots from a live DSH `0.1.1-rc.2` run. The first shows the dry run and the second shows the applied result. If this saves you setup time, [star dsh-movein](https://github.com/sjh9714/dsh-movein).

## ✨ Key Features

- Claude Code is the primary path
- Dry run is the default
- Every category can be included or excluded
- Conflicts and unsupported entries appear before apply
- Codex and OpenCode stay available under the secondary origin panel

## 📦 Install

```bash
dsh plugin --profile web add dsh-movein
```

## 🚀 Quick Start

```bash
# Claude Code
npx dsh-movein
npx dsh-movein --apply

# Codex
npx dsh-movein --from codex
npx dsh-movein --from codex --apply

# OpenCode
npx dsh-movein --from opencode
npx dsh-movein --from opencode --apply
```

## 🔗 Links

- [GitHub Repository](https://github.com/sjh9714/dsh-movein)
- [Full README](https://github.com/sjh9714/dsh-movein#readme)
- [Back to the MCP & Integrations list](../integrations.md)
