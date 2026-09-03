---
title: "mnemon"
description: "LLM 监督的 Agent 持久记忆：图召回与跨会话知识，单二进制。"
keywords: "mnemon, harness, related, memory, deepseek harness, dsh"
---
# mnemon

> ⭐ **500** · ✅ 活跃 · 相关 · 近期 ⬆️ +6

| | | | |
|---|---|---|---|
| 类型 | 相关 | 分类 | Harness |
| 星数 | ⭐ 500 | 状态 | ✅ 活跃 |
| 作者 | [mnemon-dev](https://github.com/mnemon-dev) | 更新时间 | 2026-08-21 |

## 一句话介绍

> LLM 监督的 Agent 持久记忆：图召回与跨会话知识，单二进制。

## 详细介绍

**LLM-supervised persistent memory for AI agents.** --- LLM agents forget everything between sessions. Context compaction drops critical decisions, cross-session knowledge vanishes, and long conversations push early information out of the window. Mnemon gives your agent persistent, cross-session memory — a four-graph knowledge store with intent-aware recall, importance decay, and automatic deduplication. The `mnemon` memory path remains one local binary with zero API keys and one setup command. Mnemon ships one executable with two separate surfaces. Memory stays at the `mnemon` root; [Agency Preview](docs/AGENCY.md) lives at `mnemon agency ...` and adds durable, project-local responsibility and effect admission to an existing Pi agent. Agency does not replace Memory or the Agent Runtime.

## ✨ 核心特性

- **Zero user-side operation** — install once; supported runtimes can use hooks, minimal runtimes can use persistent rules
- **LLM-supervised** — the host LLM decides what to remember, update, and forget; no embedded LLM, no API keys
- **Multi-framework support** — Claude Code, Codex, Cursor, ZCode, TRAE/TRAE Work, Qoder/QoderWork, CodeBuddy, WorkBuddy, Kimi Code, OpenCode, and Hermes Agent (h
- **Runtime-native integration** — runtime-specific `SKILL.md`, shared `guide.md`, and supported hooks or extensions
- **Four-graph architecture** — temporal, entity, causal, and semantic edges, not just vector similarity
- **Intent-native protocol** — three primitives (`remember`, `link`, `recall`) map to the LLM's cognitive vocabulary, not database syntax; structured JSON output 
- **Intent-aware recall** — graph traversal + optional vector search (RRF fusion), enabled by default for all queries
- **Built-in deduplication** — `remember` auto-detects duplicates and conflicts; skips or auto-replaces

## 📦 安装

```bash
brew install --cask mnemon-dev/tap/mnemon
```

## 🚀 快速开始

```bash
go install github.com/mnemon-dev/mnemon@latest
```

## 📚 更多信息

**Install**

**Homebrew Cask** (macOS): brew install --cask mnemon-dev/tap/mnemon **Go install** (macOS / Linux / Windows): go install github.com/mnemon-dev/mnemon@latest Windows supports the core Memory commands. Agency remains unavailable on Windows until its local authority boundary has native Windows security. **From source** (macOS / Linux): git clone https://github.com/mnemon-dev/mnemon.git && cd mnemon 

**FAQ**

**Do different sessions share memory?** Yes. By default, all sessions use the same `default` store — a decision remembered in one session is available in every future session. **Can I isolate memory per project or agent?** Yes. Use named stores to separate memory: mnemon store create work # create a new store mnemon store set work # set as default MNEMON_STORE=work mnemon recall "query" # or use e

**Configuration**

**Retention**: Each automatic deletion is soft, appears in the oplog as a `prune` operation, and is reported by ID in the triggering command's `auto_pruned_ids` field. **Embedding** (only relevant if using embeddings): The embedding client speaks the Ollama API by default and the OpenAI-compatible embeddings API when the endpoint ends in `/v1` (or when `MNEMON_EMBED_PROTOCOL=openai` is set). For e

## 🔗 链接

- [GitHub 仓库](https://github.com/mnemon-dev/mnemon)
- [完整 README](https://github.com/mnemon-dev/mnemon#readme)
- [返回mnemon所在分类](../related.md)
