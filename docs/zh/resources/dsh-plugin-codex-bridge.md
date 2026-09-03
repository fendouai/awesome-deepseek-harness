---
title: "dsh-plugin-codex-bridge"
description: "Bridge codex skills and config into DeepSeek Harness"
keywords: "dsh-plugin-codex-bridge, developer, integration, coding, deepseek harness, dsh"
---
# dsh-plugin-codex-bridge

> ⭐ **2** · ✅ 活跃 · 集成

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | 开发者工具 |
| 星数 | ⭐ 2 | 状态 | ✅ 活跃 |
| 作者 | [YYTbit](https://github.com/YYTbit) | 更新时间 | — |

## 一句话介绍

> Bridge codex skills and config into DeepSeek Harness

## 详细介绍

Bridge OpenAI Codex's skills, instructions, and configuration into DeepSeek Harness -- zero migration.

## ✨ 核心特性

- `~/.codex/skills/<name>/SKILL.md` -- Injects skills as available skills
- `~/.codex/instructions.md` -- Injects instructions into system prompt
- `~/.codex/config.toml` -- Injects model/provider context

## 📦 安装

```bash
dsh plugin --profile your-profile add dsh-plugin-codex-bridge
```

## 🚀 快速开始

```bash
- id: codex-bridge
  name: dsh-plugin-codex-bridge
  config:
    enableSkills: true
    maxSkills: 30
    enableInstructions: true
    enableConfig: true
```

## 📚 更多信息

**Configuration**

name: dsh-plugin-codex-bridge config: enableSkills: true maxSkills: 30 enableInstructions: true enableConfig: true

## 🔗 链接

- [GitHub 仓库](https://github.com/YYTbit/dsh-plugin-codex-bridge)
- [完整 README](https://github.com/YYTbit/dsh-plugin-codex-bridge#readme)
- [返回dsh-plugin-codex-bridge所在分类](../integrations.md)
