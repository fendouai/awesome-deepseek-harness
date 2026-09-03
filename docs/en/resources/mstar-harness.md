---
title: "mstar-harness"
description: "Skill-driven harness/loop engineering workflow agent: tune agent loops as a first-class workflow."
keywords: "mstar-harness, workflow, multi-agent, deepseek harness, dsh"
---
# mstar-harness

> ⭐ **52** · ✅ active · workflow · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | workflow | Category | Workflows |
| Stars | ⭐ 52 | Status | ✅ active |
| Author | [btspoony](https://github.com/btspoony) | Updated | 2026-08-21 |

## One-liner

> Skill-driven harness/loop engineering workflow agent: tune agent loops as a first-class workflow.

## About

Harness Workflow Engine · Agent Plugin English / [中文](README_CN.md) GitHub · Issues **Morning Star** is an Agent Plugin for harness engineering workflows: a TypeScript **Harness Workflow Engine** (`@mstar-harness/engine`) enforces deterministic workflow gates, while `mstar-*` judgment skills drive multi-agent code delivery. - **Deterministic gates, enforced by a TS engine** — path/status/lease/dispatch/sdd/iteration/lint gates run in `@mstar-harness/engine`, not as prompt suggestions - **Judgment stays in `mstar-*` skills** — skills remain the single source of truth (SSOT) for roles, gates, and workflow judgment - **One engine across hosts** — the same engine + skills power dsh (DeepSeek Harness), omp, OpenCode, Cursor, Kimi Code, ZCode, and Codex - **Agent Plugin packaging** — one-command

## ✨ Key Features

- **Deterministic gates, enforced by a TS engine** — path/status/lease/dispatch/sdd/iteration/lint gates run in `@mstar-harness/engine`, not as prompt suggestions
- **Judgment stays in `mstar-*` skills** — skills remain the single source of truth (SSOT) for roles, gates, and workflow judgment
- **One engine across hosts** — the same engine + skills power dsh (DeepSeek Harness), omp, OpenCode, Cursor, Kimi Code, ZCode, and Codex
- **Agent Plugin packaging** — one-command install; portable across any Agent Plugins v1.0.0 client
- **Pluggable JSON persistence** — coordination docs (`status.json`, workflow snapshots, project residuals, review envelopes) persist through an `ArtifactStore`; 
- **Recommended host** (best → usable): **dsh = omp ≥ OpenCode ≥ Cursor > Kimi = ZCode > Codex**

## 📦 Install

```bash
npm i -g @mstar-harness/cli
```

## 🔗 Links

- [GitHub Repository](https://github.com/btspoony/mstar-harness)
- [Full README](https://github.com/btspoony/mstar-harness#readme)
- [Back to the Workflows & Automation list](../workflows.md)
