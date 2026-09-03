---
title: "dsh-plugin-development"
description: "Portable Agent Skill for developing and auditing DeepSeek Harness plugins, with an optional profile-installable DSH bundle adapter."
keywords: "dsh-plugin-development, learning, skill, coding, multi-agent, deepseek harness, dsh"
---
# dsh-plugin-development

> ⭐ **14** · ✅ 活跃 · 技能 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 技能 | 分类 | 学习 |
| 星数 | ⭐ 14 | 状态 | ✅ 活跃 |
| 作者 | [w2112515](https://github.com/w2112515) | 更新时间 | 2026-08-17 |

## 一句话介绍

> Portable Agent Skill for developing and auditing DeepSeek Harness plugins, with an optional profile-installable DSH bundle adapter.

## 详细介绍

DSH Plugin Development is a portable Agent Skill for designing, implementing, packaging, reviewing, and diagnosing [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) plugins. The same canonical Skill directory works with Codex, Claude Code, and DSH. An optional DSH bundle adapter adds profile-scoped installation and reversible removal without creating another copy of the workflow.

## ✨ 核心特性

- a personal Skill at `~/.codex/skills/dsh-plugin-development`; or
- a repository Skill at `<repo>/.agents/skills/dsh-plugin-development`.

## 📦 安装

```bash
dsh plugin --profile web add https://github.com/w2112515/dsh-plugin-development/releases/download/v0.2.0-beta.1/dsh-plugin-development-0.2.0-beta.1.tgz
dsh --profile web --dump-config
```

## 🚀 快速开始

```bash
dsh plugin --profile web add .
```

## 📚 更多信息

**Does installation execute package build scripts?**

No. The DSH adapter has no `prepare`, `install`, or `postinstall` script. Always inspect third-party source and the exact artifact before installation.

## 🔗 链接

- [GitHub 仓库](https://github.com/w2112515/dsh-plugin-development)
- [完整 README](https://github.com/w2112515/dsh-plugin-development#readme)
- [返回dsh-plugin-development所在分类](../skills.md)
