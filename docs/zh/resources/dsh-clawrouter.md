---
title: "dsh-clawrouter"
description: "A safety gate for DeepSeek Harness: a stronger model reviews dangerous tool calls before they run. Plus vision and BlockRun's full model catalog from one wallet, paid per request over x402."
keywords: "dsh-clawrouter, vision, plugin, coding, multimodal, deepseek harness, dsh"
---
# dsh-clawrouter

> ⭐ **20** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 20 | 状态 | ✅ 活跃 |
| 作者 | [BlockRunAI](https://github.com/BlockRunAI) | 更新时间 | — |
| 子分类 | 👁️ 视觉工具 | 能力 | coding, multimodal |

## 一句话介绍

> A safety gate for DeepSeek Harness: a stronger model reviews dangerous tool calls before they run. Plus vision and BlockRun's full model catalog from one wallet, paid per request over x402.

## 详细介绍

Two things people keep asking for in the Harness discussions: `Full Access` is all-or-nothing: approve every command by hand, or approve nothing and hope. This adds a third option.

## 📦 安装

```bash
dsh plugin --profile web add dsh-clawrouter
```

## 🚀 快速开始

```bash
- id: blockrun-review
  config:
    enabled: true
    reviewerModel: anthropic/claude-opus-5
```

## 📚 更多信息

**Quick Start**

dsh plugin --profile web add dsh-clawrouter export BASE_CHAIN_WALLET_KEY=0x... # or store it via the credentials service **The install prints `✕ missing peer` for six harness packages. That is expected.** The harness itself supplies them at runtime, and every first-party bundle declares its peers the same way — the alternative, depending on them directly, gives the profile a second copy of cordis 

## 🔗 链接

- [GitHub 仓库](https://github.com/BlockRunAI/dsh-clawrouter)
- [完整 README](https://github.com/BlockRunAI/dsh-clawrouter#readme)
- [返回dsh-clawrouter所在分类](../plugins.md)
