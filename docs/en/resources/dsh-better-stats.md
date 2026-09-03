---
title: "dsh-better-stats"
description: "Enhanced stats strip for the DeepSeek Harness Web UI: official CNY pricing (peak/off-peak tiers, auto price sync), per-model accounting, live timers, agent-team tree merging, direct balance, budget alerts and streaming cost estimation."
keywords: "dsh-better-stats, developer, plugin, observability, ui, deepseek harness, dsh"
---
# dsh-better-stats

> ⭐ **2** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 2 | Status | ✅ active |
| Author | [null5069](https://github.com/null5069) | Updated | — |
| Subcategory | 💰 Cost & billing | Capabilities | observability, ui |

## One-liner

> Enhanced stats strip for the DeepSeek Harness Web UI: official CNY pricing (peak/off-peak tiers, auto price sync), per-model accounting, live timers, agent-team tree merging, direct balance, budget alerts and streaming cost estimation.

## About

A richer stats strip for the DeepSeek Harness (DSH) Web UI, sitting right below the composer: official CNY pricing (peak/off-peak tiers, auto-synced from the official pricing page), per-model accounting, live timers, subagent-tree merging, direct account balance, budget alerts, and streaming cost estimation. DeepSeek Official | Balance ¥8.67 | Turn ¥0.1676 · Session ¥29.49 | 20 turns · 345 steps | LLM 1h 12m · Tool 5m 6s | TTFT avg 3.88s · 111.72tok/s | Cache 103.98M · hit 98.64% | In 1.44M · Out 336.53K

## ✨ Key Features

- **Balance**: host queries `api.deepseek.com/user/balance` directly (the `DEEPSEEK_API_KEY` credential goes through the DSH credentials seam, never the browser),
- **Pricing**: official CNY price table ([api-docs.deepseek.com/zh-cn/quick_start/pricing](https://api-docs.deepseek.com/zh-cn/quick_start/pricing/)), re-synced b
- **Per-model accounting**: each message is priced with the model that produced it (`deepseek-v4-flash` / `deepseek-v4-pro` / `deepseek-v4-flash-vision-exp` each 
- **Cache buckets**: uncached input, cache-read and cache-write are billed separately (cache-read at the much lower hit price), and the cache-hit rate is shown.
- **Turn**: the current turn is settled from the settled steps' event-level fold (each step priced at its own event time/model), plus a **streaming character-leve
- **Session / live Agent Team tree**: every second the host `/live` route publishes one coherent tree cut keyed by session id and event revision. Exact usage, CNY
- **Accounting contract**: `outputTokens` already includes `reasoningTokens` — reasoning is a display-only subset used for detail stats only, never billed twice, 
- **Budget alerts (optional, off by default)**: `config: { dailyBudgetCny: 20, monthlyBudgetCny: 100 }` — the spend group turns amber past 80% and red with ⚠ over

## 📦 Install

```bash
cd ~/.dsh/profiles/web
pnpm add dsh-better-stats
```

## 🚀 Quick Start

```bash
git clone https://github.com/null5069/dsh-better-stats.git
cd dsh-better-stats        # no runtime dependencies — no npm install needed
```

## 📚 Learn more

**Architecture**

Every route response carries `pricing: { source: "official"|"builtin"|"stale", fetchedAt, tables }` and an optional `budget`, so the client never hard-codes price numbers.

## 🔗 Links

- [GitHub Repository](https://github.com/null5069/dsh-better-stats)
- [Full README](https://github.com/null5069/dsh-better-stats#readme)
- [Back to the Plugins list](../plugins.md)
