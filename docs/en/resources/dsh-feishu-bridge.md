---
title: "dsh-feishu-bridge"
description: "Fail-closed Feishu (Lark) channel bridge for DeepSeek Harness (dsh) — chat with a bot, get agent turns back. Opt-in human-in-the-loop bash approval (Allow/Deny cards, fail-closed timeout), one-message /pair onboarding, webhook signature/timestamp/replay verification, daily latest-SDK canary. Community plugin, not DeepSeek-official."
keywords: "dsh-feishu-bridge, channel, integration, coding, multi-agent, deepseek harness, dsh"
---
# dsh-feishu-bridge

> ⭐ **5** · ✅ active · integration

| | | | |
|---|---|---|---|
| Type | integration | Category | Channels |
| Stars | ⭐ 5 | Status | ✅ active |
| Author | [wz-heng](https://github.com/wz-heng) | Updated | — |

## One-liner

> Fail-closed Feishu (Lark) channel bridge for DeepSeek Harness (dsh) — chat with a bot, get agent turns back. Opt-in human-in-the-loop bash approval (Allow/Deny cards, fail-closed timeout), one-message /pair onboarding, webhook signature/timestamp/replay verification, daily latest-SDK canary. Community plugin, not DeepSeek-official.

## About

The SDK canary runs daily against the *latest* `deepseek-harness-sdk` and `lark-channel-sdk` releases (not the pinned versions this repo ships), so a breaking upstream change gets caught within a day instead of silently bit-rotting. A Feishu (Lark) channel bridge for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`): message a Feishu bot, it runs a `dsh` agent turn, the reply comes back to the chat. **This is an independent community project. It is not built, maintained, or endorsed by DeepSeek.** It drives `dsh` entirely through its public Python SDK (`deepseek-harness-sdk`) — a subprocess boundary, no forked/patched harness code.

## ✨ Key Features

- A production-grade Feishu bot bridge: fail-closed allowlist, one-time card nonces, per-chat verbosity, sticky sessions, both `ws` and `webhook` transports.
- The thin adapter that talks to `deepseek-harness-sdk` lives in one file, `src/dsh_feishu_bridge/dsh_adapter.py`, and the SDK version is pinned exactly — the har

## 📦 Install

```bash
git clone https://github.com/wz-heng/dsh-feishu-bridge.git
cd dsh-feishu-bridge
python3.12 -m venv .venv
. .venv/bin/activate
pip install -e ".[dev]"
```

## 🚀 Quick Start

```bash
python -m dsh_feishu_bridge
# or: dsh-feishu-bridge
```

## 📚 Learn more

**Quickstart (5 minutes)**

git clone https://github.com/wz-heng/dsh-feishu-bridge.git cd dsh-feishu-bridge python3.12 -m venv .venv . .venv/bin/activate pip install -e ".[dev]" Set your credentials as environment variables — never in a committed file: export DEEPSEEK_API_KEY=sk-your-key-here

**Install as a dsh plugin**

Instead of running the standalone process above, `dsh plugin add` can install this repo into a `dsh` profile: the plugin is a thin Node/cordis shell (`package.json`, `cordis.patch.yml`, `lib/`) that spawns and supervises the same unmodified Python process — it does not reimplement or patch any bridge logic. **Two steps, in order — the plugin never installs Python dependencies for you:** 1. **Insta

**Configuration reference**

Everything is an environment variable. An optional YAML file (path via `DSH_FEISHU_BRIDGE_CONFIG`, or `--config`) can supply the non-secret knobs (allowlists, model, provider) — see `examples/config.example.yaml`. Env vars always win when both are set, and credentials are never read from the YAML file on purpose.

## 🔗 Links

- [GitHub Repository](https://github.com/wz-heng/dsh-feishu-bridge)
- [Full README](https://github.com/wz-heng/dsh-feishu-bridge#readme)
- [Back to the MCP & Integrations list](../integrations.md)
