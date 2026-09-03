---
title: "dsh-plugin-meta-memory"
description: "Structured long-term memory system for DeepSeek Harness"
keywords: "dsh-plugin-meta-memory, memory, plugin, coding, deepseek harness, dsh"
---
# dsh-plugin-meta-memory

> ⭐ **3** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 记忆与上下文 |
| 星数 | ⭐ 3 | 状态 | ✅ 活跃 |
| 作者 | [YYTbit](https://github.com/YYTbit) | 更新时间 | 2026-08-14 |
| 子分类 | 🧠 记忆系统 | 能力 | coding, memory |

## 一句话介绍

> Structured long-term memory system for DeepSeek Harness

## 详细介绍

Teaches the agent how to organize memories using a structured system: - **Units**: Work categories named `verb-modifier-noun.unit` - **Records**: Each memory has a brief (quick scan) and full (detailed) version - **Index**: Self-maintained global storyline - **Auto-injection**: Relevant briefs are injected into context automatically

## ✨ 核心特性

- **Units**: Work categories named `verb-modifier-noun.unit`
- **Records**: Each memory has a brief (quick scan) and full (detailed) version
- **Index**: Self-maintained global storyline
- **Auto-injection**: Relevant briefs are injected into context automatically

## 📦 安装

```bash
dsh plugin --profile your-profile add dsh-plugin-meta-memory
```

## 🚀 快速开始

```bash
.meta-memory/
├── index.md
└── units/
    ├── debug-auth-module.unit/
    │   ├── 0.token-refresh-fail.brief.md
    │   └── 0.token-refresh-fail.full.md
    └── read-deeplearning-paper.unit/
        ├── 0.transformer-attention.brief.md
        └── 0.transformer-attention.full.md
```

## 📚 更多信息

**Configuration**

name: dsh-plugin-meta-memory config: memoryPath: '~/.dsh/meta-memory' enableInjection: true enableSkill: true maxBriefBytes: 4096

## 🔗 链接

- [GitHub 仓库](https://github.com/YYTbit/dsh-plugin-meta-memory)
- [完整 README](https://github.com/YYTbit/dsh-plugin-meta-memory#readme)
- [返回dsh-plugin-meta-memory所在分类](../plugins.md)
