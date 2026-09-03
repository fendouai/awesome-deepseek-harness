---
title: "dsh-memoryhub"
description: "MemoryHub (mh) plugin for DeepSeek Harness (dsh): auto-loads checkpoint memory on session start, adds mh_* tools and the mh skill, and a Memory tab in the web UI"
keywords: "dsh-memoryhub, learning, skill, coding, memory, ui, deepseek harness, dsh"
---
# dsh-memoryhub

> ⭐ **3** · ✅ 活跃 · 技能

| | | | |
|---|---|---|---|
| 类型 | 技能 | 分类 | 学习 |
| 星数 | ⭐ 3 | 状态 | ✅ 活跃 |
| 作者 | [solknight48](https://github.com/solknight48) | 更新时间 | 2026-08-15 |

## 一句话介绍

> MemoryHub (mh) plugin for DeepSeek Harness (dsh): auto-loads checkpoint memory on session start, adds mh_* tools and the mh skill, and a Memory tab in the web UI

## 详细介绍

[MemoryHub](https://github.com/solknight48/memoryhub) (`mh`) integration for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`). MemoryHub keeps project memory as **purified sessions in git-versioned checkpoints** under `.memoryhub/`. This plugin wires that into dsh: - **Auto-load on session start** — runs `mh load` in the session workspace and injects the checkpoint memory as durable plugin context. No prompt, no tool call; the model simply starts with its memory back. - **`mh_save` bridges dsh sessions to mh** — dsh session files are not among the transcript formats mh discovers (Claude Code / pi / Codex), so the plugin renders the live session's durable event log as a pi-format JSONL transcript (in the temp dir) and saves through mh's existing `--transcript` pat

## ✨ 核心特性

- **Auto-load on session start** — runs `mh load` in the session workspace and
- **`mh_save` bridges dsh sessions to mh** — dsh session files are not among
- **Six tools** — `mh_load`, `mh_save`, `mh_status`, `mh_list`, `mh_search`,
- **A "Memory" tab in the web UI** — beside chat and trajectory: the `mh ui`
- **The `mh` workflow skill** — registered at runtime, it teaches the model

## 📦 安装

```bash
dsh plugin --profile web add github:solknight48/dsh-memoryhub
```

## 🚀 快速开始

```bash
[memoryhub] memory ≈ 31,240 tokens ≈ 12.2% of the 256,000-token context window (adapter-reported); session total after load ≈ 18.6%
```

## 📚 更多信息

**Install**

dsh plugin --profile web add github:solknight48/dsh-memoryhub The package declares `dsh.bundle`, so the install appends its patch layer to the profile. For a checkout instead: `dsh plugin --profile web add ./dsh-memoryhub`. Git installs fetch sources, and pnpm ≥ 10 asks before running this package's `prepare` build the first time; allowlist `dsh-memoryhub` in the profile's `pnpm-workspace.yaml` as

## 🔗 链接

- [GitHub 仓库](https://github.com/solknight48/dsh-memoryhub)
- [完整 README](https://github.com/solknight48/dsh-memoryhub#readme)
- [返回dsh-memoryhub所在分类](../skills.md)
