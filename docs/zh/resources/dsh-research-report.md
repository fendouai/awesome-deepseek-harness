---
title: "dsh-research-report"
description: "可验证研究报告引擎：内容寻址证据台账 + 版本化封存报告，逐条声明带核验结论。"
keywords: "dsh-research-report, research, plugin, deepseek harness, dsh"
---
# dsh-research-report

> ⭐ **44** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 研究 |
| 星数 | ⭐ 44 | 状态 | ✅ 活跃 |
| 作者 | [PerryLink](https://github.com/PerryLink) | 更新时间 | — |

## 一句话介绍

> 可验证研究报告引擎：内容寻址证据台账 + 版本化封存报告，逐条声明带核验结论。

## 详细介绍

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-research-report` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **A verifiable research-report engine for DeepSeek Harness.** *Every claim is bound to immutable evidence snapshots, verified byte-for-byte, and sealed into a versioned report whose manifest hash anyone can recompute.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ 核心特性

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-research-report` (counts toward the [deepseek1024.com](https://deeps

## 📦 安装

```bash
# From a scratch profile (pins the commit; runs the self-contained `prepare` build)
dsh plugin --profile demo add "github:YOUR_ORG/dsh-research-report#<sha>"
# The profile's pnpm-workspace.yaml gains an allowBuilds entry for dsh-research-report on first add.
```

## 🚀 快速开始

```bash
dsh plugin --profile demo add dsh-research-report
```

## 📚 更多信息

**Install & uninstall**

dsh plugin --profile demo add dsh-research-report # install dsh plugin --profile demo remove dsh-research-report # uninstall Verify the row mounts: `dsh --profile demo --dump-config | grep dsh-research-report`.

**Configuration**

All tunables are Schemastery `Config` fields; invalid values fail the profile load loudly. Relative roots resolve against the harness working directory (the workspace).

## 🔗 链接

- [GitHub 仓库](https://github.com/PerryLink/dsh-research-report)
- [完整 README](https://github.com/PerryLink/dsh-research-report#readme)
- [返回dsh-research-report所在分类](../plugins.md)
