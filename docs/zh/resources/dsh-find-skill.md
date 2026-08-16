---
title: "dsh-find-skill"
description: "桥接 vercel-labs/skills 生态：LLM 驱动技能搜索、安装与管理。"
keywords: "dsh-find-skill, learning, plugin, search, workflow, deepseek harness, dsh"
---
# dsh-find-skill

> ⭐ 2 · ✅ 活跃 · 插件

## 一句话介绍

桥接 vercel-labs/skills 生态：LLM 驱动技能搜索、安装与管理。

## 详细介绍

[English](README_en.md) | 中文 将 [vercel-labs/skills](https://github.com/vercel-labs/skills) 开放 agent 技能生态接入 [DeepSeek Harness（dsh）](https://github.com/deepseek-ai/deepseek-harness)。 插件让 **LLM 自行决定**何时需要加载技能：当任务超出既有工具与已加载技能的能力时，模型搜索技能生态（`skill_find`）、通过 dsh 内置的 `ask_user_question` 询问用户选择哪个技能与作用域，然后加载为 **临时**（默认，仅当前会话）、**项目**（随工作区共享）或 **全局**（所有会话）。安装落在插件自有的根目录，与手写的 `.dsh/skills` 和共享的 `.agents/skills` 完全隔离。

## 作者
**[Moximxxx](https://github.com/Moximxxx)**

## 链接

- [GitHub 仓库](https://github.com/Moximxxx/dsh-find-skill)
- [完整 README](https://github.com/Moximxxx/dsh-find-skill#readme)
- [返回dsh-find-skill所在分类](../skills.md)
