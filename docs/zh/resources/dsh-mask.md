---
title: "dsh-mask"
description: "PII masking middleware for DeepSeek Harness: anonymize names, phones, emails, ID cards, bank cards, keys, and addresses to placeholders before they reach the model, restore them at the display layer, keep the restore table only in memory and a controlled storage domain, never log plaintext, and expose /mask and the mask_test tool"
keywords: "dsh-mask, registry, awesome-list, coding, memory, ui, deepseek harness, dsh"
---
# dsh-mask

> ⭐ **3** · ✅ 活跃 · 精选列表

| | | | |
|---|---|---|---|
| 类型 | 精选列表 | 分类 | 注册表 |
| 星数 | ⭐ 3 | 状态 | ✅ 活跃 |
| 作者 | [PerryLink](https://github.com/PerryLink) | 更新时间 | — |

## 一句话介绍

> PII masking middleware for DeepSeek Harness: anonymize names, phones, emails, ID cards, bank cards, keys, and addresses to placeholders before they reach the model, restore them at the display layer, keep the restore table only in memory and a controlled storage domain, never log plaintext, and expose /mask and the mask_test tool

## 详细介绍

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-mask` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **PII masking middleware for DeepSeek Harness — anonymize personal data before it reaches the model, restore it at the display layer.** *Phones, emails, ID cards, bank cards, keys, and more become placeholders at the model boundary; the plaintext never enters your session log.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ 核心特性

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-mask` (counts toward the [deepseek1024.com](https://deepseek1024.com

## 📦 安装

```bash
# 1. install the bundle into your profile
dsh plugin --profile web add "github:PerryLink/dsh-mask#main"

# or from npm (published releases)
dsh plugin --profile web add dsh-mask

# 2. verify the row mounts
dsh --profile web --dump-config | grep -A2 'id: mask'
```

## 🚀 快速开始

```bash
- insert:
    - id: mask
      name: dsh-mask
      config:
        entities: [phone, email, id-card, bank-card, key]
```

## 📚 更多信息

**Install & uninstall**

`dsh-mask` no longer bundles the storage stack. Profiles that already compose it (the `web` profile does, via `@deepseek-ai/dsh-web-app`) provide `storageDomain`, so persistence works out of the box. On a bare profile without storage the plugin still mounts and masks, but the restore table is memory-only (lost on restart) — compose the storage stack in your profile patch, or set `persistRestoreTab

**Configuration**

All tunables are Schemastery `Config` fields (changeable from cordis.yml). An id-targeted override replaces the whole row — restate every key you need. `cordis.patch.yml` documents each key inline. Example override in your profile patch: - id: mask name: dsh-mask config: entities: [phone, email, id-card, bank-card, key, ip] persistRestoreTable: false registerCommand: true

## 🔗 链接

- [GitHub 仓库](https://github.com/PerryLink/dsh-mask)
- [完整 README](https://github.com/PerryLink/dsh-mask#readme)
- [返回dsh-mask所在分类](../awesome-lists.md)
