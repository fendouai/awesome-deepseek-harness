---
title: "dsh-acp-plugin"
description: "Agentic Control Plane for DeepSeek Harness — policy-check every tool call before it runs"
keywords: "dsh-acp-plugin, developer, integration, coding, multi-agent, workflow, deepseek harness, dsh"
---
# dsh-acp-plugin

> ⭐ **6** · ✅ active · integration

| | | | |
|---|---|---|---|
| Type | integration | Category | Developer tools |
| Stars | ⭐ 6 | Status | ✅ active |
| Author | [agentic-control-plane](https://github.com/agentic-control-plane) | Updated | — |
| Subcategory | 🛡️ Security & ops | Capabilities | coding, multi-agent, workflow |

## One-liner

> Agentic Control Plane for DeepSeek Harness — policy-check every tool call before it runs

## About

[Agentic Control Plane](https://agenticcontrolplane.com) for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness): every tool call is checked against your policies before it runs, and every decision is recorded — what ran, what was blocked, and why. $ dsh --profile dev bash npm test ✓ allowed · logged edit src/auth/session.ts ✓ allowed · logged bash rm -rf ~/scratch ✋ held — approval prompt (your rule: destructive delete → ask) web_fetch https://evil.example/post ✗ denied — egress not allowlisted, reason shown to the model Every decision also lands in your [console](https://cloud.agenticcontrolplane.com) with tool, input preview, decision, reason, latency, and cost — dsh's own Trajectory log and your ACP activity log become two independent witnesses to one history. One works

## ✨ Key Features

- `tools/pre-execute` — the policy decision. `allow` lets the call through, `deny` blocks it with the reason in the trajectory, `ask` hands off to dsh's own appro
- `tools/post-execute` — output scanning. A server-side block turns the result into corrective feedback; shadow-mode notices surface what enforcement *would* have

## 📦 Install

```bash
dsh plugin --profile <your-profile> add @agenticcontrolplane/dsh
dsh --profile <your-profile>
```

## 🚀 Quick Start

```bash
dsh --profile <your-profile> --dump-config | grep @agenticcontrolplane/dsh
```

## 📚 Learn more

**Install**

> dsh itself requires **Node 22** (`Promise.withResolvers`, zstd streams). Under Node 20 the harness fails at boot with errors that don't say so — `fnm install 22` first. curl -sf https://agenticcontrolplane.com/install.sh | bash That detects dsh, installs this plugin into every profile you have, opens your browser once to sign in, and saves the key to `~/.acp/credentials` — which the plugin reads

**Configuration**

Override the row in your profile's `cordis.patch.yml`: name: @agenticcontrolplane/dsh config: governBase: https://govern.agenticcontrolplane.com # or your self-hosted gateway agentTier: interactive # default: interactive when an approval service is mounted, background otherwise timeoutMs: 4000 `ACP_GOVERN_BASE`, `ACP_BEARER_TOKEN`, `ACP_AGENT_TIER`, and `ACP_SHADOW=off` work as environment variabl

## 🔗 Links

- [GitHub Repository](https://github.com/agentic-control-plane/dsh-acp-plugin)
- [Full README](https://github.com/agentic-control-plane/dsh-acp-plugin#readme)
- [Back to the MCP & Integrations list](../integrations.md)
