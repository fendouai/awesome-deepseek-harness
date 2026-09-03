---
title: "dsh-plugin-guide"
description: "skill for Deepseek-Harness plugins development"
keywords: "dsh-plugin-guide, learning, skill, coding, deepseek harness, dsh"
---
# dsh-plugin-guide

> ⭐ **0** · ✅ 活跃 · 技能

| | | | |
|---|---|---|---|
| 类型 | 技能 | 分类 | 学习 |
| 星数 | ⭐ 0 | 状态 | ✅ 活跃 |
| 作者 | [HarcoChen](https://github.com/HarcoChen) | 更新时间 | — |

## 一句话介绍

> skill for Deepseek-Harness plugins development

## 详细介绍

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-plugin-guide` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **Everything you need to build [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) plugins.** *Official docs archive · Cordis primer · community deep-dives · battle-tested pitfalls · agent skill · CLI toolchain* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ 核心特性

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-plugin-guide` (counts toward the [deepseek1024.com](https://deepseek

## 📦 安装

```bash
# 1. install the bundle into your profile
dsh plugin --profile web add "github:PerryLink/dsh-plugin-guide#main"

# or from npm (published releases)
dsh plugin --profile web add dsh-plugin-guide

# 2. restart and verify the row
dsh --profile web --dump-config | grep -A3 'id: dsh-plugin-guide'
```

## 🚀 快速开始

```bash
npx dsh-plugin-guide new hello-plugin            # scaffold a TS plugin repo
npx dsh-plugin-guide check --json                # static-check it
npx dsh-plugin-guide verify                      # pack + clean-profile smoke
```

## 📚 更多信息

**Upstream roadmap**

`dsh-plugin-dev` is an upstream candidate for the official plugin-development CLI (planned item C12): the scaffolder/checker/verifier are the mechanical layers, while `SKILL.md` + `guide/` stay the cognitive layer.

**Configuration**

The skill bundle exposes no Schemastery `Config` — it registers the knowledge base as an agent skill with no tunable keys. The `dsh-plugin-dev` CLI reads its tunables from flags and `DSH_PLUGIN_DEV_*` environment variables (see [CLI toolchain](#cli-toolchain)).

## 🔗 链接

- [GitHub 仓库](https://github.com/HarcoChen/dsh-plugin-guide)
- [完整 README](https://github.com/HarcoChen/dsh-plugin-guide#readme)
- [返回dsh-plugin-guide所在分类](../skills.md)
