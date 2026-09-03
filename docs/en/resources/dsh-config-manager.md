---
title: "dsh-config-manager"
description: "DeepSeek Harness (DSH) backup & restore plugin — export, import, migrate and sync your complete DSH configuration, plugins, MCP servers, skills and workspace. One-click migration to another machine."
keywords: "dsh-config-manager, registry, awesome-list, coding, mcp, deepseek harness, dsh"
---
# dsh-config-manager

> ⭐ **48** · ✅ active · awesome-list

| | | | |
|---|---|---|---|
| Type | awesome-list | Category | Registries |
| Stars | ⭐ 48 | Status | ✅ active |
| Author | [xiajiajun516](https://github.com/xiajiajun516) | Updated | — |

## One-liner

> DeepSeek Harness (DSH) backup & restore plugin — export, import, migrate and sync your complete DSH configuration, plugins, MCP servers, skills and workspace. One-click migration to another machine.

## About

**DeepSeek Harness Backup, Restore & Migration Plugin.** Backup, restore, export, import, migrate and sync your complete DeepSeek Harness (DSH) configuration — settings, model providers, plugins, MCP servers, skills, agent presets and workspaces — and restore your whole environment on a new machine with one click. - 🔄 **Backup & Restore** DeepSeek Harness configuration - 📦 **Export / Import** complete DSH configuration - 🚚 **Migrate** DSH to another machine - ⏰ **Scheduled full backups** — automatic, on your own cadence (6h / 12h / 24h / 7d / custom weekly), secrets never included - 🔌 Backup installed **plugins** and plugin configuration - 🧩 Backup **MCP servers** and **Skills** - 🔐 Encrypted backups with optional credentials - ☁️ **Git / WebDAV** configuration sync - 🛒 **Configuration mar

## ✨ Key Features

- 🔄 **Backup & Restore** DeepSeek Harness configuration
- 📦 **Export / Import** complete DSH configuration
- 🚚 **Migrate** DSH to another machine
- ⏰ **Scheduled full backups** — automatic, on your own cadence (6h / 12h / 24h / 7d / custom weekly), secrets never included
- 🔌 Backup installed **plugins** and plugin configuration
- 🧩 Backup **MCP servers** and **Skills**

## 📦 Install

```bash
# ① Install the plugin
dsh plugin --profile web add dsh-config-manager@latest

# ② Restart DSH (a "Backup & Migration" entry appears in Settings)
```

## 🚀 Quick Start

```bash
>   dsh plugin --profile web add dsh-config-manager@0.1.8
>
```

## 📚 Learn more

**🎒 DSH Config Manager**

**DeepSeek Harness Backup, Restore & Migration Plugin.** Backup, restore, export, import, migrate and sync your complete DeepSeek Harness (DSH) configuration — settings, model providers, plugins, MCP servers, skills, agent presets and workspaces — and restore your whole environment on a new machine with one click. [English](README.md) · [简体中文](README.zh-CN.md) ---

**Backup DeepSeek Harness configuration**

Create a portable backup of your DSH settings, model providers, plugins, MCP servers, skills, agent presets, profiles and workspace — one ZIP file, no secret values included by default.

**Migrate DSH configuration to a new computer**

Move your complete DeepSeek Harness setup without manually reinstalling plugins, MCP servers and skills. Dead absolute paths are detected and remapped automatically (batch prefix mapping supported).

**Sync DSH configuration across machines**

Keep portable configuration synchronized between machines through a private Git repository or WebDAV — secrets never sync.

## 🔗 Links

- [GitHub Repository](https://github.com/xiajiajun516/dsh-config-manager)
- [Full README](https://github.com/xiajiajun516/dsh-config-manager#readme)
- [Back to the Awesome Lists & Registries list](../awesome-lists.md)
