---
title: "dsh-notifier"
description: "Unified notification and remote-control plugin for DeepSeek Harness (DSH): one zero-dependency notify() API across 27 channels, with phone-friendly approvals/questions, six inbound control channels, and a loopback web console."
keywords: "dsh-notifier, search, plugin, coding, deepseek harness, dsh"
---
# dsh-notifier

> ⭐ **79** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 79 | Status | ✅ active |
| Author | [THEWOLFWALKER](https://github.com/THEWOLFWALKER) | Updated | — |
| Subcategory | 🌐 Web search | Capabilities | coding |

## One-liner

> Unified notification and remote-control plugin for DeepSeek Harness (DSH): one zero-dependency notify() API across 27 channels, with phone-friendly approvals/questions, six inbound control channels, and a loopback web console.

## About

**English** · [**简体中文**](README.zh-CN.md) Package metadata: `dsh-notifier@0.9.0` · 1352 automated contract tests (1351 pass + 1 skip) · MIT licensed. Bring your [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) agent to the places you already use. dsh-notifier puts one minimal `notify()` API in front of 27 channels, then adds phone-friendly approvals, questions, session controls, and a calm local console — with no second runtime to deploy. [Get started](docs/guide.md) · [Upgrade guide](docs/upgrade-guide.en.md) · [Plugin integration](PLUGINS.md) Your agent and the harness itself both push through it: session events (`turn/end` · `approval/asked` · `agent/error`) auto-notify, the model calls a `notify` tool directly, and six inbound channels bring approvals and conversatio

## 📦 Install

```bash
dsh plugin add dsh-notifier --profile <profile-name>
```

## 🚀 Quick Start

```bash
insert:
  - id: dsh-notifier
    name: dsh-notifier
    config:
      channels:
        - type: telegram
          botToken: "123456:ABC-DEF..."
          chatId: "987654321"
        - type: dingtalk
          webhook: "https://oapi.dingtalk.com/robot/send?access_token=..."
          secret: "SEC..."
        - type: bark
          key: "your-device-key"
```

## 📚 Learn more

**Screenshots**

The web admin console (`admin.enabled: true`, loopback only, mobile-friendly since v0.5) — all six pages (demo data). The browser opens in personal mode: first configure, pair, test, then use; bindings and sessions stay behind an explicit advanced-settings toggle. Open the exact loopback URL printed by the `Web 管理台已就绪` startup line instead of guessing port `8104`:

**Quick start**

dsh plugin add dsh-notifier --profile <profile-name> > `--profile` is required (DSH 0.1.0-rc.6+): plugin installs target a named profile — use the one you run (e.g. `web`). Add channels to your profile patch (`cordis.patch.yml`): insert: - id: dsh-notifier name: dsh-notifier config: channels: - type: telegram botToken: "123456:ABC-DEF..." chatId: "987654321" - type: dingtalk webhook: "https://oapi

**Configuration**

All channels live under `config.channels`. Key example: insert: - id: dsh-notifier config: channels: - type: telegram botToken: "123456:ABC-DEF..." chatId: "987654321" - type: feishu webhook: "https://open.feishu.cn/open-apis/bot/v2/hook/..." - type: wxpusher appToken: "AT_..." uids: ["UID_..."] - type: serverchan sct: "SCT..." Optional blocks each opt in under their own key: v0.5 status line defa

**Architecture**

src/ adapters/ 27 channel adapters (resolve(cfg) + send(msg)) + declarative spec engine config.mjs channel registry + config schema — single source of truth for the matrix index.mjs plugin assembly: patch, tools, event listeners, admin wiring event-listener.mjs auto-push line (debounce, dedup, level routing) + v0.5 status wiring status/ v0.5 turn tracker (heartbeat / stall detection, pure logic) a

## 🔗 Links

- [GitHub Repository](https://github.com/THEWOLFWALKER/dsh-notifier)
- [Full README](https://github.com/THEWOLFWALKER/dsh-notifier#readme)
- [Back to the Plugins list](../plugins.md)
