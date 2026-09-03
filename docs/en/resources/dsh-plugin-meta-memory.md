---
title: "dsh-plugin-meta-memory"
description: "Structured long-term memory system for DeepSeek Harness"
keywords: "dsh-plugin-meta-memory, memory, plugin, coding, deepseek harness, dsh"
---
# dsh-plugin-meta-memory

> ⭐ **3** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Memory & context |
| Stars | ⭐ 3 | Status | ✅ active |
| Author | [YYTbit](https://github.com/YYTbit) | Updated | 2026-08-14 |
| Subcategory | 🧠 Memory systems | Capabilities | coding, memory |

## One-liner

> Structured long-term memory system for DeepSeek Harness

## About

Teaches the agent how to organize memories using a structured system: - **Units**: Work categories named `verb-modifier-noun.unit` - **Records**: Each memory has a brief (quick scan) and full (detailed) version - **Index**: Self-maintained global storyline - **Auto-injection**: Relevant briefs are injected into context automatically

## ✨ Key Features

- **Units**: Work categories named `verb-modifier-noun.unit`
- **Records**: Each memory has a brief (quick scan) and full (detailed) version
- **Index**: Self-maintained global storyline
- **Auto-injection**: Relevant briefs are injected into context automatically

## 📦 Install

```bash
dsh plugin --profile your-profile add dsh-plugin-meta-memory
```

## 🚀 Quick Start

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

## 📚 Learn more

**Configuration**

name: dsh-plugin-meta-memory config: memoryPath: '~/.dsh/meta-memory' enableInjection: true enableSkill: true maxBriefBytes: 4096

## 🔗 Links

- [GitHub Repository](https://github.com/YYTbit/dsh-plugin-meta-memory)
- [Full README](https://github.com/YYTbit/dsh-plugin-meta-memory#readme)
- [Back to the Plugins list](../plugins.md)
