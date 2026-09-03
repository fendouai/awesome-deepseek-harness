---
title: "dsh-codex-auth"
description: "DeepSeek Harness plugin that reuses the local Codex CLI ChatGPT login and adds a native GPT Auth settings card"
keywords: "dsh-codex-auth, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-codex-auth

> ⭐ **13** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 13 | Status | ✅ active |
| Author | [suntianc](https://github.com/suntianc) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> DeepSeek Harness plugin that reuses the local Codex CLI ChatGPT login and adds a native GPT Auth settings card

## About

Current alpha release: **v0.3.3-alpha.5**, aligned with DSH `0.1.2-alpha.5`, Cordis `4.0.2`, Schemastery `3.18.2`, and pi-ai `0.84.4`. A self-contained [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) **Codex Capability Bundle**. It reuses the ChatGPT login maintained by the official **Codex CLI** (`~/.codex/auth.json`, or `$CODEX_HOME/auth.json`) for: - the `openai-codex` LLM route; - a Global Codex Search Provider behind DSH's stock `web_search` tool; - durable image generation and editing through `generate_image`, plus the model-facing `list_images` catalog; - resilient weekly Codex usage status; - one native **GPT Auth** Settings section with Login, LLM Context, Web Search, and Image Creation cards; detailed Search/Image controls collapse into compact rows.

## ✨ Key Features

- the `openai-codex` LLM route;
- a Global Codex Search Provider behind DSH's stock `web_search` tool;
- durable image generation and editing through `generate_image`, plus the
- resilient weekly Codex usage status;
- one native **GPT Auth** Settings section with Login, LLM Context, Web Search,

## 📦 Install

```bash
dsh plugin --profile web add dsh-codex-auth@0.3.3-alpha.5
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add https://github.com/suntianc/dsh-codex-auth/releases/download/v0.3.3-alpha.5/dsh-codex-auth-0.3.3-alpha.5.tgz
```

## 📚 Learn more

**Install from npm (recommended)**

The npm package includes prebuilt Host and browser bundles, so no install-time build permission is required. Install the alpha.5-aligned release explicitly: dsh plugin --profile web add dsh-codex-auth@0.3.3-alpha.5 With the Web Host bound explicitly to `127.0.0.1`, restart `dsh web`, open Settings, and select **GPT Auth**.

**Install a prebuilt release**

dsh plugin --profile web add https://github.com/suntianc/dsh-codex-auth/releases/download/v0.3.3-alpha.5/dsh-codex-auth-0.3.3-alpha.5.tgz With the Web Host bound explicitly to `127.0.0.1`, restart `dsh web`, open Settings, and select **GPT Auth**.

**Install from the tagged GitHub source**

dsh plugin --profile web add github:suntianc/dsh-codex-auth#v0.3.3-alpha.5 Git dependencies are built by the package's `prepare` script. pnpm 10+ blocks that script until explicitly allowed, so the first command may print an `allowBuilds` key and stop. Copy the **exact key printed by dsh** under `allowBuilds` in the `pnpm-workspace.yaml` path printed by dsh, then run the command again. Only grant 

**Install a tarball**

git clone --branch v0.3.3-alpha.5 --depth 1 https://github.com/suntianc/dsh-codex-auth.git cd dsh-codex-auth pnpm install pnpm pack dsh plugin --profile web add ./dsh-codex-auth-0.3.3-alpha.5.tgz

## 🔗 Links

- [GitHub Repository](https://github.com/suntianc/dsh-codex-auth)
- [Full README](https://github.com/suntianc/dsh-codex-auth#readme)
- [Back to the Plugins list](../plugins.md)
