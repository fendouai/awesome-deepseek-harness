---
title: "memtrace-public"
description: "Structural memory for AI coding agents. Bi-temporal graph, MCP-native, zero LLM calls. Cursor · Claude Code · Codex · DeepSeek Harness · Hermes · VS Code · Windsurf."
keywords: "memtrace-public, mcp, integration, coding, memory, multi-agent, deepseek harness, dsh"
---
# memtrace-public

> ⭐ **459** · ✅ 活跃 · 集成 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | MCP |
| 星数 | ⭐ 459 | 状态 | ✅ 活跃 |
| 作者 | [syncable-dev](https://github.com/syncable-dev) | 更新时间 | 2026-08-20 |

## 一句话介绍

> Structural memory for AI coding agents. Bi-temporal graph, MCP-native, zero LLM calls. Cursor · Claude Code · Codex · DeepSeek Harness · Hermes · VS Code · Windsurf.

## 详细介绍

Memtrace runs as a [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) plugin. Install Harness first (`npm install -g @deepseek-ai/dsh` — that is the `dsh` command), then add Memtrace: npx -y @deepseek-ai/dsh plugin --profile web add github:syncable-dev/dsh-plugin-memtrace Then ask the agent to index the workspace and pull blast radius, evolution, or an architecture briefing. Details: [syncable-dev/dsh-plugin-memtrace](https://github.com/syncable-dev/dsh-plugin-memtrace). ---

## 📦 安装

```bash
npx -y @deepseek-ai/dsh plugin --profile web add github:syncable-dev/dsh-plugin-memtrace
```

## 🚀 快速开始

```bash
npm install -g @deepseek-ai/dsh
dsh plugin --profile web add github:syncable-dev/dsh-plugin-memtrace
```

## 📚 更多信息

**Uninstall**

memtrace uninstall # removes skills, MCP server, plugin, settings npm uninstall -g memtrace Already ran `npm uninstall` first? The cleanup script is at `~/.memtrace/uninstall.js`: node ~/.memtrace/uninstall.js

**Install troubleshooting**

`npm install -g memtrace` ships a small main package + a platform-specific binary (one of `@memtrace/darwin-arm64`, `@memtrace/linux-x64`, `@memtrace/win32-x64`). If `memtrace start` ever says *"Could not find binary for your platform"*:

**Or install the platform binary directly (Apple Silicon shown**

npm install -g @memtrace/darwin-arm64 This typically only happens on machines where npm is configured to skip optional dependencies (corporate npmrc, certain CI caches). ---

## 🔗 链接

- [GitHub 仓库](https://github.com/syncable-dev/memtrace-public)
- [完整 README](https://github.com/syncable-dev/memtrace-public#readme)
- [返回memtrace-public所在分类](../integrations.md)
