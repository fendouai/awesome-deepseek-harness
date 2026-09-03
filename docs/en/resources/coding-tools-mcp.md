---
title: "Coding Tools MCP"
description: "Coding-oriented MCP tool collection that appears in the emerging DSH ecosystem: give any AI agent the ability to code."
keywords: "Coding Tools MCP, mcp, integration, coding, deepseek harness, dsh"
---
# Coding Tools MCP

> ⭐ **846** · ✅ active · integration · ⬆️ +5 recently

| | | | |
|---|---|---|---|
| Type | integration | Category | MCP |
| Stars | ⭐ 846 | Status | ✅ active |
| Author | [xyTom](https://github.com/xyTom) | Updated | 2026-08-18 |

## One-liner

> Coding-oriented MCP tool collection that appears in the emerging DSH ecosystem: give any AI agent the ability to code.

## About

Coding Tools MCP is a **model-neutral coding runtime** served over the [Model Context Protocol](https://modelcontextprotocol.io): file reading and search, structured multi-file patches, command execution, interactive sessions, and git — one server that any MCP client can drive. Claude Desktop, Claude Code, Codex, Cursor, Cline, VS Code, Windsurf, Gemini CLI, or an agent you build yourself all get the same 18 battle-tested tools, confined to one workspace, gated by permission modes.

## ✨ Key Features

- **It turns a chat app into a coding agent.** Claude Desktop — or any MCP
- **Safety is the product, not an afterthought.** One workspace root per
- **It is model- and vendor-neutral.** A fixed, truthfully annotated catalog —
- **It is engineered for context windows.** Results are summarized, paginated,

## 📦 Install

```bash
python -m pip install "coding-tools-mcp[desktop]"
coding-tools-mcp-desktop
```

## 🚀 Quick Start

```bash
python -m pip install -e ".[dev]"
make ci        # lint, typecheck, tests, protocol/integration suites, gates
```

## 📚 Learn more

**Quickstart**

Run it with whichever toolchain you already have (the server is Python ≥ 3.11 from PyPI; the npm package is a thin launcher that starts it via `uv` or `pipx`): uvx coding-tools-mcp --stdio --workspace /path/to/repo # Python toolchain npx coding-tools-mcp --stdio --workspace /path/to/repo # Node toolchain Wire it into Claude Desktop, Claude Code, Codex, Cursor, VS Code, Windsurf, Gemini CLI, or Cli

## 🔗 Links

- [GitHub Repository](https://github.com/xyTom/coding-tools-mcp)
- [Full README](https://github.com/xyTom/coding-tools-mcp#readme)
- [Back to the MCP & Integrations list](../integrations.md)
