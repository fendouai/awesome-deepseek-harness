---
title: "dsh-plugin-opencode-bridge"
description: "Bridge opencode skills and config into DeepSeek Harness"
keywords: "dsh-plugin-opencode-bridge, developer, integration, coding, deepseek harness, dsh"
---
# dsh-plugin-opencode-bridge

> ⭐ **4** · ✅ active · integration

| | | | |
|---|---|---|---|
| Type | integration | Category | Developer tools |
| Stars | ⭐ 4 | Status | ✅ active |
| Author | [YYTbit](https://github.com/YYTbit) | Updated | — |

## One-liner

> Bridge opencode skills and config into DeepSeek Harness

## About

Bridge OpenCode's skills and configuration into DeepSeek Harness -- zero migration.

## ✨ Key Features

- `~/.config/opencode/skills/<name>/SKILL.md` -- Injects skills as available skills
- `~/.config/opencode/opencode.jsonc` -- Injects config context

## 📦 Install

```bash
dsh plugin --profile your-profile add dsh-plugin-opencode-bridge
```

## 🚀 Quick Start

```bash
- id: opencode-bridge
  name: dsh-plugin-opencode-bridge
  config:
    enableSkills: true
    maxSkills: 30
    enableConfig: true
```

## 📚 Learn more

**Configuration**

name: dsh-plugin-opencode-bridge config: enableSkills: true maxSkills: 30 enableConfig: true

## 🔗 Links

- [GitHub Repository](https://github.com/YYTbit/dsh-plugin-opencode-bridge)
- [Full README](https://github.com/YYTbit/dsh-plugin-opencode-bridge#readme)
- [Back to the MCP & Integrations list](../integrations.md)
