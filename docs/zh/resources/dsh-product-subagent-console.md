---
title: "dsh-product-subagent-console"
description: "为 DSH 对话增加多 Agent 工作台，支持可编辑任务方案、真实子会话树、计划与实际运行对照，以及基于证据的恢复预览。"
keywords: "dsh-product-subagent-console, multi-agent, plugin, workflow, ui, observability, deepseek harness, dsh"
---
# dsh-product-subagent-console

> ⭐ **1** · 🧪 实验性 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 多智能体 |
| 星数 | ⭐ 1 | 状态 | 🧪 实验性 |
| 作者 | [Jokasa7](https://github.com/Jokasa7) | 更新时间 | — |

## 一句话介绍

> 为 DSH 对话增加多 Agent 工作台，支持可编辑任务方案、真实子会话树、计划与实际运行对照，以及基于证据的恢复预览。

## 详细介绍

English · [简体中文](README.zh.md) From a reviewable plan to evidence-backed recovery — inside one [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) conversation. This is an independent community plugin, not an official DeepSeek Harness component. [Install](#install) · [Try it in 60 seconds](#try-it-in-60-seconds) · [Full product tour](docs/product-tour.md) · [Report an issue](https://github.com/Jokasa7/dsh-product-subagent-console/issues) DSH Product Subagent Console adds a draggable **Subagents** workbench for designing a multi-Agent run, watching the real child tree, checking what actually happened, and preparing a safe next step.

## ✨ 核心特性

- Parallel code, documentation, or repository review where ownership and dependencies should stay visible.
- Phased implementation followed by independent verification or synthesis.
- Diagnosing a run that is stuck, incomplete, unexpectedly branched, or missing evidence.
- Turning a repeatedly verified workflow into a reusable starting point without auto-running it.

## 📦 安装

```bash
sha256sum --check SHA256SUMS.txt

# DSH Desktop — run in Open DSH Terminal
dsh plugin add ./dsh-product-subagent-console-0.9.0.tgz

# Regular Web profile
dsh plugin --profile web add ./dsh-product-subagent-console-0.9.0.tgz
```

## 🚀 快速开始

```bash
- id: agent-planner
  name: dsh-product-subagent-console/plan-tool
  config:
    toolName: design_subagent_plan
    executeToolName: execute_subagent_plan
```

## 📚 更多信息

**Install**

Download the `.tgz` file and `SHA256SUMS.txt` from the matching [GitHub Release](https://github.com/Jokasa7/dsh-product-subagent-console/releases), verify the archive, and install it into your active profile: sha256sum --check SHA256SUMS.txt

## 🔗 链接

- [GitHub 仓库](https://github.com/Jokasa7/dsh-product-subagent-console)
- [完整 README](https://github.com/Jokasa7/dsh-product-subagent-console#readme)
- [返回dsh-product-subagent-console所在分类](../plugins.md)
