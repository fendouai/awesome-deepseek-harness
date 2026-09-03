---
title: "dsh-routed-subagent"
description: "从任意会话派发一个完整挂载到任意 agent preset 的一次性子代理，支持按次指定模型/provider、模型可用性预检，以及外部 CLI 引擎（codex / claude / codebuddy），支持后台任务、实时进度、终止与可续会话。"
keywords: "dsh-routed-subagent, developer, plugin, multi-agent, deepseek harness, dsh"
---
# dsh-routed-subagent

> ⭐ **0** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 0 | 状态 | ✅ 活跃 |
| 作者 | [bpc-oss](https://github.com/bpc-oss) | 更新时间 | 2026-08-21 |
| 子分类 | 🛡️ 安全与运维 | 能力 | multi-agent |

## 一句话介绍

> 从任意会话派发一个完整挂载到任意 agent preset 的一次性子代理，支持按次指定模型/provider、模型可用性预检，以及外部 CLI 引擎（codex / claude / codebuddy），支持后台任务、实时进度、终止与可续会话。

## 详细介绍

A global [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) plugin that lets **any session dispatch a one-shot subagent fully mounted on ANY agent preset**, with **per-call model/provider override** and a **model-availability pre-check**. The stock `subagent` / `subagent_fork` tools force children to inherit the PARENT's preset. This plugin replaces that with a custom subagent provider whose async child setup calls `agentPresets.mount(childCtx, )` — so the child adopts the TARGET preset's complete composition: persona, prompt sections, skill catalog, and tools.

## ✨ 核心特性

- **Background by default, parallel dispatch** — the call returns a job id immediately (like the stock subagent tool); the conversation stays free to do other wor
- **Full preset mount** — the child runs under the target preset's standing composition (not a persona copy): identity, mission section, skills, tools.
- **Per-call model override** — `model` / `provider` arguments route the child's LLM call to a different model than this session's (via the official `resolveChild
- **Model pre-check** — an invalid model fails fast with the provider's candidate list instead of an opaque child failure.
- **Official subagent ecosystem** — one-shot lifecycle events, UI rows, trajectory; returns the child's final output.
- **Idempotent provider registration** — multiple presets can mount the row; the host-plane provider registry is never duplicated.

## 🚀 快速开始

```bash
// external codex subagent (background, explicit model, live progress)
await subagent_routed({
  engine: 'codex',
  provider: undefined,       // external engines ignore the DSH provider
  model: 'gpt-5.6-sol',      // explicit codex thread model
  prompt: '...',
  run_in_background: true,
})
```

## 📚 更多信息

**1. Link the package into the harness install**

The plugin statically imports `@deepseek-ai/*` packages, which resolve via Node ESM from the package location. Create a `node_modules` junction/symlink in the package directory pointing at the harness install: :: Windows mklink /J "<plugin-dir>\node_modules" "<harness>\resources\host\node_modules"

**Usage**

subagent_routed(prompt="Use the dev engineer standard to review this repository", preset="dev", description="dev review") # background one-shot subagent_routed(prompt="Continue the review", preset="dev-reviewer", description="follow-up", fork=true) # inherits THIS conversation subagent_routed(preset="dev", prompt="Audit this repo", description="audit", continuable=true) # send_message(<subagentId>

## 🔗 链接

- [GitHub 仓库](https://github.com/bpc-oss/dsh-routed-subagent)
- [完整 README](https://github.com/bpc-oss/dsh-routed-subagent#readme)
- [返回dsh-routed-subagent所在分类](../plugins.md)
