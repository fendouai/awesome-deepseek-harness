---
title: "DeepSeek-Reasonix"
description: "DeepSeek-native AI coding agent for your terminal, engineered around prefix-cache stability — leave it running."
keywords: "DeepSeek-Reasonix, harness, related, coding, terminal, deepseek harness, dsh"
---
# DeepSeek-Reasonix

> ⭐ **35,284** · ✅ active · related

| | | | |
|---|---|---|---|
| Type | related | Category | Harness |
| Stars | ⭐ 35,284 | Status | ✅ active |
| Author | [esengine](https://github.com/esengine) | Updated | — |

## One-liner

> DeepSeek-native AI coding agent for your terminal, engineered around prefix-cache stability — leave it running.

## About

- **Config-driven.** Providers, the agent, enabled tools, and plugins are all declared in `reasonix.toml`. No hardcoded models. - **Multi-model & composable.** DeepSeek ships as a preset; any OpenAI-compatible endpoint is a config entry, not new code. Optionally run two models together (executor + planner) in separate, cache-stable sessions. - **Plugin-driven.** MCP servers contribute tools, prompts, and resources; Extension Protocol v1 sidecars can also intercept runtime events, contribute Providers and structured UI, and ship versioned plugin packages. - **Cache-aware context maintenance.** Startup injects a small stable environment summary, stale tool output is snipped/pruned before summary compaction, and the built-in tool schema contract is documented for regression review. - **Zero-f

## ✨ Key Features

- **Config-driven.** Providers, the agent, enabled tools, and plugins are all
- **Multi-model & composable.** DeepSeek ships as a preset; any
- **Plugin-driven.** MCP servers contribute tools, prompts, and resources;
- **Cache-aware context maintenance.** Startup injects a small stable environment
- **Zero-friction distribution.** `CGO_ENABLED=0` single binary; cross-compile

## 📦 Install

```bash
npm i -g reasonix                  # any OS; pulls the prebuilt native binary
brew install esengine/reasonix/reasonix   # macOS
```

## 🚀 Quick Start

```bash
git clone https://github.com/esengine/DeepSeek-Reasonix.git
cd DeepSeek-Reasonix
```

## 📚 Learn more

**Install**

Choose the path that matches how you want to use Reasonix. The CLI/TUI, desktop app, and VS Code extension all use the same local Reasonix engine.

## 🔗 Links

- [GitHub Repository](https://github.com/esengine/DeepSeek-Reasonix)
- [Full README](https://github.com/esengine/DeepSeek-Reasonix#readme)
- [Back to the Related Agent Harnesses list](../related.md)
