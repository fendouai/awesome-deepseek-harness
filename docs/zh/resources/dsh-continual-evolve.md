---
title: "dsh-continual-evolve"
description: "Continual self-evolution plugin for DeepSeek Harness: versioned, auditable, rollback-safe harness state refined from session trajectories, with a benchmark-driven validation loop."
keywords: "dsh-continual-evolve, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-continual-evolve

> ⭐ **16** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 16 | 状态 | ✅ 活跃 |
| 作者 | [ZK-Andy](https://github.com/ZK-Andy) | 更新时间 | — |
| 子分类 | 👁️ 视觉工具 | 能力 | coding |

## 一句话介绍

> Continual self-evolution plugin for DeepSeek Harness: versioned, auditable, rollback-safe harness state refined from session trajectories, with a benchmark-driven validation loop.

## 详细介绍

[中文](README.zh.md) | English Continual self-evolution for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness): a versioned, auditable, rollback-safe harness state layer — prompt notes, memories, skills, subagent specs — refined from session trajectories. **The model proposes, the code guarantees.** Every mechanical safety property — schema validation, atomic writes, snapshots, versioning, audit trail, acceptance decisions — is enforced in code, never by prompt discipline.

## ✨ 核心特性

- **Local scope** per session; **global scope** across sessions with merge semantics — plus mechanical promotion guards so only portable, substantial, non-duplica
- **Deterministic rollback**: inverse edits generated from applied results — no LLM re-guessing
- **Benchmark loop**: candidate refinements are evaluated against frozen cases by a separate scorer before acceptance (rubric encrypted at rest)
- **Store hygiene**: `/evolve consolidate` turns write-time conflict hints and zero-use staleness into one approved, fully reversible batch of archives — with `me

## 📦 安装

```bash
# from npm (installs and activates — ships its own bundle patch)
dsh plugin add dsh-continual-evolve

# or from source (first GitHub installs require approving the allowBuilds step)
dsh plugin add ZK-Andy/dsh-continual-evolve
```

## 🚀 快速开始

```bash
- id: continual-evolve
  config:
    autoReview: true
    reviewIntervalTurns: 6
```

## 📚 更多信息

**or from source (first GitHub installs require approving the **

dsh plugin add ZK-Andy/dsh-continual-evolve Restart `dsh web` after installing or updating.

**Usage**

Commands (in-session): Model tools: `evolve_list / add / update / delete / rollback`. For third-party consumers: every applied evolution (gate or manual) appends a structured `evolve_complete` event to `reviews.jsonl` (`src/evolve-event.ts` defines the shape) alongside the human-readable audit records. Injection shape: prompt notes and delegation specs inject with content (≤6/kind × 180 chars, rel

## 🔗 链接

- [GitHub 仓库](https://github.com/ZK-Andy/dsh-continual-evolve)
- [完整 README](https://github.com/ZK-Andy/dsh-continual-evolve#readme)
- [返回dsh-continual-evolve所在分类](../plugins.md)
