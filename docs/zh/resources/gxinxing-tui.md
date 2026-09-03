---
title: "deepseek-harness-tui (gxinxing)"
description: "基于 Ink（终端 React）构建的终端原生交互 TUI。"
keywords: "deepseek-harness-tui (gxinxing), terminal, client, deepseek harness, dsh"
---
# deepseek-harness-tui (gxinxing)

> ⭐ **7** · ✅ 活跃 · 客户端

| | | | |
|---|---|---|---|
| 类型 | 客户端 | 分类 | 终端 |
| 星数 | ⭐ 7 | 状态 | ✅ 活跃 |
| 作者 | [gxinxing](https://github.com/gxinxing) | 更新时间 | 2026-08-13 |

## 一句话介绍

> 基于 Ink（终端 React）构建的终端原生交互 TUI。

## 详细介绍

**An interactive terminal chat for DeepSeek Harness — terminal-native style, built with Ink (React for terminals).** Give it a TokenDance key and a `dsh` install; run `dsh --profile tui` and you get a zero-chrome terminal chat with DeepSeek models: bottom-anchored transcript, tool calls folded into cells, thinking folding, and a theme that adapts to your terminal via OSC 11. It's a thin, readable plugin (~800 lines of UI) — not a re-implementation of the harness. [English](README.md) · [简体中文](README.zh-CN.md)

## ✨ 核心特性

- **Terminal-native UI, not a re-skinned echo.** The transcript is the surface — no boxes, no chrome. The DeepSeek brand banner (ANSI Shadow logo, gradient) greet
- **Tool calls fold into cells.** `⠋ Running <cmd>` while active → `✓ <cmd> • 1.2s` (or `✗` on error), with output merged into the cell, dimmed, and truncated hea
- **Theme derived from your terminal.** OSC 11 probes the real background: message tints and code chips are blended from it (12% white over dark, 4% black over li
- **Thinking you can fold.** `ctrl + t` toggles the reasoning trace; `esc` aborts the turn at any time via `agent.cancel({ kind: 'user' })`.
- **Markdown that keeps its shape.** Headers keep their `#`, fenced blocks keep their fences, inline code gets a subtle chip — and CJK/emoji wrap at correct chara
- **A live viewport.** The transcript is bottom-anchored; the tail is always visible. Busy state shows a braille spinner + compact elapsed timer (`Working 5s`).

## 📦 安装

```bash
npm install -g @deepseek-ai/dsh        # the harness (no Homebrew tap yet)
git clone https://github.com/gxinxing/deepseek-harness-tui
cd deepseek-harness-tui && pnpm install
```

## 🚀 快速开始

```bash
dsh plugin --profile tui add @deepseek-ai/dsh-headless
dsh plugin --profile tui add /path/to/deepseek-harness-tui
```

## 📚 更多信息

**Install**

Requires **Node.js ≥ 20** and the [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) CLI: npm install -g @deepseek-ai/dsh # the harness (no Homebrew tap yet) git clone https://github.com/gxinxing/deepseek-harness-tui cd deepseek-harness-tui && pnpm install Wire the plugin bundle into the `tui` profile (one-time): dsh plugin --profile tui add @deepseek-ai/dsh-headless dsh plugin --

## 🔗 链接

- [GitHub 仓库](https://github.com/gxinxing/deepseek-harness-tui)
- [完整 README](https://github.com/gxinxing/deepseek-harness-tui#readme)
- [返回deepseek-harness-tui (gxinxing)所在分类](../clients.md)
