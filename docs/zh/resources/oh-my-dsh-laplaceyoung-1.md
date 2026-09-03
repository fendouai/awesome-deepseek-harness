---
title: "oh-my-dsh"
description: "面向 DSH 的插件生态：700+ 插件，只通过扩展接缝注册，不修改 agent-loop 骨架。"
keywords: "oh-my-dsh, registry, awesome-list, search, deepseek harness, dsh"
---
# oh-my-dsh

> ⭐ **51** · ✅ 活跃 · 精选列表 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 精选列表 | 分类 | 注册表 |
| 星数 | ⭐ 51 | 状态 | ✅ 活跃 |
| 作者 | [LaplaceYoung](https://github.com/LaplaceYoung) | 更新时间 | 2026-08-15 |

## 一句话介绍

> 面向 DSH 的插件生态：700+ 插件，只通过扩展接缝注册，不修改 agent-loop 骨架。

## 详细介绍

`deep-research` decomposes a compound question into sub-questions, searches and fetches sources in parallel through DSH's portable web seam, and synthesizes a cited report. Configure a `provider` + `model` and synthesis runs through the LLM; leave them unset and a deterministic template report still lands — every path degrades gracefully, none require a real key to test.

## 📦 安装

```bash
git clone https://github.com/LaplaceYoung/oh-my-dsh.git
cd oh-my-dsh
pnpm install
```

## 🚀 快速开始

```bash
- id: omd-deep-research
  name: '@oh-my-dsh/deep-research'
  config:
    provider: deepseek-official
    model: deepseek-v4-flash
```

## 📚 更多信息

**Install**

git clone https://github.com/LaplaceYoung/oh-my-dsh.git cd oh-my-dsh pnpm install Plugins are ESM packages under `plugins/<name>` (`@oh-my-dsh/<name>`). Mount them in a DSH `cordis.yml` composition: name: '@oh-my-dsh/deep-research' config: provider: deepseek-official model: deepseek-v4-flash

**Architecture**

DSH is an all-plugin harness: the agent loop itself is a plugin, and new behavior lands through documented seams — never by editing the skeleton.

## 🔗 链接

- [GitHub 仓库](https://github.com/LaplaceYoung/oh-my-dsh)
- [完整 README](https://github.com/LaplaceYoung/oh-my-dsh#readme)
- [返回oh-my-dsh所在分类](../awesome-lists.md)
