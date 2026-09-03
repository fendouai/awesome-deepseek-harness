---
title: "dsh-auto-memory"
description: "DSH 自动记忆插件:三层记忆(用户级/项目笔记/每日日志)自动注入与检索、每日反思、可视化面板与设置页,支持继承其他 AI 工具的历史记忆。An auto-memory plugin for the DeepSeek Harness Web GUI: three-layer memory (user-level / project notes / daily logs) with automatic injection and retrieval, daily reflections, a visual panel and settings page, and inheritance of memories from other AI tools."
keywords: "dsh-auto-memory, memory, plugin, coding, ui, deepseek harness, dsh"
---
# dsh-auto-memory

> ⭐ **25** · ✅ active · plugin · ⬆️ +4 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Memory & context |
| Stars | ⭐ 25 | Status | ✅ active |
| Author | [Aik358](https://github.com/Aik358) | Updated | 2026-08-21 |
| Subcategory | 🧠 Memory systems | Capabilities | coding, memory, ui |

## One-liner

> DSH 自动记忆插件:三层记忆(用户级/项目笔记/每日日志)自动注入与检索、每日反思、可视化面板与设置页,支持继承其他 AI 工具的历史记忆。An auto-memory plugin for the DeepSeek Harness Web GUI: three-layer memory (user-level / project notes / daily logs) with automatic injection and retrieval, daily reflections, a visual panel and settings page, and inheritance of memories from other AI tools.

## About

🌐 Landing page (full feature tour · data flow · papers · screenshots) Promo gallery · six frames · click any thumbnail to view full size Promo gallery, frame by frame (expand and flip through)

## 📦 Install

```bash
cd ~/.dsh/profiles/web
pnpm add @a9i5k4/dsh-auto-memory
```

## 🚀 Quick Start

```bash
"@a9i5k4/dsh-auto-memory"
```

## 📚 Learn more

**Install (one command)**

> Prerequisite: install [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) and start `dsh web` at least once. Run in the **profile directory** (`~/.dsh/profiles/web`): cd ~/.dsh/profiles/web pnpm add @a9i5k4/dsh-auto-memory Then edit `package.json` in that directory and append to the `dsh.profile.bundles` array: "@a9i5k4/dsh-auto-memory" Restart **dsh web** (the 「Memory」entry appe

**approve the onnxruntime-node / sharp native install scripts,**

pnpm approve-builds pnpm add @huggingface/transformers Restart `dsh web` — the welcome tour's semantic-engine step auto-detects readiness (SHA256 verify + inference self-test). Lexical BM25 (0GB) always works as a fallback; skipping the engine only lowers recall precision. > No pnpm? `npm install @a9i5k4/dsh-auto-memory` works the same. > pnpm v11 blocks packages published <1 day ago: set `minimum

**AI-era installation**

Copy this to the AI assistant you're already using: Install the npm package @a9i5k4/dsh-auto-memory in the DeepSeek Harness web profile directory ~/.dsh/profiles/web (pnpm add or npm install), append "@a9i5k4/dsh-auto-memory" to the dsh.profile.bundles array in package.json, then restart dsh web to activate the plugin.

**Configuration**

Config file `~/.dsh/dsh-auto-memory.json` (everything adjustable in the Settings GUI, zh/en UI and panel font size included): { "userMemoryDir": "~/.dsh/memory", "memoryRoot": "~/.dsh/memory/workspaces", "injectEnabled": true, "injectBudgetChars": 2400, "recentDaysInjected": 1, "reflectEnabled": true, "autoConsolidate": true, "autoConsolidateCooldownMinutes": 30, "autoConsolidateDailyMax": 8, "una

## 🔗 Links

- [GitHub Repository](https://github.com/Aik358/dsh-auto-memory)
- [Full README](https://github.com/Aik358/dsh-auto-memory#readme)
- [Back to the Plugins list](../plugins.md)
