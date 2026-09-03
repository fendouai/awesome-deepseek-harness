---
title: "dsh-plugin-product-subagents"
description: "Role-based Codex/Claude Code/ACP subagent providers: continuable children with durable state."
keywords: "dsh-plugin-product-subagents, multi-agent, agent, deepseek harness, dsh"
---
# dsh-plugin-product-subagents

> ⭐ **17** · ✅ active · agent

| | | | |
|---|---|---|---|
| Type | agent | Category | Multi-agent |
| Stars | ⭐ 17 | Status | ✅ active |
| Author | [shaokeyibb](https://github.com/shaokeyibb) | Updated | 2026-08-17 |

## One-liner

> Role-based Codex/Claude Code/ACP subagent providers: continuable children with durable state.

## About

Role-based **Codex / Claude Code / ACP** subagent providers for the DeepSeek Harness. Turns external agent CLIs into durable, continuable subagents with a declarative role library, per-role product permissions, delegation with a permission ceiling, and cross-platform process launching.

## ✨ Key Features

- **Continuable children** — one-shot sync or async continuable (control with
- **Session continuity** — a child's remote product session survives idle
- **Declarative roles** (`roles/*.json`) — `general` (default), `code-review`,
- **Two-layer permission model** — the relay model is always a read-only
- **Permission ceiling** — a child can never spawn a descendant with more
- **Any ACP agent** — add Cursor (`agent acp`), CodeBuddy (`cbc --acp`),
- **Resource management** — idle disposal, configurable timeouts, concurrency
- **Cross-platform** — Windows `.cmd` shims, Windows-safe path escaping;

## 📦 Install

```bash
dsh plugin --profile web add dsh-plugin-product-subagents
```

## 🚀 Quick Start

```bash
- id: product-subagents
  config:
    idleTimeoutMs: 600000
    providers:
      cursor:    { type: acp, command: agent, args: [acp] }
      codebuddy: { type: acp, command: cbc, args: [--acp] }
```

## 📚 Learn more

**Install via your agent (one line)**

Paste this to your DeepSeek Harness agent (or any coding agent with shell access to the harness home) — it performs every step itself: > Install the `dsh-plugin-product-subagents` plugin into my DeepSeek Harness > web profile: run `dsh plugin --profile web add dsh-plugin-product-subagents`, > then tell me to restart the harness so the plugin loads.

**Quick start**

In a session, the model has six tools: product_delegate role=general task="Refactor demo-project/calc.js and run its tests" product_wait subagent_id=<childId>

**Configuration**

config: providers: { cursor: { type: acp, command: agent, args: [acp] } } idleTimeoutMs: 600000 # settled children release their remote session # after this idle period (0 disables) maxConcurrentChildren: 8 # cap on simultaneous continuable children rolesDir: <path> # declarative role library (default: roles/) registryPath: <path> # durable remote-session registry

## 🔗 Links

- [GitHub Repository](https://github.com/shaokeyibb/dsh-plugin-product-subagents)
- [Full README](https://github.com/shaokeyibb/dsh-plugin-product-subagents#readme)
- [Back to the Agents & Multi-Agent list](../agents.md)
