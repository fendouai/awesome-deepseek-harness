---
title: "engineer-software"
description: "Runtime-neutral, evidence-driven software engineering workflow for Codex and DeepSeek Harness."
keywords: "engineer-software, workflow, coding, deepseek harness, dsh"
---
# engineer-software

> ⭐ **6** · ✅ active · workflow

| | | | |
|---|---|---|---|
| Type | workflow | Category | Workflows |
| Stars | ⭐ 6 | Status | ✅ active |
| Author | [KirschBluteX](https://github.com/KirschBluteX) | Updated | 2026-08-15 |

## One-liner

> Runtime-neutral, evidence-driven software engineering workflow for Codex and DeepSeek Harness.

## About

**A runtime-neutral, evidence-driven software engineering workflow for AI coding agents.** Choose the smallest trustworthy engineering move before changing code. [Six workflows](#six-workflows) · [How it works](#how-it-works) · [Real examples](#real-examples) · [Quick start](#quick-start) · [Validation](#validation) · [简体中文](README.zh-CN.md) Engineer Software gives Codex and DeepSeek Harness two runtime entries into one canonical workflow. For substantive software work, it selects exactly one bounded engineering mode and defines the evidence required before an agent can change direction or claim completion. **At a glance:** 6 bounded workflows · 25 deterministic routing cases · 2 runtime paths · 1 canonical source **Use it when** requirements, failure mechanisms, design choices, implementa

## 📦 Install

```bash
python scripts/sync_harness_skill.py --check
python scripts/validate_harness.py --check
npx @deepseek-ai/dsh web
```

## 🚀 Quick Start

```bash
git pull --ff-only
python scripts/sync_harness_skill.py --write
python scripts/validate_harness.py --check
```

## 📚 Learn more

**Real examples**

Each example follows the same shape: prompt → route → evidence required to proceed. **Trace Failure** → reproduce the symptom, establish the cause, then add a focused regression. **Probe Choice** → observe the named trade-off and record the decision consequence. contract.” → **Deliver Change** → implement the closed contract and verify the final state. without adding workflow overhead. These examp

**Contributing and roadmap**

Start with [CONTRIBUTING.md](CONTRIBUTING.md). Keep `plugins/engineer-software/skills/engineer-software/` as the only editable workflow source, run the projection check after changes, and add routing fixtures for new transitions. [ROADMAP.md](ROADMAP.md) records the deliberately small next steps; it does not promise a long-lived adapter framework.

## 🔗 Links

- [GitHub Repository](https://github.com/KirschBluteX/engineer-software)
- [Full README](https://github.com/KirschBluteX/engineer-software#readme)
- [Back to the Workflows & Automation list](../workflows.md)
