---
title: "dsh-auto-mode"
description: "Safe automatic permissions for DeepSeek Harness."
keywords: "dsh-auto-mode, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-auto-mode

> ⭐ **115** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 115 | Status | ✅ active |
| Author | [NanmiCoder](https://github.com/NanmiCoder) | Updated | 2026-08-17 |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> Safe automatic permissions for DeepSeek Harness.

## About

Coding agents need broad access to build, test, and inspect a project without stopping every few steps. But DeepSeek Harness currently leaves a sharp choice: restricted modes interrupt normal development, while Full access removes approval entirely. `dsh-auto-mode` adds the missing middle ground. Routine project work runs directly inside the official `workspace-write` sandbox, only semantic risks outside that boundary are classified using the current DSH model and the direct user's instructions, genuine ambiguity asks once, and destructive access to critical paths is denied before execution.

## 📦 Install

```bash
dsh plugin --profile web add --save-exact @nanmicoder/dsh-auto-mode@latest
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add --save-exact @nanmicoder/dsh-auto-mode@0.1.5
```

## 📚 Learn more

**Install**

> [!NOTE] > Requires an existing [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) installation. > [!IMPORTANT] > Plugin `0.1.6` targets **DeepSeek Harness 0.1.2-alpha.2 and 0.1.2-alpha.3**. Plugin `0.1.5` belongs to the older Harness `0.1.1-rc.2` line and fails to load on both tested Alpha hosts. Keep plugin `0.1.5` pinned while staying on that RC host; Alpha users should instal

**Configuration**

No extra endpoint or API key is needed by default. Auto uses the current Session's DSH provider and model. A trusted profile may pin a dedicated route: config: classifierProvider: deepseek-official classifierModel: deepseek-v4-flash classifierTimeoutMs: 30000 classifierMaxOutputTokens: 1024 See [DESIGN.md](./DESIGN.md) for the complete decision order, threat model, Windows path handling, classifie

## 🔗 Links

- [GitHub Repository](https://github.com/NanmiCoder/dsh-auto-mode)
- [Full README](https://github.com/NanmiCoder/dsh-auto-mode#readme)
- [Back to the Plugins list](../plugins.md)
