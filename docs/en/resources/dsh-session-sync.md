---
title: "dsh-session-sync"
description: "Synchronize sessions, presets and settings between DSH desktop‑shell embedded instance and external web browser instance. Fix session isolation issue for third‑party packaged DeepSeek‑Harness desktop builds."
keywords: "dsh-session-sync, desktop, client, browser, coding, ui, deepseek harness, dsh"
---
# dsh-session-sync

> ⭐ **1** · ✅ active · client

| | | | |
|---|---|---|---|
| Type | client | Category | Desktop |
| Stars | ⭐ 1 | Status | ✅ active |
| Author | [hajimimaodie8](https://github.com/hajimimaodie8) | Updated | — |

## One-liner

> Synchronize sessions, presets and settings between DSH desktop‑shell embedded instance and external web browser instance. Fix session isolation issue for third‑party packaged DeepSeek‑Harness desktop builds.

## About

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-session-sync` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **Cross-device session sync for DeepSeek Harness — a dedicated git mirror of your session store.** *Sync your sessions between devices, keep both sides on any conflict, never lose a turn.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ Key Features

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-session-sync` (counts toward the [deepseek1024.com](https://deepseek

## 📦 Install

```bash
# 1. install the bundle into your profile
dsh plugin --profile web add "github:PerryLink/dsh-session-sync#main"

# or from npm (published releases)
dsh plugin --profile web add dsh-session-sync

# 2. point it at a private git remote and verify the row
dsh --profile web --dump-config | grep -A2 'id: session-sync'
```

## 🚀 Quick Start

```bash
- insert:
    - id: session-sync
      name: dsh-session-sync
      config:
        remote: git@github.com:you/your-dsh-sessions.git
```

## 📚 Learn more

**Configuration**

All tunables are Schemastery `Config` fields (changeable from cordis.yml). An id-targeted override replaces the whole row — restate every key you need. `cordis.patch.yml` documents each key inline. Example override in your profile patch: - id: session-sync name: dsh-session-sync config: remote: git@github.com:you/your-dsh-sessions.git branch: main autoPushOnTurnEnd: true pullIntervalMinutes: 30 co

## 🔗 Links

- [GitHub Repository](https://github.com/hajimimaodie8/DSH-Session-Sync)
- [Full README](https://github.com/hajimimaodie8/DSH-Session-Sync#readme)
- [Back to the Clients (Desktop & TUI) list](../clients.md)
