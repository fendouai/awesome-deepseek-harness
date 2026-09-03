---
title: "dsh-multica-runtime"
description: "Support the dsh runtime on Multica."
keywords: "dsh-multica-runtime, desktop, client, deepseek harness, dsh"
---
# dsh-multica-runtime

> ⭐ **53** · ✅ active · client · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | client | Category | Desktop |
| Stars | ⭐ 53 | Status | ✅ active |
| Author | [multica-ai](https://github.com/multica-ai) | Updated | 2026-08-14 |

## One-liner

> Support the dsh runtime on Multica.

## About

Private, out-of-tree runtime bridge between Multica and the public [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness). It exposes a versioned JSONL protocol over stdio and composes over `@deepseek-ai/dsh-base`. It does not require changes to DeepSeek Harness.

## ✨ Key Features

- This repository contains only the Multica integration layer. It does not
- Never commit API keys, MCP secrets, session logs, or generated profiles.
- DSH telemetry is disabled by the bundle patch.
- stdout is protocol-only; diagnostics go to stderr.

## 📦 Install

```bash
pnpm install
pnpm check
pnpm build
```

## 🚀 Quick Start

```bash
dsh plugin --profile multica add /absolute/path/to/multica-dsh-runtime
```

## 🔗 Links

- [GitHub Repository](https://github.com/multica-ai/dsh-multica-runtime)
- [Full README](https://github.com/multica-ai/dsh-multica-runtime#readme)
- [Back to the Clients (Desktop & TUI) list](../clients.md)
