---
title: "dsh-llm-ollama"
description: "Native Ollama Cloud provider and Web configuration plugin for DeepSeek Harness"
keywords: "dsh-llm-ollama, search, plugin, coding, deepseek harness, dsh"
---
# dsh-llm-ollama

> ⭐ **3** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 3 | Status | ✅ active |
| Author | [NOirBRight](https://github.com/NOirBRight) | Updated | — |
| Subcategory | 🌐 Web search | Capabilities | coding |

## One-liner

> Native Ollama Cloud provider and Web configuration plugin for DeepSeek Harness

## About

Ollama Cloud integration for DeepSeek Harness. Chat uses Ollama's OpenAI-compatible Chat Completions endpoint through the shared pi-ai-backed adapter. Model discovery and the Web Search/Fetch providers remain on Ollama-native APIs because those independent capabilities are not part of the chat protocol. The package root exposes the Cordis plugin contract and OllamaAdapter. The same artifact exports ./client, which contributes the Ollama Cloud card under Settings → LLM Providers. The protocol and capability split is recorded in [ADR 0001](docs/adr/0001-separate-chat-protocol-from-ollama-capabilities.md). Compatibility: this release requires DeepSeek Harness `0.1.2-alpha.4` and `@deepseek-ai/cordis@4.0.2`; it is not compatible with Alpha.1–Alpha.3. Users on older runtimes must keep the last 

## ✨ Key Features

- This plugin contributes only its keyed card (`key: llm-ollama`) and its Host ``llm`` route; it does not install the page or the shared `llm-providers` namespace
- Without the owner (Headless or Web without `dsh-llm-providers-ui`): the Host model route `ollama-cloud` still works; in Web the Providers page and this card are
- The nav globe glyph is a temporary Alpha.4 DOM adapter owned only by `dsh-llm-providers-ui` (`src/client/nav-icon.ts`); this plugin does not ship that adapter.

## 📚 Learn more

**Installation**

DeepSeek Harness 0.1.2-alpha.4 is required. Install directly from GitHub: ~~~sh dsh plugin --profile web add --force \ https://github.com/NOirBRight/dsh-llm-providers-ui/releases/download/v0.1.3/dsh-llm-providers-ui-0.1.3.tgz dsh plugin --profile web add --force \ https://github.com/NOirBRight/dsh-llm-ollama/releases/download/v0.6.16/dsh-llm-ollama-0.6.16.tgz dsh web ~~~ The repository tracks rele

**Web configuration**

Open Settings → LLM Providers → Ollama Cloud. The card manages settings and credentials through the authenticated Connection RPC. The Host never returns the stored literal, and settings revision fencing does not pretend that credential storage and settings save are one atomic transaction. Fetch available models opens the picker immediately and calls the authenticated Connection RPC with the unsave

**Plugin configuration screenshots**

Cloud usage and the complete weekly model activity list: Sortable model catalog: The Models page lists saved ollama-cloud models and can select them. Current Harness releases do not expose a third-party editor slot inside that page, so this package owns its editor under Plugin configuration.

**Config**

~~~yaml name: 'dsh-llm-ollama' config: apiKeyEnv: OLLAMA_API_KEY baseURL: https://ollama.com/api defaultContextWindow: 262144 streamIdleTimeoutMs: 300000 webRequestTimeoutMs: 15000 retryPolicy: mode: normal maxRetries: 8 backoff: initialDelayMs: 500 maxDelayMs: 10000 jitterRatio: 0.1 models: - id: gpt-oss:20b name: GPT-OSS 20B contextWindow: 131072 thinking: true - id: llava name: LLaVA contextWin

## 🔗 Links

- [GitHub Repository](https://github.com/NOirBRight/dsh-llm-ollama)
- [Full README](https://github.com/NOirBRight/dsh-llm-ollama#readme)
- [Back to the Plugins list](../plugins.md)
