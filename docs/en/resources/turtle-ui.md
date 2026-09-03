---
title: "turtle-ui"
description: "Official UI plugin reference implementation."
keywords: "turtle-ui, learning, example, ui, coding, deepseek harness, dsh"
---
# turtle-ui

> ⭐ **8** · ✅ active · example · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | example | Category | Learning |
| Stars | ⭐ 8 | Status | ✅ active |
| Author | [turtle1999](https://github.com/turtle1999) | Updated | 2026-08-13 |

## One-liner

> Official UI plugin reference implementation.

## About

This repository contains the former `packages/ui/tui` implementation, its unit and terminal snapshot tests, and a dsh profile bundle patch. The TUI owns terminal presentation and input; DeepSeek Harness owns the agent, model, tools, persistence, and `dsh` launcher.

## 📦 Install

```bash
(cd ../deepseek-harness && pnpm install && pnpm run build)
pnpm install
pnpm run build
```

## 🚀 Quick Start

```bash
pnpm run build
dsh plugin --profile tui add file:.
dsh --profile tui
```

## 🔗 Links

- [GitHub Repository](https://github.com/turtle1999/turtle-ui)
- [Full README](https://github.com/turtle1999/turtle-ui#readme)
- [Back to the Examples & Starters list](../examples.md)
