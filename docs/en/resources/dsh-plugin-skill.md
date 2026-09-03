---
title: "dsh-plugin-skill"
description: "Agent skill (SKILL.md) for creating DeepSeek Harness (dsh) plugins: authoritative defineTool API, schema rules, project layout and workflow — works with Claude Code, Codex, Cursor, Gemini CLI, opencode"
keywords: "dsh-plugin-skill, workflow, coding, multi-agent, deepseek harness, dsh"
---
# dsh-plugin-skill

> ⭐ **0** · ✅ active · workflow

| | | | |
|---|---|---|---|
| Type | workflow | Category | Workflows |
| Stars | ⭐ 0 | Status | ✅ active |
| Author | [dsh-io](https://github.com/dsh-io) | Updated | 2026-08-17 |

## One-liner

> Agent skill (SKILL.md) for creating DeepSeek Harness (dsh) plugins: authoritative defineTool API, schema rules, project layout and workflow — works with Claude Code, Codex, Cursor, Gemini CLI, opencode

## About

An agent skill for building tools and plugins for **DeepSeek Harness (dsh)** — the official plugin API, project layout, and workflow, distilled from the real `@deepseek-ai/dsh-tools` type definitions. Written in the standard `SKILL.md` format so every mainstream AI coding agent can load it. If your agent has ever refused to write a dsh plugin (unfamiliar API) or confidently emitted a wrong one (`run` instead of `execute`, missing `output`, no `inject`), this skill fixes both: it gives the agent authoritative signatures it can copy verbatim.

## 📦 Install

```bash
mkdir -p ~/.claude/skills && \
git clone --depth 1 https://github.com/dsh-io/dsh-plugin-skill.git ~/.claude/skills/creating-dsh-plugins
# swap the destination path for your agent (table above); for Codex/Gemini use ~/.agents/skills
```

## 📚 Learn more

**Install**

The skill is a single `SKILL.md` folder. Install it in the skills directory your agent reads. The common locations: One-line install: mkdir -p ~/.claude/skills && \ git clone --depth 1 https://github.com/dsh-io/dsh-plugin-skill.git ~/.claude/skills/creating-dsh-plugins

## 🔗 Links

- [GitHub Repository](https://github.com/dsh-io/dsh-plugin-skill)
- [Full README](https://github.com/dsh-io/dsh-plugin-skill#readme)
- [Back to the Workflows & Automation list](../workflows.md)
