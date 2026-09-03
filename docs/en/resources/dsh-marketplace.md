---
title: "dsh-marketplace"
description: "A safe, live plugin marketplace for DeepSeek Harness"
keywords: "dsh-marketplace, registry, awesome-list, coding, deepseek harness, dsh"
---
# dsh-marketplace

> ⭐ **3** · ✅ active · awesome-list

| | | | |
|---|---|---|---|
| Type | awesome-list | Category | Registries |
| Stars | ⭐ 3 | Status | ✅ active |
| Author | [ouyangyipeng](https://github.com/ouyangyipeng) | Updated | 2026-08-14 |

## One-liner

> A safe, live plugin marketplace for DeepSeek Harness

## About

[DS-Harness Desktop](https://github.com/ouyangyipeng/dsh-desktop) 从 `desktop-v0.2.0` 起离线内置固定版本的 Marketplace。打开应用后进入 **设置 → 插件 → Marketplace**，不需要先安装本插件。 内置版本显示“Desktop 内置”，不能在 Marketplace 里更新或卸载自己；它随经过验证的 Desktop release 更新。其他插件仍安装进 Desktop 隔离的 `web` profile。

## 📦 Install

```bash
dsh plugin --profile web add "github:ouyangyipeng/dsh-marketplace#v0.1.1"
```

## 🚀 Quick Start

```bash
dsh plugin --profile web update dsh-marketplace
dsh plugin --profile web remove dsh-marketplace
```

## 📚 Learn more

**配置**

独立安装使用以下保守默认值： - id: dsh-marketplace name: dsh-marketplace config: profile: web cacheTtlMs: 600000 可选配置：

## 🔗 Links

- [GitHub Repository](https://github.com/ouyangyipeng/dsh-marketplace)
- [Full README](https://github.com/ouyangyipeng/dsh-marketplace#readme)
- [Back to the Awesome Lists & Registries list](../awesome-lists.md)
