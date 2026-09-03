---
title: "ruflo"
description: "Agent 元级 harness：多智能体集群部署、自主工作流编排、自适应记忆、自学习智能、RAG 集成，原生支持 Claude Code / Codex 等。"
keywords: "ruflo, harness, related, multi-agent, workflow, deepseek harness, dsh"
---
# ruflo

> ⭐ **69,896** · ✅ 活跃 · 相关

| | | | |
|---|---|---|---|
| 类型 | 相关 | 分类 | Harness |
| 星数 | ⭐ 69,896 | 状态 | ✅ 活跃 |
| 作者 | [ruvnet](https://github.com/ruvnet) | 更新时间 | — |

## 一句话介绍

> Agent 元级 harness：多智能体集群部署、自主工作流编排、自适应记忆、自学习智能、RAG 集成，原生支持 Claude Code / Codex 等。

## 详细介绍

**An agent meta-harness for Claude Code and Codex.** One `npx ruflo init` gives Claude Code a nervous system: agents self-organize into swarms, learn from every task, remember across sessions, and — with federation — securely talk to agents on other machines without leaking data. You keep writing code. Ruflo handles the coordination. Self-Learning / Self-Optimizing Agent Architecture User --> Ruflo (CLI/MCP) --> Router --> Swarm --> Agents --> Memory --> LLM Providers ^ | +---- Learning Loop 📖 Background — where the name comes from ---

## 📦 安装

```bash
# Interactive setup wizard — runs identically on every platform
npx ruflo@latest init wizard

# Quick non-interactive init
# npx ruflo@latest init

# Or install globally
npm install -g ruflo@latest
```

## 🚀 快速开始

```bash
# Add Ruflo as an MCP server in Claude Code
claude mcp add claude-flow -- npx ruflo@latest mcp start
```

## 📚 更多信息

**Quick Start**

There are **two different install paths** with very different surface areas. Pick based on what you need (#1744):

**Install core + any plugins you need**

/plugin install ruflo-core@ruflo /plugin install ruflo-swarm@ruflo /plugin install ruflo-rag-memory@ruflo /plugin install ruflo-neural-trader@ruflo This adds slash commands and agent definitions. `ruflo-core` (installed above) does register its own MCP server on install — its tools are callable as `mcp__plugin_ruflo-core_ruflo__*` (e.g. `mcp__plugin_ruflo-core_ruflo__memory_store`), not the bare `

**One-line install (POSIX shells only — see Windows note below**

curl -fsSL https://cdn.jsdelivr.net/gh/ruvnet/ruflo@main/scripts/install.sh | bash **All platforms (including native Windows PowerShell / cmd):**

**Or install globally**

npm install -g ruflo@latest > 💡 **Windows users:** the `curl ... | bash` form needs a POSIX shell (Git-Bash, WSL, MSYS). The `npx ruflo@latest init wizard` line works natively in PowerShell and cmd. If you hit an `'bash' is not recognized` error, use the `npx` line instead — both end up running the same init flow.

## 🔗 链接

- [GitHub 仓库](https://github.com/ruvnet/ruflo)
- [完整 README](https://github.com/ruvnet/ruflo#readme)
- [返回ruflo所在分类](../related.md)
