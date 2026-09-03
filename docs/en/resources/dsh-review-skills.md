---
title: "dsh-review-skills"
description: "Code review skill pack for DeepSeek Harness."
keywords: "dsh-review-skills, coding, skill, deepseek harness, dsh"
---
# dsh-review-skills

> ⭐ **2** · ✅ active · skill

| | | | |
|---|---|---|---|
| Type | skill | Category | Coding |
| Stars | ⭐ 2 | Status | ✅ active |
| Author | [ben7am1n](https://github.com/ben7am1n) | Updated | 2026-08-13 |

## One-liner

> Code review skill pack for DeepSeek Harness.

## About

**Engineering-discipline skill pack for DeepSeek Harness** — five battle-tested procedures delivered as a bundled skill provider: code review, simplification, plan-then-execute, test-first, and conflict resolution.

## ✨ Key Features

- Solo developers who want a senior-engineer checklist without hiring one.
- Teams that want consistent review and planning standards across sessions.
- Anyone building on the dsh skill system who wants a reference-quality skill pack to copy.

## 📦 Install

```bash
cd /path/to/deepseek-harness
pnpm dsh plugin --profile web add /path/to/dsh-review-skills
```

## 🚀 Quick Start

```bash
pnpm dsh plugin --profile web add github:<you>/dsh-review-skills
```

## 📚 Learn more

**Install / Uninstall**

Install into a dsh profile (local checkout): cd /path/to/deepseek-harness pnpm dsh plugin --profile web add /path/to/dsh-review-skills From GitHub (source install — pnpm runs the `prepare` script, so allow it once): pnpm dsh plugin --profile web add github:<you>/dsh-review-skills From npm (once published): pnpm dsh plugin --profile web add dsh-review-skills Uninstall: pnpm dsh plugin --profile web

**Quick start**

Install the bundle, restart dsh, then simply ask: Use the code-review skill on the current diff before we merge. or mention a skill by name in context: Plan-then-execute: refactor the auth module, then implement. The harness resolves the skill through `ctx.skills` and injects its procedure when the model invokes it.

**Configuration**

None. The plugin registers its provider with no config; the skills and their routing metadata live in `skills/*/SKILL.md` frontmatter (`name`, `description`, `whenToUse`, `disable-model-invocation`, `user-invocable`).

## 🔗 Links

- [GitHub Repository](https://github.com/ben7am1n/dsh-review-skills)
- [Full README](https://github.com/ben7am1n/dsh-review-skills#readme)
- [Back to the Skills list](../skills.md)
