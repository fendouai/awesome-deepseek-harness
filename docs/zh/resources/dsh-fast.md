---
title: "dsh-fast"
description: "只读性能诊断：会话加载耗时、spill/压缩统计、上下文注入量与 LLM 缓存命中率。"
keywords: "dsh-fast, developer, plugin, observability, deepseek harness, dsh"
---
# dsh-fast

> ⭐ **3** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 3 | 状态 | ✅ 活跃 |
| 作者 | [PerryLink](https://github.com/PerryLink) | 更新时间 | — |
| 子分类 | 💰 费用与统计 | 能力 | observability |

## 一句话介绍

> 只读性能诊断：会话加载耗时、spill/压缩统计、上下文注入量与 LLM 缓存命中率。

## 详细介绍

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-fast` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **Read-only performance diagnostics for DeepSeek Harness.** *Observes the session event stream — never the model hot path — and reports where latency and context budget actually go.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ 核心特性

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-fast` (counts toward the [deepseek1024.com](https://deepseek1024.com

## 📦 安装

```bash
# From a scratch profile (pins the commit; runs the self-contained `prepare` build)
dsh plugin --profile demo add "github:YOUR_ORG/dsh-fast#<sha>"
# The profile's pnpm-workspace.yaml gains an allowBuilds entry for dsh-fast on first add.
```

## 🚀 快速开始

```bash
dsh plugin --profile demo add dsh-fast
```

## 📚 更多信息

**Install & uninstall**

dsh plugin --profile demo add dsh-fast # install dsh plugin --profile demo remove dsh-fast # uninstall Verify the row mounts: `dsh --profile demo --dump-config | grep dsh-fast`.

**Configuration**

All tunables are Schemastery `Config` fields; invalid values fail the profile load loudly.

## 🔗 链接

- [GitHub 仓库](https://github.com/PerryLink/dsh-fast)
- [完整 README](https://github.com/PerryLink/dsh-fast#readme)
- [返回dsh-fast所在分类](../plugins.md)
