---
title: "dsh-eval"
description: "Agent evaluation platform: benchmark YAML, headless dsh runs, trace-based metrics, scripted grading and run comparison."
keywords: "dsh-eval, research, workflow, observability, deepseek harness, dsh"
---
# dsh-eval

> ⭐ **1** · ✅ active · workflow · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | workflow | Category | Research |
| Stars | ⭐ 1 | Status | ✅ active |
| Author | [hccccc01333](https://github.com/hccccc01333) | Updated | 2026-08-14 |

## One-liner

> Agent evaluation platform: benchmark YAML, headless dsh runs, trace-based metrics, scripted grading and run comparison.

## About

**Agent Evaluation Platform for [deepseek-harness](https://github.com/deepseek-ai/deepseek-harness).** Run benchmarks against headless `dsh` profiles, harvest persisted session logs as traces, fold automatic metrics, grade task success and tool selection, and report or compare runs — one `benchmark.yaml` in, one JSON run + Markdown report out.

## ✨ Key Features

- `dsh eval run benchmark.yaml` — orchestrate one headless `dsh` subprocess per case × trial
- Trace harvesting from persisted session logs (everything a model sees is reconstructable from the log)
- Automatic metrics: task success, tool success, tool-selection accuracy, steps, tokens, latency, cost, retry, invalid tool calls, context usage
- Scripted grading: `expected.tool` (tool-selection accuracy) and `expected.check` (task success)
- LLM judge: final-answer score and hallucination flags from a judge model
- Subagent trace merging: child session logs fold into the trial metrics

## 📦 Install

```bash
pnpm add dsh-eval
dsh plugin --profile eval add dsh-eval
```

## 🚀 Quick Start

```bash
git clone https://github.com/hccccc01333/dsh-eval.git
cd dsh-eval
```

## 📚 Learn more

**Quick start**

Install the package directly: pnpm add dsh-eval dsh plugin --profile eval add dsh-eval The npm package targets the official `@deepseek-ai/*` releases (`0.1.0-rc.6` peers). For the source flow, clone this repo and link it to a deepseek-harness checkout: git clone https://github.com/hccccc01333/dsh-eval.git cd dsh-eval Windows (junction): New-Item -ItemType Junction -Path harness -Target D:\path\to\

## 🔗 Links

- [GitHub Repository](https://github.com/hccccc01333/dsh-eval)
- [Full README](https://github.com/hccccc01333/dsh-eval#readme)
- [Back to the Workflows & Automation list](../workflows.md)
