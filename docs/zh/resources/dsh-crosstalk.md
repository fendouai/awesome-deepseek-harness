---
title: "dsh-crosstalk"
description: "跨会话消息：同机 DSH 会话之间可发现、互发消息并协同。"
keywords: "dsh-crosstalk, multi-agent, agent, deepseek harness, dsh"
---
# dsh-crosstalk

> ⭐ 2 · ✅ 活跃 · 智能体

## 一句话介绍

跨会话消息：同机 DSH 会话之间可发现、互发消息并协同。

## 详细介绍

**Cross-session messaging for DSH.** Any session on the machine can list and message any other — Claude Code-style horizontal messaging, no daemon. `dsh-crosstalk` is a DeepSeek Harness bundle. Every session running the bundle publishes a heartbeat to a local registry under `~/.dsh/crosstalk/` (files + atomic rename, no daemon — if two sessions can see the same home directory, they can message). Each session gets a stable name (`<repo-or-cwd-slug>-<adjective>`, e.g. `dsh-cowork-amber`) plus a du

## 作者
**[Jesse-njx](https://github.com/Jesse-njx)**

## 链接

- [GitHub 仓库](https://github.com/Jesse-njx/dsh-crosstalk)
- [完整 README](https://github.com/Jesse-njx/dsh-crosstalk#readme)
- [返回dsh-crosstalk所在分类](../agents.md)
