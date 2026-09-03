---
title: "memos"
description: "Self-evolving memory OS for LLM & AI Agents: ultra-persistent memory, hybrid-retrieval, and cross-task skill reuse, with 35.24% token savings and DeepSeek Harness support."
keywords: "memos, learning, skill, coding, memory, multi-agent, deepseek harness, dsh"
---
# memos

> ⭐ **10,873** · ✅ active · skill · ⬆️ +34 recently

| | | | |
|---|---|---|---|
| Type | skill | Category | Learning |
| Stars | ⭐ 10,873 | Status | ✅ active |
| Author | [MemTensor](https://github.com/MemTensor) | Updated | 2026-08-21 |

## One-liner

> Self-evolving memory OS for LLM & AI Agents: ultra-persistent memory, hybrid-retrieval, and cross-task skill reuse, with 35.24% token savings and DeepSeek Harness support.

## About

**MemOS** is a Memory Operating System for LLMs and AI agents that unifies **store / retrieve / manage** for long-term memory, enabling **context-aware and personalized** interactions with **KB**, **multi-modal**, **tool memory**, and **enterprise-grade** optimizations built in.

## ✨ Key Features

- **Unified Memory API**: A single API to add, retrieve, edit, and delete memory—structured as a graph, inspectable and editable by design, not a black-box embedd
- **Multi-Modal Memory**: Natively supports text, images, tool traces, and personas, retrieved and reasoned together in one memory system.
- **Multi-Cube Knowledge Base Management**: Manage multiple knowledge bases as composable memory cubes, enabling isolation, controlled sharing, and dynamic compos
- **Asynchronous Ingestion via MemScheduler**: Run memory operations asynchronously with millisecond-level latency for production stability under high concurrency
- **Memory Feedback & Correction**: Refine memory with natural-language feedback—correcting, supplementing, or replacing existing memories over time.

## 📦 Install

```bash
git clone https://github.com/MemTensor/MemOS.git
cd MemOS
cp docker/.env.example .env          # fill in your API keys in .env
cd docker
docker compose up                    # starts MemOS API + Neo4j + Qdrant
```

## 🚀 Quick Start

```bash
git clone https://github.com/MemTensor/MemOS.git
cd MemOS
cp docker/.env.example .env          # fill in your API keys in .env
# Ensure Neo4j and Qdrant are running, then:
cd src
uvicorn memos.api.server_api:app --host 0.0.0.0 --port 8000 --workers 1
```

## 📚 Learn more

**🚀 Quick Start**

MemOS is built around four entry points. Pick the one that matches your scenario.

## 🔗 Links

- [GitHub Repository](https://github.com/MemTensor/MemOS)
- [Full README](https://github.com/MemTensor/MemOS#readme)
- [Back to the Skills list](../skills.md)
