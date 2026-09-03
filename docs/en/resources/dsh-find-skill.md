---
title: "dsh-find-skill"
description: "Bridges the vercel-labs/skills ecosystem: LLM-driven skill search, install and management."
keywords: "dsh-find-skill, learning, plugin, search, workflow, deepseek harness, dsh"
---
# dsh-find-skill

> ⭐ **3** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Learning |
| Stars | ⭐ 3 | Status | ✅ active |
| Author | [Moximxxx](https://github.com/Moximxxx) | Updated | 2026-08-15 |

## One-liner

> Bridges the vercel-labs/skills ecosystem: LLM-driven skill search, install and management.

## About

[English](README_en.md) | 中文 将 [vercel-labs/skills](https://github.com/vercel-labs/skills) 开放 agent 技能生态接入 [DeepSeek Harness（dsh）](https://github.com/deepseek-ai/deepseek-harness)。 插件让 **LLM 自行决定**何时需要加载技能：当任务超出既有工具与已加载技能的能力时，模型搜索技能生态（`skill_find`）、通过 dsh 内置的 `ask_user_question` 询问用户选择哪个技能与作用域，然后加载为 **临时**（默认，仅当前会话）、**项目**（随工作区共享）或 **全局**（所有会话）。安装落在插件自有的根目录，与手写的 `.dsh/skills` 和共享的 `.agents/skills` 完全隔离。

## ✨ Key Features

- **`skill_find`** —— 通过官方 skills.sh API 远程搜索（与 CLI `find` 命令同源）。候选携带安装数、来源、浏览链接与本地"已安装"标记。工具描述为低优先级：明确要求模型仅在既有工具与已加载技能都不适用时使用。
- **`skill_install`** —— 通过官方 CLI（`npx -y skills@latest`，按项目决策自动取最新版）在隔离的一次性 work/home 环境内抓取，只收养目标技能目录到托管作用域。临时安装注册为运行时技能；项目/全局安装写入托管根目录，并通过自有的 `ctx.skills` provi
- **`skill_remove`** —— 从临时/项目/全局移除；未指定作用域时按 临时→项目→全局 顺序尝试。
- **`/skill` 命令** —— 面向人的 `find | install | update | sync | remove | list` 子命令；`update` 按安装时记录的来源重新拉取并替换；`sync` 通过官方 CLI 的 `experimental_sync` 扫描项目 `node_modules`
- **生命周期** —— 临时技能通过安装它的 agent 的作用域上下文注册：**仅安装它的会话可见**（其他会话读取不到），agent/会话销毁时注册自动回滚、物化目录随 `session/disposed` 清理；`compactDisposePolicy: keep | dispose | ask` 控制压缩（c
- **Web UI 卡片** —— `dsh-find-skill-client` 客户端包为 `skill_find` / `skill_install` / `skill_remove` 工具调用渲染专用会话卡片（可重放、只读展示）。

## 📦 Install

```bash
git clone https://github.com/Moximxxx/dsh-find-skill.git
cd dsh-find-skill
git checkout develop          # 完整开发分支（含 AGENTS.md、.dsh/）
pnpm install --config.minimumReleaseAge=0   # rc.6 依赖需绕过发布年龄策略
pnpm build                    # tsc → lib/
pnpm test                     # 单元 + 快照测试
```

## 🚀 Quick Start

```bash
- insert:
    - id: dsh-find-skill
      name: '/abs/path/to/dsh-find-skill/src/index.ts'
```

## 📚 Learn more

**使用流程（模型驱动）**

1. 用户提出需求；模型发现既有工具与已加载技能均不适用。 2. 模型调用 `skill_find` → 评估候选（安装数、来源、链接）。 3. 模型通过内置 `ask_user_question` 询问用户（选哪个技能？临时/项目/全局？）。 4. 模型调用 `skill_install` → 技能在下一步进入会话技能目录；用 `skill` 工具加载，或用户直接输入 `/<skill-name>`。 5. 清理：临时技能在会话结束或 `skill_remove` 时消失；项目/全局技能持久存在直到移除。

## 🔗 Links

- [GitHub Repository](https://github.com/Moximxxx/dsh-find-skill)
- [Full README](https://github.com/Moximxxx/dsh-find-skill#readme)
- [Back to the Skills list](../skills.md)
