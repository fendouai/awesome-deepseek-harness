---
title: "dsh-cowork"
description: "READ + WRITE for office documents & notebooks in DeepSeek Harness — doc_read/doc_write tools (xlsx, pdf, docx, pptx, ipynb) plus MCP server and CLI"
keywords: "dsh-cowork, mcp, integration, coding, deepseek harness, dsh"
---
# dsh-cowork

> ⭐ **5** · ✅ 活跃 · 集成

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | MCP |
| 星数 | ⭐ 5 | 状态 | ✅ 活跃 |
| 作者 | [Jesse-njx](https://github.com/Jesse-njx) | 更新时间 | — |

## 一句话介绍

> READ + WRITE for office documents & notebooks in DeepSeek Harness — doc_read/doc_write tools (xlsx, pdf, docx, pptx, ipynb) plus MCP server and CLI

## 详细介绍

**READ + WRITE for office documents and Jupyter notebooks inside [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) — and anywhere else your agent runs.** DSH Cowork adds first-class document handling to coding agents: **中文版见 [README.zh.md](README.zh.md).**

## 📦 安装

```bash
# GitHub delivery (not published to npm)
git clone https://github.com/Jesse-njx/dsh-cowork.git
cd dsh-cowork
pnpm install          # installs deps and builds all packages (prepare)
dsh plugin --profile <your-profile> add ./packages/dsh
```

## 🚀 快速开始

```bash
# Codex / Claude Code MCP config
# { "mcpServers": { "cowork": { "command": "node", "args": ["<repo>/packages/mcp/lib/index.js"], "cwd": "<your working dir>" } } }
```

## 📚 更多信息

**Architecture**

┌──────────────────────────────────────────────┐ │ @dsh-cowork/core │ │ sniff → readDocument / writeDocument → caps │ └───────┬──────────────┬──────────────┬────────┘ │ │ │ ┌──────────▼───┐ ┌───────▼──────┐ ┌────▼───────┐ │ packages/dsh│ │ packages/mcp │ │ packages/cli│ │ DSH bundle │ │ MCP stdio │ │ + SKILL.md │ └──────────────┘ └──────────────┘ └────────────┘ The DSH bundle routes reads through 

## 🔗 链接

- [GitHub 仓库](https://github.com/Jesse-njx/dsh-cowork)
- [完整 README](https://github.com/Jesse-njx/dsh-cowork#readme)
- [返回dsh-cowork所在分类](../integrations.md)
