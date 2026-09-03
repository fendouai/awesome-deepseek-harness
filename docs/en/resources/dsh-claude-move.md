---
title: "dsh-claude-move"
description: "Four-source migration wizard for DeepSeek Harness: move Claude Code, Codex, OpenCode and Hermes sessions, memories, skills, instructions and slash commands into DSH (/move wizard + resumable sessions, approval-gated, idempotent)."
keywords: "dsh-claude-move, learning, skill, coding, deepseek harness, dsh"
---
# dsh-claude-move

> ⭐ **11** · ✅ active · skill

| | | | |
|---|---|---|---|
| Type | skill | Category | Learning |
| Stars | ⭐ 11 | Status | ✅ active |
| Author | [PerryLink](https://github.com/PerryLink) | Updated | — |

## One-liner

> Four-source migration wizard for DeepSeek Harness: move Claude Code, Codex, OpenCode and Hermes sessions, memories, skills, instructions and slash commands into DSH (/move wizard + resumable sessions, approval-gated, idempotent).

## About

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-claude-move` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **Migrate Claude Code, Codex, OpenCode and Hermes into DeepSeek Harness — copy sessions, memories, skills, instructions and slash commands as resumable DSH sessions, copy-only and approval-gated.** *Keep your Claude Code history when you move: one install, resumable sessions, live sync with a running Claude Code, and a four-source migration wizard.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ Key Features

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-claude-move` (counts toward the [deepseek1024.com](https://deepseek1

## 📦 Install

```bash
# 1. install the bundle into your profile
dsh plugin --profile web add "github:PerryLink/dsh-claude-move#master"

# or from npm (published releases)
dsh plugin --profile web add dsh-claude-move

# 2. restart and verify the row
dsh --profile web --dump-config | grep -A4 'id: claude-move'
```

## 🚀 Quick Start

```bash
/claude-import-all      # scan → copy every Claude session → report
```

## 📚 Learn more

**Usage**

Call the tools in any session with the plugin mounted: claude_scan # full scan (incremental cache) claude_scan { path: "~/.claude/projects/<slug>" } # partial scan claude_scan { refresh: true } # skip cache, rescan everything claude_scan { projectsLimit: 10, sessionsLimit: 5, fields: "brief" } # trim output import_claude { path: "~/.claude/projects/<slug>/<sessionId>.jsonl" } # one session import_

## 🔗 Links

- [GitHub Repository](https://github.com/PerryLink/dsh-claude-move)
- [Full README](https://github.com/PerryLink/dsh-claude-move#readme)
- [Back to the Skills list](../skills.md)
