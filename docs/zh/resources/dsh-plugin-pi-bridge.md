---
title: "dsh-plugin-pi-bridge"
description: "Bridge pi skills and config into DeepSeek Harness"
keywords: "dsh-plugin-pi-bridge, developer, integration, coding, deepseek harness, dsh"
---
# dsh-plugin-pi-bridge

> ⭐ **2** · ✅ 活跃 · 集成

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | 开发者工具 |
| 星数 | ⭐ 2 | 状态 | ✅ 活跃 |
| 作者 | [YYTbit](https://github.com/YYTbit) | 更新时间 | — |

## 一句话介绍

> Bridge pi skills and config into DeepSeek Harness

## 详细介绍

Bridge Pi Agent's skills into DeepSeek Harness -- zero migration.

## ✨ 核心特性

- `~/.config/pi/skills/<name>/SKILL.md` -- Injects skills as available skills

## 📦 安装

```bash
dsh plugin --profile your-profile add dsh-plugin-pi-bridge
```

## 🚀 快速开始

```bash
- id: pi-bridge
  name: dsh-plugin-pi-bridge
  config:
    enableSkills: true
    maxSkills: 30
```

## 🔗 链接

- [GitHub 仓库](https://github.com/YYTbit/dsh-plugin-pi-bridge)
- [完整 README](https://github.com/YYTbit/dsh-plugin-pi-bridge#readme)
- [返回dsh-plugin-pi-bridge所在分类](../integrations.md)
