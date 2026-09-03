---
title: "dsh-file-mentions"
description: "Clickable file paths in DSH replies: inline open, reveal in file manager and a mentioned-files chip list."
keywords: "dsh-file-mentions, developer, plugin, files, ui, deepseek harness, dsh"
---
# dsh-file-mentions

> ⭐ **11** · ✅ active · plugin · ⬆️ +5 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 11 | Status | ✅ active |
| Author | [a903067276-rgb](https://github.com/a903067276-rgb) | Updated | 2026-08-21 |
| Subcategory | 📁 Files & import | Capabilities | files, ui |

## One-liner

> Clickable file paths in DSH replies: inline open, reveal in file manager and a mentioned-files chip list.

## About

[English](README.md) | [简体中文](README.zh-CN.md) **Clickable file paths in DSH replies** — a DeepSeek Harness (DSH) web plugin with a Codex-style experience. *Unofficial project: independently developed and maintained by a community member, not an official DeepSeek product.*

## 📦 Install

```bash
dsh plugin --profile web add "github:a903067276-rgb/dsh-file-mentions#main"
```

## 📚 Learn more

**Screenshot**

Inline paths wrapped in backticks (`` `~/...` ``, absolute, relative, or Chinese paths) become **click-to-open**; each clickable path carries a small folder-icon button that reveals the file in your file manager; a "📎 mentioned files" chip list at the turn tail covers the rest. URLs are already auto-linked by the official renderer, so this plugin leaves them alone. The external-drive whitelist (Se

**Install**

This repository is an official **bundle plugin** (`dsh.bundle` + `dsh.client` in the root `package.json`), installed through the official profile manager: dsh plugin --profile web add "github:a903067276-rgb/dsh-file-mentions#main" Then **restart `dsh web`** (bundle layers are composed at startup; HMR does not apply). Requires `pnpm` on PATH (`dsh plugin` forwards to pnpm). Manual mount fallback: s

**Usage**

Have the agent wrap paths in backticks (e.g. `` `~/docs/plan.md` ``) to make them clickable inline. The tail chip list appears automatically — no configuration.

## 🔗 Links

- [GitHub Repository](https://github.com/a903067276-rgb/dsh-file-mentions)
- [Full README](https://github.com/a903067276-rgb/dsh-file-mentions#readme)
- [Back to the Plugins list](../plugins.md)
