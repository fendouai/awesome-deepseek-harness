---
title: "dsh-cowork"
description: "READ + WRITE for office documents & notebooks in DeepSeek Harness — doc_read/doc_write tools (xlsx, pdf, docx, pptx, ipynb) plus MCP server and CLI"
keywords: "dsh-cowork, mcp, integration, coding, deepseek harness, dsh"
---
# dsh-cowork

> ⭐ **5** · ✅ active · integration

| | | | |
|---|---|---|---|
| Type | integration | Category | MCP |
| Stars | ⭐ 5 | Status | ✅ active |
| Author | [Jesse-njx](https://github.com/Jesse-njx) | Updated | — |

## One-liner

> READ + WRITE for office documents & notebooks in DeepSeek Harness — doc_read/doc_write tools (xlsx, pdf, docx, pptx, ipynb) plus MCP server and CLI

## About

**READ + WRITE for office documents and Jupyter notebooks inside [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) — and anywhere else your agent runs.** DSH Cowork adds first-class document handling to coding agents: **中文版见 [README.zh.md](README.zh.md).**

## 📦 Install

```bash
# GitHub delivery (not published to npm)
git clone https://github.com/Jesse-njx/dsh-cowork.git
cd dsh-cowork
pnpm install          # installs deps and builds all packages (prepare)
dsh plugin --profile <your-profile> add ./packages/dsh
```

## 🚀 Quick Start

```bash
# Codex / Claude Code MCP config
# { "mcpServers": { "cowork": { "command": "node", "args": ["<repo>/packages/mcp/lib/index.js"], "cwd": "<your working dir>" } } }
```

## 📚 Learn more

**Architecture**

┌──────────────────────────────────────────────┐ │ @dsh-cowork/core │ │ sniff → readDocument / writeDocument → caps │ └───────┬──────────────┬──────────────┬────────┘ │ │ │ ┌──────────▼───┐ ┌───────▼──────┐ ┌────▼───────┐ │ packages/dsh│ │ packages/mcp │ │ packages/cli│ │ DSH bundle │ │ MCP stdio │ │ + SKILL.md │ └──────────────┘ └──────────────┘ └────────────┘ The DSH bundle routes reads through 

## 🔗 Links

- [GitHub Repository](https://github.com/Jesse-njx/dsh-cowork)
- [Full README](https://github.com/Jesse-njx/dsh-cowork#readme)
- [Back to the MCP & Integrations list](../integrations.md)
