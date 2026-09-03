---
title: "dsh-plugin-skills"
description: "构建与测试 DSH 插件的 Agent 技能：从脚手架到发布。"
keywords: "dsh-plugin-skills, learning, skill, coding, workflow, deepseek harness, dsh"
---
# dsh-plugin-skills

> ⭐ **11** · ✅ 活跃 · 技能 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 技能 | 分类 | 学习 |
| 星数 | ⭐ 11 | 状态 | ✅ 活跃 |
| 作者 | [omdsh-dev](https://github.com/omdsh-dev) | 更新时间 | 2026-08-11 |

## 一句话介绍

> 构建与测试 DSH 插件的 Agent 技能：从脚手架到发布。

## 详细介绍

Agent skills for building and testing **DeepSeek Harness** plugins — from scaffolding a new plugin package to choosing the right test tiers, entirely inside an agent session.

## 🚀 快速开始

```bash
cp -r dsh-write-plugin dsh-test-plugin <your-project>/.agents/skills/
```

## 📚 更多信息

**Install**

Copy the skill folders into your project's agent skills directory: cp -r dsh-write-plugin dsh-test-plugin <your-project>/.agents/skills/ Claude Code projects usually symlink `.claude/skills` to `.agents/skills`; if yours does not: ln -s ../.agents/skills <your-project>/.claude/skills That's it. The agent picks the skills up automatically (the skill catalog hot-refreshes on disk changes) — just ask

## 🔗 链接

- [GitHub 仓库](https://github.com/omdsh-dev/dsh-plugin-skills)
- [完整 README](https://github.com/omdsh-dev/dsh-plugin-skills#readme)
- [返回dsh-plugin-skills所在分类](../skills.md)
