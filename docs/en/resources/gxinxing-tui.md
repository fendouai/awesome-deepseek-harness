---
title: "deepseek-harness-tui (gxinxing)"
description: "Terminal-native interactive TUI built with Ink (React for terminals)."
keywords: "deepseek-harness-tui (gxinxing), terminal, client, deepseek harness, dsh"
---
# deepseek-harness-tui (gxinxing)

> ⭐ **7** · ✅ active · client

| | | | |
|---|---|---|---|
| Type | client | Category | Terminal |
| Stars | ⭐ 7 | Status | ✅ active |
| Author | [gxinxing](https://github.com/gxinxing) | Updated | 2026-08-13 |

## One-liner

> Terminal-native interactive TUI built with Ink (React for terminals).

## About

**An interactive terminal chat for DeepSeek Harness — terminal-native style, built with Ink (React for terminals).** Give it a TokenDance key and a `dsh` install; run `dsh --profile tui` and you get a zero-chrome terminal chat with DeepSeek models: bottom-anchored transcript, tool calls folded into cells, thinking folding, and a theme that adapts to your terminal via OSC 11. It's a thin, readable plugin (~800 lines of UI) — not a re-implementation of the harness. [English](README.md) · [简体中文](README.zh-CN.md)

## ✨ Key Features

- **Terminal-native UI, not a re-skinned echo.** The transcript is the surface — no boxes, no chrome. The DeepSeek brand banner (ANSI Shadow logo, gradient) greet
- **Tool calls fold into cells.** `⠋ Running <cmd>` while active → `✓ <cmd> • 1.2s` (or `✗` on error), with output merged into the cell, dimmed, and truncated hea
- **Theme derived from your terminal.** OSC 11 probes the real background: message tints and code chips are blended from it (12% white over dark, 4% black over li
- **Thinking you can fold.** `ctrl + t` toggles the reasoning trace; `esc` aborts the turn at any time via `agent.cancel({ kind: 'user' })`.
- **Markdown that keeps its shape.** Headers keep their `#`, fenced blocks keep their fences, inline code gets a subtle chip — and CJK/emoji wrap at correct chara
- **A live viewport.** The transcript is bottom-anchored; the tail is always visible. Busy state shows a braille spinner + compact elapsed timer (`Working 5s`).

## 📦 Install

```bash
npm install -g @deepseek-ai/dsh        # the harness (no Homebrew tap yet)
git clone https://github.com/gxinxing/deepseek-harness-tui
cd deepseek-harness-tui && pnpm install
```

## 🚀 Quick Start

```bash
dsh plugin --profile tui add @deepseek-ai/dsh-headless
dsh plugin --profile tui add /path/to/deepseek-harness-tui
```

## 📚 Learn more

**Install**

Requires **Node.js ≥ 20** and the [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) CLI: npm install -g @deepseek-ai/dsh # the harness (no Homebrew tap yet) git clone https://github.com/gxinxing/deepseek-harness-tui cd deepseek-harness-tui && pnpm install Wire the plugin bundle into the `tui` profile (one-time): dsh plugin --profile tui add @deepseek-ai/dsh-headless dsh plugin --

## 🔗 Links

- [GitHub Repository](https://github.com/gxinxing/deepseek-harness-tui)
- [Full README](https://github.com/gxinxing/deepseek-harness-tui#readme)
- [Back to the Clients (Desktop & TUI) list](../clients.md)
