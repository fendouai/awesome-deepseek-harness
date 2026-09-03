---
title: "deepseek-harness-control-center"
description: "DeepSeek Harness account monitoring, usage accounting, completion alerts, official recharge, flexible layout, and agent-assisted session controls. / 账户监控、提醒、充值与会话控制中心"
keywords: "deepseek-harness-control-center, vision, plugin, coding, multi-agent, deepseek harness, dsh"
---
# deepseek-harness-control-center

> ⭐ **61** · ✅ active · plugin · ⬆️ +4 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 61 | Status | ✅ active |
| Author | [feibi-mochi](https://github.com/feibi-mochi) | Updated | 2026-08-20 |
| Subcategory | 👁️ Vision tools | Capabilities | coding, multi-agent |

## One-liner

> DeepSeek Harness account monitoring, usage accounting, completion alerts, official recharge, flexible layout, and agent-assisted session controls. / 账户监控、提醒、充值与会话控制中心

## About

**DeepSeek Harness monitoring, alerts, recharge, and session control center.** `Balance ¥5.89 · Session ¥0.72 · Official 18.8M | Third-party 800K · ↗ Recharge` [English](./README.md) · [简体中文](https://github.com/feibi-mochi/deepseek-harness-control-center/blob/main/docs/i18n/README.zh-CN.md) · [Install](#install) · [Compatibility](#browser-desktop-and-os-compatibility) · [Changelog](./CHANGELOG.md)

## ✨ Key Features

- **Official DeepSeek** — live balance (60s global refresh with fast boot retries), an estimated current-session cost (not an official bill) locked to the price a
- **Vision model accounting** — `deepseek-v4-flash-vision-exp` is priced like V4 Flash; image tokens reported by the Harness are included with text tokens.
- **v4 peak/off-peak ring clock** — a resident 24-hour sidebar footer widget for `v4-flash`, `v4-pro`, and `v4-flash-vision-exp`. Weekday peak windows are 09:00–1
- **Official pricing sync** — periodically checks the official DeepSeek pricing page and applies only a fully validated table. Network failures retain the last va
- **Z.ai Coding Plan quotas** — a generic official-plan adapter monitors configured Global and China plans without exposing credentials. It separates the 5-hour m
- **Provider-aware composer surfaces** — the chip and sidebar clock follow the session's selected provider/model. Z.ai replaces DeepSeek balance, recharge, and pe
- **365-day local usage ledger** — Wallet settings keeps the heatmap visible, while compact wallet panels keep it collapsible. Stable request identities are dedup
- **Third-party total** — current-session tokens (input / cache read / output) remain available with zero configuration.

## 📦 Install

```bash
dsh plugin --profile web add deepseek-harness-wallet
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add github:feibi-mochi/deepseek-harness-control-center
```

## 📚 Learn more

**Install**

From npm (published stable v0.3.8): dsh plugin --profile web add deepseek-harness-wallet or from GitHub `main`: dsh plugin --profile web add github:feibi-mochi/deepseek-harness-control-center Restart `dsh web`, then hard-refresh the page.

**Quick use**

1. Click the wallet or peak/off-peak card to open its control panel; open the Harness settings card for health and compatibility checks. 2. The peak card supports horizontal/vertical layout and 100%–120% scaling. The wallet chip uses a separate scale: 100%–105% in the composer and up to 125% when docked or floating. 3. Turn the official recharge button off when you need a smaller card; official an

## 🔗 Links

- [GitHub Repository](https://github.com/feibi-mochi/deepseek-harness-control-center)
- [Full README](https://github.com/feibi-mochi/deepseek-harness-control-center#readme)
- [Back to the Plugins list](../plugins.md)
