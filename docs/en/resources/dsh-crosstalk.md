---
title: "dsh-crosstalk"
description: "Cross-session messaging: DSH sessions on the same machine can discover, message and coordinate with each other."
keywords: "dsh-crosstalk, multi-agent, agent, deepseek harness, dsh"
---
# dsh-crosstalk

> ⭐ 2 · ✅ active · agent

## One-liner

Cross-session messaging: DSH sessions on the same machine can discover, message and coordinate with each other.

## About

**Cross-session messaging for DSH.** Any session on the machine can list and message any other — Claude Code-style horizontal messaging, no daemon. `dsh-crosstalk` is a DeepSeek Harness bundle. Every session running the bundle publishes a heartbeat to a local registry under `~/.dsh/crosstalk/` (files + atomic rename, no daemon — if two sessions can see the same home directory, they can message). Each session gets a stable name (`<repo-or-cwd-slug>-<adjective>`, e.g. `dsh-cowork-amber`) plus a du

## Author
**[Jesse-njx](https://github.com/Jesse-njx)**

## Links

- [GitHub Repository](https://github.com/Jesse-njx/dsh-crosstalk)
- [Full README](https://github.com/Jesse-njx/dsh-crosstalk#readme)
- [Back to the Agents & Multi-Agent list](../agents.md)
