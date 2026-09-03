---
title: "dsh-taskboard"
description: "Native local Taskboard plugin for DeepSeek Harness. SQLite-backed projects, Agent claim/review, and a native Web UI — no iframe, no second chat runtime."
keywords: "dsh-taskboard, learning, skill, coding, multi-agent, ui, deepseek harness, dsh"
---
# dsh-taskboard

> ⭐ **195** · ✅ active · skill

| | | | |
|---|---|---|---|
| Type | skill | Category | Learning |
| Stars | ⭐ 195 | Status | ✅ active |
| Author | [shengsheng90](https://github.com/shengsheng90) | Updated | — |

## One-liner

> Native local Taskboard plugin for DeepSeek Harness. SQLite-backed projects, Agent claim/review, and a native Web UI — no iframe, no second chat runtime.

## About

Native, local project task management for DeepSeek Harness. SQLite is the sole task authority. Harness Agent Sessions, Goals, Workspaces, tools, permissions, and the Web Client remain the execution and conversation owners. This README is written so a human **or another coding agent** can install the plugin into a live Harness profile, verify it, and start using it without guessing. **Package:** `@shengsheng/dsh-taskboard` **Repository:** https://github.com/shengsheng90/DSH-taskboard **License:** Apache-2.0 **Compatible Host:** DeepSeek Harness `0.1.2-alpha.2` If you are an installing agent, jump to [Install into DeepSeek Harness](#install-into-deepseek-harness) and follow every step in order. Do **not** add this Git repository as a raw plugin source: `lib/` is gitignored, so a git install 

## ✨ Key Features

- A **Taskboard** sidebar button and a native overlay page (not an iframe, not a second chat runtime)
- Local SQLite projects, tasks, comments, relations, attachments, workflows, and automation
- Stable readable keys such as `DSH-42` plus opaque ids and optimistic versions
- Seven statuses: `backlog` → `todo` → `in_progress` → `in_review` → `done`, plus `blocked` and `canceled`
- In-process Agent tools `taskboard_*` (no accept / no generic status mutation)
- Headless JSON CLI `dsh-taskboard`

## 📦 Install

```bash
git clone https://github.com/shengsheng90/DSH-taskboard.git
cd DSH-taskboard
pnpm install
pnpm build
pnpm pack
```

## 🚀 Quick Start

```bash
/absolute/path/to/DSH-taskboard/shengsheng-dsh-taskboard-<version>.tgz
```

## 📚 Learn more

**Install into DeepSeek Harness**

Use these constants. Read live values from disk; do not invent a different package name. `<version>` is whatever this repo's `package.json` currently declares — read it there rather than copying a number out of this document. After `pnpm pack`, use the tarball that was actually written. A longer copy-paste prompt for a Harness-side agent is in [docs/install-plugin-prompt.zh.md](docs/install-plugin

**Install troubleshooting**

Install only packages you trust. `pnpm` runs package lifecycle scripts, and Harness then loads the plugin.

**Configuration**

`cordis.patch.yml` mounts one Host plugin id `taskboard`. Override values in the profile composition or with environment variables. Paths are resolved by the Host. The browser cannot choose the database or attachment root. Attachment content types and sizes are validated before publication. Downloads stream from disk. Dashboard and `storage status` share the same bounded SQLite integrity, revision

## 🔗 Links

- [GitHub Repository](https://github.com/shengsheng90/DSH-taskboard)
- [Full README](https://github.com/shengsheng90/DSH-taskboard#readme)
- [Back to the Skills list](../skills.md)
