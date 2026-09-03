---
title: "dsh-plugin-claude-bridge"
description: "把 Claude Code 的记忆、技能与配置桥接到 DSH。"
keywords: "dsh-plugin-claude-bridge, multi-agent, agent, memory, deepseek harness, dsh"
---
# dsh-plugin-claude-bridge

> ⭐ **9** · ✅ 活跃 · 智能体 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 智能体 | 分类 | 多智能体 |
| 星数 | ⭐ 9 | 状态 | ✅ 活跃 |
| 作者 | [YYTbit](https://github.com/YYTbit) | 更新时间 | 2026-08-14 |

## 一句话介绍

> 把 Claude Code 的记忆、技能与配置桥接到 DSH。

## 详细介绍

Bridge Claude Code's memory, skills, and configuration into DeepSeek Harness -- zero migration, full compatibility.

## ✨ 核心特性

- `~/.claude/projects/<project>/memory/*.md` -- Injects memories as dynamic system prompt context
- `~/.claude/skills/<name>/SKILL.md` -- Adds skills to the available catalog
- `~/.claude/CLAUDE.md` -- Injects global instructions into system prompt

## 📦 安装

```bash
dsh plugin --profile your-profile add dsh-plugin-claude-bridge
```

## 🚀 快速开始

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

## 📚 更多信息

**Configuration**

Works out of the box with zero configuration. All options are optional: name: dsh-plugin-claude-bridge config: claudeHome: '~/.claude' enableMemory: true maxMemoryBytes: 8192 enableSkills: true maxSkills: 30 enableGlobalInstructions: true extraSkillDirs: - '~/.agents/skills'

## 🔗 链接

- [GitHub 仓库](https://github.com/YYTbit/dsh-plugin-claude-bridge)
- [完整 README](https://github.com/YYTbit/dsh-plugin-claude-bridge#readme)
- [返回dsh-plugin-claude-bridge所在分类](../agents.md)
