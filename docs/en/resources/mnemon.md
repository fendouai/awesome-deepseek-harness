---
title: "mnemon"
description: "LLM-supervised persistent memory for AI agents: graph-based recall and cross-session knowledge in a single binary."
keywords: "mnemon, harness, related, memory, deepseek harness, dsh"
---
# mnemon

> ⭐ **500** · ✅ active · related · ⬆️ +6 recently

| | | | |
|---|---|---|---|
| Type | related | Category | Harness |
| Stars | ⭐ 500 | Status | ✅ active |
| Author | [mnemon-dev](https://github.com/mnemon-dev) | Updated | 2026-08-21 |

## One-liner

> LLM-supervised persistent memory for AI agents: graph-based recall and cross-session knowledge in a single binary.

## About

**LLM-supervised persistent memory for AI agents.** --- LLM agents forget everything between sessions. Context compaction drops critical decisions, cross-session knowledge vanishes, and long conversations push early information out of the window. Mnemon gives your agent persistent, cross-session memory — a four-graph knowledge store with intent-aware recall, importance decay, and automatic deduplication. The `mnemon` memory path remains one local binary with zero API keys and one setup command. Mnemon ships one executable with two separate surfaces. Memory stays at the `mnemon` root; [Agency Preview](docs/AGENCY.md) lives at `mnemon agency ...` and adds durable, project-local responsibility and effect admission to an existing Pi agent. Agency does not replace Memory or the Agent Runtime.

## ✨ Key Features

- **Zero user-side operation** — install once; supported runtimes can use hooks, minimal runtimes can use persistent rules
- **LLM-supervised** — the host LLM decides what to remember, update, and forget; no embedded LLM, no API keys
- **Multi-framework support** — Claude Code, Codex, Cursor, ZCode, TRAE/TRAE Work, Qoder/QoderWork, CodeBuddy, WorkBuddy, Kimi Code, OpenCode, and Hermes Agent (h
- **Runtime-native integration** — runtime-specific `SKILL.md`, shared `guide.md`, and supported hooks or extensions
- **Four-graph architecture** — temporal, entity, causal, and semantic edges, not just vector similarity
- **Intent-native protocol** — three primitives (`remember`, `link`, `recall`) map to the LLM's cognitive vocabulary, not database syntax; structured JSON output 
- **Intent-aware recall** — graph traversal + optional vector search (RRF fusion), enabled by default for all queries
- **Built-in deduplication** — `remember` auto-detects duplicates and conflicts; skips or auto-replaces

## 📦 Install

```bash
brew install --cask mnemon-dev/tap/mnemon
```

## 🚀 Quick Start

```bash
go install github.com/mnemon-dev/mnemon@latest
```

## 📚 Learn more

**Install**

**Homebrew Cask** (macOS): brew install --cask mnemon-dev/tap/mnemon **Go install** (macOS / Linux / Windows): go install github.com/mnemon-dev/mnemon@latest Windows supports the core Memory commands. Agency remains unavailable on Windows until its local authority boundary has native Windows security. **From source** (macOS / Linux): git clone https://github.com/mnemon-dev/mnemon.git && cd mnemon 

**FAQ**

**Do different sessions share memory?** Yes. By default, all sessions use the same `default` store — a decision remembered in one session is available in every future session. **Can I isolate memory per project or agent?** Yes. Use named stores to separate memory: mnemon store create work # create a new store mnemon store set work # set as default MNEMON_STORE=work mnemon recall "query" # or use e

**Configuration**

**Retention**: Each automatic deletion is soft, appears in the oplog as a `prune` operation, and is reported by ID in the triggering command's `auto_pruned_ids` field. **Embedding** (only relevant if using embeddings): The embedding client speaks the Ollama API by default and the OpenAI-compatible embeddings API when the endpoint ends in `/v1` (or when `MNEMON_EMBED_PROTOCOL=openai` is set). For e

## 🔗 Links

- [GitHub Repository](https://github.com/mnemon-dev/mnemon)
- [Full README](https://github.com/mnemon-dev/mnemon#readme)
- [Back to the Related Agent Harnesses list](../related.md)
