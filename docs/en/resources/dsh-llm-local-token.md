---
title: "dsh-llm-local-token"
description: "DeepSeek Harness provider routes that reuse local Codex CLI and Claude Code OAuth tokens instead of API keys."
keywords: "dsh-llm-local-token, developer, plugin, security, observability, deepseek harness, dsh"
---
# dsh-llm-local-token

> ⭐ **0** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 0 | Status | ✅ active |
| Author | [tianxia--](https://github.com/tianxia--) | Updated | 2026-08-17 |
| Subcategory | 💰 Cost & billing | Capabilities | security, observability |

## One-liner

> DeepSeek Harness provider routes that reuse local Codex CLI and Claude Code OAuth tokens instead of API keys.

## About

A [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) plugin that serves LLM calls with the OAuth tokens your **local CLIs already hold** — no separate API key, no extra login. If you are signed in to the Codex CLI or to Claude Code, those subscriptions become usable model routes inside DSH. Both routes appear in the model picker as soon as the plugin loads. A route whose credential is missing is skipped instead of failing the boot. The usage badge additionally reports a **GLM Coding Plan** subscription, which DSH already serves through pi-ai's own `zai-coding-cn` route — the plugin adds the quota, not a second route, so the model picker gains no duplicate. See [Subscription usage badge](#subscription-usage-badge). Both subscriptions as routes in the model picker Subscripti

## 📦 Install

```bash
dsh plugin --profile web add dsh-llm-local-token

# or straight from git
dsh plugin --profile web add https://github.com/tianxia--/dsh-llm-local-token.git
```

## 🚀 Quick Start

```bash
- insert:
    - id: llm-local-token
      name: dsh-llm-local-token
```

## 📚 Learn more

**~/.dsh/settings.yaml**

agent-default-model: provider: openai-codex model: gpt-5.6-terra reasoningEffort: medium

**Subscription usage badge**

Codex and Claude state their quota in response headers, so reading it off a real request costs nothing. A route you never call has nothing to report, though — so the plugin also refreshes on a schedule, with one deliberately tiny request per provider (16 input tokens for Codex, 9 for Anthropic) that carries no prompt, skills, tools or history and is never stored. A badge appears in the composer ba

**`Provider is not configured: openai-codex`**

Means the pi-ai provider refused an API-key override. This plugin already attaches an api-key auth method to the OAuth-only Codex provider; seeing this error again implies a pi-ai version whose `resolveProviderAuth` changed — open an issue with your `@earendil-works/pi-ai` version.

## 🔗 Links

- [GitHub Repository](https://github.com/tianxia--/dsh-llm-local-token)
- [Full README](https://github.com/tianxia--/dsh-llm-local-token#readme)
- [Back to the Plugins list](../plugins.md)
