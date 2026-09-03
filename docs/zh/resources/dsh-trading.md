---
title: "dsh-trading"
description: "纯研究型交易工作台插件：类型化行情数据缝（自带 provider）、多周期指标快照、带溯源门控标注的交互图表卡片，以及拒绝执行型工具调用的风险护栏——架构上不提供执行能力。"
keywords: "dsh-trading, research, plugin, security, ui, deepseek harness, dsh"
---
# dsh-trading

> ⭐ **12** · ✅ 活跃 · 插件 · 近期 ⬆️ +2

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 研究 |
| 星数 | ⭐ 12 | 状态 | ✅ 活跃 |
| 作者 | [maddogfinance](https://github.com/maddogfinance) | 更新时间 | 2026-08-21 |

## 一句话介绍

> 纯研究型交易工作台插件：类型化行情数据缝（自带 provider）、多周期指标快照、带溯源门控标注的交互图表卡片，以及拒绝执行型工具调用的风险护栏——架构上不提供执行能力。

## 详细介绍

A trading **research** workbench built as plugins for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`). No fork, no patched core — just a bundle you stack on the stock `web` or `headless` profile.

## 📦 安装

```bash
dsh plugin --profile trading add @dsh-trading/bundle
```

## 🚀 快速开始

```bash
pnpm install && pnpm build
node examples/generate-sample-data.mjs

dsh plugin --profile trading add ./bundle/trading \
    ./packages/market-data ./packages/provider-csv ./packages/tool-market \
    ./packages/verdict ./packages/risk-guard ./packages/client-chart
```

## 📚 更多信息

**Demo**

The column is pinned to Micron. The agent's six marks are for Bitcoin — a different instrument, so the predicate refuses the merge and **nothing lands on the wrong chart**. They are offered on a pill instead; one click loads that chart with its marks. The clock in the top-right corner is a live feed off a local OpenD, ticking through the whole clip. ▶ **[Watch the full 90-second demo with narratio

## 🔗 链接

- [GitHub 仓库](https://github.com/maddogfinance/dsh-trading)
- [完整 README](https://github.com/maddogfinance/dsh-trading#readme)
- [返回dsh-trading所在分类](../plugins.md)
