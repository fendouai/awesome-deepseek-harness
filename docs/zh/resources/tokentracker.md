---
title: "TokenTracker"
description: "本地优先的 AI Token 用量与费用追踪器，支持 31 款编码工具（含 Claude Code、Codex、Cursor、Gemini 与 DeepSeek Harness）。"
keywords: "TokenTracker, developer, plugin, observability, deepseek harness, dsh"
---
# TokenTracker

> ⭐ **1,395** · ✅ 活跃 · 插件 · 近期 ⬆️ +15

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 1,395 | 状态 | ✅ 活跃 |
| 作者 | [xiufengsun](https://github.com/xiufengsun) | 更新时间 | 2026-08-21 |
| 子分类 | 💰 费用与统计 | 能力 | observability |

## 一句话介绍

> 本地优先的 AI Token 用量与费用追踪器，支持 31 款编码工具（含 Claude Code、Codex、Cursor、Gemini 与 DeepSeek Harness）。

## 详细介绍

**English** · [简体中文](./README.zh-CN.md) · [日本語](./README.ja.md) · [한국어](./README.ko.md) · [Deutsch](./README.de.md)

## ✨ 核心特性

- 🔌 **36 AI tools out of the box** — Claude Code, Codex CLI, Cursor, Gemini CLI, Antigravity, Kiro, OpenCode, OpenClaw, Every Code, Hermes Agent, GitHub Copilot, 
- 🏠 **100% local** — Token data never leaves your machine. No account, no API keys.
- 🚀 **Zero config** — Hooks auto-install on first run. From zero to dashboard in 30 seconds.
- 📊 **Beautiful dashboard** — Usage trends, cost breakdowns by model, GitHub-style activity heatmap, project attribution
- 🖥️ **Native desktop app** — macOS menu bar (+ widgets) and Windows system tray, each with an embedded server and the dashboard in a native webview
- 🐾 **Desktop pet** — A pixel companion powered by real coding activity: it works when you work, celebrates streaks, and sleeps when you rest
- 🎨 **4 desktop widgets** — Pin Usage / Activity Heatmap / Top Models / Usage Limits to your desktop
- 🏆 **15 achievement tracks** — Turn daily usage, streaks, tools, models, and milestones into collectible badges worth sharing

## 📦 安装

```bash
npm i -g tokentracker-cli

tokentracker              # Open the dashboard
tokentracker sync         # Manual sync
tokentracker status       # Check hook status
tokentracker status --json     # Machine-readable summary (pipe to jq, ingest from AI agents)
tokentracker status --light    # Plain ASCII table (CI / SSH, no spinner)
tokentracker doctor       # Health check
```

## 🚀 快速开始

```bash
# macOS menu bar app (DMG)
brew install --cask xiufengsun/tokentracker/tokentracker

# CLI only
brew install xiufengsun/tokentracker/tokentracker
```

## 📚 更多信息

**Track every AI token — then bring your usage to life**

An accurate, local-first token usage and cost dashboard for **36 AI coding tools** — plus a desktop pet, **4 native widgets**, and **15 achievement tracks**. No cloud account, no API keys, no setup.           <br/> <strong>📊 See the token dashboard in action</strong> <br/><br/> <video src="https://github.com/user-attachments/assets/3275979d-bbed-4639-83e2-8b7d83bed6af" controls muted playsinline p

**⚡ Quick Start**

> **Requirements**: Node.js **20+** (CLI runs on macOS / Linux / Windows; native desktop app ships for macOS (menu bar), Windows (system tray) and Linux (AppImage, tray). Cursor token reading uses the system `sqlite3` CLI when available and falls back to `node:sqlite` on supported Node releases). npx tokentracker-cli That's it. First run installs hooks, syncs your data, and opens the dashboard at 

**🆚 Why TokenTracker? <a id="ccusage-alternative"></a>**

> **Looking for a ccusage alternative with a GUI?** TokenTracker covers 36 tools (not just Claude Code), adds native macOS and Windows apps + desktop widgets, and de-duplicates token records correctly across providers — so your numbers match the providers' own billing. <sub>¹ `reqId`-based deduplication over-counts providers that omit a request ID (DeepSeek / Kimi / MiniMax / Claude sub-agents) by

## 🔗 链接

- [GitHub 仓库](https://github.com/xiufengsun/TokenTracker)
- [完整 README](https://github.com/xiufengsun/TokenTracker#readme)
- [返回TokenTracker所在分类](../plugins.md)
