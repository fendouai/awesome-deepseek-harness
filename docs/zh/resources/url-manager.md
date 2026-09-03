---
title: "URL Manager"
description: "Agent 优先的 URL 与知识收集系统：自动分类、标签、全文检索与共享收藏。"
keywords: "URL Manager, search, plugin, research, files, deepseek harness, dsh"
---
# URL Manager

> ⭐ **3** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 搜索与研究 |
| 星数 | ⭐ 3 | 状态 | ✅ 活跃 |
| 作者 | [Piccolo123](https://github.com/Piccolo123) | 更新时间 | 2026-08-14 |
| 子分类 | 🌐 网页搜索 | 能力 | search, research, files |

## 一句话介绍

> Agent 优先的 URL 与知识收集系统：自动分类、标签、全文检索与共享收藏。

## 详细介绍

**Deliver results as beautiful cards, not raw link dumps.** An [agentskills.io](https://agentskills.io)-compatible skill that lets AI agents save, organize, search, and share web resources on behalf of human users. Agents auto-register on first use — zero manual setup.

## ✨ 核心特性

- **Agent-first auto-registration** — zero human setup
- **Save anything** — web links (URL auto-fetched) or plain-text notes
- **Full-text search** — across titles, descriptions, and AI summaries
- **Categories, tags, category sets** — hierarchical organization
- **Shared categories** — team collaboration with cocreate (co-editing) and subscribe (read-only) modes
- **Batch operations** — reorganize up to 50 items at once
- **Magic link delivery** — send organized collections as a polished card interface
- **Cross-platform** — Hermes, Claude Code, Cursor, Codex, OpenClaw

## 📦 安装

```bash
# User-level (any workspace):
mkdir -p ~/.dsh/skills
git clone --depth 1 https://github.com/Piccolo123/url-manager.git ~/.dsh/skills/url-manager

# Or project-level (one workspace):
mkdir -p .dsh/skills && cp -r SKILL.md scripts .dsh/skills/url-manager/
```

## 🚀 快速开始

```bash
- insert:
    - id: mcp-url-manager
      name: '@deepseek-ai/dsh-mcp-client'
      config:
        serverName: url_manager
        transport: stdio
        command: uvx
        args: ['url-manager-mcp']
        env:
          FOOTPRINTS_ENDPOINT: 'https://ai.ocean94.com'
```

## 📚 更多信息

**Install**

hermes skills tap add Piccolo123/url-manager Works across Hermes, Claude Code, Cursor, Codex, and any agentskills.io-compatible agent.

## 🔗 链接

- [GitHub 仓库](https://github.com/Piccolo123/url-manager)
- [完整 README](https://github.com/Piccolo123/url-manager#readme)
- [返回URL Manager所在分类](../plugins.md)
