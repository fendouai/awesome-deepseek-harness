---
title: "dsh-eval"
description: "Agent 评测平台：benchmark YAML、无头 dsh 运行、基于 trace 的指标、脚本评分与运行对比。"
keywords: "dsh-eval, research, workflow, observability, deepseek harness, dsh"
---
# dsh-eval

> ⭐ **1** · ✅ 活跃 · 工作流 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 工作流 | 分类 | 研究 |
| 星数 | ⭐ 1 | 状态 | ✅ 活跃 |
| 作者 | [hccccc01333](https://github.com/hccccc01333) | 更新时间 | 2026-08-14 |

## 一句话介绍

> Agent 评测平台：benchmark YAML、无头 dsh 运行、基于 trace 的指标、脚本评分与运行对比。

## 详细介绍

**Agent Evaluation Platform for [deepseek-harness](https://github.com/deepseek-ai/deepseek-harness).** Run benchmarks against headless `dsh` profiles, harvest persisted session logs as traces, fold automatic metrics, grade task success and tool selection, and report or compare runs — one `benchmark.yaml` in, one JSON run + Markdown report out.

## ✨ 核心特性

- `dsh eval run benchmark.yaml` — orchestrate one headless `dsh` subprocess per case × trial
- Trace harvesting from persisted session logs (everything a model sees is reconstructable from the log)
- Automatic metrics: task success, tool success, tool-selection accuracy, steps, tokens, latency, cost, retry, invalid tool calls, context usage
- Scripted grading: `expected.tool` (tool-selection accuracy) and `expected.check` (task success)
- LLM judge: final-answer score and hallucination flags from a judge model
- Subagent trace merging: child session logs fold into the trial metrics

## 📦 安装

```bash
pnpm add dsh-eval
dsh plugin --profile eval add dsh-eval
```

## 🚀 快速开始

```bash
git clone https://github.com/hccccc01333/dsh-eval.git
cd dsh-eval
```

## 📚 更多信息

**Quick start**

Install the package directly: pnpm add dsh-eval dsh plugin --profile eval add dsh-eval The npm package targets the official `@deepseek-ai/*` releases (`0.1.0-rc.6` peers). For the source flow, clone this repo and link it to a deepseek-harness checkout: git clone https://github.com/hccccc01333/dsh-eval.git cd dsh-eval Windows (junction): New-Item -ItemType Junction -Path harness -Target D:\path\to\

## 🔗 链接

- [GitHub 仓库](https://github.com/hccccc01333/dsh-eval)
- [完整 README](https://github.com/hccccc01333/dsh-eval#readme)
- [返回dsh-eval所在分类](../workflows.md)
