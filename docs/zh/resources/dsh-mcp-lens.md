---
title: "dsh-mcp-lens"
description: "DeepSeek Harness MCP tool search for large catalogs: 1,000 MCP tools behind 2 MCP-facing schemas, exact-schema calls, allow/deny controls, and a local calculator."
keywords: "dsh-mcp-lens, mcp, integration, coding, search, deepseek harness, dsh"
---
# dsh-mcp-lens

> ⭐ **6** · ✅ 活跃 · 集成

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | MCP |
| 星数 | ⭐ 6 | 状态 | ✅ 活跃 |
| 作者 | [labmimors](https://github.com/labmimors) | 更新时间 | — |

## 一句话介绍

> DeepSeek Harness MCP tool search for large catalogs: 1,000 MCP tools behind 2 MCP-facing schemas, exact-schema calls, allow/deny controls, and a local calculator.

## 详细介绍

[Website](https://deepseek-harness-mcp-lens.charmingkla.chatgpt.site) · [Local schema calculator](https://labmimors.github.io/dsh-mcp-lens/) · [Install rc.9](#install) **Shrink large MCP catalogs to a two-tool model surface.** MCP Lens lets DeepSeek Harness search and call 1,000 remote tools through two stable model-facing interfaces. Instead of sending every tool schema on every turn, it reveals exact schemas only for a small ranked set when a tool is actually needed. If this keeps a large MCP catalog manageable for you, [star the repository](https://github.com/labmimors/dsh-mcp-lens) so more DeepSeek Harness users can find it. Why users install it: - Spend less on input-heavy turns: in the dated three-task pilot, estimated DeepSeek V4 Flash cost fell from `$0.0307204` to `$0.0034707`. - 

## ✨ 核心特性

- Spend less on input-heavy turns: in the dated three-task pilot, estimated DeepSeek V4 Flash cost fell from `$0.0307204` to `$0.0034707`.
- Keep more room for the real task: the same pilot reduced `request/header.tools` JSON from `674,249 B` to `27,401 B`.
- Retrieve more relevant covered calls: on a frozen MCP-Atlas-derived convenience holdout, Recall@5 rose from `0.062610` to `0.246656` across 304 untouched prompt
- Avoid rebuilding the same search index on every query: rc.9 reuses the tokenized index for each Lens-owned frozen catalog and policy generation, then invalidate
- Narrow the tool-choice surface: search reveals only a small ranked set of exact schemas, and the final `server/tool` is still gated by `allowTools` and `denyToo
- Preserve completion in the tested pilot: both arms completed `3/3` tasks, while Lens used one extra search step.

## 📦 安装

```bash
dsh plugin --profile web add dsh-mcp-lens@next
```

## 🚀 快速开始

```bash
dsh plugin --profile web add dsh-mcp-lens@0.1.0-rc.9
```

## 📚 更多信息

**Install rc.9**

Prerequisites: DeepSeek Harness `0.1.0-rc.6`, Node.js `^22.19.0` or `>=24.0.0`, and `pnpm` on `PATH`. The `dsh plugin` command delegates installation to pnpm. Fastest install: dsh plugin --profile web add dsh-mcp-lens@next For a reproducible install, pin the reviewed version: dsh plugin --profile web add dsh-mcp-lens@0.1.0-rc.9 The npm `next` tag currently resolves to `0.1.0-rc.9`. The registry ta

**Configuration reference**

Most users only need `servers`, `cachePath`, `allowTools`, and `denyTools`. The remaining fields already have bounded defaults: <details> <summary>Show all bounded defaults</summary> See the shipped [`cordis.patch.yml`](cordis.patch.yml) for the canonical defaults. </details>

## 🔗 链接

- [GitHub 仓库](https://github.com/labmimors/dsh-mcp-lens)
- [完整 README](https://github.com/labmimors/dsh-mcp-lens#readme)
- [返回dsh-mcp-lens所在分类](../integrations.md)
