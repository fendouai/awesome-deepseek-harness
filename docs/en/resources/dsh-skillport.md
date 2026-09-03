---
title: "dsh-skillport"
description: "Every skill you already have — Claude Code, Codex, Cursor, Gemini CLI — works in DSH."
keywords: "dsh-skillport, learning, plugin, workflow, coding, deepseek harness, dsh"
---
# dsh-skillport

> ⭐ **2** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Learning |
| Stars | ⭐ 2 | Status | ✅ active |
| Author | [Jesse-njx](https://github.com/Jesse-njx) | Updated | 2026-08-13 |

## One-liner

> Every skill you already have — Claude Code, Codex, Cursor, Gemini CLI — works in DSH.

## About

**Every skill you already have — Claude Code, Codex, Cursor, Gemini CLI — works in DSH.** `dsh-skillport` is a [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) plugin bundle that makes DSH the next implementer of the open **Agent Skills** standard (`SKILL.md`). Anthropic released the spec in Dec 2025 and 30+ harnesses read it (Codex CLI, Cursor, Gemini CLI, Copilot/VS Code, Goose, Windsurf); DSH did not. Skillport imports the whole existing ecosystem with **zero migration**: your `.claude/skills/` library, your Cursor rules, your Claude Code slash commands all become DSH skills the moment the plugin loads.

## ✨ Key Features

- `.dsh/skills` + `.agents/skills` are scanned by DSH's native `dsh-skill-filesystem`; skillport detects that provider and skips those sets (falling back to scann
- The spec's "injection" (names + descriptions) and "use_skill" (load body + resolve resources) are the native `dsh-tool-skill` catalog and `skill` tool — skillpo
- `AGENTS.md`/`CLAUDE.md` are injected natively by `dsh-agent-instructions`; skillport takes over only when that plugin is absent.

## 📦 Install

```bash
dsh plugin --profile web add @dsh-skillport/bundle
```

## 🚀 Quick Start

```bash
skills-doctor --cwd ~/work/projectx list
skills-doctor --cwd ~/work/projectx test-fire "deploy the app to production"
```

## 📚 Learn more

**Install**

dsh plugin --profile web add @dsh-skillport/bundle Then in a session: ask the model to load a skill you used to own in Claude Code — the catalog lists it and the `skill` tool loads it, bundled resources included.

**Config**

All fields optional (profile patch or `cordis.patch.yml`): plugins: dsh-skillport: sources: [dsh, claude, agents, gemini] # which discovery sets to scan extraPaths: [] # extra SKILL.md dirs (e.g. ~/skills, a shared drive) convert: cursorRules: true # .cursor/rules/*.mdc → skills contextFiles: true # AGENTS.md / CLAUDE.md (skipped when DSH handles natively) claudeCommands: true # .claude/commands/*

## 🔗 Links

- [GitHub Repository](https://github.com/Jesse-njx/dsh-skillport)
- [Full README](https://github.com/Jesse-njx/dsh-skillport#readme)
- [Back to the Skills list](../skills.md)
