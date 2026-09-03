---
title: "dsh-plugin-cc"
description: "将 DSH 桥接到 Claude Code：审查、批判、委托与会话导入。"
keywords: "dsh-plugin-cc, multi-agent, agent, coding, deepseek harness, dsh"
---
# dsh-plugin-cc

> ⭐ **29** · ✅ 活跃 · 智能体 · 近期 ⬆️ +10

| | | | |
|---|---|---|---|
| 类型 | 智能体 | 分类 | 多智能体 |
| 星数 | ⭐ 29 | 状态 | ✅ 活跃 |
| 作者 | [cpj-dev](https://github.com/cpj-dev) | 更新时间 | 2026-08-18 |

## 一句话介绍

> 将 DSH 桥接到 Claude Code：审查、批判、委托与会话导入。

## 详细介绍

[English](README.md) | [简体中文](README.zh-CN.md) Claude Code plugin that runs **DeepSeek Harness** (`dsh`) from slash commands: review, critique, one-shot tasks, and resumable multi-turn sessions. Pin: [`@deepseek-ai/dsh@0.1.1-rc.2`](https://www.npmjs.com/package/@deepseek-ai/dsh). After upgrading the plugin, rerun `/dsh:setup`. Re-verify [docs/dsh-compat.md](docs/dsh-compat.md) on every dsh upgrade.

## ✨ 核心特性

- this run: `/dsh:run --mode minimal …` or `--mode anchored-standard`
- this shell: `DSH_CC_MODE=minimal`
- this machine: `/dsh:setup --mode minimal`

## 🚀 快速开始

```bash
/plugin marketplace add cpj-dev/dsh-plugin-cc
/plugin install dsh@deepseek-dsh
/dsh:setup
/dsh:review
```

## 📚 更多信息

**Quick start**

Needs Node >= 20 and a `DEEPSEEK_API_KEY`. `/dsh:setup` also needs Node >= 22.19, `npm`, and `pnpm` (`corepack enable`). /plugin marketplace add cpj-dev/dsh-plugin-cc /plugin install dsh@deepseek-dsh /dsh:setup /dsh:review Already have a built [deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) checkout? `/dsh:setup --harness <path>`. Already have a `dsh` binary? set `DSH_BINARY`. 

## 🔗 链接

- [GitHub 仓库](https://github.com/cpj-dev/dsh-plugin-cc)
- [完整 README](https://github.com/cpj-dev/dsh-plugin-cc#readme)
- [返回dsh-plugin-cc所在分类](../agents.md)
