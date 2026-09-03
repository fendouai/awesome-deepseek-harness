---
title: "dsh-plugin-claude-bridge"
description: "Bridge Claude Code memory, skills and config into DeepSeek Harness."
keywords: "dsh-plugin-claude-bridge, multi-agent, agent, memory, deepseek harness, dsh"
---
# dsh-plugin-claude-bridge

> ⭐ **9** · ✅ active · agent · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | agent | Category | Multi-agent |
| Stars | ⭐ 9 | Status | ✅ active |
| Author | [YYTbit](https://github.com/YYTbit) | Updated | 2026-08-14 |

## One-liner

> Bridge Claude Code memory, skills and config into DeepSeek Harness.

## About

Bridge Claude Code's memory, skills, and configuration into DeepSeek Harness -- zero migration, full compatibility.

## ✨ Key Features

- `~/.claude/projects/<project>/memory/*.md` -- Injects memories as dynamic system prompt context
- `~/.claude/skills/<name>/SKILL.md` -- Adds skills to the available catalog
- `~/.claude/CLAUDE.md` -- Injects global instructions into system prompt

## 📦 Install

```bash
dsh plugin --profile your-profile add dsh-plugin-claude-bridge
```

## 🚀 Quick Start

```bash
- id: claude-bridge
  name: dsh-plugin-claude-bridge
  config:
    claudeHome: '~/.claude'
    enableMemory: true
    maxMemoryBytes: 8192
    enableSkills: true
    maxSkills: 30
    enableGlobalInstructions: true
    extraSkillDirs:
      - '~/.agents/skills'
```

## 📚 Learn more

**Configuration**

Works out of the box with zero configuration. All options are optional: name: dsh-plugin-claude-bridge config: claudeHome: '~/.claude' enableMemory: true maxMemoryBytes: 8192 enableSkills: true maxSkills: 30 enableGlobalInstructions: true extraSkillDirs: - '~/.agents/skills'

## 🔗 Links

- [GitHub Repository](https://github.com/YYTbit/dsh-plugin-claude-bridge)
- [Full README](https://github.com/YYTbit/dsh-plugin-claude-bridge#readme)
- [Back to the Agents & Multi-Agent list](../agents.md)
