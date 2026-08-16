---
title: "dsh-find-skill"
description: "Bridges the vercel-labs/skills ecosystem: LLM-driven skill search, install and management."
keywords: "dsh-find-skill, learning, plugin, search, workflow, deepseek harness, dsh"
---
# dsh-find-skill

> ⭐ 2 · ✅ active · plugin

## One-liner

Bridges the vercel-labs/skills ecosystem: LLM-driven skill search, install and management.

## About

[English](README_en.md) | 中文 将 [vercel-labs/skills](https://github.com/vercel-labs/skills) 开放 agent 技能生态接入 [DeepSeek Harness（dsh）](https://github.com/deepseek-ai/deepseek-harness)。 插件让 **LLM 自行决定**何时需要加载技能：当任务超出既有工具与已加载技能的能力时，模型搜索技能生态（`skill_find`）、通过 dsh 内置的 `ask_user_question` 询问用户选择哪个技能与作用域，然后加载为 **临时**（默认，仅当前会话）、**项目**（随工作区共享）或 **全局**（所有会话）。安装落在插件自有的根目录，与手写的 `.dsh/skills` 和共享的 `.agents/skills` 完全隔离。

## Author
**[Moximxxx](https://github.com/Moximxxx)**

## Links

- [GitHub Repository](https://github.com/Moximxxx/dsh-find-skill)
- [Full README](https://github.com/Moximxxx/dsh-find-skill#readme)
- [Back to the Skills list](../skills.md)
