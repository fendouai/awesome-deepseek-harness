---
title: "dsh-capability-receipt"
description: "Content-addressed receipts for skills actually loaded by DeepSeek Harness"
keywords: "dsh-capability-receipt, learning, skill, coding, deepseek harness, dsh"
---
# dsh-capability-receipt

> ⭐ **4** · ✅ 活跃 · 技能

| | | | |
|---|---|---|---|
| 类型 | 技能 | 分类 | 学习 |
| 星数 | ⭐ 4 | 状态 | ✅ 活跃 |
| 作者 | [dongsheng123132](https://github.com/dongsheng123132) | 更新时间 | — |

## 一句话介绍

> Content-addressed receipts for skills actually loaded by DeepSeek Harness

## 详细介绍

`dsh-capability-receipt` proves which skill DeepSeek Harness actually loaded. It hashes the effective instruction body returned by `ctx.skills.get()`, records the winning provider/source/invocation policy, and—when the resource base is local—hashes a bounded resource-directory closure. It can then compare that runtime observation with hashes pinned by a trusted source artifact and write a deterministic content-addressed receipt. This is deliberately not another skill package format, dependency resolver, installer, registry, evaluator, per-turn summary, or event audit ledger. Use [pack-agent](https://github.com/sakikoTGW/pack-agent) for packaging and distribution; use this plugin for the missing last hop between a fixed source artifact and the effective capability inside DSH. Version 0.3.0 

## ✨ 核心特性

- `dsh_capability_receipt_inspect`: returns structural fields and hashes without returning skill instructions, metadata, or absolute paths.
- `dsh_capability_receipt_issue`: requires `expectedContentSha256`, accepts optional resource/provider/source/invocation expectations, and writes only beneath an 
- `dsh_capability_receipt_issue_from_pack`: reads a workspace-relative pack-agent `agent-pack/lock/v1`, recomputes pack-agent's directory and portable-bundle skil

## 📦 安装

```bash
dsh plugin --profile capability-proof add \
  github:owner/dsh-capability-receipt#<commit>
```

## 🚀 快速开始

```bash
dsh-capability-receipt verify \
  --receipt artifacts/capability-receipt-<sha256>.json \
  --require-verified
```

## 📚 更多信息

**Install in DSH**

Pin a reviewed commit in an isolated DSH profile: dsh plugin --profile capability-proof add \ github:owner/dsh-capability-receipt#<commit> The package declares its DSH bundle and ships `cordis.patch.yml`, so a successful plugin install adds the layer to that profile automatically.

## 🔗 链接

- [GitHub 仓库](https://github.com/dongsheng123132/dsh-capability-receipt)
- [完整 README](https://github.com/dongsheng123132/dsh-capability-receipt#readme)
- [返回dsh-capability-receipt所在分类](../skills.md)
