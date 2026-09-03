---
title: "dsh-industry-research"
description: "行业与公司研究域包：方法论技能、产业链结构模型、公开源政策/新闻跟踪与公司扫描卡，输出可审计。"
keywords: "dsh-industry-research, research, plugin, deepseek harness, dsh"
---
# dsh-industry-research

> ⭐ **46** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 研究 |
| 星数 | ⭐ 46 | 状态 | ✅ 活跃 |
| 作者 | [PerryLink](https://github.com/PerryLink) | 更新时间 | — |

## 一句话介绍

> 行业与公司研究域包：方法论技能、产业链结构模型、公开源政策/新闻跟踪与公司扫描卡，输出可审计。

## 详细介绍

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-industry-research` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **Industry and company research domain pack for DeepSeek Harness.** *Chain maps, public-source tracking, company cards, and auditable reports — every number traces to a source, every gap is declared.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) --- **仅供研究，不构成投资建议 — Research only, not investment advice.** This pack does research support only: no trading, no price prediction, no paid/login-walled sources.

## ✨ 核心特性

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-industry-research` (counts toward the [deepseek1024.com](https://dee

## 📦 安装

```bash
# From a scratch profile (pins the commit; runs the self-contained `prepare` build)
dsh plugin --profile demo add "github:PerryLink/dsh-industry-research#<sha>"
# The profile's pnpm-workspace.yaml gains an allowBuilds entry for dsh-industry-research on first add.
```

## 🚀 快速开始

```bash
dsh plugin --profile demo add dsh-industry-research
```

## 📚 更多信息

**Install & uninstall**

dsh plugin --profile demo add dsh-industry-research # install dsh plugin --profile demo remove dsh-industry-research # uninstall Verify the row mounts: `dsh --profile demo --dump-config | grep dsh-industry-research`.

**Configuration**

All tunables are Schemastery `Config` fields; invalid values fail the profile load loudly.

## 🔗 链接

- [GitHub 仓库](https://github.com/PerryLink/dsh-industry-research)
- [完整 README](https://github.com/PerryLink/dsh-industry-research#readme)
- [返回dsh-industry-research所在分类](../plugins.md)
