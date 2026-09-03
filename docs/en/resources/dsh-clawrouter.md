---
title: "dsh-clawrouter"
description: "A safety gate for DeepSeek Harness: a stronger model reviews dangerous tool calls before they run. Plus vision and BlockRun's full model catalog from one wallet, paid per request over x402."
keywords: "dsh-clawrouter, vision, plugin, coding, multimodal, deepseek harness, dsh"
---
# dsh-clawrouter

> ⭐ **20** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 20 | Status | ✅ active |
| Author | [BlockRunAI](https://github.com/BlockRunAI) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding, multimodal |

## One-liner

> A safety gate for DeepSeek Harness: a stronger model reviews dangerous tool calls before they run. Plus vision and BlockRun's full model catalog from one wallet, paid per request over x402.

## About

Two things people keep asking for in the Harness discussions: `Full Access` is all-or-nothing: approve every command by hand, or approve nothing and hope. This adds a third option.

## 📦 Install

```bash
dsh plugin --profile web add dsh-clawrouter
```

## 🚀 Quick Start

```bash
- id: blockrun-review
  config:
    enabled: true
    reviewerModel: anthropic/claude-opus-5
```

## 📚 Learn more

**Quick Start**

dsh plugin --profile web add dsh-clawrouter export BASE_CHAIN_WALLET_KEY=0x... # or store it via the credentials service **The install prints `✕ missing peer` for six harness packages. That is expected.** The harness itself supplies them at runtime, and every first-party bundle declares its peers the same way — the alternative, depending on them directly, gives the profile a second copy of cordis 

## 🔗 Links

- [GitHub Repository](https://github.com/BlockRunAI/dsh-clawrouter)
- [Full README](https://github.com/BlockRunAI/dsh-clawrouter#readme)
- [Back to the Plugins list](../plugins.md)
