---
title: "mstar-harness"
description: "技能驱动的 Harness/Loop 工程工作流 Agent：把 Agent 循环调优作为一等工作流。"
keywords: "mstar-harness, workflow, multi-agent, deepseek harness, dsh"
---
# mstar-harness

> ⭐ **52** · ✅ 活跃 · 工作流 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 工作流 | 分类 | 工作流 |
| 星数 | ⭐ 52 | 状态 | ✅ 活跃 |
| 作者 | [btspoony](https://github.com/btspoony) | 更新时间 | 2026-08-21 |

## 一句话介绍

> 技能驱动的 Harness/Loop 工程工作流 Agent：把 Agent 循环调优作为一等工作流。

## 详细介绍

Harness Workflow Engine · Agent Plugin English / [中文](README_CN.md) GitHub · Issues **Morning Star** is an Agent Plugin for harness engineering workflows: a TypeScript **Harness Workflow Engine** (`@mstar-harness/engine`) enforces deterministic workflow gates, while `mstar-*` judgment skills drive multi-agent code delivery. - **Deterministic gates, enforced by a TS engine** — path/status/lease/dispatch/sdd/iteration/lint gates run in `@mstar-harness/engine`, not as prompt suggestions - **Judgment stays in `mstar-*` skills** — skills remain the single source of truth (SSOT) for roles, gates, and workflow judgment - **One engine across hosts** — the same engine + skills power dsh (DeepSeek Harness), omp, OpenCode, Cursor, Kimi Code, ZCode, and Codex - **Agent Plugin packaging** — one-command

## ✨ 核心特性

- **Deterministic gates, enforced by a TS engine** — path/status/lease/dispatch/sdd/iteration/lint gates run in `@mstar-harness/engine`, not as prompt suggestions
- **Judgment stays in `mstar-*` skills** — skills remain the single source of truth (SSOT) for roles, gates, and workflow judgment
- **One engine across hosts** — the same engine + skills power dsh (DeepSeek Harness), omp, OpenCode, Cursor, Kimi Code, ZCode, and Codex
- **Agent Plugin packaging** — one-command install; portable across any Agent Plugins v1.0.0 client
- **Pluggable JSON persistence** — coordination docs (`status.json`, workflow snapshots, project residuals, review envelopes) persist through an `ArtifactStore`; 
- **Recommended host** (best → usable): **dsh = omp ≥ OpenCode ≥ Cursor > Kimi = ZCode > Codex**

## 📦 安装

```bash
npm i -g @mstar-harness/cli
```

## 🔗 链接

- [GitHub 仓库](https://github.com/btspoony/mstar-harness)
- [完整 README](https://github.com/btspoony/mstar-harness#readme)
- [返回mstar-harness所在分类](../workflows.md)
