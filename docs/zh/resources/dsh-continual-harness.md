---
title: "dsh-continual-harness"
description: "DeepSeek Harness plugin for continual self-evolution: persistent memory, periodic review-and-refine, cross-session shared knowledge, and automatic rollback — a plan→validate→apply→rollback loop driven by a model-callable harness_refine tool."
keywords: "dsh-continual-harness, workflow, coding, memory, deepseek harness, dsh"
---
# dsh-continual-harness

> ⭐ **4** · ✅ 活跃 · 工作流

| | | | |
|---|---|---|---|
| 类型 | 工作流 | 分类 | 工作流 |
| 星数 | ⭐ 4 | 状态 | ✅ 活跃 |
| 作者 | [jasen215](https://github.com/jasen215) | 更新时间 | 2026-08-20 |

## 一句话介绍

> DeepSeek Harness plugin for continual self-evolution: persistent memory, periodic review-and-refine, cross-session shared knowledge, and automatic rollback — a plan→validate→apply→rollback loop driven by a model-callable harness_refine tool.

## 详细介绍

A **DeepSeek Harness (DSH) plugin for self-improving AI agents**, providing continual learning through persistent memory, periodic review and refinement, cross-session knowledge sharing, and automatic rollback on failure. It forms a closed loop of plan → validate → apply → rollback. The design is inspired by the open-source [prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) from Prime Intellect, a self-improving coding harness.

## 📦 安装

```bash
dsh plugin --profile <name> add dsh-continual-harness
```

## 🚀 快速开始

```bash
- insert:
    - id: continual-harness
      name: dsh-continual-harness
      config:
        defaultGlobal: true
```

## 📚 更多信息

**Architecture**

src/ domain.ts event declaration merging (SessionEventMap / MessageSourceMap / cordis Events) types.ts HarnessState / RefinementProposal / RefinementResult and other types storage.ts disk read/write of state and history (atomic writes, corruption degradation, local/global merge, jsonl history) refine.ts validation, application, rollback (baseline conflict detection, version increments, growth limi

## 🔗 链接

- [GitHub 仓库](https://github.com/jasen215/dsh-continual-harness)
- [完整 README](https://github.com/jasen215/dsh-continual-harness#readme)
- [返回dsh-continual-harness所在分类](../workflows.md)
