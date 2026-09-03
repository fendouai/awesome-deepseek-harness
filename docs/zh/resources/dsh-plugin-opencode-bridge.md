---
title: "dsh-plugin-opencode-bridge"
description: "Bridge opencode skills and config into DeepSeek Harness"
keywords: "dsh-plugin-opencode-bridge, developer, integration, coding, deepseek harness, dsh"
---
# dsh-plugin-opencode-bridge

> ⭐ **4** · ✅ 活跃 · 集成

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | 开发者工具 |
| 星数 | ⭐ 4 | 状态 | ✅ 活跃 |
| 作者 | [YYTbit](https://github.com/YYTbit) | 更新时间 | — |

## 一句话介绍

> Bridge opencode skills and config into DeepSeek Harness

## 详细介绍

Bridge OpenCode's skills and configuration into DeepSeek Harness -- zero migration.

## ✨ 核心特性

- `~/.config/opencode/skills/<name>/SKILL.md` -- Injects skills as available skills
- `~/.config/opencode/opencode.jsonc` -- Injects config context

## 📦 安装

```bash
dsh plugin --profile your-profile add dsh-plugin-opencode-bridge
```

## 🚀 快速开始

```bash
- id: opencode-bridge
  name: dsh-plugin-opencode-bridge
  config:
    enableSkills: true
    maxSkills: 30
    enableConfig: true
```

## 📚 更多信息

**Configuration**

name: dsh-plugin-opencode-bridge config: enableSkills: true maxSkills: 30 enableConfig: true

## 🔗 链接

- [GitHub 仓库](https://github.com/YYTbit/dsh-plugin-opencode-bridge)
- [完整 README](https://github.com/YYTbit/dsh-plugin-opencode-bridge#readme)
- [返回dsh-plugin-opencode-bridge所在分类](../integrations.md)
