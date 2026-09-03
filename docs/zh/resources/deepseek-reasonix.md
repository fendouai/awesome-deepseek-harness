---
title: "DeepSeek-Reasonix"
description: "面向终端、DeepSeek 原生的 AI 编程代理，围绕前缀缓存稳定性设计——可常驻运行。"
keywords: "DeepSeek-Reasonix, harness, related, coding, terminal, deepseek harness, dsh"
---
# DeepSeek-Reasonix

> ⭐ **35,284** · ✅ 活跃 · 相关

| | | | |
|---|---|---|---|
| 类型 | 相关 | 分类 | Harness |
| 星数 | ⭐ 35,284 | 状态 | ✅ 活跃 |
| 作者 | [esengine](https://github.com/esengine) | 更新时间 | — |

## 一句话介绍

> 面向终端、DeepSeek 原生的 AI 编程代理，围绕前缀缓存稳定性设计——可常驻运行。

## 详细介绍

- **Config-driven.** Providers, the agent, enabled tools, and plugins are all declared in `reasonix.toml`. No hardcoded models. - **Multi-model & composable.** DeepSeek ships as a preset; any OpenAI-compatible endpoint is a config entry, not new code. Optionally run two models together (executor + planner) in separate, cache-stable sessions. - **Plugin-driven.** MCP servers contribute tools, prompts, and resources; Extension Protocol v1 sidecars can also intercept runtime events, contribute Providers and structured UI, and ship versioned plugin packages. - **Cache-aware context maintenance.** Startup injects a small stable environment summary, stale tool output is snipped/pruned before summary compaction, and the built-in tool schema contract is documented for regression review. - **Zero-f

## ✨ 核心特性

- **Config-driven.** Providers, the agent, enabled tools, and plugins are all
- **Multi-model & composable.** DeepSeek ships as a preset; any
- **Plugin-driven.** MCP servers contribute tools, prompts, and resources;
- **Cache-aware context maintenance.** Startup injects a small stable environment
- **Zero-friction distribution.** `CGO_ENABLED=0` single binary; cross-compile

## 📦 安装

```bash
npm i -g reasonix                  # any OS; pulls the prebuilt native binary
brew install esengine/reasonix/reasonix   # macOS
```

## 🚀 快速开始

```bash
git clone https://github.com/esengine/DeepSeek-Reasonix.git
cd DeepSeek-Reasonix
```

## 📚 更多信息

**Install**

Choose the path that matches how you want to use Reasonix. The CLI/TUI, desktop app, and VS Code extension all use the same local Reasonix engine.

## 🔗 链接

- [GitHub 仓库](https://github.com/esengine/DeepSeek-Reasonix)
- [完整 README](https://github.com/esengine/DeepSeek-Reasonix#readme)
- [返回DeepSeek-Reasonix所在分类](../related.md)
