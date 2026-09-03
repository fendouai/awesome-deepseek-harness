---
title: "engineer-software"
description: "与运行时无关、证据驱动的软件工程工作流，适用于 Codex 与 DeepSeek Harness。"
keywords: "engineer-software, workflow, coding, deepseek harness, dsh"
---
# engineer-software

> ⭐ **6** · ✅ 活跃 · 工作流

| | | | |
|---|---|---|---|
| 类型 | 工作流 | 分类 | 工作流 |
| 星数 | ⭐ 6 | 状态 | ✅ 活跃 |
| 作者 | [KirschBluteX](https://github.com/KirschBluteX) | 更新时间 | 2026-08-15 |

## 一句话介绍

> 与运行时无关、证据驱动的软件工程工作流，适用于 Codex 与 DeepSeek Harness。

## 详细介绍

**A runtime-neutral, evidence-driven software engineering workflow for AI coding agents.** Choose the smallest trustworthy engineering move before changing code. [Six workflows](#six-workflows) · [How it works](#how-it-works) · [Real examples](#real-examples) · [Quick start](#quick-start) · [Validation](#validation) · [简体中文](README.zh-CN.md) Engineer Software gives Codex and DeepSeek Harness two runtime entries into one canonical workflow. For substantive software work, it selects exactly one bounded engineering mode and defines the evidence required before an agent can change direction or claim completion. **At a glance:** 6 bounded workflows · 25 deterministic routing cases · 2 runtime paths · 1 canonical source **Use it when** requirements, failure mechanisms, design choices, implementa

## 📦 安装

```bash
python scripts/sync_harness_skill.py --check
python scripts/validate_harness.py --check
npx @deepseek-ai/dsh web
```

## 🚀 快速开始

```bash
git pull --ff-only
python scripts/sync_harness_skill.py --write
python scripts/validate_harness.py --check
```

## 📚 更多信息

**Real examples**

Each example follows the same shape: prompt → route → evidence required to proceed. **Trace Failure** → reproduce the symptom, establish the cause, then add a focused regression. **Probe Choice** → observe the named trade-off and record the decision consequence. contract.” → **Deliver Change** → implement the closed contract and verify the final state. without adding workflow overhead. These examp

**Contributing and roadmap**

Start with [CONTRIBUTING.md](CONTRIBUTING.md). Keep `plugins/engineer-software/skills/engineer-software/` as the only editable workflow source, run the projection check after changes, and add routing fixtures for new transitions. [ROADMAP.md](ROADMAP.md) records the deliberately small next steps; it does not promise a long-lived adapter framework.

## 🔗 链接

- [GitHub 仓库](https://github.com/KirschBluteX/engineer-software)
- [完整 README](https://github.com/KirschBluteX/engineer-software#readme)
- [返回engineer-software所在分类](../workflows.md)
