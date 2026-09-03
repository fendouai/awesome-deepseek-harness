---
title: "dsh-mnemon"
description: "Three-tier local memory: runtime hot memory, project documents and long-term memory spaces, with supervised writeback."
keywords: "dsh-mnemon, memory, plugin, context, deepseek harness, dsh"
---
# dsh-mnemon

> ⭐ **156** · ✅ active · plugin · ⬆️ +23 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Memory & context |
| Stars | ⭐ 156 | Status | ✅ active |
| Author | [omdsh-dev](https://github.com/omdsh-dev) | Updated | 2026-08-21 |
| Subcategory | 🧠 Memory systems | Capabilities | memory, context |

## One-liner

> Three-tier local memory: runtime hot memory, project documents and long-term memory spaces, with supervised writeback.

## About

The tiers are not copies. A useful rule is: **every-turn context goes to Runtime, complete narratives go to Documents, and cross-task evidence goes to Memory Spaces.** Current instructions, repository files, and live tool results always outrank historical memory.

## 📦 Install

```bash
# macOS
brew install --cask mnemon-dev/tap/mnemon

# macOS / Linux via Go
go install github.com/mnemon-dev/mnemon@latest

mnemon --version
```

## 🚀 Quick Start

```bash
npm install -g @deepseek-ai/dsh@0.1.1-rc.2
dsh --version
```

## 📚 Learn more

**2. Install DSH and the plugin**

The registry installation remains verified against stable DSH 0.1.1-rc.2, whose complete profiles require Node.js `^22.19.0 || >=24.0.0`; Node 20 lacks host primitives used by rc.2. Source compatibility is also verified against the latest DSH 0.1.2-alpha.5 preview while rc.2 remains the recommended registry target. The dsh-mnemon package itself retains Node.js 20 compatibility for older compatible

## 🔗 Links

- [GitHub Repository](https://github.com/omdsh-dev/dsh-mnemon)
- [Full README](https://github.com/omdsh-dev/dsh-mnemon#readme)
- [Back to the Plugins list](../plugins.md)
