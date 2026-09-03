---
title: "dsh-codex"
description: "Use your ChatGPT subscription in DeepSeek Harness through OpenAI's Codex sign-in flow"
keywords: "dsh-codex, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-codex

> ⭐ **51** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 51 | Status | ✅ active |
| Author | [Yan-Zero](https://github.com/Yan-Zero) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> Use your ChatGPT subscription in DeepSeek Harness through OpenAI's Codex sign-in flow

## About

Use a ChatGPT subscription in [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) through OpenAI's Codex sign-in flow—no OpenAI Platform API key required and no dsh source patch required. `dsh-codex` is an independent dsh bundle. It adds: - ChatGPT OAuth from the dsh Settings panel or a standalone CLI, with automatic token refresh - the Codex GPT catalog, including vision-capable models when the account offers them - a live client-side context-window capacity override for dsh's token meter and compaction policy - streaming, tool calls, reasoning replay, prompt caching, and dsh compaction through the normal LLM service - Codex standalone web search through dsh's existing `web_search` tool - optional HTTP(S) URL input added to Harness's existing `read_image` tool - an `imageg

## ✨ Key Features

- ChatGPT OAuth from the dsh Settings panel or a standalone CLI, with automatic token refresh
- the Codex GPT catalog, including vision-capable models when the account offers them
- a live client-side context-window capacity override for dsh's token meter and compaction policy
- streaming, tool calls, reasoning replay, prompt caching, and dsh compaction through the normal LLM service
- Codex standalone web search through dsh's existing `web_search` tool
- optional HTTP(S) URL input added to Harness's existing `read_image` tool

## 📦 Install

```bash
dsh plugin --profile web add dsh-codex
dsh web
```

## 🚀 Quick Start

```bash
dsh plugin --profile web exec dsh-openai-codex login
dsh plugin --profile web exec dsh-openai-codex login --device-code
dsh plugin --profile web exec dsh-openai-codex status
dsh plugin --profile web exec dsh-openai-codex doctor --json
dsh plugin --profile web exec dsh-openai-codex logout
```

## 📚 Learn more

**Install**

Install the prebuilt bundle from npm into the selected dsh profile: dsh plugin --profile web add dsh-codex dsh web From a DeepSeek Harness source checkout, use `pnpm dsh plugin --profile web add dsh-codex`. A local plugin checkout can still be installed with `link:/absolute/path/to/dsh-codex` for development. Open **Settings → OpenAI Codex → Sign in with ChatGPT**. The plugin opens OpenAI's author

## 🔗 Links

- [GitHub Repository](https://github.com/Yan-Zero/dsh-codex)
- [Full README](https://github.com/Yan-Zero/dsh-codex#readme)
- [Back to the Plugins list](../plugins.md)
