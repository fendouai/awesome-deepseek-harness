---
title: "dsh-continual-harness"
description: "DeepSeek Harness plugin for continual self-evolution: persistent memory, periodic review-and-refine, cross-session shared knowledge, and automatic rollback — a plan→validate→apply→rollback loop driven by a model-callable harness_refine tool."
keywords: "dsh-continual-harness, workflow, coding, memory, deepseek harness, dsh"
---
# dsh-continual-harness

> ⭐ **4** · ✅ active · workflow

| | | | |
|---|---|---|---|
| Type | workflow | Category | Workflows |
| Stars | ⭐ 4 | Status | ✅ active |
| Author | [jasen215](https://github.com/jasen215) | Updated | 2026-08-20 |

## One-liner

> DeepSeek Harness plugin for continual self-evolution: persistent memory, periodic review-and-refine, cross-session shared knowledge, and automatic rollback — a plan→validate→apply→rollback loop driven by a model-callable harness_refine tool.

## About

A **DeepSeek Harness (DSH) plugin for self-improving AI agents**, providing continual learning through persistent memory, periodic review and refinement, cross-session knowledge sharing, and automatic rollback on failure. It forms a closed loop of plan → validate → apply → rollback. The design is inspired by the open-source [prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) from Prime Intellect, a self-improving coding harness.

## 📦 Install

```bash
dsh plugin --profile <name> add dsh-continual-harness
```

## 🚀 Quick Start

```bash
- insert:
    - id: continual-harness
      name: dsh-continual-harness
      config:
        defaultGlobal: true
```

## 📚 Learn more

**Architecture**

src/ domain.ts event declaration merging (SessionEventMap / MessageSourceMap / cordis Events) types.ts HarnessState / RefinementProposal / RefinementResult and other types storage.ts disk read/write of state and history (atomic writes, corruption degradation, local/global merge, jsonl history) refine.ts validation, application, rollback (baseline conflict detection, version increments, growth limi

## 🔗 Links

- [GitHub Repository](https://github.com/jasen215/dsh-continual-harness)
- [Full README](https://github.com/jasen215/dsh-continual-harness#readme)
- [Back to the Workflows & Automation list](../workflows.md)
