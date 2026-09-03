---
title: "dsh-skillport"
description: "让 Claude Code、Codex、Cursor、Gemini CLI 已有的技能在 DSH 中直接可用。"
keywords: "dsh-skillport, learning, plugin, workflow, coding, deepseek harness, dsh"
---
# dsh-skillport

> ⭐ **2** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 学习 |
| 星数 | ⭐ 2 | 状态 | ✅ 活跃 |
| 作者 | [Jesse-njx](https://github.com/Jesse-njx) | 更新时间 | 2026-08-13 |

## 一句话介绍

> 让 Claude Code、Codex、Cursor、Gemini CLI 已有的技能在 DSH 中直接可用。

## 详细介绍

**Every skill you already have — Claude Code, Codex, Cursor, Gemini CLI — works in DSH.** `dsh-skillport` is a [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) plugin bundle that makes DSH the next implementer of the open **Agent Skills** standard (`SKILL.md`). Anthropic released the spec in Dec 2025 and 30+ harnesses read it (Codex CLI, Cursor, Gemini CLI, Copilot/VS Code, Goose, Windsurf); DSH did not. Skillport imports the whole existing ecosystem with **zero migration**: your `.claude/skills/` library, your Cursor rules, your Claude Code slash commands all become DSH skills the moment the plugin loads.

## ✨ 核心特性

- `.dsh/skills` + `.agents/skills` are scanned by DSH's native `dsh-skill-filesystem`; skillport detects that provider and skips those sets (falling back to scann
- The spec's "injection" (names + descriptions) and "use_skill" (load body + resolve resources) are the native `dsh-tool-skill` catalog and `skill` tool — skillpo
- `AGENTS.md`/`CLAUDE.md` are injected natively by `dsh-agent-instructions`; skillport takes over only when that plugin is absent.

## 📦 安装

```bash
dsh plugin --profile web add @dsh-skillport/bundle
```

## 🚀 快速开始

```bash
skills-doctor --cwd ~/work/projectx list
skills-doctor --cwd ~/work/projectx test-fire "deploy the app to production"
```

## 📚 更多信息

**Install**

dsh plugin --profile web add @dsh-skillport/bundle Then in a session: ask the model to load a skill you used to own in Claude Code — the catalog lists it and the `skill` tool loads it, bundled resources included.

**Config**

All fields optional (profile patch or `cordis.patch.yml`): plugins: dsh-skillport: sources: [dsh, claude, agents, gemini] # which discovery sets to scan extraPaths: [] # extra SKILL.md dirs (e.g. ~/skills, a shared drive) convert: cursorRules: true # .cursor/rules/*.mdc → skills contextFiles: true # AGENTS.md / CLAUDE.md (skipped when DSH handles natively) claudeCommands: true # .claude/commands/*

## 🔗 链接

- [GitHub 仓库](https://github.com/Jesse-njx/dsh-skillport)
- [完整 README](https://github.com/Jesse-njx/dsh-skillport#readme)
- [返回dsh-skillport所在分类](../skills.md)
