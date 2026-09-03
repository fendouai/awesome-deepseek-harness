---
title: "dsh-permission-rules"
description: "Claude Code-style declarative permission rules for DeepSeek Harness: ordered allow/deny/ask rules with tool-name, argument (glob/regex), and workspace-path matching on the tools/pre-execute waterfall, session-log audit, and HMR reload."
keywords: "dsh-permission-rules, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-permission-rules

> ⭐ **65** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 65 | 状态 | ✅ 活跃 |
| 作者 | [PerryLink](https://github.com/PerryLink) | 更新时间 | — |
| 子分类 | 👁️ 视觉工具 | 能力 | coding |

## 一句话介绍

> Claude Code-style declarative permission rules for DeepSeek Harness: ordered allow/deny/ask rules with tool-name, argument (glob/regex), and workspace-path matching on the tools/pre-execute waterfall, session-log audit, and HMR reload.

## 详细介绍

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-permission-rules` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **Claude Code-style declarative permission rules for DeepSeek Harness.** *Rules decide what is known. A reviewer model decides what is not.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ 核心特性

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-permission-rules` (counts toward the [deepseek1024.com](https://deep

## 📦 安装

```bash
# 1. install the bundle into your profile
dsh plugin --profile web add "github:PerryLink/dsh-permission-rules#main"

# or from npm (published releases)
dsh plugin --profile web add dsh-permission-rules

# 2. restart and verify the row
dsh --profile web --dump-config | grep -A4 'id: permission-rules'
```

## 🚀 快速开始

```bash
node scripts/repair-session-logs.mjs scan [--home DIR]      # report foreign rows, change nothing
node scripts/repair-session-logs.mjs repair [--home DIR] [--dry-run]
```

## 📚 更多信息

**Configuration**

All tunables are Schemastery `Config` fields (changeable from cordis.yml). An id-targeted override replaces the whole row — restate every key you need.

## 🔗 链接

- [GitHub 仓库](https://github.com/PerryLink/dsh-permission-rules)
- [完整 README](https://github.com/PerryLink/dsh-permission-rules#readme)
- [返回dsh-permission-rules所在分类](../plugins.md)
