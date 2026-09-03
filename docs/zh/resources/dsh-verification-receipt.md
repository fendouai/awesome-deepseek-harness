---
title: "dsh-verification-receipt"
description: "Privacy-minimal heuristic per-turn verification summaries for DeepSeek Harness"
keywords: "dsh-verification-receipt, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-verification-receipt

> ⭐ **4** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 4 | 状态 | ✅ 活跃 |
| 作者 | [030611](https://github.com/030611) | 更新时间 | 2026-08-14 |

## 一句话介绍

> Privacy-minimal heuristic per-turn verification summaries for DeepSeek Harness

## 详细介绍

[中文](README.zh.md) dsh plugin --profile web add dsh-verification-receipt The receipt summarizes recorded tool counts and lexical verification-shaped signals. It does **not** prove that tests ran or that code is correct. DSH Verification Receipt is a small, passive Profile Bundle for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness). After each durable `turn/end`, it appends one privacy-minimal, heuristic execution summary to a local JSONL file. It records execution traces, not semantic correctness. A receipt shows only that DSH logged tool calls and that a lexical heuristic found a possible verification signal. It never proves that a test ran. It cannot show that the right command executed, that assertions were sufficient, that output was truthful, or that the assistant's

## 📦 安装

```bash
dsh plugin --profile web add dsh-verification-receipt
```

## 🚀 快速开始

```bash
dsh plugin --profile web add dsh-verification-receipt
dsh --profile web --dump-config
```

## 📚 更多信息

**Install**

Add the published package to every profile that should emit receipts: dsh plugin --profile web add dsh-verification-receipt dsh --profile web --dump-config Repeat the first command with another profile name (for example, `headless`) when that profile also needs receipts. For local development, clone this repository, run `pnpm install --frozen-lockfile && pnpm run check`, and pass the checkout path

## 🔗 链接

- [GitHub 仓库](https://github.com/030611/dsh-verification-receipt)
- [完整 README](https://github.com/030611/dsh-verification-receipt#readme)
- [返回dsh-verification-receipt所在分类](../plugins.md)
