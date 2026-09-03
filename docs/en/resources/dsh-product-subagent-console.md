---
title: "dsh-product-subagent-console"
description: "Adds a conversation-level multi-agent workbench for editable task plans, real child-session trees, plan-to-runtime comparison, and evidence-backed recovery previews."
keywords: "dsh-product-subagent-console, multi-agent, plugin, workflow, ui, observability, deepseek harness, dsh"
---
# dsh-product-subagent-console

> ⭐ **1** · 🧪 experimental · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Multi-agent |
| Stars | ⭐ 1 | Status | 🧪 experimental |
| Author | [Jokasa7](https://github.com/Jokasa7) | Updated | — |

## One-liner

> Adds a conversation-level multi-agent workbench for editable task plans, real child-session trees, plan-to-runtime comparison, and evidence-backed recovery previews.

## About

English · [简体中文](README.zh.md) From a reviewable plan to evidence-backed recovery — inside one [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) conversation. This is an independent community plugin, not an official DeepSeek Harness component. [Install](#install) · [Try it in 60 seconds](#try-it-in-60-seconds) · [Full product tour](docs/product-tour.md) · [Report an issue](https://github.com/Jokasa7/dsh-product-subagent-console/issues) DSH Product Subagent Console adds a draggable **Subagents** workbench for designing a multi-Agent run, watching the real child tree, checking what actually happened, and preparing a safe next step.

## ✨ Key Features

- Parallel code, documentation, or repository review where ownership and dependencies should stay visible.
- Phased implementation followed by independent verification or synthesis.
- Diagnosing a run that is stuck, incomplete, unexpectedly branched, or missing evidence.
- Turning a repeatedly verified workflow into a reusable starting point without auto-running it.

## 📦 Install

```bash
sha256sum --check SHA256SUMS.txt

# DSH Desktop — run in Open DSH Terminal
dsh plugin add ./dsh-product-subagent-console-0.9.0.tgz

# Regular Web profile
dsh plugin --profile web add ./dsh-product-subagent-console-0.9.0.tgz
```

## 🚀 Quick Start

```bash
- id: agent-planner
  name: dsh-product-subagent-console/plan-tool
  config:
    toolName: design_subagent_plan
    executeToolName: execute_subagent_plan
```

## 📚 Learn more

**Install**

Download the `.tgz` file and `SHA256SUMS.txt` from the matching [GitHub Release](https://github.com/Jokasa7/dsh-product-subagent-console/releases), verify the archive, and install it into your active profile: sha256sum --check SHA256SUMS.txt

## 🔗 Links

- [GitHub Repository](https://github.com/Jokasa7/dsh-product-subagent-console)
- [Full README](https://github.com/Jokasa7/dsh-product-subagent-console#readme)
- [Back to the Plugins list](../plugins.md)
