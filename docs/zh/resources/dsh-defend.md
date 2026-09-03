---
title: "dsh-defend"
description: "Prompt-injection, jailbreak, and secret-leak defense for DeepSeek Harness: Aho-Corasick detection with allow/ask/block interception and sanitized audit events"
keywords: "dsh-defend, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-defend

> ⭐ **5** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 5 | 状态 | ✅ 活跃 |
| 作者 | [PerryLink](https://github.com/PerryLink) | 更新时间 | — |
| 子分类 | 👁️ 视觉工具 | 能力 | coding |

## 一句话介绍

> Prompt-injection, jailbreak, and secret-leak defense for DeepSeek Harness: Aho-Corasick detection with allow/ask/block interception and sanitized audit events

## 详细介绍

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-defend` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **Prompt-injection, jailbreak, and secret-leak defense for DeepSeek Harness.** *Rules decide the known. Interception decides the rest — and everything is audited.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ 核心特性

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-defend` (counts toward the [deepseek1024.com](https://deepseek1024.c

## 📦 安装

```bash
# 1. install the bundle into your profile
dsh plugin --profile web add "github:PerryLink/dsh-defend#main"

# or from npm (published releases)
dsh plugin --profile web add dsh-defend

# 2. restart and verify the row
dsh --profile web --dump-config | grep -A3 'id: dsh-defend'
```

## 🚀 快速开始

```bash
inbound message ── agent/pre-step ── scan ── clean → next()/enter
tool arguments ── tools/pre-execute ── scan ── allow → next()
tool results   ── tools/post-execute ── scan ── block → feedback
                                  │
                                  └─ defend/detection audit (rule id, family,
                                     severity, decision — never matched text)
```

## 📚 更多信息

**Configuration**

All tunables are Schemastery `Config` fields (changeable from cordis.yml). An id-targeted override replaces the whole row — restate every key you need. `cordis.patch.yml` documents each key inline.

## 🔗 链接

- [GitHub 仓库](https://github.com/PerryLink/dsh-defend)
- [完整 README](https://github.com/PerryLink/dsh-defend#readme)
- [返回dsh-defend所在分类](../plugins.md)
