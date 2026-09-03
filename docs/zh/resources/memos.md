---
title: "memos"
description: "Self-evolving memory OS for LLM & AI Agents: ultra-persistent memory, hybrid-retrieval, and cross-task skill reuse, with 35.24% token savings and DeepSeek Harness support."
keywords: "memos, learning, skill, coding, memory, multi-agent, deepseek harness, dsh"
---
# memos

> ⭐ **10,873** · ✅ 活跃 · 技能 · 近期 ⬆️ +34

| | | | |
|---|---|---|---|
| 类型 | 技能 | 分类 | 学习 |
| 星数 | ⭐ 10,873 | 状态 | ✅ 活跃 |
| 作者 | [MemTensor](https://github.com/MemTensor) | 更新时间 | 2026-08-21 |

## 一句话介绍

> Self-evolving memory OS for LLM & AI Agents: ultra-persistent memory, hybrid-retrieval, and cross-task skill reuse, with 35.24% token savings and DeepSeek Harness support.

## 详细介绍

**MemOS** is a Memory Operating System for LLMs and AI agents that unifies **store / retrieve / manage** for long-term memory, enabling **context-aware and personalized** interactions with **KB**, **multi-modal**, **tool memory**, and **enterprise-grade** optimizations built in.

## ✨ 核心特性

- **Unified Memory API**: A single API to add, retrieve, edit, and delete memory—structured as a graph, inspectable and editable by design, not a black-box embedd
- **Multi-Modal Memory**: Natively supports text, images, tool traces, and personas, retrieved and reasoned together in one memory system.
- **Multi-Cube Knowledge Base Management**: Manage multiple knowledge bases as composable memory cubes, enabling isolation, controlled sharing, and dynamic compos
- **Asynchronous Ingestion via MemScheduler**: Run memory operations asynchronously with millisecond-level latency for production stability under high concurrency
- **Memory Feedback & Correction**: Refine memory with natural-language feedback—correcting, supplementing, or replacing existing memories over time.

## 📦 安装

```bash
git clone https://github.com/MemTensor/MemOS.git
cd MemOS
cp docker/.env.example .env          # fill in your API keys in .env
cd docker
docker compose up                    # starts MemOS API + Neo4j + Qdrant
```

## 🚀 快速开始

```bash
git clone https://github.com/MemTensor/MemOS.git
cd MemOS
cp docker/.env.example .env          # fill in your API keys in .env
# Ensure Neo4j and Qdrant are running, then:
cd src
uvicorn memos.api.server_api:app --host 0.0.0.0 --port 8000 --workers 1
```

## 📚 更多信息

**🚀 Quick Start**

MemOS is built around four entry points. Pick the one that matches your scenario.

## 🔗 链接

- [GitHub 仓库](https://github.com/MemTensor/MemOS)
- [完整 README](https://github.com/MemTensor/MemOS#readme)
- [返回memos所在分类](../skills.md)
