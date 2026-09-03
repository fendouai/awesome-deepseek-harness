---
title: "dsh-doublecheck"
description: "工程纪律循环：编辑前需求拷问、红/绿测试证据门、对抗式交付审查。"
keywords: "dsh-doublecheck, workflow, coding, deepseek harness, dsh"
---
# dsh-doublecheck

> ⭐ **4** · ✅ 活跃 · 工作流 · 近期 ⬆️ +2

| | | | |
|---|---|---|---|
| 类型 | 工作流 | 分类 | 工作流 |
| 星数 | ⭐ 4 | 状态 | ✅ 活跃 |
| 作者 | [PerryLink](https://github.com/PerryLink) | 更新时间 | 2026-08-21 |

## 一句话介绍

> 工程纪律循环：编辑前需求拷问、红/绿测试证据门、对抗式交付审查。

## 详细介绍

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-doublecheck` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **The delivery quality gate for DeepSeek Harness: grill the requirements, test the implementation, prove the delivery — then gate the handoff with a deliverable/rework decision.** *Requirements get interrogated before the first edit; delivery is proven, never claimed.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ 核心特性

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-doublecheck` (counts toward the [deepseek1024.com](https://deepseek1

## 📦 安装

```bash
# 1. install the bundle into your profile
dsh plugin --profile web add "github:PerryLink/dsh-doublecheck#main"

# or from npm (published releases)
dsh plugin --profile web add dsh-doublecheck

# 2. restart and verify the row
dsh --profile web --dump-config | grep -E -A3 'id: doublecheck-(grill|guard)'
```

## 🚀 快速开始

```bash
# JSON (PR comment / status payload)
doublecheck-gate --format json --input gate-report.json
# SARIF 2.1.0 (code-scanning upload / status check)
doublecheck-gate --format sarif < gate-report.json
```

## 📚 更多信息

**Install & uninstall**

For a zero-configuration strict mode (every gate on at `block` intensity, gate coverage required), apply the shipped overlay on top of the bundle patch: `dsh --profile web --patch ./node_modules/dsh-doublecheck/strict.patch.yml`.

**Configuration**

All tunables are Schemastery `Config` fields (changeable from cordis.yml). An id-targeted override replaces the whole row — restate every key you need. `cordis.patch.yml` documents each key inline; Schema defaults are the single source of tuning defaults. Misconfiguration fails loud at load: invalid regexes, empty or duplicated name lists, out-of-range thresholds, and duplicate checklist ids throw

## 🔗 链接

- [GitHub 仓库](https://github.com/PerryLink/dsh-doublecheck)
- [完整 README](https://github.com/PerryLink/dsh-doublecheck#readme)
- [返回dsh-doublecheck所在分类](../workflows.md)
