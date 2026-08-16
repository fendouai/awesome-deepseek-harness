---
title: "dsh-memoryhub"
description: "MemoryHub (mh) plugin for DeepSeek Harness (dsh): auto-loads checkpoint memory on session start, adds mh_* tools and the mh skill, and a Memory tab in the web UI"
keywords: "dsh-memoryhub, learning, skill, coding, memory, ui, deepseek harness, dsh"
---
# dsh-memoryhub

> ⭐ 3 · ✅ 活跃 · 技能

## 一句话介绍

MemoryHub (mh) plugin for DeepSeek Harness (dsh): auto-loads checkpoint memory on session start, adds mh_* tools and the mh skill, and a Memory tab in the web UI

## 详细介绍

[MemoryHub](https://github.com/solknight48/memoryhub) (`mh`) integration for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`). MemoryHub keeps project memory as **purified sessions in git-versioned checkpoints** under `.memoryhub/`. This plugin wires that into dsh: - **Auto-load on session start** — runs `mh load` in the session workspace and injects the checkpoint memory as durable plugin context. No prompt, no tool call; the model simply starts with its memory back. 

## 作者
**[solknight48](https://github.com/solknight48)**

## 链接

- [GitHub 仓库](https://github.com/solknight48/dsh-memoryhub)
- [完整 README](https://github.com/solknight48/dsh-memoryhub#readme)
- [返回dsh-memoryhub所在分类](../skills.md)
