---
title: "dsh-memory (Jesse-njx)"
description: "Cited memory over DSH's lossless session log: distilled, human-auditable facts with citations."
keywords: "dsh-memory (Jesse-njx), memory, plugin, deepseek harness, dsh"
---
# dsh-memory (Jesse-njx)

> ⭐ **2** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Memory & context |
| Stars | ⭐ 2 | Status | ✅ active |
| Author | [Jesse-njx](https://github.com/Jesse-njx) | Updated | 2026-08-13 |
| Subcategory | 🧠 Memory systems | Capabilities | memory |

## One-liner

> Cited memory over DSH's lossless session log: distilled, human-auditable facts with citations.

## About

**Cited memory over DSH's lossless session log.** Distilled facts that can always escalate back to the exact original context. `dsh-memory` is a DeepSeek Harness bundle. When a session ends, a background distillation pass extracts durable facts — user preferences, project decisions, environment quirks, corrections — into small markdown files under `~/.dsh/memory/`. Every memory carries a **citation** `(sessionId, [start..end])` pointing at the exact log events it came from. The next session gets a compact index of those memories, plus two tools: `memory_read` (the full memory) and `memory_expand` (the cited original log excerpt). The key idea: **summaries are an index into ground truth, never the truth.** Retrieval surfaces the one-line distilled fact (cheap); when the agent needs more, `m

## 📦 Install

```bash
dsh plugin --profile web add @dsh-memory/bundle
```

## 🚀 Quick Start

```bash
The user prefers TypeScript for new projects and tests.
```

## 📚 Learn more

**Install**

dsh plugin --profile web add @dsh-memory/bundle The distillation pass routes through `ctx.llm` — it reuses the session's own provider/model by default, so a polyglot-style provider chain or your normal model serves it too. Override with `distill.provider` / `distill.model`.

**Config**

All fields optional (profile patch or `cordis.patch.yml`): plugins: dsh-memory: enabled: true home: ~/.dsh/memory # memory root override (default: $DSH_HOME/memory or ~/.dsh/memory) maxIndexTokens: 800 # hard token cap for the injected recall index maxExpandBytes: 8192 # output byte cap for one memory_expand excerpt recall: enabled: true cacheMs: 5000 # index cache TTL distill: enabled: true provi

## 🔗 Links

- [GitHub Repository](https://github.com/Jesse-njx/dsh-memory)
- [Full README](https://github.com/Jesse-njx/dsh-memory#readme)
- [Back to the Plugins list](../plugins.md)
