---
title: "dsh-governance"
description: "Authority layer for agentic AI as a DSH plugin: governs every tool call against your policies."
keywords: "dsh-governance, workflow, security, deepseek harness, dsh"
---
# dsh-governance

> ⭐ **1** · ✅ active · workflow

| | | | |
|---|---|---|---|
| Type | workflow | Category | Workflows |
| Stars | ⭐ 1 | Status | ✅ active |
| Author | [tappass](https://github.com/tappass) | Updated | 2026-08-18 |

## One-liner

> Authority layer for agentic AI as a DSH plugin: governs every tool call against your policies.

## About

**The authority layer for agentic AI, as a DeepSeek Harness plugin.** Everything in DeepSeek Harness is a plugin. This is the one that decides what your agents are allowed to do. Guardrails and safety classifiers ask *"is this output harmful?"* That is a property of the model. TapPass asks a different question: *"is this agent **allowed** to do this, under **our** rules, right now?"* That is a property of your business, and no model level tool can answer it, because the answer lives in your organisation, not in the weights. This plugin intercepts every tool call at the harness's `tools/pre-execute` seam, sends it to the TapPass policy decision point (`POST /v1/govern`), and allows, denies, or escalates it for human approval.

## ✨ Key Features

- **Business rules, not model safety.** Write the rule once, in your language:
- **Authority is earned.** The plugin ships in **observe mode**: from the first
- **Harness and model agnostic.** The same rules that govern an agent here
- **EU hosted, EU AI Act ready.**

## 📦 Install

```bash
# create a profile if you do not have one, then add the plugin
dsh plugin --profile default add @tappass/dsh-governance

# point it at your TapPass workspace
export TAPPASS_API_KEY="tp_dev_..."      # a TapPass developer key

# verify the layer without booting, then run
dsh --profile default --dump-config
dsh --profile default
```

## 🚀 Quick Start

```bash
# $DSH_HOME/profiles/default/cordis.patch.yml
- tappass-governance:
    config:
      mode: enforce
```

## 📚 Learn more

**Configure**

Every tool call is governed once it is installed. Configuration is optional; the defaults are safe. Set them in your profile's patch, for example to enforce:

## 🔗 Links

- [GitHub Repository](https://github.com/tappass/dsh-governance)
- [Full README](https://github.com/tappass/dsh-governance#readme)
- [Back to the Workflows & Automation list](../workflows.md)
