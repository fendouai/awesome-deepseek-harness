---
title: "dsh-status-bar"
description: "Know what your agent is doing at a glance — 17-segment configurable status bar for DeepSeek Harness: status/model/context/tokens/TPS/cost/jobs. 一眼看清你的 agent 正在做什么：17 段可配置 DSH 会话状态栏。"
keywords: "dsh-status-bar, memory, plugin, coding, context, multi-agent, deepseek harness, dsh"
---
# dsh-status-bar

> ⭐ **5** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Memory & context |
| Stars | ⭐ 5 | Status | ✅ active |
| Author | [Starlight-bananice](https://github.com/Starlight-bananice) | Updated | 2026-08-19 |
| Subcategory | 📦 Context management | Capabilities | coding, context, multi-agent |

## One-liner

> Know what your agent is doing at a glance — 17-segment configurable status bar for DeepSeek Harness: status/model/context/tokens/TPS/cost/jobs. 一眼看清你的 agent 正在做什么：17 段可配置 DSH 会话状态栏。

## About

**The problem:** the native DSH bottom status bar is one long, fixed line — the more it shows, the more it overflows, and on narrow windows parts of it get **truncated**. You cannot see the current model, how full the context window is, how fast tokens are streaming, or what a session has cost — and there is no way to arrange that information the way you work. **Who it is for:** power users and teams running DSH daily — anyone who wants live session telemetry without leaving the composer, and without running a separate monitor. **What it does:** - **Near-native experience, fully yours** — 17 toggleable, reorderable segments: status dot, model, title, workspace, agent preset, turns & steps, model/tool time, TTFT & decode speed, cache-hit rate, tokens, context pressure, live TPS, session tim

## ✨ Key Features

- **Near-native experience, fully yours** — 17 toggleable, reorderable segments: status dot, model, title, workspace, agent preset, turns & steps, model/tool time
- **Live throughput (TPS)** — a host-side projection folds every `assistant/chunk` event, so the speed updates chunk by chunk while streaming; no polling, no exte
- **Cost estimation with a user-maintained model price book** — per-model rates, per-model peak/off-peak schedules, **each message/step priced with the model that
- **Zero-config default** — 13 segments ship enabled; everything else is a checkbox away
- **Useful options** — multi-line wrapping (so nothing gets truncated), live TPS, per-model cost estimation with peak/off-peak pricing, currency choice (CNY / USD
- **Clean takeover** — the plugin's bar shadows the built-in `stats` cell at lower priority: while loaded it renders, when unloaded the built-in line returns unto

## 📦 Install

```bash
dsh plugin --profile web remove @bananiceee/dsh-status-bar
```

## 🚀 Quick Start

```bash
# In Settings → Plugins → Status Bar → Model price book:
   # model "deepseek-chat" → input 2 / cache read 0.5 / cache write 2 / output 8 (CNY per 1M tokens)
   # optional: enable peak/off-peak with DeepSeek's official windows 09:00–12:00, 14:00–18:00
```

## 📚 Learn more

**Screenshots**

The status bar replaces the built-in stats line with near-native live session telemetry (status · model · turns · context · cache · TPS · session time · jobs · queue · errors), managed from a dedicated settings page — including a per-model price book with peak/off-peak pricing:

**Uninstall**

dsh plugin --profile web remove @bananiceee/dsh-status-bar Removal restores the built-in stats line automatically (shadow cell released). **Data left behind:** browser `localStorage` (`dsh.statusBar.v1`) and the host usage file (see [Permissions & data](#permissions--data)) are not deleted — remove them manually if you want a clean slate.

**Quick start**

1. Install (above), restart DSH Web. 2. Start a session — the bar shows status · model · turns · durations · speeds · cache hit · tokens · context · TPS · session time · jobs · queue · errors by default. 3. Open **Settings → Plugins → Status Bar** to toggle/reorder segments, enable wrapping, or reset. 4. Want cost estimates? Add the models you use to the **model price book**: ```sh # In Settings →

**Configuration**

All configuration is client-side, stored in browser `localStorage` under **`dsh.statusBar.v1`**, edited via the settings page or the in-composer gear menu. **Default segment state:** on — status, model, counts, durations, speeds, cache hit, tokens, context, TPS, session time, jobs, queue, errors; off — title, workspace, agent, cost. **Model price book entry** (values added when a model is configur

## 🔗 Links

- [GitHub Repository](https://github.com/Starlight-bananice/dsh-status-bar)
- [Full README](https://github.com/Starlight-bananice/dsh-status-bar#readme)
- [Back to the Plugins list](../plugins.md)
