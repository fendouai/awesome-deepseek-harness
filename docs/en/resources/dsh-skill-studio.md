---
title: "dsh-skill-studio"
description: "Skill studio for DeepSeek Harness: visualize every agent skill (name, description, source root, nested flag, invocation state), view/edit SKILL.md bodies, and enable or disable model/user invocation via settings panel and skillmgr_* tools."
keywords: "dsh-skill-studio, ui, plugin, workflow, deepseek harness, dsh"
---
# dsh-skill-studio

> ⭐ **3** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 3 | Status | ✅ active |
| Author | [zhengjy01](https://github.com/zhengjy01) | Updated | — |
| Subcategory | 💡 Generative UI | Capabilities | ui, workflow |

## One-liner

> Skill studio for DeepSeek Harness: visualize every agent skill (name, description, source root, nested flag, invocation state), view/edit SKILL.md bodies, and enable or disable model/user invocation via settings panel and skillmgr_* tools.

## About

Visualize, edit and manage DeepSeek Harness **skills** right from the web settings panel — list every skill DSH discovered, view its full `SKILL.md`, edit the body, and enable/disable model & user invocation with a switch.

## ✨ Key Features

- **Skill 管理器 settings panel** — 设置 → Skill 管理器: list every skill (name, description, source root, nested flag, model/user invocation state), open any skill to se
- **skillmgr_list** — list all skills with source, nested flag and invocation state.
- **skillmgr_get** — view one skill's full detail (body + path + policy).
- **skillmgr_save** — save a full-body edit (frontmatter + markdown) back to the file.
- **skillmgr_policy** — enable/disable a skill (`enabled` master switch, or per-interface `modelInvocable` / `userInvocable`).
- **Two merged catalogs**: ① direct filesystem scan of the standard roots (project `.dsh/skills` / `.agents/skills`, user `~/.dsh/skills` / `~/.agents/skills`), e
- Enable/disable is implemented with line-level frontmatter surgery on `disable-model-invocation` / `user-invocable`; all other frontmatter lines are preserved ve
- Read-only safety: only skills with a real file path (filesystem sources) are editable; runtime / bundled skills are shown as read-only. Routes are loopback-only

## 📦 Install

```bash
# local development
dsh plugin --profile web add link:/path/to/dsh-skill-studio

# after publishing to GitHub (repo tagged with the `dsh-plugin` topic)
dsh plugin --profile web add github:zhengjy01/dsh-skill-studio
```

## 🚀 Quick Start

```bash
列出所有 skill，并告诉我哪些被禁用了
帮我禁用 session-knowledge 技能
```

## 📚 Learn more

**Usage**

In the web settings page (设置 → Skill 管理器) you can: You can also just tell your agent: 列出所有 skill，并告诉我哪些被禁用了 帮我禁用 session-knowledge 技能 The agent will use the `skillmgr_*` tools.

## 🔗 Links

- [GitHub Repository](https://github.com/zhengjy01/dsh-skill-studio)
- [Full README](https://github.com/zhengjy01/dsh-skill-studio#readme)
- [Back to the Plugins list](../plugins.md)
