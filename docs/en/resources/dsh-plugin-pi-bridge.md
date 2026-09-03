---
title: "dsh-plugin-pi-bridge"
description: "Bridge pi skills and config into DeepSeek Harness"
keywords: "dsh-plugin-pi-bridge, developer, integration, coding, deepseek harness, dsh"
---
# dsh-plugin-pi-bridge

> ⭐ **2** · ✅ active · integration

| | | | |
|---|---|---|---|
| Type | integration | Category | Developer tools |
| Stars | ⭐ 2 | Status | ✅ active |
| Author | [YYTbit](https://github.com/YYTbit) | Updated | — |

## One-liner

> Bridge pi skills and config into DeepSeek Harness

## About

Bridge Pi Agent's skills into DeepSeek Harness -- zero migration.

## ✨ Key Features

- `~/.config/pi/skills/<name>/SKILL.md` -- Injects skills as available skills

## 📦 Install

```bash
dsh plugin --profile your-profile add dsh-plugin-pi-bridge
```

## 🚀 Quick Start

```bash
- id: pi-bridge
  name: dsh-plugin-pi-bridge
  config:
    enableSkills: true
    maxSkills: 30
```

## 🔗 Links

- [GitHub Repository](https://github.com/YYTbit/dsh-plugin-pi-bridge)
- [Full README](https://github.com/YYTbit/dsh-plugin-pi-bridge#readme)
- [Back to the MCP & Integrations list](../integrations.md)
