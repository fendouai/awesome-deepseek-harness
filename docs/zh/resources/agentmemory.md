---
title: "agentmemory"
description: "基于真实基准的 AI 编码 Agent 持久记忆（DSH agentmemory 移植的上游项目）。"
keywords: "agentmemory, harness, related, memory, deepseek harness, dsh"
---
# agentmemory

> ⭐ **27,233** · ✅ 活跃 · 相关 · 近期 ⬆️ +36

| | | | |
|---|---|---|---|
| 类型 | 相关 | 分类 | Harness |
| 星数 | ⭐ 27,233 | 状态 | ✅ 活跃 |
| 作者 | [rohitg00](https://github.com/rohitg00) | 更新时间 | 2026-08-17 |

## 一句话介绍

> 基于真实基准的 AI 编码 Agent 持久记忆（DSH agentmemory 移植的上游项目）。

## 详细介绍

Requirements: - Node.js 20 or newer with npm and npx (`node -v`, `npm -v`, and `npx -v`). - macOS/Linux automatic iii-engine installation also needs `curl`, a POSIX `sh`, and `tar`. Minimal images such as `node:20-slim` may not include them. - Native Windows requires the pinned iii-engine v0.11.2 `iii.exe` to be installed manually. WSL2 or Docker Desktop are the other supported paths. Canonical fresh-install command: npx -y @agentmemory/agentmemory@latest The first run is an interactive setup: pick the agents to wire (Claude Code, Cursor, Codex, Gemini CLI, OpenCode, ...), pick an LLM provider or stay keyless, and it seeds the config, starts the memory server and its pinned iii engine, and offers to install globally so the bare `agentmemory` command works everywhere afterward. `-y` accepts

## ✨ 核心特性

- Node.js 20 or newer with npm and npx (`node -v`, `npm -v`, and `npx -v`).
- macOS/Linux automatic iii-engine installation also needs `curl`, a POSIX `sh`, and `tar`. Minimal images such as `node:20-slim` may not include them.
- Native Windows requires the pinned iii-engine v0.11.2 `iii.exe` to be installed manually. WSL2 or Docker Desktop are the other supported paths.

## 📦 安装

```bash
npm install -g @agentmemory/agentmemory@latest
```

## 🚀 快速开始

```bash
npx -y @agentmemory/agentmemory@latest --data-dir ~/.agentmemory-projects/main
AGENTMEMORY_DATA_DIR=~/.agentmemory-projects/main npx -y @agentmemory/agentmemory@latest
```

## 📚 更多信息

**Install**

Requirements: Canonical fresh-install command: npx -y @agentmemory/agentmemory@latest The first run is an interactive setup: pick the agents to wire (Claude Code, Cursor, Codex, Gemini CLI, OpenCode, ...), pick an LLM provider or stay keyless, and it seeds the config, starts the memory server and its pinned iii engine, and offers to install globally so the bare `agentmemory` command works everywhe

**Validate a fresh install and restart persistence**

With the server running, validate REST, health, the viewer, and the iii-backed runtime status: curl -fsS http://localhost:3111/agentmemory/livez curl -fsS http://localhost:3111/agentmemory/health curl -fsS -o /dev/null http://localhost:3113/ npx -y @agentmemory/agentmemory@latest status The startup ready panel accounts for all four ports: REST/MCP HTTP on 3111, iii streams on 3112, the viewer on 3

**Claude Code without the plugin install (MCP-standalone path)**

If you wire agentmemory's MCP server through `~/.claude.json` directly instead of using `/plugin install`, Claude Code never resolves `${CLAUDE_PLUGIN_ROOT}` and you have to point hook scripts at absolute paths in `~/.claude/settings.json`. Those paths typically embed the agentmemory version (e.g. `~/.codex/plugins/cache/agentmemory/agentmemory/0.9.22/scripts/…`), so the next upgrade silently brea

**2. register the agentmemory marketplace and install the plug**

codex plugin marketplace add rohitg00/agentmemory codex plugin add agentmemory@agentmemory The Codex plugin ships from the same `plugin/` directory as the Claude Code plugin. It registers: Codex's hook engine injects `CLAUDE_PLUGIN_ROOT` into hook subprocesses (per [`codex-rs/hooks/src/engine/discovery.rs`](https://github.com/openai/codex/blob/main/codex-rs/hooks/src/engine/discovery.rs)), so the 

## 🔗 链接

- [GitHub 仓库](https://github.com/rohitg00/agentmemory)
- [完整 README](https://github.com/rohitg00/agentmemory#readme)
- [返回agentmemory所在分类](../related.md)
