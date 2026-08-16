---
title: "dsh-cost-meter"
description: "dsh plugin: per-turn USD cost badge in the Web UI (session total + per-message footer, hover breakdown) from token usage x a configurable pricing table."
keywords: "dsh-cost-meter, ui, plugin, coding, deepseek harness, dsh"
---
# dsh-cost-meter

> ⭐ 0 · ✅ active · plugin

## One-liner

dsh plugin: per-turn USD cost badge in the Web UI (session total + per-message footer, hover breakdown) from token usage x a configurable pricing table.

## About

Out-of-tree [dsh](https://github.com/deepseek-ai/deepseek-harness) plugin that shows a live **USD cost badge** for the open conversation in the Web UI. It is a dual-face `dsh.client` package: - **Host half** (`lib/index.js`) registers a `sessionCost` projection on the session-projection seam. The fold tracks the current provider/model from `request/header` events and accumulates cost from the provider-reported usage buckets (uncached input / output / cache-read / cache-write), reusing token-mete

## Author
**[Sttrevens](https://github.com/Sttrevens)**

## Links

- [GitHub Repository](https://github.com/Sttrevens/dsh-cost-meter)
- [Full README](https://github.com/Sttrevens/dsh-cost-meter#readme)
- [Back to the Plugins list](../plugins.md)
