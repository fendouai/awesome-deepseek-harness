---
title: "deeptide"
description: "DeepSeek 官方出品的 Swift 原生 macOS 编码 Agent。"
keywords: "deeptide, harness, related, coding, deepseek harness, dsh"
---
# deeptide

> ⭐ **1,091** · ✅ 活跃 · 相关 · 近期 ⬆️ +3

| | | | |
|---|---|---|---|
| 类型 | 相关 | 分类 | Harness |
| 星数 | ⭐ 1,091 | 状态 | ✅ 活跃 |
| 作者 | [paean-ai](https://github.com/paean-ai) | 更新时间 | 2026-07-08 |

## 一句话介绍

> DeepSeek 官方出品的 Swift 原生 macOS 编码 Agent。

## 详细介绍

This repository is the **community front door for all three** — docs, FAQ, issue tracking — and is the home of two npm packages: - [`deeptide`](./package.json) — the current TypeScript/Bun CLI (forwards to [`@paean-ai/zero-cli`](https://www.npmjs.com/package/@paean-ai/zero-cli)) - [`deeptide-rs`](./npm/deeptide-rs) — the Rust CLI (ships a native binary via GitHub Releases postinstall) The two CLI packages **do not conflict** — they expose different binary names (`deeptide`/`tide` vs `deeptide-rs`) so you can install both and switch between them freely while we mature the Rust port. The Rust port lives under [`crates/`](./crates). It is intended to grow into the canonical cross-platform CLI over time, but the `deeptide` package will remain available as long as users find value in it — there

## ✨ 核心特性

- **Multi-turn agentic loop** — plan → tool → observe → adapt
- **Streaming responses** — see the model think and act in real time
- **30+ built-in tools** — file I/O, shell, web, tasks, MCP, scheduling, sub-agents
- **25+ slash commands** — `/status`, `/cost`, `/diff`, `/init`, `/permission`, `/hooks`, …
- **Permission modes** — default · accept-edits · plan · bypass
- **Hooks engine** — pre/post tool, user-prompt, session, compaction shell hooks
- **Memory system** — persistent project memory across sessions
- **Sub-agents from markdown** — define custom agents in your project

## 📦 安装

```bash
# bun (recommended, fastest install)
bun add -g deeptide

# npm (works too; bun is still required at runtime)
npm install -g deeptide

# pnpm
pnpm add -g deeptide
```

## 🚀 快速开始

```bash
tide                          # interactive REPL (preferred — short)
deeptide                      # same thing, full name
tide -p "explain this repo"   # one-shot mode
tide --help                   # all options
```

## 📚 更多信息

**Install on macOS (recommended)**

For Mac users, the recommended path is the native Deeptide build from [deeptide.sh](https://deeptide.sh/). It downloads the signed build for your Mac architecture and installs both `deeptide` and the shorter `tide` command: curl -fsSL https://deeptide.sh/install.sh | sh Then start with: tide auth login # Paean OAuth, multimodal-aware tide login # or save a DeepSeek API key directly tide # launch t

**Install on Linux / Windows (Zero CLI alias)**

> **Prerequisite:** [Bun](https://bun.com/) must be installed and on > PATH. The CLI runtime requires it (matches the underlying > [Zero CLI](https://github.com/a8e-ai/zero-cli)). Bun does not > replace your Node install — it sits alongside. On non-Mac systems, this npm package is the cross-platform DeepTide-flavored entrypoint powered by [Zero CLI](https://github.com/a8e-ai/zero-cli). It installs

**Quick start (CLI)**

DeepTide CLI talks to the **DeepSeek API** by default (matching the DeepTide native app), and can also drive any Anthropic-protocol-compatible endpoint via BYOK — Zhipu GLM, Volcengine, Paean, Qwen, Moonshot, self-hosted gateways, and so on.

## 🔗 链接

- [GitHub 仓库](https://github.com/paean-ai/deeptide)
- [完整 README](https://github.com/paean-ai/deeptide#readme)
- [返回deeptide所在分类](../related.md)
