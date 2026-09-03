---
title: "dsh-crosstalk"
description: "dsh-crosstalk — cross-session messaging for DSH, Claude Code-style, plus event-driven auto-collab coordination"
keywords: "dsh-crosstalk, multi-agent, agent, coding, deepseek harness, dsh"
---
# dsh-crosstalk

> ⭐ **3** · ✅ 活跃 · 智能体

| | | | |
|---|---|---|---|
| 类型 | 智能体 | 分类 | 多智能体 |
| 星数 | ⭐ 3 | 状态 | ✅ 活跃 |
| 作者 | [lileikeji](https://github.com/lileikeji) | 更新时间 | — |

## 一句话介绍

> dsh-crosstalk — cross-session messaging for DSH, Claude Code-style, plus event-driven auto-collab coordination

## 详细介绍

**Cross-session messaging for DSH.** Any session on the machine can list and message any other — Claude Code-style horizontal messaging, no daemon. `dsh-crosstalk` is a DeepSeek Harness bundle. Every session running the bundle publishes a heartbeat to a local registry under `~/.dsh/crosstalk/` (files + atomic rename, no daemon — if two sessions can see the same home directory, they can message). Each session gets a stable name (`-`, e.g. `dsh-cowork-amber`) plus a durable ref id; any session can list the live ones and send a message that arrives in the target as a **clearly-labeled turn** — `[message from session dsh-cowork-amber (/Users/me/projects/dsh-cowork)]` — with the sender's name riding along, so replying is just `send_message` back.

## 📦 安装

```bash
dsh plugin --profile web add github:Jesse-njx/dsh-crosstalk
dsh plugin --profile <other-profile> add github:Jesse-njx/dsh-crosstalk
```

## 🚀 快速开始

```bash
git clone https://github.com/Jesse-njx/dsh-crosstalk
cd dsh-crosstalk
pnpm install
pnpm build
dsh plugin --profile web add "$PWD"
dsh plugin --profile <other-profile> add "$PWD"
```

## 📚 更多信息

**Config**

Adding the bundle mounts the plugin automatically (its `cordis.patch.yml` inserts the `crosstalk` entry). To override any field, target that entry by id in your profile's `cordis.patch.yml` — do **not** insert a second `crosstalk` row (that is a duplicate-entry error):

## 🔗 链接

- [GitHub 仓库](https://github.com/lileikeji/dsh-crosstalk)
- [完整 README](https://github.com/lileikeji/dsh-crosstalk#readme)
- [返回dsh-crosstalk所在分类](../agents.md)
