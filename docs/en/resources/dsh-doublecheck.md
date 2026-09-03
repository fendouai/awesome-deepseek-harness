---
title: "dsh-doublecheck"
description: "Engineering-discipline loop: requirement grilling before edits, red/green test-evidence gates and adversarial delivery review."
keywords: "dsh-doublecheck, workflow, coding, deepseek harness, dsh"
---
# dsh-doublecheck

> ⭐ **4** · ✅ active · workflow · ⬆️ +2 recently

| | | | |
|---|---|---|---|
| Type | workflow | Category | Workflows |
| Stars | ⭐ 4 | Status | ✅ active |
| Author | [PerryLink](https://github.com/PerryLink) | Updated | 2026-08-21 |

## One-liner

> Engineering-discipline loop: requirement grilling before edits, red/green test-evidence gates and adversarial delivery review.

## About

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-doublecheck` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **The delivery quality gate for DeepSeek Harness: grill the requirements, test the implementation, prove the delivery — then gate the handoff with a deliverable/rework decision.** *Requirements get interrogated before the first edit; delivery is proven, never claimed.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ Key Features

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-doublecheck` (counts toward the [deepseek1024.com](https://deepseek1

## 📦 Install

```bash
# 1. install the bundle into your profile
dsh plugin --profile web add "github:PerryLink/dsh-doublecheck#main"

# or from npm (published releases)
dsh plugin --profile web add dsh-doublecheck

# 2. restart and verify the row
dsh --profile web --dump-config | grep -E -A3 'id: doublecheck-(grill|guard)'
```

## 🚀 Quick Start

```bash
# JSON (PR comment / status payload)
doublecheck-gate --format json --input gate-report.json
# SARIF 2.1.0 (code-scanning upload / status check)
doublecheck-gate --format sarif < gate-report.json
```

## 📚 Learn more

**Install & uninstall**

For a zero-configuration strict mode (every gate on at `block` intensity, gate coverage required), apply the shipped overlay on top of the bundle patch: `dsh --profile web --patch ./node_modules/dsh-doublecheck/strict.patch.yml`.

**Configuration**

All tunables are Schemastery `Config` fields (changeable from cordis.yml). An id-targeted override replaces the whole row — restate every key you need. `cordis.patch.yml` documents each key inline; Schema defaults are the single source of tuning defaults. Misconfiguration fails loud at load: invalid regexes, empty or duplicated name lists, out-of-range thresholds, and duplicate checklist ids throw

## 🔗 Links

- [GitHub Repository](https://github.com/PerryLink/dsh-doublecheck)
- [Full README](https://github.com/PerryLink/dsh-doublecheck#readme)
- [Back to the Workflows & Automation list](../workflows.md)
