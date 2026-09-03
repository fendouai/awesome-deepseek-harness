---
title: "dsh-win32"
description: "Fix and diagnose DeepSeek Harness on native Windows. Official PowerShell, Workspace Write, shortcuts, and legacy preset repair. No WSL."
keywords: "dsh-win32, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-win32

> ⭐ **25** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 25 | 状态 | ✅ 活跃 |
| 作者 | [sjh9714](https://github.com/sjh9714) | 更新时间 | — |
| 子分类 | 👁️ 视觉工具 | 能力 | coding |

## 一句话介绍

> Fix and diagnose DeepSeek Harness on native Windows. Official PowerShell, Workspace Write, shortcuts, and legacy preset repair. No WSL.

## 详细介绍

**Official PowerShell. Workspace Write. One command.** npx dsh-win32 setup Current DeepSeek Harness already includes persistent PowerShell and a Windows ACL sandbox. dsh-win32 checks that official stack, finds known Windows failures, applies the repairs it can prove safe, and creates a desktop shortcut. It does not install Git, PowerShell, busybox, WSL, or another DSH bundle on the current path. [中文](./docs/README.zh.md) · [Windows evidence and legacy details](./docs/windows-details.md) Using a coding agent? [Copy the setup and verification request](https://github.com/sjh9714/dsh-win32/blob/master/docs/agent-setup.md). For a guided walkthrough, see [Windows troubleshooting in Chinese](https://github.com/sjh9714/dsh-win32/blob/master/docs/windows-first-run.zh.md).

## ✨ 核心特性

- Checks the latest published DSH Windows package contract
- Checks PowerShell 7 and known broken koffi runtimes
- Creates a `DeepSeek Harness` desktop shortcut for the Web profile
- Leaves the official profile and preset unchanged
- Shows the exact next steps for a first session

## 🚀 快速开始

```bash
npx dsh-win32 setup
```

## 📚 更多信息

**Live verification of an installed stack**

npx dsh-win32 verify npx dsh-win32 verify --json `verify` is a model- and API-key-free acceptance run against an **already installed** `@deepseek-ai/dsh` dependency tree. It does not use registry metadata as proof. In an isolated temporary home and workspace it invokes the installed model-facing persistent `pwsh` tool through the official terminal, subprocess, Workspace Write policy, and Windows A

## 🔗 链接

- [GitHub 仓库](https://github.com/sjh9714/dsh-win32)
- [完整 README](https://github.com/sjh9714/dsh-win32#readme)
- [返回dsh-win32所在分类](../plugins.md)
