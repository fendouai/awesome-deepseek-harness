---
title: "Coding Tools MCP"
description: "面向编码的 MCP 工具集：让任何 AI Agent 获得编码能力。"
keywords: "Coding Tools MCP, mcp, integration, coding, deepseek harness, dsh"
---
# Coding Tools MCP

> ⭐ **846** · ✅ 活跃 · 集成 · 近期 ⬆️ +5

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | MCP |
| 星数 | ⭐ 846 | 状态 | ✅ 活跃 |
| 作者 | [xyTom](https://github.com/xyTom) | 更新时间 | 2026-08-18 |

## 一句话介绍

> 面向编码的 MCP 工具集：让任何 AI Agent 获得编码能力。

## 详细介绍

Coding Tools MCP is a **model-neutral coding runtime** served over the [Model Context Protocol](https://modelcontextprotocol.io): file reading and search, structured multi-file patches, command execution, interactive sessions, and git — one server that any MCP client can drive. Claude Desktop, Claude Code, Codex, Cursor, Cline, VS Code, Windsurf, Gemini CLI, or an agent you build yourself all get the same 18 battle-tested tools, confined to one workspace, gated by permission modes.

## ✨ 核心特性

- **It turns a chat app into a coding agent.** Claude Desktop — or any MCP
- **Safety is the product, not an afterthought.** One workspace root per
- **It is model- and vendor-neutral.** A fixed, truthfully annotated catalog —
- **It is engineered for context windows.** Results are summarized, paginated,

## 📦 安装

```bash
python -m pip install "coding-tools-mcp[desktop]"
coding-tools-mcp-desktop
```

## 🚀 快速开始

```bash
python -m pip install -e ".[dev]"
make ci        # lint, typecheck, tests, protocol/integration suites, gates
```

## 📚 更多信息

**Quickstart**

Run it with whichever toolchain you already have (the server is Python ≥ 3.11 from PyPI; the npm package is a thin launcher that starts it via `uv` or `pipx`): uvx coding-tools-mcp --stdio --workspace /path/to/repo # Python toolchain npx coding-tools-mcp --stdio --workspace /path/to/repo # Node toolchain Wire it into Claude Desktop, Claude Code, Codex, Cursor, VS Code, Windsurf, Gemini CLI, or Cli

## 🔗 链接

- [GitHub 仓库](https://github.com/xyTom/coding-tools-mcp)
- [完整 README](https://github.com/xyTom/coding-tools-mcp#readme)
- [返回Coding Tools MCP所在分类](../integrations.md)
