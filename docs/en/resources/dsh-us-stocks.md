---
title: "dsh-us-stocks"
description: "US stock market data tools for DeepSeek Harness, powered by yahoo-finance2"
keywords: "dsh-us-stocks, registry, awesome-list, coding, deepseek harness, dsh"
---
# dsh-us-stocks

> ⭐ **8** · ✅ active · awesome-list

| | | | |
|---|---|---|---|
| Type | awesome-list | Category | Registries |
| Stars | ⭐ 8 | Status | ✅ active |
| Author | [Realyujie](https://github.com/Realyujie) | Updated | — |

## One-liner

> US stock market data tools for DeepSeek Harness, powered by yahoo-finance2

## About

US stock market data tools for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness), powered by [yahoo-finance2](https://github.com/gadicc/yahoo-finance2). Gives the agent six first-class tools for quotes, price history, financial statements, analyst consensus, news and ownership — instead of leaving it to improvise against HTML pages.

## 📦 Install

```bash
dsh plugin --profile web add dsh-us-stocks
```

## 🚀 Quick Start

```bash
npx @deepseek-ai/dsh plugin --profile web add dsh-us-stocks
```

## 📚 Learn more

**Configuration**

enabled: true # register the tools market: us # only "us" today quoteTtlMs: 10000 # live quote cache lifetime referenceTtlMs: 300000 # statements, bars, ratings and news cache lifetime Caching is in-memory and per-process. Concurrent identical requests are collapsed onto a single upstream call, so an agent fanning six tools at one ticker does not make six redundant round trips. Failures are never 

## 🔗 Links

- [GitHub Repository](https://github.com/Realyujie/dsh-us-stocks)
- [Full README](https://github.com/Realyujie/dsh-us-stocks#readme)
- [Back to the Awesome Lists & Registries list](../awesome-lists.md)
