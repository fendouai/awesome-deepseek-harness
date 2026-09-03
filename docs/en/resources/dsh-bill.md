---
title: "dsh-bill"
description: "DSH (DeepSeek Harness) plugin: per-session cost line + cost attribution report, priced by llm-pricing"
keywords: "dsh-bill, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-bill

> ⭐ **3** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 3 | Status | ✅ active |
| Author | [Jannchie](https://github.com/Jannchie) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> DSH (DeepSeek Harness) plugin: per-session cost line + cost attribution report, priced by llm-pricing

## About

Cost tracking for DSH (DeepSeek Harness). A line under each turn tells you what that turn cost; the **Cost** tab tells you what the money went on.

## ✨ Key Features

- **Cost attribution** — the bill split by kind of content: tool output, model output, system prompt, terminal commands (grouped by `git` / `pnpm` / `rg`), tool i
- **Per-turn cost** — one line under every finished turn: what it cost, how many steps, the cache-hit rate. It reads the session log itself, so turns from before 
- **Always on screen** — a line under the shipped stats line (all-time, this session, peak share), and today's spend against the budget in the sidebar. Each of th
- **Report** — a **Cost** tab in the conversation, beside Chat and Trajectory: total, tokens, cache hit, peak share, monthly forecast, account balance; broken dow
- **Budget** — a daily / monthly / all-time limit that turns amber past 80% and red when you go over.
- **Multi-currency** — live rates for ~166 currencies; each model's base rate is shown in the currency its vendor prices it in.
- **Agent tool** — `bill_stats`, so the model can answer questions about spend directly.
- English and Chinese follow the DSH language setting; history from before the install is backfilled from the session log.

## 📦 Install

```bash
dsh plugin --profile web add dsh-bill
```

## 🚀 Quick Start

```bash
- insert:
    - id: bill
      name: 'dsh-bill'
      config:
        priceOverrides:
          'anthropic/claude-sonnet-4-6':
            inputPerM: 3.0        # USD per million input tokens (uncached)
            outputPerM: 15.0
            cacheReadPerM: 0.3
            cacheWritePerM: 3.75
```

## 📚 Learn more

**Configuration**

The budget, its currency, and which of the four surfaces are shown are all set on the **Cost** page in settings, and stored in `$DSH_HOME/dsh-bill/prefs.json`. (Not in the harness's own settings document: its API proxy serves a fixed allowlist of namespaces to the browser, so a plugin's namespace is never readable or writable from there.) `maxRecords` (the in-memory ring buffer size, default 20000

## 🔗 Links

- [GitHub Repository](https://github.com/Jannchie/dsh-bill)
- [Full README](https://github.com/Jannchie/dsh-bill#readme)
- [Back to the Plugins list](../plugins.md)
