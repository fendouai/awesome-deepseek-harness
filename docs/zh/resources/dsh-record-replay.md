---
title: "dsh-record-replay"
description: "Record & Replay for DSH web GUI: session replay, replay packs, screen recording -> skill generation. #dsh-plugin"
keywords: "dsh-record-replay, learning, skill, coding, ui, deepseek harness, dsh"
---
# dsh-record-replay

> ⭐ **0** · ✅ 活跃 · 技能

| | | | |
|---|---|---|---|
| 类型 | 技能 | 分类 | 学习 |
| 星数 | ⭐ 0 | 状态 | ✅ 活跃 |
| 作者 | [kangshifu1](https://github.com/kangshifu1) | 更新时间 | — |

## 一句话介绍

> Record & Replay for DSH web GUI: session replay, replay packs, screen recording -> skill generation. #dsh-plugin

## 详细介绍

A [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) plugin that turns the [Open Record/Replay](https://github.com/humblebanana/open-record-replay) macOS workflow recorder into first-class harness capabilities. It registers the **`open-record-replay` skill** and **six model-facing `orr_*` tools**, so an agent can learn a user-demonstrated desktop workflow: record the user's real macOS actions, validate the evidence, and package it for the host agent's native skill creator. user demonstrates a workflow -> orr_record_start (capture session.json + events.jsonl) -> orr_record_stop (finalize) -> orr_session_validate (check the evidence against the contract) -> orr_session_events (read what the user actually did) -> orr_skill_prepare (package a skill-input directory) -> host ski

## ✨ 核心特性

- macOS (the recorder's native backend is Swift; it needs Xcode Command Line Tools).
- Node.js `>= 22.19` (the Harness runtime).
- A DeepSeek Harness installation.
- An [open-record-replay](https://github.com/humblebanana/open-record-replay)

## 📦 安装

```bash
git clone https://github.com/<you>/dsh-record-replay.git
cd dsh-record-replay
pnpm install
pnpm build
pnpm pack                      # produces dsh-record-replay-0.1.0.tgz
dsh plugin --profile web add ./dsh-record-replay-0.1.0.tgz
```

## 🚀 快速开始

```bash
- id: record-replay
  config:
    repoRoot: '/absolute/path/to/open-record-replay'
    runsOut: 'runs'
    skillInputsOut: 'skill-inputs'
```

## 📚 更多信息

**Install**

Build the package and add it to a profile as a bundle: git clone https://github.com/<you>/dsh-record-replay.git cd dsh-record-replay pnpm install pnpm build pnpm pack # produces dsh-record-replay-0.1.0.tgz dsh plugin --profile web add ./dsh-record-replay-0.1.0.tgz `dsh plugin add` records the package in the profile's `package.json` dependencies and `dsh.profile.bundles`, and the harness heals the 

**Configuration**

The CLI runs with the session workspace as its working directory, so recordings and skill packages land where the agent's filesystem tools can read them.

## 🔗 链接

- [GitHub 仓库](https://github.com/kangshifu1/dsh-record-replay)
- [完整 README](https://github.com/kangshifu1/dsh-record-replay#readme)
- [返回dsh-record-replay所在分类](../skills.md)
