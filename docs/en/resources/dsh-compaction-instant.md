---
title: "dsh-compaction-instant"
description: "LLM-free lossless* compaction engine for DeepSeek Harness"
keywords: "dsh-compaction-instant, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-compaction-instant

> ⭐ **13** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 13 | Status | ✅ active |
| Author | [TsFreddie](https://github.com/TsFreddie) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> LLM-free lossless* compaction engine for DeepSeek Harness

## About

[English](README.md) | [简体中文](README.zh-CN.md) Instant, near-lossless context compaction for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) — a **drop-in replacement for `@deepseek-ai/dsh-compaction-basic`** that replaces LLM summarization with the deterministic conversation-compiler principle of [lllyasviel/VCC](https://github.com/lllyasviel/VCC). A compaction compresses a shadowed history span in **milliseconds, with zero model calls**, keeping **original tokens only** — no paraphrase, no hallucination, no summarizer cost. Everything that is cut is still recoverable through `(seq N)` pointers into the durable session log.

## ✨ Key Features

- **LLM-free** — compaction never invokes a model. No summarizer prompt, no inference latency, no token spend; the compile is deterministic text processing, so a 
- **Near-lossless** — output contains only original tokens; every cut is marked and points at its durable `seq`, and prior checkpoints are copied verbatim.
- **Instant** — a single deterministic pass over the shadowed nodes; no network, no model, no KV-cache concerns.
- **Contract-exact drop-in** — same seam, events, provenance and failure vocabulary as `compaction-basic`; every built-in preset loads it unchanged (alias install

## 📦 Install

```bash
dsh plugin --profile web add <spec>
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add "@deepseek-ai/dsh-compaction-basic@npm:dsh-compaction-instant"
```

## 📚 Learn more

**Example**

A region containing a user request, an assistant text + tool call, and its result compiles to: [user] please fix the bug [assistant] on it [user] next question Every tool call is ONE line: the key argument for whitelisted tools (`toolArgTools`), name-only for the rest (`* job_kill (seq 9 -> result 10)`), nothing at all for `hideTools` rows. Tool results never occupy entries — the `-> result N` poi

**Configuration**

All fields optional; defaults shown. The tool and command plugins each take their own `{ maxRecallTokens?: 16000, maxSearchHits?: 50 }` config. > **Cordis config gotcha:** the plugin row's config passes through the schemastery schema, whose `~standard` adapter injects **`[]` for every absent array key** (`toolArgTools`, `hideTools`, `noisePatterns`, `toolKeyFields`, `modelPolicies`). The resolver 

**Browser settings card (Settings → Plugins)**

Since 0.1.4 the engine exposes a **user-owned settings namespace** (`compaction-instant`) on every deployment that composes the settings domain (the standard web/desktop profiles do). The editable subset, persisted to `settings.yaml` and layered **over** the plugin row's cordis config: Everything else (`modelPolicies`, `toolArgTools`, `debug`, `debugLogPath`, the deprecated `maxTokens`/`checkpoint

**Installation**

All three methods below install the package (published to npm as `dsh-compaction-instant`) with the harness's own plugin manager (which runs pnpm inside the profile directory, making the package resolvable to both the host composition and every agent preset): dsh plugin --profile web add <spec> `dsh-command-compact` (`/compact`) is backend-independent, so it keeps working unchanged in every method

## 🔗 Links

- [GitHub Repository](https://github.com/TsFreddie/dsh-compaction-instant)
- [Full README](https://github.com/TsFreddie/dsh-compaction-instant#readme)
- [Back to the Plugins list](../plugins.md)
