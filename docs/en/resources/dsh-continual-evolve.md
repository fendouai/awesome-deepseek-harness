---
title: "dsh-continual-evolve"
description: "Continual self-evolution plugin for DeepSeek Harness: versioned, auditable, rollback-safe harness state refined from session trajectories, with a benchmark-driven validation loop."
keywords: "dsh-continual-evolve, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-continual-evolve

> ⭐ **16** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 16 | Status | ✅ active |
| Author | [ZK-Andy](https://github.com/ZK-Andy) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> Continual self-evolution plugin for DeepSeek Harness: versioned, auditable, rollback-safe harness state refined from session trajectories, with a benchmark-driven validation loop.

## About

[中文](README.zh.md) | English Continual self-evolution for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness): a versioned, auditable, rollback-safe harness state layer — prompt notes, memories, skills, subagent specs — refined from session trajectories. **The model proposes, the code guarantees.** Every mechanical safety property — schema validation, atomic writes, snapshots, versioning, audit trail, acceptance decisions — is enforced in code, never by prompt discipline.

## ✨ Key Features

- **Local scope** per session; **global scope** across sessions with merge semantics — plus mechanical promotion guards so only portable, substantial, non-duplica
- **Deterministic rollback**: inverse edits generated from applied results — no LLM re-guessing
- **Benchmark loop**: candidate refinements are evaluated against frozen cases by a separate scorer before acceptance (rubric encrypted at rest)
- **Store hygiene**: `/evolve consolidate` turns write-time conflict hints and zero-use staleness into one approved, fully reversible batch of archives — with `me

## 📦 Install

```bash
# from npm (installs and activates — ships its own bundle patch)
dsh plugin add dsh-continual-evolve

# or from source (first GitHub installs require approving the allowBuilds step)
dsh plugin add ZK-Andy/dsh-continual-evolve
```

## 🚀 Quick Start

```bash
- id: continual-evolve
  config:
    autoReview: true
    reviewIntervalTurns: 6
```

## 📚 Learn more

**or from source (first GitHub installs require approving the **

dsh plugin add ZK-Andy/dsh-continual-evolve Restart `dsh web` after installing or updating.

**Usage**

Commands (in-session): Model tools: `evolve_list / add / update / delete / rollback`. For third-party consumers: every applied evolution (gate or manual) appends a structured `evolve_complete` event to `reviews.jsonl` (`src/evolve-event.ts` defines the shape) alongside the human-readable audit records. Injection shape: prompt notes and delegation specs inject with content (≤6/kind × 180 chars, rel

## 🔗 Links

- [GitHub Repository](https://github.com/ZK-Andy/dsh-continual-evolve)
- [Full README](https://github.com/ZK-Andy/dsh-continual-evolve#readme)
- [Back to the Plugins list](../plugins.md)
