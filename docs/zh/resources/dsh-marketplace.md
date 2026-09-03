---
title: "dsh-marketplace"
description: "A safe, live plugin marketplace for DeepSeek Harness"
keywords: "dsh-marketplace, registry, awesome-list, coding, deepseek harness, dsh"
---
# dsh-marketplace

> ⭐ **3** · ✅ 活跃 · 精选列表

| | | | |
|---|---|---|---|
| 类型 | 精选列表 | 分类 | 注册表 |
| 星数 | ⭐ 3 | 状态 | ✅ 活跃 |
| 作者 | [ouyangyipeng](https://github.com/ouyangyipeng) | 更新时间 | 2026-08-14 |

## 一句话介绍

> A safe, live plugin marketplace for DeepSeek Harness

## 详细介绍

[DS-Harness Desktop](https://github.com/ouyangyipeng/dsh-desktop) 从 `desktop-v0.2.0` 起离线内置固定版本的 Marketplace。打开应用后进入 **设置 → 插件 → Marketplace**，不需要先安装本插件。 内置版本显示“Desktop 内置”，不能在 Marketplace 里更新或卸载自己；它随经过验证的 Desktop release 更新。其他插件仍安装进 Desktop 隔离的 `web` profile。

## 📦 安装

```bash
dsh plugin --profile web add "github:ouyangyipeng/dsh-marketplace#v0.1.1"
```

## 🚀 快速开始

```bash
dsh plugin --profile web update dsh-marketplace
dsh plugin --profile web remove dsh-marketplace
```

## 📚 更多信息

**配置**

独立安装使用以下保守默认值： - id: dsh-marketplace name: dsh-marketplace config: profile: web cacheTtlMs: 600000 可选配置：

## 🔗 链接

- [GitHub 仓库](https://github.com/ouyangyipeng/dsh-marketplace)
- [完整 README](https://github.com/ouyangyipeng/dsh-marketplace#readme)
- [返回dsh-marketplace所在分类](../awesome-lists.md)
