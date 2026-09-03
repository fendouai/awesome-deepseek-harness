---
title: "modlens"
description: "The first vision plugin for DeepSeek Harness and the vision bridge for every text-only coding agent: paste an image and it works."
keywords: "modlens, vision, plugin, multimodal, deepseek harness, dsh"
---
# modlens

> ⭐ **3,495** · ✅ active · plugin · ⬆️ +119 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 3,495 | Status | ✅ active |
| Author | [liustack](https://github.com/liustack) | Updated | 2026-08-20 |
| Subcategory | 👁️ Vision tools | Capabilities | multimodal, vision |

## One-liner

> The first vision plugin for DeepSeek Harness and the vision bridge for every text-only coding agent: paste an image and it works.

## About

Issues are welcome any time: [open one](https://github.com/liustack/modlens/issues/new/choose). Follow the liustack WeChat official account, and come find me on X: **[@liustack](https://x.com/liustack)**. What you built with it, which harness you are on, and what should come next are all shared on WeChat and X. A proper community space is on the way.

## ✨ Key Features

- **The lightest touch on the market.** No hooks, no wrappers, no local proxy daemon, not a single line changed in any harness config: on the skill harnesses it i
- **Zero-config start.** Reuses existing setup in Claude Code, Codex, OpenCode, and Pi, plus other multimodal models already on your machine. Nothing installed lo
- **Comma-separated keys rotate on auth, rate-limit, or quota failures.** Other failures skip remaining keys and keep the existing provider failover.
- **Evidence, not imagination.** Full transcription, reading-order layout regions, entity and relation lists. The model quotes specifics.
- **Install once, use everywhere.** Verified on real machines in Claude Code, Codex, Pi, and OpenCode.

## 📦 Install

```bash
npx -y @deepseek-ai/dsh plugin --profile web add @liustack/modsearch@latest
```

## 🚀 Quick Start

```bash
curl -fsSL https://antigravity.google/cli/install.sh | bash
agy                                                           # sign in, then exit
```

## 📚 Learn more

**Install in other harnesses**

**Step 1, hand it to your AI.** Send it this line: > Install and configure the modlens skill following https://github.com/liustack/modlens/blob/main/INSTALL.md, then run the health check and tell me the result. The install starts by checking what your machine already has. An existing login in Claude Code, Codex, OpenCode, or Pi can be enough: modlens asks before reusing any of them, and the health

**Usage**

Once installed, just chat. Paste an image or drop a path, ask anything, and the skill triggers on its own: the image goes to a vision engine and the answer comes back grounded in what it read. Paste once, and later questions about the same image do not need another paste.

## 🔗 Links

- [GitHub Repository](https://github.com/liustack/modlens)
- [Full README](https://github.com/liustack/modlens#readme)
- [Back to the Plugins list](../plugins.md)
