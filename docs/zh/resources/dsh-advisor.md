---
title: "dsh-advisor"
description: "配对第二模型被动审查每一回合并注入建议。"
keywords: "dsh-advisor, multi-agent, agent, context, deepseek harness, dsh"
---
# dsh-advisor

> ⭐ 9 · ✅ 活跃 · 智能体

## 一句话介绍

配对第二模型被动审查每一回合并注入建议。

## 详细介绍

A standalone dsh plugin bundle porting the omp "advisor" subsystem: a per-session reviewer model that observes the primary transcript, reviews each stepped turn with an explicitly configured model (provider + model are required), and injects severity-ranked advice (nit / concern / blocker) back into the session — without polluting or recursively reviewing itself. Install with a single command: dsh plugin --profile web add dsh-advisor # <name> = your profile name **Advisory only.** The advisor ne

## 作者
**[omdsh-dev](https://github.com/omdsh-dev)**

## 链接

- [GitHub 仓库](https://github.com/omdsh-dev/dsh-advisor)
- [完整 README](https://github.com/omdsh-dev/dsh-advisor#readme)
- [返回dsh-advisor所在分类](../agents.md)
