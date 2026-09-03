---
title: "dsh-codex-oauth"
description: "Use your OpenAI subscription with DeepSeek Harness to access GPT models, image generation, and web search."
keywords: "dsh-codex-oauth, search, plugin, coding, multimodal, deepseek harness, dsh"
---
# dsh-codex-oauth

> ⭐ **15** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 15 | Status | ✅ active |
| Author | [WNJXYK](https://github.com/WNJXYK) | Updated | — |
| Subcategory | 🌐 Web search | Capabilities | coding, multimodal, search |

## One-liner

> Use your OpenAI subscription with DeepSeek Harness to access GPT models, image generation, and web search.

## About

- **🚀 Direct subscription access** — GPT models, image generation, and web search share your OpenAI subscription quota. - **🧩 Controlled integration** — the model picker, generated images, and web search integrate into DeepSeek Harness with dedicated controls. - **🔐 Multiple sign-in methods** — supports browser sign-in and headless device-code authorization. - **🌗 UI adaptation** — follows DSH's English/Chinese language and Light, Dark, or System theme.

## ✨ Key Features

- **🚀 Direct subscription access** — GPT models, image generation, and web search share your OpenAI subscription quota.
- **🧩 Controlled integration** — the model picker, generated images, and web search integrate into DeepSeek Harness with dedicated controls.
- **🔐 Multiple sign-in methods** — supports browser sign-in and headless device-code authorization.
- **🌗 UI adaptation** — follows DSH's English/Chinese language and Light, Dark, or System theme.

## 📦 Install

```bash
dsh plugin --profile web add -w @wnjxyk/dsh-codex-oauth@latest
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add -w github:WNJXYK/dsh-codex-oauth
```

## 📚 Learn more

**🗑️ Uninstall**

npm and GitHub installations use the same removal command: dsh plugin --profile web remove -w @wnjxyk/dsh-codex-oauth

**⚙️ Detailed configuration**

No configuration is normally required. Available options are: Example Cordis configuration: - id: dsh-codex-oauth name: "@wnjxyk/dsh-codex-oauth" config: dshHome: /data/dsh path: /secure/codex-oauth.json preferencesPath: /secure/codex-oauth-preferences.json issuer: https://auth.openai.com usageUrl: https://chatgpt.com/backend-api/wham/usage controlPort: 1456 redirectPort: 1455 - id: codex-web-sear

## 🔗 Links

- [GitHub Repository](https://github.com/WNJXYK/dsh-codex-oauth)
- [Full README](https://github.com/WNJXYK/dsh-codex-oauth#readme)
- [Back to the Plugins list](../plugins.md)
