---
title: "dsh-closerai"
description: "CloserAI - a local-first, model-agnostic, permission-transparent desktop AI workbench built on DeepSeek Harness."
keywords: "dsh-closerai, desktop, client, coding, ui, deepseek harness, dsh"
---
# dsh-closerai

> ⭐ **4** · ✅ 活跃 · 客户端

| | | | |
|---|---|---|---|
| 类型 | 客户端 | 分类 | 桌面端 |
| 星数 | ⭐ 4 | 状态 | ✅ 活跃 |
| 作者 | [sb1733831438-maker](https://github.com/sb1733831438-maker) | 更新时间 | 2026-08-19 |

## 一句话介绍

> CloserAI - a local-first, model-agnostic, permission-transparent desktop AI workbench built on DeepSeek Harness.

## 详细介绍

[English](README.md) · [简体中文](README.zh.md) CloserAI is an open-source desktop client that hosts a [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) process inside a hardened Electron shell. It is **not a thin wrapper**: it keeps DSH as the agent runtime and adds a desktop supervisor, three permission-isolated working modes, local-first session storage, OS-keychain secrets, and a plugin security model.

## ✨ 核心特性

- **Hardened shell** — context isolation, sandbox, strict CSP, locked-down navigation, single instance, deep links.
- **Three permission-isolated modes** — Chat / Work / Code, so the model only gets exactly the tools and files it should.
- **Local-first sessions** — every conversation is persisted under `DSH_HOME`, with history, projects, export/import, and restart recovery.
- **Native desktop** — system tray, crash/recovery notifications, launch at login.
- **Transparent by design** — a management page shows capability toggles, a per-mode permission manifest, and redacted diagnostics.
- **Model-agnostic** — DeepSeek, any OpenAI-compatible endpoint, or fully-offline **Mock mode** (no API key needed).

## 📦 安装

```bash
pnpm install
pnpm check          # format + lint + build + typecheck + test
pnpm smoke          # end-to-end: onboarding → DSH UI → management page
cd apps/desktop && pnpm run dev
```

## 🚀 快速开始

```bash
git clone https://github.com/sb1733831438-maker/DSH-closerAI.git
cd DSH-closerAI
pnpm install
pnpm check
cd apps/desktop
pnpm run pack     # build the Windows installer (release/CloserAI-*-Setup-x64.exe)
```

## 📚 更多信息

**🚀 Quick start**

**Option A — install the Windows build (recommended)** 1. Download the latest installer: **Windows** `CloserAI-0.8.0-Setup-x64.exe`, **macOS** `CloserAI-0.8.0-arm64.dmg`, or **Linux** `CloserAI-0.8.0.AppImage` — all on the [Releases](https://github.com/sb1733831438-maker/DSH-closerAI/releases/latest) page. 2. Verify the SHA-256 against `SHA256SUMS.txt` (Windows: `Get-FileHash -Algorithm SHA256 .\C

## 🔗 链接

- [GitHub 仓库](https://github.com/sb1733831438-maker/DSH-closerAI)
- [完整 README](https://github.com/sb1733831438-maker/DSH-closerAI#readme)
- [返回dsh-closerai所在分类](../clients.md)
