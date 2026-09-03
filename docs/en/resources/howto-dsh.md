---
title: "howto-dsh"
description: "Verified field notes for DeepSeek Harness (dsh): traps, skills, hooks, profiles. Every claim dated against a dsh version, with source paths to re-verify. Not affiliated with DeepSeek."
keywords: "howto-dsh, learning, skill, coding, deepseek harness, dsh"
---
# howto-dsh

> ⭐ **1** · ✅ active · skill

| | | | |
|---|---|---|---|
| Type | skill | Category | Learning |
| Stars | ⭐ 1 | Status | ✅ active |
| Author | [dshworks](https://github.com/dshworks) | Updated | 2026-08-20 |

## One-liner

> Verified field notes for DeepSeek Harness (dsh): traps, skills, hooks, profiles. Every claim dated against a dsh version, with source paths to re-verify. Not affiliated with DeepSeek.

## About

Verified field notes for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`), DeepSeek's agent harness. Traps, skills, hooks, profiles. **Every claim here was tested against a real run, with source paths included so you can re-verify.** Each page states the version and date it was verified against; this README's notes are from `0.1.0-rc.5` (2026-08-13), the pages below from `0.1.0-rc.6` (2026-08-15). **Structural re-check 2026-08-25 against `dsh-v0.1.1-rc.2`: all 32 cited source paths still resolve, and traps 9 and 10 were re-run** &mdash; 10 no longer reproduces and says so in place. The behavioural traps have not been re-run against rc.2 and still carry their original dates; a version bump without that would be the dishonest half. dsh is a developer preview and th

## ✨ Key Features

- **`dsh web` now opens your browser.** It waits for the whole Loader tree to
- **The Claude Code and Codex subagents are separate optional Bundles now.**
- **`SubagentReportDelivery` renamed `'wakeup'` to `'next-step'`**, and the
- **The SQLite session store changed format incompatibly** for read, write, and

## 📦 Install

```bash
npx @deepseek-ai/dsh web
```

## 🚀 Quick Start

```bash
- dsh-hooks-claude-code:
    configPath: ./.claude/hooks.json
    pluginRoot: ./.claude/plugins/my-plugin
    projectDir: .
```

## 🔗 Links

- [GitHub Repository](https://github.com/dshworks/howto-dsh)
- [Full README](https://github.com/dshworks/howto-dsh#readme)
- [Back to the Skills list](../skills.md)
