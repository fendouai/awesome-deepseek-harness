---
title: "dsh-explain"
description: "Local-first learning mode: cross-session global learning threads, explain-by-source, ExplainContext and compression."
keywords: "dsh-explain, learning, tutorial, context, deepseek harness, dsh"
---
# dsh-explain

> ⭐ **11** · ✅ active · tutorial · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | tutorial | Category | Learning |
| Stars | ⭐ 11 | Status | ✅ active |
| Author | [yuezengwu](https://github.com/yuezengwu) | Updated | 2026-08-20 |

## One-liner

> Local-first learning mode: cross-session global learning threads, explain-by-source, ExplainContext and compression.

## About

The 28-second preview runs against real assembled DSH Web `0.1.2-alpha.5` with deterministic, private fixture data. [Watch the higher-quality MP4](docs/assets/dsh-explain-demo.mp4) or read the [recording contract](docs/DEMO.md).

## 📦 Install

```bash
npx @deepseek-ai/dsh@0.1.2-alpha.5 plugin --profile web add github:yuezengwu/dsh-explain
npx @deepseek-ai/dsh@0.1.2-alpha.5 --profile web
```

## 🚀 Quick Start

```bash
pnpm install
DSH_SOURCE_DIR=/absolute/path/to/dsh pnpm dsh:link
DSH_SOURCE_DIR=/absolute/path/to/dsh pnpm dsh:link:check
pnpm typecheck
pnpm test
DSH_SOURCE_DIR=/absolute/path/to/dsh pnpm test:web
DSH_SOURCE_DIR=/absolute/path/to/dsh pnpm test:m6
pnpm build
```

## 📚 Learn more

**Quick start**

Current `main` targets DSH `0.1.2-alpha.5`: npx @deepseek-ai/dsh@0.1.2-alpha.5 plugin --profile web add github:yuezengwu/dsh-explain npx @deepseek-ai/dsh@0.1.2-alpha.5 --profile web Open **Settings → Learning**, choose an auxiliary provider and model, enable learning mode, and save. Explain observes only future completed top-level turns; it does not scan existing history. Git-hosted plugins build 

## 🔗 Links

- [GitHub Repository](https://github.com/yuezengwu/dsh-explain)
- [Full README](https://github.com/yuezengwu/dsh-explain#readme)
- [Back to the Tutorials & Learning list](../tutorials.md)
