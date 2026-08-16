---
title: "dsh-memoryhub"
description: "MemoryHub (mh) plugin for DeepSeek Harness (dsh): auto-loads checkpoint memory on session start, adds mh_* tools and the mh skill, and a Memory tab in the web UI"
keywords: "dsh-memoryhub, learning, skill, coding, memory, ui, deepseek harness, dsh"
---
# dsh-memoryhub

> ⭐ 3 · ✅ active · skill

## One-liner

MemoryHub (mh) plugin for DeepSeek Harness (dsh): auto-loads checkpoint memory on session start, adds mh_* tools and the mh skill, and a Memory tab in the web UI

## About

[MemoryHub](https://github.com/solknight48/memoryhub) (`mh`) integration for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`). MemoryHub keeps project memory as **purified sessions in git-versioned checkpoints** under `.memoryhub/`. This plugin wires that into dsh: - **Auto-load on session start** — runs `mh load` in the session workspace and injects the checkpoint memory as durable plugin context. No prompt, no tool call; the model simply starts with its memory back. 

## Author
**[solknight48](https://github.com/solknight48)**

## Links

- [GitHub Repository](https://github.com/solknight48/dsh-memoryhub)
- [Full README](https://github.com/solknight48/dsh-memoryhub#readme)
- [Back to the Skills list](../skills.md)
