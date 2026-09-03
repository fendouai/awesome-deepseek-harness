---
title: "dsh-translate"
description: "Vendor parameter translation and deterministic JSON repair for DeepSeek Harness: /translate maps temperature/top_p/max_tokens/stop/system across 11 vendors, and the post-execute repair layer (plus fix_json) fixes broken JSON tool output without ever fabricating data"
keywords: "dsh-translate, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-translate

> ⭐ **2** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 2 | 状态 | ✅ 活跃 |
| 作者 | [PerryLink](https://github.com/PerryLink) | 更新时间 | — |
| 子分类 | 👁️ 视觉工具 | 能力 | coding |

## 一句话介绍

> Vendor parameter translation and deterministic JSON repair for DeepSeek Harness: /translate maps temperature/top_p/max_tokens/stop/system across 11 vendors, and the post-execute repair layer (plus fix_json) fixes broken JSON tool output without ever fabricating data

## 详细介绍

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-translate` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **Vendor parameter translation and deterministic JSON repair for DeepSeek Harness.** *Same request, every vendor. Broken JSON, fixed without inventing data.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ 核心特性

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-translate` (counts toward the [deepseek1024.com](https://deepseek102

## 📦 安装

```bash
# 1. install the bundle into your profile
dsh plugin --profile web add "github:PerryLink/dsh-translate#main"

# or from npm (published releases)
dsh plugin --profile web add dsh-translate

# 2. restart and verify the row
dsh --profile web --dump-config | grep -A2 'id: dsh-translate'
```

## 🚀 快速开始

```bash
> /translate openai ernie max_tokens
> Use fix_json to repair: {"a": 1,} against {"type":"object","properties":{"a":{"type":"integer"}},"required":["a"]}
```

## 📚 更多信息

**Configuration**

All tunables are Schemastery `Config` fields (changeable from cordis.yml). An id-targeted override replaces the whole row — restate every key you need. `cordis.patch.yml` documents each key inline. Example override in your profile patch: - id: dsh-translate name: dsh-translate config: enabled: true repair: enabled: true toolNames: ['emit-json'] strategies: escapeRepair: true trailingComma: true tr

## 🔗 链接

- [GitHub 仓库](https://github.com/PerryLink/dsh-translate)
- [完整 README](https://github.com/PerryLink/dsh-translate#readme)
- [返回dsh-translate所在分类](../plugins.md)
