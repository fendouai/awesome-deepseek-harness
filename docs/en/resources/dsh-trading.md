---
title: "dsh-trading"
description: "Research-only trading workbench for DSH: typed market-data seam (BYO provider), multi-timeframe indicator snapshots, interactive chart cards with provenance-gated annotations, and a risk-guard denying execution-shaped tool calls. No execution seam by construction."
keywords: "dsh-trading, research, plugin, security, ui, deepseek harness, dsh"
---
# dsh-trading

> ⭐ **12** · ✅ active · plugin · ⬆️ +2 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Research |
| Stars | ⭐ 12 | Status | ✅ active |
| Author | [maddogfinance](https://github.com/maddogfinance) | Updated | 2026-08-21 |

## One-liner

> Research-only trading workbench for DSH: typed market-data seam (BYO provider), multi-timeframe indicator snapshots, interactive chart cards with provenance-gated annotations, and a risk-guard denying execution-shaped tool calls. No execution seam by construction.

## About

A trading **research** workbench built as plugins for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`). No fork, no patched core — just a bundle you stack on the stock `web` or `headless` profile.

## 📦 Install

```bash
dsh plugin --profile trading add @dsh-trading/bundle
```

## 🚀 Quick Start

```bash
pnpm install && pnpm build
node examples/generate-sample-data.mjs

dsh plugin --profile trading add ./bundle/trading \
    ./packages/market-data ./packages/provider-csv ./packages/tool-market \
    ./packages/verdict ./packages/risk-guard ./packages/client-chart
```

## 📚 Learn more

**Demo**

The column is pinned to Micron. The agent's six marks are for Bitcoin — a different instrument, so the predicate refuses the merge and **nothing lands on the wrong chart**. They are offered on a pill instead; one click loads that chart with its marks. The clock in the top-right corner is a live feed off a local OpenD, ticking through the whole clip. ▶ **[Watch the full 90-second demo with narratio

## 🔗 Links

- [GitHub Repository](https://github.com/maddogfinance/dsh-trading)
- [Full README](https://github.com/maddogfinance/dsh-trading#readme)
- [Back to the Plugins list](../plugins.md)
