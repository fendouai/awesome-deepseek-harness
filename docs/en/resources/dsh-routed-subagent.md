---
title: "dsh-routed-subagent"
description: "Run a one-shot subagent fully mounted on any agent preset from any session, with per-call model/provider override, a model-availability pre-check, and external CLI engines (codex / claude / codebuddy) with background jobs, live progress, kill, and continuable sessions."
keywords: "dsh-routed-subagent, developer, plugin, multi-agent, deepseek harness, dsh"
---
# dsh-routed-subagent

> ⭐ **0** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 0 | Status | ✅ active |
| Author | [bpc-oss](https://github.com/bpc-oss) | Updated | 2026-08-21 |
| Subcategory | 🛡️ Security & ops | Capabilities | multi-agent |

## One-liner

> Run a one-shot subagent fully mounted on any agent preset from any session, with per-call model/provider override, a model-availability pre-check, and external CLI engines (codex / claude / codebuddy) with background jobs, live progress, kill, and continuable sessions.

## About

A global [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) plugin that lets **any session dispatch a one-shot subagent fully mounted on ANY agent preset**, with **per-call model/provider override** and a **model-availability pre-check**. The stock `subagent` / `subagent_fork` tools force children to inherit the PARENT's preset. This plugin replaces that with a custom subagent provider whose async child setup calls `agentPresets.mount(childCtx, )` — so the child adopts the TARGET preset's complete composition: persona, prompt sections, skill catalog, and tools.

## ✨ Key Features

- **Background by default, parallel dispatch** — the call returns a job id immediately (like the stock subagent tool); the conversation stays free to do other wor
- **Full preset mount** — the child runs under the target preset's standing composition (not a persona copy): identity, mission section, skills, tools.
- **Per-call model override** — `model` / `provider` arguments route the child's LLM call to a different model than this session's (via the official `resolveChild
- **Model pre-check** — an invalid model fails fast with the provider's candidate list instead of an opaque child failure.
- **Official subagent ecosystem** — one-shot lifecycle events, UI rows, trajectory; returns the child's final output.
- **Idempotent provider registration** — multiple presets can mount the row; the host-plane provider registry is never duplicated.

## 🚀 Quick Start

```bash
// external codex subagent (background, explicit model, live progress)
await subagent_routed({
  engine: 'codex',
  provider: undefined,       // external engines ignore the DSH provider
  model: 'gpt-5.6-sol',      // explicit codex thread model
  prompt: '...',
  run_in_background: true,
})
```

## 📚 Learn more

**1. Link the package into the harness install**

The plugin statically imports `@deepseek-ai/*` packages, which resolve via Node ESM from the package location. Create a `node_modules` junction/symlink in the package directory pointing at the harness install: :: Windows mklink /J "<plugin-dir>\node_modules" "<harness>\resources\host\node_modules"

**Usage**

subagent_routed(prompt="Use the dev engineer standard to review this repository", preset="dev", description="dev review") # background one-shot subagent_routed(prompt="Continue the review", preset="dev-reviewer", description="follow-up", fork=true) # inherits THIS conversation subagent_routed(preset="dev", prompt="Audit this repo", description="audit", continuable=true) # send_message(<subagentId>

## 🔗 Links

- [GitHub Repository](https://github.com/bpc-oss/dsh-routed-subagent)
- [Full README](https://github.com/bpc-oss/dsh-routed-subagent#readme)
- [Back to the Plugins list](../plugins.md)
