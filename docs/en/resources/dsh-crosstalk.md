---
title: "dsh-crosstalk"
description: "dsh-crosstalk — cross-session messaging for DSH, Claude Code-style, plus event-driven auto-collab coordination"
keywords: "dsh-crosstalk, multi-agent, agent, coding, deepseek harness, dsh"
---
# dsh-crosstalk

> ⭐ **3** · ✅ active · agent

| | | | |
|---|---|---|---|
| Type | agent | Category | Multi-agent |
| Stars | ⭐ 3 | Status | ✅ active |
| Author | [lileikeji](https://github.com/lileikeji) | Updated | — |

## One-liner

> dsh-crosstalk — cross-session messaging for DSH, Claude Code-style, plus event-driven auto-collab coordination

## About

**Cross-session messaging for DSH.** Any session on the machine can list and message any other — Claude Code-style horizontal messaging, no daemon. `dsh-crosstalk` is a DeepSeek Harness bundle. Every session running the bundle publishes a heartbeat to a local registry under `~/.dsh/crosstalk/` (files + atomic rename, no daemon — if two sessions can see the same home directory, they can message). Each session gets a stable name (`-`, e.g. `dsh-cowork-amber`) plus a durable ref id; any session can list the live ones and send a message that arrives in the target as a **clearly-labeled turn** — `[message from session dsh-cowork-amber (/Users/me/projects/dsh-cowork)]` — with the sender's name riding along, so replying is just `send_message` back.

## 📦 Install

```bash
dsh plugin --profile web add github:Jesse-njx/dsh-crosstalk
dsh plugin --profile <other-profile> add github:Jesse-njx/dsh-crosstalk
```

## 🚀 Quick Start

```bash
git clone https://github.com/Jesse-njx/dsh-crosstalk
cd dsh-crosstalk
pnpm install
pnpm build
dsh plugin --profile web add "$PWD"
dsh plugin --profile <other-profile> add "$PWD"
```

## 📚 Learn more

**Config**

Adding the bundle mounts the plugin automatically (its `cordis.patch.yml` inserts the `crosstalk` entry). To override any field, target that entry by id in your profile's `cordis.patch.yml` — do **not** insert a second `crosstalk` row (that is a duplicate-entry error):

## 🔗 Links

- [GitHub Repository](https://github.com/lileikeji/dsh-crosstalk)
- [Full README](https://github.com/lileikeji/dsh-crosstalk#readme)
- [Back to the Agents & Multi-Agent list](../agents.md)
