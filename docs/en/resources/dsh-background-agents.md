---
title: "dsh-background-agents"
description: "Interactive long-session background agents for DeepSeek Harness: start a durable continuable child agent, watch its progress in the Web UI sidebar, message it any time, and interrupt it - all through the official subagent seam."
keywords: "dsh-background-agents, multi-agent, agent, coding, ui, deepseek harness, dsh"
---
# dsh-background-agents

> ⭐ **7** · ✅ active · agent

| | | | |
|---|---|---|---|
| Type | agent | Category | Multi-agent |
| Stars | ⭐ 7 | Status | ✅ active |
| Author | [PerryLink](https://github.com/PerryLink) | Updated | — |

## One-liner

> Interactive long-session background agents for DeepSeek Harness: start a durable continuable child agent, watch its progress in the Web UI sidebar, message it any time, and interrupt it - all through the official subagent seam.

## About

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-background-agents` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **Interactive long-session background agents plus persistent multi-agent team rooms for DeepSeek Harness — start a durable child agent that keeps working while you keep talking.** *Steer live conversations and coordinate a team across sessions; everything survives restarts through the harness's own storage.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ Key Features

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-background-agents` (counts toward the [deepseek1024.com](https://dee

## 📦 Install

```bash
# 1. install the bundle into your profile
dsh plugin --profile web add "github:PerryLink/dsh-background-agents#main"

# or from npm (published releases)
dsh plugin --profile web add dsh-background-agents

# 2. restart and verify the row
dsh --profile web --dump-config | grep -A4 'id: background-agents'
```

## 🚀 Quick Start

```bash
background_agent "watch the repo for test failures and keep me posted" (label: test-watch)
bg_list
bg_message <agentId> "also check the snapshot tests now"
bg_stop <agentId>
```

## 📚 Learn more

**Configuration**

Every tunable is a validated Schemastery `Config` field — change it in cordis.yml, never in code. Only `provider` is required.

## 🔗 Links

- [GitHub Repository](https://github.com/PerryLink/dsh-background-agents)
- [Full README](https://github.com/PerryLink/dsh-background-agents#readme)
- [Back to the Agents & Multi-Agent list](../agents.md)
