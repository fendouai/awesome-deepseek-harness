---
title: "dsh-review-skills"
description: "DSH 代码评审技能集。"
keywords: "dsh-review-skills, coding, skill, deepseek harness, dsh"
---
# dsh-review-skills

> ⭐ **2** · ✅ 活跃 · 技能

| | | | |
|---|---|---|---|
| 类型 | 技能 | 分类 | 编码 |
| 星数 | ⭐ 2 | 状态 | ✅ 活跃 |
| 作者 | [ben7am1n](https://github.com/ben7am1n) | 更新时间 | 2026-08-13 |

## 一句话介绍

> DSH 代码评审技能集。

## 详细介绍

**Engineering-discipline skill pack for DeepSeek Harness** — five battle-tested procedures delivered as a bundled skill provider: code review, simplification, plan-then-execute, test-first, and conflict resolution.

## ✨ 核心特性

- Solo developers who want a senior-engineer checklist without hiring one.
- Teams that want consistent review and planning standards across sessions.
- Anyone building on the dsh skill system who wants a reference-quality skill pack to copy.

## 📦 安装

```bash
cd /path/to/deepseek-harness
pnpm dsh plugin --profile web add /path/to/dsh-review-skills
```

## 🚀 快速开始

```bash
pnpm dsh plugin --profile web add github:<you>/dsh-review-skills
```

## 📚 更多信息

**Install / Uninstall**

Install into a dsh profile (local checkout): cd /path/to/deepseek-harness pnpm dsh plugin --profile web add /path/to/dsh-review-skills From GitHub (source install — pnpm runs the `prepare` script, so allow it once): pnpm dsh plugin --profile web add github:<you>/dsh-review-skills From npm (once published): pnpm dsh plugin --profile web add dsh-review-skills Uninstall: pnpm dsh plugin --profile web

**Quick start**

Install the bundle, restart dsh, then simply ask: Use the code-review skill on the current diff before we merge. or mention a skill by name in context: Plan-then-execute: refactor the auth module, then implement. The harness resolves the skill through `ctx.skills` and injects its procedure when the model invokes it.

**Configuration**

None. The plugin registers its provider with no config; the skills and their routing metadata live in `skills/*/SKILL.md` frontmatter (`name`, `description`, `whenToUse`, `disable-model-invocation`, `user-invocable`).

## 🔗 链接

- [GitHub 仓库](https://github.com/ben7am1n/dsh-review-skills)
- [完整 README](https://github.com/ben7am1n/dsh-review-skills#readme)
- [返回dsh-review-skills所在分类](../skills.md)
