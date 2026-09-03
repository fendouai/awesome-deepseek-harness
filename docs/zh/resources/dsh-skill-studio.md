---
title: "dsh-skill-studio"
description: "DSH skill 可视化与管理插件：设置面板列出全部 skill（含来源、嵌套标记与调用状态）、查看并编辑 SKILL.md 正文、一键启用/禁用模型与用户调用，并提供 skillmgr_list/get/save/policy 工具。"
keywords: "dsh-skill-studio, ui, plugin, workflow, deepseek harness, dsh"
---
# dsh-skill-studio

> ⭐ **3** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 3 | 状态 | ✅ 活跃 |
| 作者 | [zhengjy01](https://github.com/zhengjy01) | 更新时间 | — |
| 子分类 | 💡 生成式界面 | 能力 | ui, workflow |

## 一句话介绍

> DSH skill 可视化与管理插件：设置面板列出全部 skill（含来源、嵌套标记与调用状态）、查看并编辑 SKILL.md 正文、一键启用/禁用模型与用户调用，并提供 skillmgr_list/get/save/policy 工具。

## 详细介绍

Visualize, edit and manage DeepSeek Harness **skills** right from the web settings panel — list every skill DSH discovered, view its full `SKILL.md`, edit the body, and enable/disable model & user invocation with a switch.

## ✨ 核心特性

- **Skill 管理器 settings panel** — 设置 → Skill 管理器: list every skill (name, description, source root, nested flag, model/user invocation state), open any skill to se
- **skillmgr_list** — list all skills with source, nested flag and invocation state.
- **skillmgr_get** — view one skill's full detail (body + path + policy).
- **skillmgr_save** — save a full-body edit (frontmatter + markdown) back to the file.
- **skillmgr_policy** — enable/disable a skill (`enabled` master switch, or per-interface `modelInvocable` / `userInvocable`).
- **Two merged catalogs**: ① direct filesystem scan of the standard roots (project `.dsh/skills` / `.agents/skills`, user `~/.dsh/skills` / `~/.agents/skills`), e
- Enable/disable is implemented with line-level frontmatter surgery on `disable-model-invocation` / `user-invocable`; all other frontmatter lines are preserved ve
- Read-only safety: only skills with a real file path (filesystem sources) are editable; runtime / bundled skills are shown as read-only. Routes are loopback-only

## 📦 安装

```bash
# local development
dsh plugin --profile web add link:/path/to/dsh-skill-studio

# after publishing to GitHub (repo tagged with the `dsh-plugin` topic)
dsh plugin --profile web add github:zhengjy01/dsh-skill-studio
```

## 🚀 快速开始

```bash
列出所有 skill，并告诉我哪些被禁用了
帮我禁用 session-knowledge 技能
```

## 📚 更多信息

**Usage**

In the web settings page (设置 → Skill 管理器) you can: You can also just tell your agent: 列出所有 skill，并告诉我哪些被禁用了 帮我禁用 session-knowledge 技能 The agent will use the `skillmgr_*` tools.

## 🔗 链接

- [GitHub 仓库](https://github.com/zhengjy01/dsh-skill-studio)
- [完整 README](https://github.com/zhengjy01/dsh-skill-studio#readme)
- [返回dsh-skill-studio所在分类](../plugins.md)
