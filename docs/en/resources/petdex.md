---
title: "petdex"
description: "A public gallery of animated pets for Codex, Claude Code, DeepSeek Harness, Hermes, OpenCode, Gemini CLI, and more."
keywords: "petdex, fun, plugin, coding, deepseek harness, dsh"
---
# petdex

> ⭐ **3,945** · ✅ active · plugin · ⬆️ +11 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Fun & lifestyle |
| Stars | ⭐ 3,945 | Status | ✅ active |
| Author | [crafter-station](https://github.com/crafter-station) | Updated | 2026-08-21 |

## One-liner

> A public gallery of animated pets for Codex, Claude Code, DeepSeek Harness, Hermes, OpenCode, Gemini CLI, and more.

## About

Petdex is three things working together: 1. **A web gallery** at [petdex.dev](https://petdex.dev) where the community submits, reviews, and showcases animated pets in the Codex sprite format. 2. **A CLI** that installs any pet on your machine with one command and ships them straight into Codex. 3. **A desktop app** that floats a pet on your screen and reacts to your coding agent's activity in real time. Every pet is a folder. Every folder is a Pokédex entry. Every entry is one `npx petdex install` away.

## 📦 Install

```bash
git clone https://github.com/crafter-station/petdex.git
cd petdex
bun install
bun run dev:docker
```

## 🚀 Quick Start

```bash
my-pet/
├── pet.json                Metadata: name, slug, tags, vibes, kind, frame size, animation states
└── spritesheet.webp        8x9 or v2 8x11 frame grid of 192x208 px each (or .png)
```

## 📚 Learn more

**Quick start**

Follow this checklist to get a pet installed, visible in Codex, and connected to the desktop app. 1. Install a known pet: npx petdex install boba You should see `~/.petdex/pets/boba/` with `pet.json` and a spritesheet. 2. Get the desktop app from [petdex.dev/download](https://petdex.dev/download). It runs on macOS, Linux and Windows. 3. Open it, then hit <kbd>Cmd</kbd>+<kbd>,</kbd> over the pet to

**Architecture**

crafter-station/petdex ├── src/ │ ├── app/[locale]/ Public site: gallery, /pets/<slug>, /collections, /built-with, /community, /create, /download, /submit, /u/<handle>, ... │ ├── app/api/cli/ CLI endpoints: OAuth config, submit (zip → presigned R2), dedup check, register │ ├── app/api/manifest/ Public manifest: every approved pet with its spritesheet URL │ ├── app/api/admin/ Admin review surface f

## 🔗 Links

- [GitHub Repository](https://github.com/crafter-station/petdex)
- [Full README](https://github.com/crafter-station/petdex#readme)
- [Back to the Plugins list](../plugins.md)
