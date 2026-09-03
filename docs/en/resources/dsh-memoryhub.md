---
title: "dsh-memoryhub"
description: "MemoryHub (mh) plugin for DeepSeek Harness (dsh): auto-loads checkpoint memory on session start, adds mh_* tools and the mh skill, and a Memory tab in the web UI"
keywords: "dsh-memoryhub, learning, skill, coding, memory, ui, deepseek harness, dsh"
---
# dsh-memoryhub

> ⭐ **3** · ✅ active · skill

| | | | |
|---|---|---|---|
| Type | skill | Category | Learning |
| Stars | ⭐ 3 | Status | ✅ active |
| Author | [solknight48](https://github.com/solknight48) | Updated | 2026-08-15 |

## One-liner

> MemoryHub (mh) plugin for DeepSeek Harness (dsh): auto-loads checkpoint memory on session start, adds mh_* tools and the mh skill, and a Memory tab in the web UI

## About

[MemoryHub](https://github.com/solknight48/memoryhub) (`mh`) integration for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`). MemoryHub keeps project memory as **purified sessions in git-versioned checkpoints** under `.memoryhub/`. This plugin wires that into dsh: - **Auto-load on session start** — runs `mh load` in the session workspace and injects the checkpoint memory as durable plugin context. No prompt, no tool call; the model simply starts with its memory back. - **`mh_save` bridges dsh sessions to mh** — dsh session files are not among the transcript formats mh discovers (Claude Code / pi / Codex), so the plugin renders the live session's durable event log as a pi-format JSONL transcript (in the temp dir) and saves through mh's existing `--transcript` pat

## ✨ Key Features

- **Auto-load on session start** — runs `mh load` in the session workspace and
- **`mh_save` bridges dsh sessions to mh** — dsh session files are not among
- **Six tools** — `mh_load`, `mh_save`, `mh_status`, `mh_list`, `mh_search`,
- **A "Memory" tab in the web UI** — beside chat and trajectory: the `mh ui`
- **The `mh` workflow skill** — registered at runtime, it teaches the model

## 📦 Install

```bash
dsh plugin --profile web add github:solknight48/dsh-memoryhub
```

## 🚀 Quick Start

```bash
[memoryhub] memory ≈ 31,240 tokens ≈ 12.2% of the 256,000-token context window (adapter-reported); session total after load ≈ 18.6%
```

## 📚 Learn more

**Install**

dsh plugin --profile web add github:solknight48/dsh-memoryhub The package declares `dsh.bundle`, so the install appends its patch layer to the profile. For a checkout instead: `dsh plugin --profile web add ./dsh-memoryhub`. Git installs fetch sources, and pnpm ≥ 10 asks before running this package's `prepare` build the first time; allowlist `dsh-memoryhub` in the profile's `pnpm-workspace.yaml` as

## 🔗 Links

- [GitHub Repository](https://github.com/solknight48/dsh-memoryhub)
- [Full README](https://github.com/solknight48/dsh-memoryhub#readme)
- [Back to the Skills list](../skills.md)
