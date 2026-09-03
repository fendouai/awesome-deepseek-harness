---
title: "ruflo"
description: "The original agent meta-harness: deploy intelligent multi-player swarms, coordinate autonomous workflows, adaptive memory, self-learning intelligence, RAG integration and native Claude Code / Codex integrations."
keywords: "ruflo, harness, related, multi-agent, workflow, deepseek harness, dsh"
---
# ruflo

> ⭐ **69,896** · ✅ active · related

| | | | |
|---|---|---|---|
| Type | related | Category | Harness |
| Stars | ⭐ 69,896 | Status | ✅ active |
| Author | [ruvnet](https://github.com/ruvnet) | Updated | — |

## One-liner

> The original agent meta-harness: deploy intelligent multi-player swarms, coordinate autonomous workflows, adaptive memory, self-learning intelligence, RAG integration and native Claude Code / Codex integrations.

## About

**An agent meta-harness for Claude Code and Codex.** One `npx ruflo init` gives Claude Code a nervous system: agents self-organize into swarms, learn from every task, remember across sessions, and — with federation — securely talk to agents on other machines without leaking data. You keep writing code. Ruflo handles the coordination. Self-Learning / Self-Optimizing Agent Architecture User --> Ruflo (CLI/MCP) --> Router --> Swarm --> Agents --> Memory --> LLM Providers ^ | +---- Learning Loop 📖 Background — where the name comes from ---

## 📦 Install

```bash
# Interactive setup wizard — runs identically on every platform
npx ruflo@latest init wizard

# Quick non-interactive init
# npx ruflo@latest init

# Or install globally
npm install -g ruflo@latest
```

## 🚀 Quick Start

```bash
# Add Ruflo as an MCP server in Claude Code
claude mcp add claude-flow -- npx ruflo@latest mcp start
```

## 📚 Learn more

**Quick Start**

There are **two different install paths** with very different surface areas. Pick based on what you need (#1744):

**Install core + any plugins you need**

/plugin install ruflo-core@ruflo /plugin install ruflo-swarm@ruflo /plugin install ruflo-rag-memory@ruflo /plugin install ruflo-neural-trader@ruflo This adds slash commands and agent definitions. `ruflo-core` (installed above) does register its own MCP server on install — its tools are callable as `mcp__plugin_ruflo-core_ruflo__*` (e.g. `mcp__plugin_ruflo-core_ruflo__memory_store`), not the bare `

**One-line install (POSIX shells only — see Windows note below**

curl -fsSL https://cdn.jsdelivr.net/gh/ruvnet/ruflo@main/scripts/install.sh | bash **All platforms (including native Windows PowerShell / cmd):**

**Or install globally**

npm install -g ruflo@latest > 💡 **Windows users:** the `curl ... | bash` form needs a POSIX shell (Git-Bash, WSL, MSYS). The `npx ruflo@latest init wizard` line works natively in PowerShell and cmd. If you hit an `'bash' is not recognized` error, use the `npx` line instead — both end up running the same init flow.

## 🔗 Links

- [GitHub Repository](https://github.com/ruvnet/ruflo)
- [Full README](https://github.com/ruvnet/ruflo#readme)
- [Back to the Related Agent Harnesses list](../related.md)
