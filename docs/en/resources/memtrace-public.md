---
title: "memtrace-public"
description: "Structural memory for AI coding agents. Bi-temporal graph, MCP-native, zero LLM calls. Cursor · Claude Code · Codex · DeepSeek Harness · Hermes · VS Code · Windsurf."
keywords: "memtrace-public, mcp, integration, coding, memory, multi-agent, deepseek harness, dsh"
---
# memtrace-public

> ⭐ **459** · ✅ active · integration · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | integration | Category | MCP |
| Stars | ⭐ 459 | Status | ✅ active |
| Author | [syncable-dev](https://github.com/syncable-dev) | Updated | 2026-08-20 |

## One-liner

> Structural memory for AI coding agents. Bi-temporal graph, MCP-native, zero LLM calls. Cursor · Claude Code · Codex · DeepSeek Harness · Hermes · VS Code · Windsurf.

## About

Memtrace runs as a [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) plugin. Install Harness first (`npm install -g @deepseek-ai/dsh` — that is the `dsh` command), then add Memtrace: npx -y @deepseek-ai/dsh plugin --profile web add github:syncable-dev/dsh-plugin-memtrace Then ask the agent to index the workspace and pull blast radius, evolution, or an architecture briefing. Details: [syncable-dev/dsh-plugin-memtrace](https://github.com/syncable-dev/dsh-plugin-memtrace). ---

## 📦 Install

```bash
npx -y @deepseek-ai/dsh plugin --profile web add github:syncable-dev/dsh-plugin-memtrace
```

## 🚀 Quick Start

```bash
npm install -g @deepseek-ai/dsh
dsh plugin --profile web add github:syncable-dev/dsh-plugin-memtrace
```

## 📚 Learn more

**Uninstall**

memtrace uninstall # removes skills, MCP server, plugin, settings npm uninstall -g memtrace Already ran `npm uninstall` first? The cleanup script is at `~/.memtrace/uninstall.js`: node ~/.memtrace/uninstall.js

**Install troubleshooting**

`npm install -g memtrace` ships a small main package + a platform-specific binary (one of `@memtrace/darwin-arm64`, `@memtrace/linux-x64`, `@memtrace/win32-x64`). If `memtrace start` ever says *"Could not find binary for your platform"*:

**Or install the platform binary directly (Apple Silicon shown**

npm install -g @memtrace/darwin-arm64 This typically only happens on machines where npm is configured to skip optional dependencies (corporate npmrc, certain CI caches). ---

## 🔗 Links

- [GitHub Repository](https://github.com/syncable-dev/memtrace-public)
- [Full README](https://github.com/syncable-dev/memtrace-public#readme)
- [Back to the MCP & Integrations list](../integrations.md)
