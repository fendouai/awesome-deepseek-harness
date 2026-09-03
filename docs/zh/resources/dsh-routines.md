---
title: "dsh-routines"
description: "dsh-routines — scheduled agents for DSH: run a prompt on a cron, get the digest where you already are (file digests, chatnode delivery, unattended-safe)"
keywords: "dsh-routines, developer, plugin, coding, multi-agent, deepseek harness, dsh"
---
# dsh-routines

> ⭐ **1** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 1 | 状态 | ✅ 活跃 |
| 作者 | [Jesse-njx](https://github.com/Jesse-njx) | 更新时间 | — |
| 子分类 | 📁 文件与导入 | 能力 | coding, multi-agent |

## 一句话介绍

> dsh-routines — scheduled agents for DSH: run a prompt on a cron, get the digest where you already are (file digests, chatnode delivery, unattended-safe)

## 详细介绍

Scheduled agents for DSH — run a prompt on a cron, get the digest where you already are. `dsh-routines` is a plugin bundle for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness). A **routine** is a named prompt + schedule + delivery stored as a plain YAML file — human-diffable, git-committable. The scheduler launches each due run through the headless runner as its **own one-shot session** (full session log = full audit, replay-able later by dsh-replay), then delivers a digest: the last assistant message when it is short, otherwise a one-shot summarizer call over the session log. ┌──────────────────────┐ every night 02:00 ┌──────────────────────────────┐ │ dsh --profile ops │ ─────────────────────▶ │ dsh --profile headless │ │ scheduler tick │ (own session, cwd │ "run the t

## 📦 安装

```bash
dsh plugin --profile web add @dsh-routines/bundle
```

## 🚀 快速开始

```bash
pnpm install
pnpm build      # tsc -> lib/
pnpm test       # node --test (46 tests: cron, scheduler matrix, store, run, cli, e2e)
```

## 📚 更多信息

**Flagship demo — nightly test triage**

A routine that runs your test suite at 2am, diagnoses the top failure, and leaves a digest in the project — then, with a conversation node installed, that digest lands in WeChat and you reply to approve follow-ups (v0.2; v0.1 delivers to file and chatnode when a node is installed).

**Architecture**

One bundle, three plugins (+ a run driver), all installable as subpaths: Runs boot `dsh --profile <routine.profile> --patch <generated overlay> -- "<prompt>"` with the routine's cwd as the workspace. The overlay disables the stock headless runner, mounts the `run` driver on the same task service, and forces the unattended approval policy — so the run keeps the full headless experience (fresh persi

## 🔗 链接

- [GitHub 仓库](https://github.com/Jesse-njx/dsh-routines)
- [完整 README](https://github.com/Jesse-njx/dsh-routines#readme)
- [返回dsh-routines所在分类](../plugins.md)
