---
title: "dsh-advisor"
description: "Pair a second model that passively reviews each turn and injects notes."
keywords: "dsh-advisor, multi-agent, agent, context, deepseek harness, dsh"
---
# dsh-advisor

> ⭐ 9 · ✅ active · agent

## One-liner

Pair a second model that passively reviews each turn and injects notes.

## About

A standalone dsh plugin bundle porting the omp "advisor" subsystem: a per-session reviewer model that observes the primary transcript, reviews each stepped turn with an explicitly configured model (provider + model are required), and injects severity-ranked advice (nit / concern / blocker) back into the session — without polluting or recursively reviewing itself. Install with a single command: dsh plugin --profile web add dsh-advisor # <name> = your profile name **Advisory only.** The advisor ne

## Author
**[omdsh-dev](https://github.com/omdsh-dev)**

## Links

- [GitHub Repository](https://github.com/omdsh-dev/dsh-advisor)
- [Full README](https://github.com/omdsh-dev/dsh-advisor#readme)
- [Back to the Agents & Multi-Agent list](../agents.md)
