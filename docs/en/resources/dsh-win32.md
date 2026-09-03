---
title: "dsh-win32"
description: "Fix and diagnose DeepSeek Harness on native Windows. Official PowerShell, Workspace Write, shortcuts, and legacy preset repair. No WSL."
keywords: "dsh-win32, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-win32

> ⭐ **25** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 25 | Status | ✅ active |
| Author | [sjh9714](https://github.com/sjh9714) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> Fix and diagnose DeepSeek Harness on native Windows. Official PowerShell, Workspace Write, shortcuts, and legacy preset repair. No WSL.

## About

**Official PowerShell. Workspace Write. One command.** npx dsh-win32 setup Current DeepSeek Harness already includes persistent PowerShell and a Windows ACL sandbox. dsh-win32 checks that official stack, finds known Windows failures, applies the repairs it can prove safe, and creates a desktop shortcut. It does not install Git, PowerShell, busybox, WSL, or another DSH bundle on the current path. [中文](./docs/README.zh.md) · [Windows evidence and legacy details](./docs/windows-details.md) Using a coding agent? [Copy the setup and verification request](https://github.com/sjh9714/dsh-win32/blob/master/docs/agent-setup.md). For a guided walkthrough, see [Windows troubleshooting in Chinese](https://github.com/sjh9714/dsh-win32/blob/master/docs/windows-first-run.zh.md).

## ✨ Key Features

- Checks the latest published DSH Windows package contract
- Checks PowerShell 7 and known broken koffi runtimes
- Creates a `DeepSeek Harness` desktop shortcut for the Web profile
- Leaves the official profile and preset unchanged
- Shows the exact next steps for a first session

## 🚀 Quick Start

```bash
npx dsh-win32 setup
```

## 📚 Learn more

**Live verification of an installed stack**

npx dsh-win32 verify npx dsh-win32 verify --json `verify` is a model- and API-key-free acceptance run against an **already installed** `@deepseek-ai/dsh` dependency tree. It does not use registry metadata as proof. In an isolated temporary home and workspace it invokes the installed model-facing persistent `pwsh` tool through the official terminal, subprocess, Workspace Write policy, and Windows A

## 🔗 Links

- [GitHub Repository](https://github.com/sjh9714/dsh-win32)
- [Full README](https://github.com/sjh9714/dsh-win32#readme)
- [Back to the Plugins list](../plugins.md)
