---
title: "dsh-llm-fallbacks"
description: "An dsh plugin for role-based LLM retry&fallback strategy. 基于角色的模型重试备用策略插件"
keywords: "dsh-llm-fallbacks, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-llm-fallbacks

> ⭐ **20** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 20 | 状态 | ✅ 活跃 |
| 作者 | [omdsh-dev](https://github.com/omdsh-dev) | 更新时间 | — |

## 一句话介绍

> An dsh plugin for role-based LLM retry&fallback strategy. 基于角色的模型重试备用策略插件

## 详细介绍

[English](README.md) | [中文](README.zh-CN.md) Automatic provider/model fallback chains for dsh (DeepSeek Harness): when an agent's LLM requests keep failing — retries exhausted, auth errors, quota exceeded, rate limiting (429) — the plugin switches provider/model along the fallback chain for the current role, and the current step/turn continues on the target model: tasks are not interrupted by model problems. Works in both dsh front ends: the **web** profile (Settings → Plugins → Fallbacks card) and the **dsh-tui** terminal profile (`/fallbacks` session diagnostics, `/fallbacks config` readback, and the `/settings` fallbacks section for editing).

## ✨ 核心特性

- **Automatic fallback for root and subagents**: any agent switches down the chain to the next available provider/model on model failure — no manual model switchi
- **Two-block config**: `rootChain` for the root agent; declared role entities (`roles.list`) referenced by `roles.rules` (or the built-in `inherit`).
- **Chain as root primary from the picker**: when `enabled` is on, the host model picker (web and TUI alike) shows a virtual `FallbacksChain` / `Auto` row — selec
- **Time slots**: optional `fallbacks.timeSlots` rows rotate the effective root chain by wall-clock windows in the config-level `tz` timezone (default `Asia/Shang
- **Dispatch-time role resolution**: on a subagent's first request its role is resolved in three stages — explicit (`agentPreset` matches a declared role id) → de
- **Cooldown and revert**: failed / switched-away models are not re-selected during cooldown; `revertPolicy: cooldown-expiry` returns to the primary model automat
- **Host subagent model policy (dsh 0.1.2)**: when the host `subagent-model-selection` policy is enabled, its allowlist is a hard constraint on every plugin-origi
- **Half-open recovery (opt-in)**: `recovery: half-open` makes recovery evidence-driven — an expired cooldown leaves the route half-open for one logged probe inst

## 📦 安装

```bash
dsh plugin --profile web add dsh-llm-fallbacks      # web profile (Settings → Fallbacks card)
dsh plugin --profile dsh-tui add dsh-llm-fallbacks  # dsh-tui terminal profile
```

## 🚀 快速开始

```bash
git clone https://github.com/omdsh-dev/dsh-llm-fallbacks.git
cd dsh-llm-fallbacks
pnpm install
pnpm repair:fallbacks-switch-logs -- --dry-run            # preview which sessions would change
pnpm repair:fallbacks-switch-logs -- --apply --backup     # mark legacy events ignorable
```

## 📚 更多信息

**Install**

dsh plugin --profile web add dsh-llm-fallbacks # web profile (Settings → Fallbacks card) dsh plugin --profile dsh-tui add dsh-llm-fallbacks # dsh-tui terminal profile Same plugin, either front end — the only difference is the `--profile` flag. Pin a version with `@<version>`. A registry install fetches the **built package** (`dist/`), nothing builds on the target machine. Registry / git / local-di

**Configuration surfaces**

The plugin's settings live in a shared `fallbacks:` namespace, editable from three surfaces: Pick the surface that matches your front end: web users get the card, terminal users get `/settings`, and the YAML file works everywhere. (`/fallbacks` and `/fallbacks config` are diagnostics — read-only views, not edit surfaces.)

**Minimal configuration**

Add a `fallbacks:` section to the shared settings document (`$DSH_HOME/settings.yaml` — see [Configuration surfaces](#configuration-surfaces)): fallbacks: enabled: true # feature switch — defaults to off (plugin is a no-op otherwise) rootChain: # all-day chain: leading entries = fallback walk, last = Default model (official V4) - anthropic/claude-3-5-sonnet # walked first - deepseek-official/deeps

## 🔗 链接

- [GitHub 仓库](https://github.com/omdsh-dev/dsh-llm-fallbacks)
- [完整 README](https://github.com/omdsh-dev/dsh-llm-fallbacks#readme)
- [返回dsh-llm-fallbacks所在分类](../plugins.md)
