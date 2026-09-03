---
title: "dsh-plugin-development"
description: "Portable Agent Skill for developing and auditing DeepSeek Harness plugins, with an optional profile-installable DSH bundle adapter."
keywords: "dsh-plugin-development, learning, skill, coding, multi-agent, deepseek harness, dsh"
---
# dsh-plugin-development

> ⭐ **14** · ✅ active · skill · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | skill | Category | Learning |
| Stars | ⭐ 14 | Status | ✅ active |
| Author | [w2112515](https://github.com/w2112515) | Updated | 2026-08-17 |

## One-liner

> Portable Agent Skill for developing and auditing DeepSeek Harness plugins, with an optional profile-installable DSH bundle adapter.

## About

DSH Plugin Development is a portable Agent Skill for designing, implementing, packaging, reviewing, and diagnosing [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) plugins. The same canonical Skill directory works with Codex, Claude Code, and DSH. An optional DSH bundle adapter adds profile-scoped installation and reversible removal without creating another copy of the workflow.

## ✨ Key Features

- a personal Skill at `~/.codex/skills/dsh-plugin-development`; or
- a repository Skill at `<repo>/.agents/skills/dsh-plugin-development`.

## 📦 Install

```bash
dsh plugin --profile web add https://github.com/w2112515/dsh-plugin-development/releases/download/v0.2.0-beta.1/dsh-plugin-development-0.2.0-beta.1.tgz
dsh --profile web --dump-config
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add .
```

## 📚 Learn more

**Does installation execute package build scripts?**

No. The DSH adapter has no `prepare`, `install`, or `postinstall` script. Always inspect third-party source and the exact artifact before installation.

## 🔗 Links

- [GitHub Repository](https://github.com/w2112515/dsh-plugin-development)
- [Full README](https://github.com/w2112515/dsh-plugin-development#readme)
- [Back to the Skills list](../skills.md)
