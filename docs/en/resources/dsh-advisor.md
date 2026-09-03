---
title: "dsh-advisor"
description: "Advisor - Pair a second model that passively reviews each turn and injects notes.  搭配一个会在每轮对话被动注入见解和审查的副模型。"
keywords: "dsh-advisor, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-advisor

> ⭐ **16** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 16 | Status | ✅ active |
| Author | [omdsh-dev](https://github.com/omdsh-dev) | Updated | — |
| Subcategory | 🧪 Code, tests & review | Capabilities | coding |

## One-liner

> Advisor - Pair a second model that passively reviews each turn and injects notes.  搭配一个会在每轮对话被动注入见解和审查的副模型。

## About

[English](README.md) | [中文](README.zh.md) A standalone dsh (DeepSeek Harness) plugin bundle porting the omp "advisor" subsystem: a per-session independent reviewer model that observes the primary transcript, reviews each stepped turn with an explicitly configured model (provider + model are required), and injects severity-ranked advice (nit / concern / blocker) back into the session — without polluting or recursively reviewing itself. **Advisory only.** The advisor never approves or rejects the primary agent's actions, and never issues commands as if it were the primary agent. Every delivered message is self-described advisory content, and a misbehaving reviewer is bounded end to end (emission guard, immuneTurns cooldown, failure policy) so it can never stall or pollute the primary loop. W

## ✨ Key Features

- **Independent reviewer per session**: a separate model call observes the primary transcript and reviews each stepped primary turn; advisor messages are excluded
- **Severity-ranked advice with inject/steer semantics**: at most one note per review — **nit** (a minor style, clarity, or quality suggestion; delivered via non-
- **Explicit model gate**: `enabled` defaults to off; `enabled: true` without `provider` + `model` never starts a model call — status reports disabled-with-reason
- **Zero-tool minimal start**: the reviewer is an independent model call only — no advisor tools, nothing it can do to the session besides advisory messages.
- **No-stall failure policy**: a failing or quota-limited advisor only drops its own bounded backlog — it can never park or pollute the primary loop.
- **Session-scoped controls**: `/advisor on|off|status|config` work per session; the toggles are ephemeral overrides, never persisted config.

## 📦 Install

```bash
dsh plugin --profile web add dsh-advisor      # web profile (Settings → Advisor card)
dsh plugin --profile dsh-tui add dsh-advisor  # dsh-tui terminal profile
```

## 🚀 Quick Start

```bash
dsh --profile web --dump-config   # shows a "# == dsh-advisor" layer with the advisor row
```

## 📚 Learn more

**Install**

dsh plugin --profile web add dsh-advisor # web profile (Settings → Advisor card) dsh plugin --profile dsh-tui add dsh-advisor # dsh-tui terminal profile Same plugin, either front end — the only difference is the `--profile` flag. Pin a version with `@<version>` (e.g. `dsh-advisor@0.1.0`). A registry install fetches the published tarball, which ships the built artifacts (`lib/` + `cordis.patch.yml`

**Configuration**

Add an `advisor:` section to the global dsh settings document (default `$DSH_HOME/settings.yaml` — shared across profiles; the web Settings card writes to this same file): advisor: enabled: true # master switch (default false) — set explicitly to enable provider: deepseek-official # REQUIRED when enabled model: deepseek-v4-flash # REQUIRED when enabled systemPrompt: "" # optional; "" = built-in re

**Limitations & roadmap**

The MVP deliberately drops full omp parity. Accepted gaps (tracked in the harness iteration roadmap):

## 🔗 Links

- [GitHub Repository](https://github.com/omdsh-dev/dsh-advisor)
- [Full README](https://github.com/omdsh-dev/dsh-advisor#readme)
- [Back to the Plugins list](../plugins.md)
