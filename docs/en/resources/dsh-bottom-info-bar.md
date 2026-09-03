---
title: "dsh-bottom-info-bar"
description: "Bottom Info Bar — an information bar plugin for DeepSeek Harness: provider/model, live balance, peak/off-peak pricing with countdown, and real persisted per-session spend in a single line."
keywords: "dsh-bottom-info-bar, channel, integration, coding, deepseek harness, dsh"
---
# dsh-bottom-info-bar

> ⭐ **26** · ✅ active · integration

| | | | |
|---|---|---|---|
| Type | integration | Category | Channels |
| Stars | ⭐ 26 | Status | ✅ active |
| Author | [songoao25](https://github.com/songoao25) | Updated | — |

## One-liner

> Bottom Info Bar — an information bar plugin for DeepSeek Harness: provider/model, live balance, peak/off-peak pricing with countdown, and real persisted per-session spend in a single line.

## About

**English** | [**中文**](README.zh-CN.md) The **best-adapted bottom info bar for [DeepSeek Harness](https://github.com/deepseek-ai)**, and a drop-in replacement for the native stats row under the composer. It shows **live balance** and **subscription quota** (ChatGPT & OpenCode Go) at a glance, alongside provider & model, peak/off-peak pricing, and real spend — **smart and concise**, **conflict-free**, and **native in look and feel**: it auto-detects the billing mode, replaces the native row instead of duplicating it, and matches the model switcher exactly. Install once; it activates automatically on every launch.

## ✨ Key Features

- **Dual-mode billing bar** — Auto-detects whether the active provider is subscription-based (Codex / OpenCode Go) or balance-based. The two modes replace each ot
- **Three-state billing bar** — Auto-detects whether the active provider is **subscription-based** (quota windows: Codex / OpenCode Go / Zhipu / Xiaomi MiMo Token
- **ChatGPT subscription card (pure local)** — When the active provider is **ChatGPT / Codex**, the bar decodes `~/.codex/auth.json` locally and shows the **real 
- **Subscription quota display (OpenCode Go / Zhipu / Xiaomi MiMo Token Plan)** — When the active provider is a subscription service, the bar shows the **subscrip
- **Cloud-billing display (real monthly bill)** — When the active provider is **Together / Fireworks / AWS Bedrock / Cloudflare**, the bar reads the official bill
- **Drop-in replacement** — Replaces the native stats row while keeping its core original information (turns/steps, LLM latency, tool calls, cache hit rate, in/ou
- **Provider & model detection** — Always shows provider and model separately, exactly as in the DSH LLM catalog (for example, `DeepSeek · V4-Flash`). The provide
- **Live balance** — Fetches real balance from DeepSeek's `/user/balance` API, auto-refreshes every 60 s, and keeps the last known snapshot on failure so usage is

## 📦 Install

```bash
git clone https://github.com/songoao25/dsh-bottom-info-bar.git
cd dsh-bottom-info-bar
./install.sh                # installs to the "web" profile; use --profile <name> to override
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add dsh-bottom-info-bar
```

## 📚 Learn more

**Configuration**

- **ChatGPT (Codex)**: install the companion plugin [**dsh-chatgpt-subscription**](https://github.com/songoao25) (separate repo) and bind your ChatGPT account once — it maintains the token in `~/.codex/auth.json` (mode `0600`) and registers the ChatGPT models. This bar only **reads** that token to fetch quota (`chatgpt.com/backend-api/wham/usage`); it never refreshes, writes back, or injects crede

## 🔗 Links

- [GitHub Repository](https://github.com/songoao25/dsh-bottom-info-bar)
- [Full README](https://github.com/songoao25/dsh-bottom-info-bar#readme)
- [Back to the MCP & Integrations list](../integrations.md)
