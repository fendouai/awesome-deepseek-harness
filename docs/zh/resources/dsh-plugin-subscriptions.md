---
title: "dsh-plugin-subscriptions"
description: "Use ChatGPT (Codex), Claude, and Grok (X Premium) subscriptions as DeepSeek Harness LLM providers — OAuth login in the web UI, no API keys"
keywords: "dsh-plugin-subscriptions, search, plugin, coding, ui, deepseek harness, dsh"
---
# dsh-plugin-subscriptions

> ⭐ **216** · ✅ 活跃 · 插件 · 近期 ⬆️ +17

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 搜索与研究 |
| 星数 | ⭐ 216 | 状态 | ✅ 活跃 |
| 作者 | [V1ki](https://github.com/V1ki) | 更新时间 | 2026-08-21 |
| 子分类 | 🌐 网页搜索 | 能力 | coding, ui |

## 一句话介绍

> Use ChatGPT (Codex), Claude, and Grok (X Premium) subscriptions as DeepSeek Harness LLM providers — OAuth login in the web UI, no API keys

## 详细介绍

Use your **ChatGPT (Codex)**, **Claude**, **Grok (X Premium)**, and **GitHub Copilot** subscriptions as LLM providers in [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) — no API keys. Codex and Grok log in via OAuth in the dsh web UI (Settings → Subscriptions), while Copilot uses the GitHub OAuth device flow; Claude imports credentials from an existing Claude Code session when there is one (macOS Keychain or `~/.claude/.credentials.json`) and otherwise falls back to the same browser OAuth flow, so the Claude Code CLI is not required. Tokens live at `~/.dsh/plugins/subscriptions/auth.json` (mode 0600) and refresh automatically.

## ✨ 核心特性

- **`x_search`** tool (Grok) — xAI's hosted X search, returning `{ answer, citations }`.
- **`image_generate`** tool (ChatGPT or Grok) — `gpt-image-2` via the Codex backend, or `grok-imagine-image-2.0` via `api.x.ai/v1/images/generations`. The `provid
- **`video_generate`** tool (Grok) — `grok-imagine-video-1.5` via `api.x.ai/v1/videos` (async submit + poll); MP4s are saved under `~/.dsh/plugins/subscriptions/v

## 📦 安装

```bash
dsh plugin --profile web add dsh-plugin-subscriptions
```

## 🚀 快速开始

```bash
dsh plugin --profile web add github:V1ki/dsh-plugin-subscriptions
```

## 📚 更多信息

**Demo**

Settings → **Subscriptions**: per-provider login/logout, no API keys. Claude imports credentials from Claude Code when available and otherwise uses OAuth, as Codex and Grok always do (account address masked in the screenshot): Logged-in providers join the session model picker with their live model catalogs: Models that advertise reasoning levels get an **Effort** selector in the same menu — Codex 

**Install**

With the `dsh` CLI available, install from npm (prebuilt artifacts, no build permission needed): dsh plugin --profile web add dsh-plugin-subscriptions Or install the sources from GitHub: dsh plugin --profile web add github:V1ki/dsh-plugin-subscriptions pnpm will ask you to allow this package's build script on first install (git installs fetch sources, not built artifacts); add the printed key to t

**Config**

name: dsh-plugin-subscriptions config: providers: [codex, claude] # subset; default all four streamIdleTimeoutMs: 300000 rateLimit: wait: true # wait out a closed rate-limit window (default) maxWaitMs: 21600000 # ceiling on one wait; 6 h, covers a 5-hour session window models: # override the discovered/built-in catalogs codex: - { id: gpt-5.6-sol, name: GPT-5.6 Sol, contextWindow: 272000, inputMod

## 🔗 链接

- [GitHub 仓库](https://github.com/V1ki/dsh-plugin-subscriptions)
- [完整 README](https://github.com/V1ki/dsh-plugin-subscriptions#readme)
- [返回dsh-plugin-subscriptions所在分类](../plugins.md)
