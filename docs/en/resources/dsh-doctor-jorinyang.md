---
title: "dsh-doctor"
description: "Deterministic diagnostics and recovery for DeepSeek Harness"
keywords: "dsh-doctor, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-doctor

> ⭐ **3** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 3 | Status | ✅ active |
| Author | [astra3294](https://github.com/astra3294) | Updated | 2026-08-21 |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> Deterministic diagnostics and recovery for DeepSeek Harness

## About

Deterministic diagnostics and recovery for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness). DSH Doctor is the safety net for the two ways a Harness usually breaks itself: it **cannot converse** (the Web UI opens but the loop is broken), or it **cannot start** (boot fails after a config, dependency, or plugin change). When the Web UI still opens, the Doctor button calls a loopback-only Host recovery service. When Harness cannot start, the same engine runs as a standalone CLI — including a boot probe that captures the failure and a one-click reset to the last healthy checkpoint, so plugin developers can experiment and always get back to a working state. [简体中文](./README.zh-CN.md)

## ✨ Key Features

- a persistent Doctor action beside Settings in the sidebar;
- an automatic recovery banner above the composer after a prompt or Agent failure;
- a full Doctor page in Settings with findings, checkpoints, and rollback;
- a floating emergency entry that appears in the frame overlay whenever the profile is broken, independent of the sidebar and conversation plugins.

## 📦 Install

```bash
dsh plugin --profile web add dsh-doctor
dsh --profile web
```

## 🚀 Quick Start

```bash
npx dsh-doctor recover --profile web
```

## 📚 Learn more

**Install**

Add Doctor to the Web profile: dsh plugin --profile web add dsh-doctor dsh --profile web This installs one package with both Host and browser halves. It contributes: If the Web UI cannot start: npx dsh-doctor recover --profile web

## 🔗 Links

- [GitHub Repository](https://github.com/astra3294/dsh-doctor)
- [Full README](https://github.com/astra3294/dsh-doctor#readme)
- [Back to the Plugins list](../plugins.md)
