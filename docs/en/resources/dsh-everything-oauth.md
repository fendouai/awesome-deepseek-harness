---
title: "dsh-everything-oauth"
description: "Import local Codex / Grok / Claude / OpenCode / CC Switch logins into DeepSeek Harness"
keywords: "dsh-everything-oauth, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-everything-oauth

> ⭐ **3** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 3 | Status | ✅ active |
| Author | [kam74515-boop](https://github.com/kam74515-boop) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> Import local Codex / Grok / Claude / OpenCode / CC Switch logins into DeepSeek Harness

## About

Import local coding-platform logins into [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) without signing in again. Scans the same places [CC Switch](https://github.com/farion1231/cc-switch) cares about: Official routes: `claude-oauth`, `codex-oauth`, `grok-oauth`, `gemini-oauth`, `copilot-oauth`. CC Switch gateways become `everything-*` custom routes (Anthropic-compatible or OpenAI-compatible).

## 📦 Install

```bash
dsh plugin --profile web add github:kam74515-boop/dsh-everything-oauth
dsh web
```

## 🚀 Quick Start

```bash
dsh plugin --profile web exec dsh-everything-oauth status
dsh plugin --profile web exec dsh-everything-oauth import live:codex-auth live:grok-auth
```

## 📚 Learn more

**Install**

dsh plugin --profile web add github:kam74515-boop/dsh-everything-oauth dsh web Then **Settings → Everything OAuth**: 1. **Sources** — select local logins / keys 2. **Imported** — enable only the models you want in the picker CLI: dsh plugin --profile web exec dsh-everything-oauth status dsh plugin --profile web exec dsh-everything-oauth import live:codex-auth live:grok-auth Source files are read-o

## 🔗 Links

- [GitHub Repository](https://github.com/kam74515-boop/dsh-everything-oauth)
- [Full README](https://github.com/kam74515-boop/dsh-everything-oauth#readme)
- [Back to the Plugins list](../plugins.md)
