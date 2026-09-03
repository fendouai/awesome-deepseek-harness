---
title: "dsh-sub2api"
description: "Connect your sub2api gateway to DeepSeek Harness: OpenAI-compatible multi-provider routes (OpenAI / Claude / Grok / Gemini) behind one base URL, with per-key model discovery, usage lookup, and a settings page."
keywords: "dsh-sub2api, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-sub2api

> ⭐ **2** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 2 | 状态 | ✅ 活跃 |
| 作者 | [GodD6366](https://github.com/GodD6366) | 更新时间 | — |
| 子分类 | 👁️ 视觉工具 | 能力 | coding |

## 一句话介绍

> Connect your sub2api gateway to DeepSeek Harness: OpenAI-compatible multi-provider routes (OpenAI / Claude / Grok / Gemini) behind one base URL, with per-key model discovery, usage lookup, and a settings page.

## 详细介绍

[中文文档](./README.zh.md) Connect your [sub2api](https://github.com/Wei-Shaw/sub2api) gateway to [DeepSeek Harness](https://github.com/deepseek-ai/dsh) as model providers. Sub2API is an AI API gateway that turns subscription quota into OpenAI-compatible endpoints. In its model, **each API key is bound to a group, and the group decides the platform** (OpenAI / Claude / Grok / Gemini) and the models that key can serve. The four provider routes (`sub2api-openai`, `sub2api-claude`, `sub2api-grok`, `sub2api-gemini`) are served by the harness's own pi-ai adapter (`dsh-llm-pi-ai`): this plugin translates its `llm-sub2api:` settings into `llm-pi-ai:` provider profiles (all sharing one **bare-host** base URL, no `/v1`), and protocol serialization, streaming, and usage accounting all live in pi-ai. The

## ✨ 核心特性

- **One base URL, four provider routes**: `sub2api-openai`, `sub2api-claude`, `sub2api-grok`, `sub2api-gemini` — each configured with its own key, registered as a
- **Streaming chat (backed by pi-ai)**: SSE streaming, tool calls, reasoning deltas, and token usage are mapped to the harness protocol by `dsh-llm-pi-ai`, which 
- **Model discovery**: one-click "fetch models" calls `GET {baseURL}/models` with the key, so each route's catalog matches exactly what the sub2api group serves.
- **Reasoning effort (thinking mode)**: `reasoning_effort` is passed straight through to the gateway and adjustable right in the chat model selector; the settings
- **Usage lookup**: "view usage" calls `GET {baseURL}/usage` and summarizes quota, balance, rate limits, and subscription windows.
- **Standards-based config**: base URL and model catalogs live in the `llm-sub2api:` settings section (`$DSH_HOME/settings.yaml`, written by the web Models page);
- **Global vision / image tools**: `analyze_image` and `generate_image` stay available even when the current chat model cannot see or create images. They call a d
- **Auto Vision wrapper**: image capability for text-only models. Every registered text-only provider route gets a same-name twin (`<route>-vision`, shown as "… +

## 📦 安装

```bash
dsh plugin --profile web add @godd6366/dsh-sub2api
```

## 🚀 快速开始

```bash
dsh plugin --profile web add .
```

## 📚 更多信息

**Install**

dsh plugin --profile web add @godd6366/dsh-sub2api or, from this repository: dsh plugin --profile web add .

**Configure**

Open **Settings → Sub2API 模型** (or edit `$DSH_HOME/settings.yaml` directly): llm-sub2api: baseURL: http://localhost:8080 providers: openai: apiKeyEnv: SUB2API_OPENAI_API_KEY models: - id: gpt-4o claude: apiKeyEnv: SUB2API_CLAUDE_API_KEY grok: apiKeyEnv: SUB2API_GROK_API_KEY gemini: apiKeyEnv: SUB2API_GEMINI_API_KEY tools: analyze: provider: openai model: gpt-4o generate: provider: openai model: gp

## 🔗 链接

- [GitHub 仓库](https://github.com/GodD6366/dsh-sub2api)
- [完整 README](https://github.com/GodD6366/dsh-sub2api#readme)
- [返回dsh-sub2api所在分类](../plugins.md)
