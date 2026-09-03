---
title: "dsh-research-report"
description: "Verifiable research-report engine with a content-addressed evidence ledger and versioned sealed reports carrying per-claim verification verdicts."
keywords: "dsh-research-report, research, plugin, deepseek harness, dsh"
---
# dsh-research-report

> ⭐ **44** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Research |
| Stars | ⭐ 44 | Status | ✅ active |
| Author | [PerryLink](https://github.com/PerryLink) | Updated | — |

## One-liner

> Verifiable research-report engine with a content-addressed evidence ledger and versioned sealed reports carrying per-claim verification verdicts.

## About

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-research-report` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **A verifiable research-report engine for DeepSeek Harness.** *Every claim is bound to immutable evidence snapshots, verified byte-for-byte, and sealed into a versioned report whose manifest hash anyone can recompute.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ Key Features

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-research-report` (counts toward the [deepseek1024.com](https://deeps

## 📦 Install

```bash
# From a scratch profile (pins the commit; runs the self-contained `prepare` build)
dsh plugin --profile demo add "github:YOUR_ORG/dsh-research-report#<sha>"
# The profile's pnpm-workspace.yaml gains an allowBuilds entry for dsh-research-report on first add.
```

## 🚀 Quick Start

```bash
dsh plugin --profile demo add dsh-research-report
```

## 📚 Learn more

**Install & uninstall**

dsh plugin --profile demo add dsh-research-report # install dsh plugin --profile demo remove dsh-research-report # uninstall Verify the row mounts: `dsh --profile demo --dump-config | grep dsh-research-report`.

**Configuration**

All tunables are Schemastery `Config` fields; invalid values fail the profile load loudly. Relative roots resolve against the harness working directory (the workspace).

## 🔗 Links

- [GitHub Repository](https://github.com/PerryLink/dsh-research-report)
- [Full README](https://github.com/PerryLink/dsh-research-report#readme)
- [Back to the Plugins list](../plugins.md)
