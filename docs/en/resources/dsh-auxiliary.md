---
title: "dsh-auxiliary"
description: "Auxiliary models for DeepSeek Harness: vision understanding and context compression through dedicated model routes. DeepSeek Harness 辅助模型插件：为视觉理解、上下文压缩、审批审查、子代理、会话标题与图片生成提供独立的模型路由、工具与系统提示，全程不触碰主对话模型。"
keywords: "dsh-auxiliary, memory, plugin, coding, context, multimodal, deepseek harness, dsh"
---
# dsh-auxiliary

> ⭐ **4** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Memory & context |
| Stars | ⭐ 4 | Status | ✅ active |
| Author | [dsh-plugins](https://github.com/dsh-plugins) | Updated | 2026-08-21 |
| Subcategory | 📦 Context management | Capabilities | coding, context, multimodal |

## One-liner

> Auxiliary models for DeepSeek Harness: vision understanding and context compression through dedicated model routes. DeepSeek Harness 辅助模型插件：为视觉理解、上下文压缩、审批审查、子代理、会话标题与图片生成提供独立的模型路由、工具与系统提示，全程不触碰主对话模型。

## About

**Auxiliary models for DeepSeek Harness — dedicated model routes, tools, and system guidance for vision, compaction, reviews, subagents, titles, and image generation, without touching the main conversation model.** `dsh-auxiliary` is a [DeepSeek Harness](https://deepseek-harness.github.io/deepseek-harness/) plugin that layers auxiliary-model capabilities on the harness LLM seam (`ctx.llm`). It never replaces the main conversation model: each feature is an independent, optional route that kicks in only for its own narrow call category, so you can give expensive or specialized work (vision, compaction summaries, approval reviews, delegated subagents, session titles, image generation) its own cheap or capable model.

## 📦 Install

```bash
npm install          # installs dependencies (typescript, @deepseek-ai/* peers)
npm run typecheck    # tsc --noEmit
npm run build        # emits lib/
```

## 🚀 Quick Start

```bash
vision:
  provider: anvilcraft-ai     # any registered provider route
  model: mimo-v2.5            # a vision-capable model on that provider
tool:
  enabled: true               # register the inspect_image tool
  maxImageBytes: 10485760     # per-file size cap
  timeoutMs: 120000           # cooperative tool-call budget
```

## 📚 Learn more

**Installation**

Copy the block below and paste it to your DSH agent (the assistant in this web GUI). The agent performs the install and verification for you — no manual npm or profile editing needed: Install the @dsh-plugin/dsh-auxiliary plugin into the profile I specify (or ask me if I didn't name one). The npm package name is `@dsh-plugin/dsh-auxiliary`; use the GitHub source `github:dsh-plugins/dsh-auxiliary`,

**3. Settings integration and the model catalog**

The plugin registers its own settings namespace (`dsh-auxiliary`) with a schemastery schema; the settings page writes through `settings.update(...)`, and `installSettingsSection` keeps the plugin's resolved view in sync. Two details matter:

**5. Everything reconfigures live**

Each feature is owned by a `reconcile*()` + disposer pair: on every settings change the plugin re-resolves the config and registers or disposes exactly the pieces whose conditions changed. Saving a route in the web UI takes effect immediately.

**Configuration**

All fields are optional; defaults are shown. config: vision: maxTokens: 2048 # inspect_image output cap (provider/model written by the settings page) handoff: true # text-only main models may reference chat images via describe_image tool: enabled: true # register the inspect_image tool maxImageBytes: 10485760 # per-file size cap timeoutMs: 120000 # cooperative tool-call budget compact: enabled: fa

## 🔗 Links

- [GitHub Repository](https://github.com/dsh-plugins/dsh-auxiliary)
- [Full README](https://github.com/dsh-plugins/dsh-auxiliary#readme)
- [Back to the Plugins list](../plugins.md)
