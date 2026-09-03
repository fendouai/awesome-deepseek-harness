---
title: "URL Manager"
description: "Agent-first URL and knowledge collection system: auto-categorize, tag, full-text search and shared collections."
keywords: "URL Manager, search, plugin, research, files, deepseek harness, dsh"
---
# URL Manager

> ⭐ **3** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 3 | Status | ✅ active |
| Author | [Piccolo123](https://github.com/Piccolo123) | Updated | 2026-08-14 |
| Subcategory | 🌐 Web search | Capabilities | search, research, files |

## One-liner

> Agent-first URL and knowledge collection system: auto-categorize, tag, full-text search and shared collections.

## About

**Deliver results as beautiful cards, not raw link dumps.** An [agentskills.io](https://agentskills.io)-compatible skill that lets AI agents save, organize, search, and share web resources on behalf of human users. Agents auto-register on first use — zero manual setup.

## ✨ Key Features

- **Agent-first auto-registration** — zero human setup
- **Save anything** — web links (URL auto-fetched) or plain-text notes
- **Full-text search** — across titles, descriptions, and AI summaries
- **Categories, tags, category sets** — hierarchical organization
- **Shared categories** — team collaboration with cocreate (co-editing) and subscribe (read-only) modes
- **Batch operations** — reorganize up to 50 items at once
- **Magic link delivery** — send organized collections as a polished card interface
- **Cross-platform** — Hermes, Claude Code, Cursor, Codex, OpenClaw

## 📦 Install

```bash
# User-level (any workspace):
mkdir -p ~/.dsh/skills
git clone --depth 1 https://github.com/Piccolo123/url-manager.git ~/.dsh/skills/url-manager

# Or project-level (one workspace):
mkdir -p .dsh/skills && cp -r SKILL.md scripts .dsh/skills/url-manager/
```

## 🚀 Quick Start

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

## 📚 Learn more

**Install**

hermes skills tap add Piccolo123/url-manager Works across Hermes, Claude Code, Cursor, Codex, and any agentskills.io-compatible agent.

## 🔗 Links

- [GitHub Repository](https://github.com/Piccolo123/url-manager)
- [Full README](https://github.com/Piccolo123/url-manager#readme)
- [Back to the Plugins list](../plugins.md)
