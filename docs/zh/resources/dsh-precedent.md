---
title: "dsh-precedent"
description: "Evidence-backed working memory for DeepSeek Harness: a cited ledger of what already worked in this workspace, built from the session log you already have. No index, no model, no capture step."
keywords: "dsh-precedent, memory, plugin, coding, ui, deepseek harness, dsh"
---
# dsh-precedent

> ⭐ **0** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 记忆与上下文 |
| 星数 | ⭐ 0 | 状态 | ✅ 活跃 |
| 作者 | [dshplugin-me](https://github.com/dshplugin-me) | 更新时间 | 2026-08-16 |
| 子分类 | 🧠 记忆系统 | 能力 | coding, memory, ui |

## 一句话介绍

> Evidence-backed working memory for DeepSeek Harness: a cited ledger of what already worked in this workspace, built from the session log you already have. No index, no model, no capture step.

## 详细介绍

**Your agent forgets. Your log doesn't.** A [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) plugin that reads the session log DSH already writes and hands the agent a short, **cited** ledger of what has actually worked in this workspace — the commands that succeed, the ones that reliably fail, and the variant that fixed them. No capture step. No index to build. No model to download. It works on sessions recorded **before** you installed it.

## ✨ 核心特性

- **Not a search tool.** It does not answer "what did we discuss in June". It answers "what already works here", before you ask. If you want verbatim transcript r
- **Not a note-taker.** Nothing asks you to write memories. There is no capture step to forget to run.
- **Not context stuffing.** The injected section is capped and prefix-stable, so it costs a fixed small number of tokens and does not invalidate the KV cache betw
- **Not a replacement for `AGENTS.md`.** Hand-written intent still wins. Precedent covers the part nobody keeps up to date: what actually happened.
- **Not cross-workspace.** By design. See below.

## 📦 安装

```bash
dsh plugin --profile web add 'github:dshplugin-me/dsh-precedent#v0.1.0'
```

## 🚀 快速开始

```bash
dsh --profile web --dump-config   # look for the "# == dsh-precedent" layer
dsh --profile web
```

## 📚 更多信息

**Example**

Launch as usual: $ dsh --profile web The agent's system prompt gains one section — this is the renderer's real output, with commands that never work sorted above commands that always do:

**Install**

dsh plugin --profile web add 'github:dshplugin-me/dsh-precedent#v0.1.0' No global `dsh` on PATH? Use `npx -y @deepseek-ai/dsh plugin --profile web add …`. Running dsh from a source checkout? Use `pnpm dsh plugin …` from the checkout root. Replace `web` with whichever profile you actually launch. Pinning the version is deliberate: an unpinned git install resolves to whatever `main` points at right 

**Configuration**

name: dsh-precedent config: maxEntries: 40 # ledger lines injected per session minRuns: 2 # ignore commands seen only once lookbackDays: 90 # ignore sessions older than this maxSessions: 200 # upper bound on logs read in one build buildTimeoutMs: 5000 # stop blocking the first step after this Scope is not configurable: sessions are matched on exact `cwd` string equality, the same conservative rule

**Roadmap**

Interfaces above are frozen against `deepseek-ai/deepseek-harness@47f943859bef` (read 2026-08-16). Anything that changes upstream will be noted here rather than silently adjusted.

## 🔗 链接

- [GitHub 仓库](https://github.com/dshplugin-me/dsh-precedent)
- [完整 README](https://github.com/dshplugin-me/dsh-precedent#readme)
- [返回dsh-precedent所在分类](../plugins.md)
