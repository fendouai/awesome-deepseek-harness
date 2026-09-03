---
title: "open-managed-agents"
description: "开源 Claude Managed Agents API 实现与自托管 Claude Tag 风格 Agent 运行时。"
keywords: "open-managed-agents, harness, related, workflow, deepseek harness, dsh"
---
# open-managed-agents

> ⭐ **243** · ✅ 活跃 · 相关 · 近期 ⬆️ +3

| | | | |
|---|---|---|---|
| 类型 | 相关 | 分类 | Harness |
| 星数 | ⭐ 243 | 状态 | ✅ 活跃 |
| 作者 | [openma-ai](https://github.com/openma-ai) | 更新时间 | 2026-08-19 |

## 一句话介绍

> 开源 Claude Managed Agents API 实现与自托管 Claude Tag 风格 Agent 运行时。

## 详细介绍

**Open-source alternative to Claude Managed Agents** — and a foundation for open-source, self-hosted Claude Tag-style agents. 🌐 **[openma.dev](https://openma.dev)** · 📖 **[docs.openma.dev](https://docs.openma.dev)** · 💬 **[github.com/openma-ai/open-managed-agents](https://github.com/openma-ai/open-managed-agents)** Write a harness. Deploy. The platform runs it — with sessions, sandboxes, tools, memory, vaults, Slack/GitHub/Linear integrations, and crash recovery out of the box. Drop-in compatible with the Claude Managed Agents API; runs on Cloudflare Workers + Durable Objects, or `docker compose up` on your own box. Use Open Managed Agents when you want: - A self-hosted Claude Managed Agents API implementation. - An open-source, self-hosted Claude Tag-style workflow with BYOK model credent

## ✨ 核心特性

- A self-hosted Claude Managed Agents API implementation.
- An open-source, self-hosted Claude Tag-style workflow with BYOK model credentials.
- MCP, private tools, encrypted vaults, and durable sessions under your own deployment boundary.

## 🚀 快速开始

```bash
oma deploy --harness my-harness.ts --agent agent_abc123
```

## 📚 更多信息

**Quick start: self-host (Docker)**

git clone https://github.com/openma-ai/open-managed-agents.git cd open-managed-agents cp .env.example .env

**Quick start: Cloudflare deploy**

Requires [Workers Paid plan](https://developers.cloudflare.com/workers/platform/pricing/) (for Durable Objects + Containers). git clone https://github.com/openma-ai/open-managed-agents.git cd open-managed-agents pnpm install

**Architecture**

A **meta-harness** is not an agent — it's the platform that runs agents. It defines stable interfaces for everything an agent needs, and stays out of the way of the agent loop: ┌─────────────────────────────────────────────────────────┐ │ Harness (the brain — your code) │ │ - Reads events, builds context, calls the model │ │ - Decides HOW: caching, compaction, tool delivery │ │ - Stateless: crash 

**Configuration**

The variables that gate boot and at-rest safety: Full list (integrations OAuth credentials, Postgres URL, sandbox tunables, memory-bucket config, Google sign-in, etc.) — see **[docs.openma.dev/reference/configuration](https://docs.openma.dev/reference/configuration/)** and `.env.example` / `.dev.vars.example`. ---

## 🔗 链接

- [GitHub 仓库](https://github.com/openma-ai/open-managed-agents)
- [完整 README](https://github.com/openma-ai/open-managed-agents#readme)
- [返回open-managed-agents所在分类](../related.md)
