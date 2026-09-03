---
title: "dsh-config-manager"
description: "DeepSeek Harness (DSH) backup & restore plugin — export, import, migrate and sync your complete DSH configuration, plugins, MCP servers, skills and workspace. One-click migration to another machine."
keywords: "dsh-config-manager, registry, awesome-list, coding, mcp, deepseek harness, dsh"
---
# dsh-config-manager

> ⭐ **48** · ✅ 活跃 · 精选列表

| | | | |
|---|---|---|---|
| 类型 | 精选列表 | 分类 | 注册表 |
| 星数 | ⭐ 48 | 状态 | ✅ 活跃 |
| 作者 | [xiajiajun516](https://github.com/xiajiajun516) | 更新时间 | — |

## 一句话介绍

> DeepSeek Harness (DSH) backup & restore plugin — export, import, migrate and sync your complete DSH configuration, plugins, MCP servers, skills and workspace. One-click migration to another machine.

## 详细介绍

**DeepSeek Harness Backup, Restore & Migration Plugin.** Backup, restore, export, import, migrate and sync your complete DeepSeek Harness (DSH) configuration — settings, model providers, plugins, MCP servers, skills, agent presets and workspaces — and restore your whole environment on a new machine with one click. - 🔄 **Backup & Restore** DeepSeek Harness configuration - 📦 **Export / Import** complete DSH configuration - 🚚 **Migrate** DSH to another machine - ⏰ **Scheduled full backups** — automatic, on your own cadence (6h / 12h / 24h / 7d / custom weekly), secrets never included - 🔌 Backup installed **plugins** and plugin configuration - 🧩 Backup **MCP servers** and **Skills** - 🔐 Encrypted backups with optional credentials - ☁️ **Git / WebDAV** configuration sync - 🛒 **Configuration mar

## ✨ 核心特性

- 🔄 **Backup & Restore** DeepSeek Harness configuration
- 📦 **Export / Import** complete DSH configuration
- 🚚 **Migrate** DSH to another machine
- ⏰ **Scheduled full backups** — automatic, on your own cadence (6h / 12h / 24h / 7d / custom weekly), secrets never included
- 🔌 Backup installed **plugins** and plugin configuration
- 🧩 Backup **MCP servers** and **Skills**

## 📦 安装

```bash
# ① Install the plugin
dsh plugin --profile web add dsh-config-manager@latest

# ② Restart DSH (a "Backup & Migration" entry appears in Settings)
```

## 🚀 快速开始

```bash
>   dsh plugin --profile web add dsh-config-manager@0.1.8
>
```

## 📚 更多信息

**🎒 DSH Config Manager**

**DeepSeek Harness Backup, Restore & Migration Plugin.** Backup, restore, export, import, migrate and sync your complete DeepSeek Harness (DSH) configuration — settings, model providers, plugins, MCP servers, skills, agent presets and workspaces — and restore your whole environment on a new machine with one click. [English](README.md) · [简体中文](README.zh-CN.md) ---

**Backup DeepSeek Harness configuration**

Create a portable backup of your DSH settings, model providers, plugins, MCP servers, skills, agent presets, profiles and workspace — one ZIP file, no secret values included by default.

**Migrate DSH configuration to a new computer**

Move your complete DeepSeek Harness setup without manually reinstalling plugins, MCP servers and skills. Dead absolute paths are detected and remapped automatically (batch prefix mapping supported).

**Sync DSH configuration across machines**

Keep portable configuration synchronized between machines through a private Git repository or WebDAV — secrets never sync.

## 🔗 链接

- [GitHub 仓库](https://github.com/xiajiajun516/dsh-config-manager)
- [完整 README](https://github.com/xiajiajun516/dsh-config-manager#readme)
- [返回dsh-config-manager所在分类](../awesome-lists.md)
