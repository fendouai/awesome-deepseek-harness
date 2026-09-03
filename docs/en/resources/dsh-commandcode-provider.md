---
title: "dsh-commandcode-provider"
description: "Unofficial DeepSeek Harness LLM provider plugin for Command Code: live model catalog, reasoning-effort support, Models-page card. Ported from pi-commandcode-provider (MIT)."
keywords: "dsh-commandcode-provider, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-commandcode-provider

> ⭐ **83** · ✅ active · plugin · ⬆️ +9 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 83 | Status | ✅ active |
| Author | [Mars-Sea](https://github.com/Mars-Sea) | Updated | 2026-08-21 |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> Unofficial DeepSeek Harness LLM provider plugin for Command Code: live model catalog, reasoning-effort support, Models-page card. Ported from pi-commandcode-provider (MIT).

## About

Unofficial [DeepSeek Harness](https://deepseek-harness.github.io/deepseek-harness/) LLM provider plugin for **Command Code**, ported from [pi-commandcode-provider](https://github.com/patlux/pi-commandcode-provider) (MIT).

## ✨ Key Features

- **Plugin bundle** — install into any dsh profile with `dsh plugin add`; registers a `commandcode` provider route with a live model catalog.
- **Dedicated settings page** — API key, connection options, a live account-usage card, and a "Hide out-of-plan models" toggle.
- **Models-page key card** — the **Settings → Models → Command Code** card carries the key status, a paste field, and the sign-in button inline.
- **In-browser sign-in for keys** — start the official authorization flow (the same one `cmd login` runs) from the settings page; the approved key lands in the lo
- **Multi-account rotation** — when one account hits its usage limit, requests switch to the next account automatically. See [Account rotation](#account-rotation)
- **Flexible API key setup** — via the settings page, an environment variable, or the official CLI login file.

## 📦 Install

```bash
dsh plugin --profile web add @mars-sea/dsh-commandcode-provider@alpha
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add @mars-sea/dsh-commandcode-provider@latest
```

## 📚 Learn more

**Install**

Pick the release line that matches your DeepSeek Harness version: ```sh dsh plugin --profile web add @mars-sea/dsh-commandcode-provider@alpha ``` ```sh dsh plugin --profile web add @mars-sea/dsh-commandcode-provider@latest ``` > The `alpha` tag never moves `latest`: a plain `@latest` install always gets the newest stable release for older Harness versions, and upgrading to the alpha line is always

**Usage dashboard**

The plugin registers a `/commandcode` slash command showing per-account usage: /commandcode (or /commandcode status) The command's user-facing copy follows the shell's locale: explicit `lang: 'en' | 'zh'` in the `llm-commandcode` plugin config wins, otherwise `LC_ALL`/`LANG` is read, otherwise it falls back to `zh`. The web settings page is independent — it follows the browser's language preferenc

**Configure**

**Settings → Command Code** covers the API key, API base URL, working directory, and request/stream timeouts; once a key is saved, a live **Account usage** card appears at the top of the page. The same options live in `$DSH_HOME/settings.yaml` (changes apply immediately, no restart): llm-commandcode: apiKeyEnv: COMMANDCODE_API_KEY # credential reference apiBase: https://api.commandcode.ai workingD

**Disabling / uninstalling**

```sh dsh plugin --profile web remove @mars-sea/dsh-commandcode-provider ``` Your API key in the dsh credential store and `~/.commandcode/auth.json` are left untouched.

## 🔗 Links

- [GitHub Repository](https://github.com/Mars-Sea/dsh-commandcode-provider)
- [Full README](https://github.com/Mars-Sea/dsh-commandcode-provider#readme)
- [Back to the Plugins list](../plugins.md)
