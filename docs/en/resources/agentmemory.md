---
title: "agentmemory"
description: "Persistent memory for AI coding agents based on real-world benchmarks (upstream of DSH agentmemory ports)."
keywords: "agentmemory, harness, related, memory, deepseek harness, dsh"
---
# agentmemory

> ⭐ **27,233** · ✅ active · related · ⬆️ +36 recently

| | | | |
|---|---|---|---|
| Type | related | Category | Harness |
| Stars | ⭐ 27,233 | Status | ✅ active |
| Author | [rohitg00](https://github.com/rohitg00) | Updated | 2026-08-17 |

## One-liner

> Persistent memory for AI coding agents based on real-world benchmarks (upstream of DSH agentmemory ports).

## About

Requirements: - Node.js 20 or newer with npm and npx (`node -v`, `npm -v`, and `npx -v`). - macOS/Linux automatic iii-engine installation also needs `curl`, a POSIX `sh`, and `tar`. Minimal images such as `node:20-slim` may not include them. - Native Windows requires the pinned iii-engine v0.11.2 `iii.exe` to be installed manually. WSL2 or Docker Desktop are the other supported paths. Canonical fresh-install command: npx -y @agentmemory/agentmemory@latest The first run is an interactive setup: pick the agents to wire (Claude Code, Cursor, Codex, Gemini CLI, OpenCode, ...), pick an LLM provider or stay keyless, and it seeds the config, starts the memory server and its pinned iii engine, and offers to install globally so the bare `agentmemory` command works everywhere afterward. `-y` accepts

## ✨ Key Features

- Node.js 20 or newer with npm and npx (`node -v`, `npm -v`, and `npx -v`).
- macOS/Linux automatic iii-engine installation also needs `curl`, a POSIX `sh`, and `tar`. Minimal images such as `node:20-slim` may not include them.
- Native Windows requires the pinned iii-engine v0.11.2 `iii.exe` to be installed manually. WSL2 or Docker Desktop are the other supported paths.

## 📦 Install

```bash
npm install -g @agentmemory/agentmemory@latest
```

## 🚀 Quick Start

```bash
npx -y @agentmemory/agentmemory@latest --data-dir ~/.agentmemory-projects/main
AGENTMEMORY_DATA_DIR=~/.agentmemory-projects/main npx -y @agentmemory/agentmemory@latest
```

## 📚 Learn more

**Install**

Requirements: Canonical fresh-install command: npx -y @agentmemory/agentmemory@latest The first run is an interactive setup: pick the agents to wire (Claude Code, Cursor, Codex, Gemini CLI, OpenCode, ...), pick an LLM provider or stay keyless, and it seeds the config, starts the memory server and its pinned iii engine, and offers to install globally so the bare `agentmemory` command works everywhe

**Validate a fresh install and restart persistence**

With the server running, validate REST, health, the viewer, and the iii-backed runtime status: curl -fsS http://localhost:3111/agentmemory/livez curl -fsS http://localhost:3111/agentmemory/health curl -fsS -o /dev/null http://localhost:3113/ npx -y @agentmemory/agentmemory@latest status The startup ready panel accounts for all four ports: REST/MCP HTTP on 3111, iii streams on 3112, the viewer on 3

**Claude Code without the plugin install (MCP-standalone path)**

If you wire agentmemory's MCP server through `~/.claude.json` directly instead of using `/plugin install`, Claude Code never resolves `${CLAUDE_PLUGIN_ROOT}` and you have to point hook scripts at absolute paths in `~/.claude/settings.json`. Those paths typically embed the agentmemory version (e.g. `~/.codex/plugins/cache/agentmemory/agentmemory/0.9.22/scripts/…`), so the next upgrade silently brea

**2. register the agentmemory marketplace and install the plug**

codex plugin marketplace add rohitg00/agentmemory codex plugin add agentmemory@agentmemory The Codex plugin ships from the same `plugin/` directory as the Claude Code plugin. It registers: Codex's hook engine injects `CLAUDE_PLUGIN_ROOT` into hook subprocesses (per [`codex-rs/hooks/src/engine/discovery.rs`](https://github.com/openai/codex/blob/main/codex-rs/hooks/src/engine/discovery.rs)), so the 

## 🔗 Links

- [GitHub Repository](https://github.com/rohitg00/agentmemory)
- [Full README](https://github.com/rohitg00/agentmemory#readme)
- [Back to the Related Agent Harnesses list](../related.md)
