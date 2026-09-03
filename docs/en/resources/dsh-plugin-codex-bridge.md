---
title: "dsh-plugin-codex-bridge"
description: "Bridge codex skills and config into DeepSeek Harness"
keywords: "dsh-plugin-codex-bridge, developer, integration, coding, deepseek harness, dsh"
---
# dsh-plugin-codex-bridge

> ⭐ **2** · ✅ active · integration

| | | | |
|---|---|---|---|
| Type | integration | Category | Developer tools |
| Stars | ⭐ 2 | Status | ✅ active |
| Author | [YYTbit](https://github.com/YYTbit) | Updated | — |

## One-liner

> Bridge codex skills and config into DeepSeek Harness

## About

Bridge OpenAI Codex's skills, instructions, and configuration into DeepSeek Harness -- zero migration.

## ✨ Key Features

- `~/.codex/skills/<name>/SKILL.md` -- Injects skills as available skills
- `~/.codex/instructions.md` -- Injects instructions into system prompt
- `~/.codex/config.toml` -- Injects model/provider context

## 📦 Install

```bash
dsh plugin --profile your-profile add dsh-plugin-codex-bridge
```

## 🚀 Quick Start

```bash
- id: codex-bridge
  name: dsh-plugin-codex-bridge
  config:
    enableSkills: true
    maxSkills: 30
    enableInstructions: true
    enableConfig: true
```

## 📚 Learn more

**Configuration**

name: dsh-plugin-codex-bridge config: enableSkills: true maxSkills: 30 enableInstructions: true enableConfig: true

## 🔗 Links

- [GitHub Repository](https://github.com/YYTbit/dsh-plugin-codex-bridge)
- [Full README](https://github.com/YYTbit/dsh-plugin-codex-bridge#readme)
- [Back to the MCP & Integrations list](../integrations.md)
