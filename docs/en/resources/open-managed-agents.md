---
title: "open-managed-agents"
description: "Open-source Claude Managed Agents API implementation and self-hosted Claude Tag-style agent runtime."
keywords: "open-managed-agents, harness, related, workflow, deepseek harness, dsh"
---
# open-managed-agents

> ⭐ **243** · ✅ active · related · ⬆️ +3 recently

| | | | |
|---|---|---|---|
| Type | related | Category | Harness |
| Stars | ⭐ 243 | Status | ✅ active |
| Author | [openma-ai](https://github.com/openma-ai) | Updated | 2026-08-19 |

## One-liner

> Open-source Claude Managed Agents API implementation and self-hosted Claude Tag-style agent runtime.

## About

**Open-source alternative to Claude Managed Agents** — and a foundation for open-source, self-hosted Claude Tag-style agents. 🌐 **[openma.dev](https://openma.dev)** · 📖 **[docs.openma.dev](https://docs.openma.dev)** · 💬 **[github.com/openma-ai/open-managed-agents](https://github.com/openma-ai/open-managed-agents)** Write a harness. Deploy. The platform runs it — with sessions, sandboxes, tools, memory, vaults, Slack/GitHub/Linear integrations, and crash recovery out of the box. Drop-in compatible with the Claude Managed Agents API; runs on Cloudflare Workers + Durable Objects, or `docker compose up` on your own box. Use Open Managed Agents when you want: - A self-hosted Claude Managed Agents API implementation. - An open-source, self-hosted Claude Tag-style workflow with BYOK model credent

## ✨ Key Features

- A self-hosted Claude Managed Agents API implementation.
- An open-source, self-hosted Claude Tag-style workflow with BYOK model credentials.
- MCP, private tools, encrypted vaults, and durable sessions under your own deployment boundary.

## 🚀 Quick Start

```bash
oma deploy --harness my-harness.ts --agent agent_abc123
```

## 📚 Learn more

**Quick start: self-host (Docker)**

git clone https://github.com/openma-ai/open-managed-agents.git cd open-managed-agents cp .env.example .env

**Quick start: Cloudflare deploy**

Requires [Workers Paid plan](https://developers.cloudflare.com/workers/platform/pricing/) (for Durable Objects + Containers). git clone https://github.com/openma-ai/open-managed-agents.git cd open-managed-agents pnpm install

**Architecture**

A **meta-harness** is not an agent — it's the platform that runs agents. It defines stable interfaces for everything an agent needs, and stays out of the way of the agent loop: ┌─────────────────────────────────────────────────────────┐ │ Harness (the brain — your code) │ │ - Reads events, builds context, calls the model │ │ - Decides HOW: caching, compaction, tool delivery │ │ - Stateless: crash 

**Configuration**

The variables that gate boot and at-rest safety: Full list (integrations OAuth credentials, Postgres URL, sandbox tunables, memory-bucket config, Google sign-in, etc.) — see **[docs.openma.dev/reference/configuration](https://docs.openma.dev/reference/configuration/)** and `.env.example` / `.dev.vars.example`. ---

## 🔗 Links

- [GitHub Repository](https://github.com/openma-ai/open-managed-agents)
- [Full README](https://github.com/openma-ai/open-managed-agents#readme)
- [Back to the Related Agent Harnesses list](../related.md)
