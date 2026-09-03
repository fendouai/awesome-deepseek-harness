---
title: "dsh-checkpoint-rewind"
description: "Claude Code /rewind for DeepSeek Harness — git-first workspace snapshots before every mutation, turn-boundary session forks, one-shot /rewind restore. A dsh-plugin capability seam."
keywords: "dsh-checkpoint-rewind, registry, awesome-list, coding, git, deepseek harness, dsh"
---
# dsh-checkpoint-rewind

> ⭐ **12** · ✅ active · awesome-list

| | | | |
|---|---|---|---|
| Type | awesome-list | Category | Registries |
| Stars | ⭐ 12 | Status | ✅ active |
| Author | [PerryLink](https://github.com/PerryLink) | Updated | — |

## One-liner

> Claude Code /rewind for DeepSeek Harness — git-first workspace snapshots before every mutation, turn-boundary session forks, one-shot /rewind restore. A dsh-plugin capability seam.

## About

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-checkpoint-rewind` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **Unified DeepSeek Harness checkpoints — session + workspace + config three-state snapshots with one-shot rollback.** *The Claude Code Checkpoints equivalent, built as a capability-seam plugin: capture before every mutation, restore any of the three states with one approved command.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ Key Features

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-checkpoint-rewind` (counts toward the [deepseek1024.com](https://dee

## 📦 Install

```bash
# 1. install the bundle into your profile
dsh plugin --profile web add "github:PerryLink/dsh-checkpoint-rewind#main"

# or from npm (published releases)
dsh plugin --profile web add dsh-checkpoint-rewind

# 2. restart and verify the row
dsh --profile web --dump-config | grep -A4 'id: checkpoint-rewind'
```

## 🚀 Quick Start

```bash
- insert:
    - id: checkpoint-rewind-storage
      name: '@deepseek-ai/dsh-storage'
    - id: checkpoint-rewind-storage-json
      name: '@deepseek-ai/dsh-storage-json'
      config:
        root: !!js dshHomePath('checkpoint-rewind/storage')
    - id: checkpoint-rewind-storage-domain
      name: '@deepseek-ai/dsh-storage-domain'
      config:
        backend: json
```

## 📚 Learn more

**Configuration**

All tunables are Schemastery `Config` fields (changeable from cordis.yml). Nothing is hardcoded. Provider options (`gitBin`, `snapshotDir`, `excludeGlobs`, `verifyByHash`) are read from the live config at use time, so cordis.yml changes apply without a restart. - id: checkpoint-rewind name: dsh-checkpoint-rewind config: provider: auto maxSnapshots: 50 maxSnapshotBytes: 536870912 pruneOnTurnEnd: tr

**FAQ**

**Does this replace git?** No — it *uses* git where available. In a git repo you get byte-perfect, deduplicated snapshot objects without touching history; in any other directory the copy provider does the same with plain files. Regular commits remain your long-term history. **Why not `git reset --hard` by default?** Because destroying state is not the job of a safety net. The plugin only creates u

**Demo**

A real assembled-headless integration run (`npm run test:integration`) drives the full flow: the agent modifies files across two turns, then `/rewind preview` inspects the impact read-only (no confirmation gate, no writes) and `/rewind <id>` restores the files and replays the session into a new child session. The run asserts the file contents, the replayed child context, the guard checkpoint, and 

## 🔗 Links

- [GitHub Repository](https://github.com/PerryLink/dsh-checkpoint-rewind)
- [Full README](https://github.com/PerryLink/dsh-checkpoint-rewind#readme)
- [Back to the Awesome Lists & Registries list](../awesome-lists.md)
