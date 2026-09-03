---
title: "dsh-us-stocks"
description: "US stock market data tools for DeepSeek Harness, powered by yahoo-finance2"
keywords: "dsh-us-stocks, registry, awesome-list, coding, deepseek harness, dsh"
---
# dsh-us-stocks

> ⭐ **8** · ✅ 活跃 · 精选列表

| | | | |
|---|---|---|---|
| 类型 | 精选列表 | 分类 | 注册表 |
| 星数 | ⭐ 8 | 状态 | ✅ 活跃 |
| 作者 | [Realyujie](https://github.com/Realyujie) | 更新时间 | — |

## 一句话介绍

> US stock market data tools for DeepSeek Harness, powered by yahoo-finance2

## 详细介绍

US stock market data tools for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness), powered by [yahoo-finance2](https://github.com/gadicc/yahoo-finance2). Gives the agent six first-class tools for quotes, price history, financial statements, analyst consensus, news and ownership — instead of leaving it to improvise against HTML pages.

## 📦 安装

```bash
dsh plugin --profile web add dsh-us-stocks
```

## 🚀 快速开始

```bash
npx @deepseek-ai/dsh plugin --profile web add dsh-us-stocks
```

## 📚 更多信息

**Configuration**

enabled: true # register the tools market: us # only "us" today quoteTtlMs: 10000 # live quote cache lifetime referenceTtlMs: 300000 # statements, bars, ratings and news cache lifetime Caching is in-memory and per-process. Concurrent identical requests are collapsed onto a single upstream call, so an agent fanning six tools at one ticker does not make six redundant round trips. Failures are never 

## 🔗 链接

- [GitHub 仓库](https://github.com/Realyujie/dsh-us-stocks)
- [完整 README](https://github.com/Realyujie/dsh-us-stocks#readme)
- [返回dsh-us-stocks所在分类](../awesome-lists.md)
