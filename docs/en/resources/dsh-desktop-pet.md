---
title: "dsh-desktop-pet"
description: "Whale desktop pet for DeepSeek Harness: the whale mirrors live agent status (thinking bubbles, working tool, error) and the API balance is rendered as a circular sea level; click to jump or 40% charged 360° dive with chatter."
keywords: "dsh-desktop-pet, ui, plugin, deepseek harness, dsh"
---
# dsh-desktop-pet

> ⭐ **5** · 🧪 experimental · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 5 | Status | 🧪 experimental |
| Author | [FenyxHuang](https://github.com/FenyxHuang) | Updated | — |
| Subcategory | 💡 Generative UI | Capabilities | ui |

## One-liner

> Whale desktop pet for DeepSeek Harness: the whale mirrors live agent status (thinking bubbles, working tool, error) and the API balance is rendered as a circular sea level; click to jump or 40% charged 360° dive with chatter.

## About

A desktop pet for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness): the official whale mark lives in the shell overlay, floats in a circular sea whose level mirrors your DeepSeek API balance, and reacts to your agent's every move.

## ✨ Key Features

- **Live agent status** — the whale rests, thinks, works, or cries (`❗`) exactly as your agent does, with a status pill that shows the phase, the current tool, an
- **Balance as sea level** — the circular sea around the whale fills to `balance / balanceScale` (¥100 = full by default), the surface is a scrolling wave with a 
- **Interactive** — click to pet it: a springy jump most of the time, or a rare (40%) charged dive with a 360° spin that lands with a big splash, a high rebound, 
- **Zero runtime dependencies** — the bundle ships prebuilt; all `@deepseek-ai/*` services come from the harness itself, so installing needs no build step and no 

## 📦 Install

```bash
# GitHub direct install (prebuilt artifacts, no build authorization needed)
dsh plugin --profile web add github:FenyxHuang/dsh-desktop-pet

# or from a local checkout
dsh plugin --profile web add link:/path/to/dsh-desktop-pet

# or as a tarball
pnpm pack
dsh plugin --profile web add ./dsh-desktop-pet-0.1.0.tgz
```

## 🚀 Quick Start

```bash
- update:
    - id: pet-status
      config:
        balanceScale: 500
        balanceRefetchMs: 60000
```

## 📚 Learn more

**Configuration**

The bundle applies the `cordis.patch.yml` layer, which mounts two rows: The host row reads your DeepSeek API key through the harness's normal credentials (`DEEPSEEK_API_KEY`) and refetches `https://api.deepseek.com/user/balance` at most every 15 seconds. Override any key in your own profile's `cordis.patch.yml`: - id: pet-status config: balanceScale: 500 balanceRefetchMs: 60000

## 🔗 Links

- [GitHub Repository](https://github.com/FenyxHuang/dsh-desktop-pet)
- [Full README](https://github.com/FenyxHuang/dsh-desktop-pet#readme)
- [Back to the Plugins list](../plugins.md)
