---
title: "dsh-cost-meter"
description: "dsh plugin: per-turn USD cost badge in the Web UI (session total + per-message footer, hover breakdown) from token usage x a configurable pricing table."
keywords: "dsh-cost-meter, ui, plugin, coding, deepseek harness, dsh"
---
# dsh-cost-meter

> ⭐ 0 · ✅ 活跃 · 插件

## 一句话介绍

dsh plugin: per-turn USD cost badge in the Web UI (session total + per-message footer, hover breakdown) from token usage x a configurable pricing table.

## 详细介绍

Out-of-tree [dsh](https://github.com/deepseek-ai/deepseek-harness) plugin that shows a live **USD cost badge** for the open conversation in the Web UI. It is a dual-face `dsh.client` package: - **Host half** (`lib/index.js`) registers a `sessionCost` projection on the session-projection seam. The fold tracks the current provider/model from `request/header` events and accumulates cost from the provider-reported usage buckets (uncached input / output / cache-read / cache-write), reusing token-mete

## 作者
**[Sttrevens](https://github.com/Sttrevens)**

## 链接

- [GitHub 仓库](https://github.com/Sttrevens/dsh-cost-meter)
- [完整 README](https://github.com/Sttrevens/dsh-cost-meter#readme)
- [返回dsh-cost-meter所在分类](../plugins.md)
