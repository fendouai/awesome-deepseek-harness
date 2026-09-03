---
title: "deeptide"
description: "Swift-native macOS coding agent built by DeepSeek, for DeepSeek."
keywords: "deeptide, harness, related, coding, deepseek harness, dsh"
---
# deeptide

> ⭐ **1,091** · ✅ active · related · ⬆️ +3 recently

| | | | |
|---|---|---|---|
| Type | related | Category | Harness |
| Stars | ⭐ 1,091 | Status | ✅ active |
| Author | [paean-ai](https://github.com/paean-ai) | Updated | 2026-07-08 |

## One-liner

> Swift-native macOS coding agent built by DeepSeek, for DeepSeek.

## About

This repository is the **community front door for all three** — docs, FAQ, issue tracking — and is the home of two npm packages: - [`deeptide`](./package.json) — the current TypeScript/Bun CLI (forwards to [`@paean-ai/zero-cli`](https://www.npmjs.com/package/@paean-ai/zero-cli)) - [`deeptide-rs`](./npm/deeptide-rs) — the Rust CLI (ships a native binary via GitHub Releases postinstall) The two CLI packages **do not conflict** — they expose different binary names (`deeptide`/`tide` vs `deeptide-rs`) so you can install both and switch between them freely while we mature the Rust port. The Rust port lives under [`crates/`](./crates). It is intended to grow into the canonical cross-platform CLI over time, but the `deeptide` package will remain available as long as users find value in it — there

## ✨ Key Features

- **Multi-turn agentic loop** — plan → tool → observe → adapt
- **Streaming responses** — see the model think and act in real time
- **30+ built-in tools** — file I/O, shell, web, tasks, MCP, scheduling, sub-agents
- **25+ slash commands** — `/status`, `/cost`, `/diff`, `/init`, `/permission`, `/hooks`, …
- **Permission modes** — default · accept-edits · plan · bypass
- **Hooks engine** — pre/post tool, user-prompt, session, compaction shell hooks
- **Memory system** — persistent project memory across sessions
- **Sub-agents from markdown** — define custom agents in your project

## 📦 Install

```bash
# bun (recommended, fastest install)
bun add -g deeptide

# npm (works too; bun is still required at runtime)
npm install -g deeptide

# pnpm
pnpm add -g deeptide
```

## 🚀 Quick Start

```bash
tide                          # interactive REPL (preferred — short)
deeptide                      # same thing, full name
tide -p "explain this repo"   # one-shot mode
tide --help                   # all options
```

## 📚 Learn more

**Install on macOS (recommended)**

For Mac users, the recommended path is the native Deeptide build from [deeptide.sh](https://deeptide.sh/). It downloads the signed build for your Mac architecture and installs both `deeptide` and the shorter `tide` command: curl -fsSL https://deeptide.sh/install.sh | sh Then start with: tide auth login # Paean OAuth, multimodal-aware tide login # or save a DeepSeek API key directly tide # launch t

**Install on Linux / Windows (Zero CLI alias)**

> **Prerequisite:** [Bun](https://bun.com/) must be installed and on > PATH. The CLI runtime requires it (matches the underlying > [Zero CLI](https://github.com/a8e-ai/zero-cli)). Bun does not > replace your Node install — it sits alongside. On non-Mac systems, this npm package is the cross-platform DeepTide-flavored entrypoint powered by [Zero CLI](https://github.com/a8e-ai/zero-cli). It installs

**Quick start (CLI)**

DeepTide CLI talks to the **DeepSeek API** by default (matching the DeepTide native app), and can also drive any Anthropic-protocol-compatible endpoint via BYOK — Zhipu GLM, Volcengine, Paean, Qwen, Moonshot, self-hosted gateways, and so on.

## 🔗 Links

- [GitHub Repository](https://github.com/paean-ai/deeptide)
- [Full README](https://github.com/paean-ai/deeptide#readme)
- [Back to the Related Agent Harnesses list](../related.md)
