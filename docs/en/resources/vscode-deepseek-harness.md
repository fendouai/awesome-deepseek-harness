---
title: "vscode-deepseek-harness"
description: "Unofficial: drive your own dsh as a native VS Code chat agent."
keywords: "vscode-deepseek-harness, ide, integration, coding, deepseek harness, dsh"
---
# vscode-deepseek-harness

> ⭐ **3** · ✅ active · integration · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | integration | Category | IDE & editors |
| Stars | ⭐ 3 | Status | ✅ active |
| Author | [kalynnka](https://github.com/kalynnka) | Updated | 2026-08-20 |

## One-liner

> Unofficial: drive your own dsh as a native VS Code chat agent.

## About

[中文文档](readme.zh.md) · [English](README.md) An unofficial VS Code extension that registers [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) as a **chat session target** in VS Code's native agent sessions view — the same surface that hosts Claude Code and Codex — rather than shipping another webview chat panel. Status: **M0–M5 implemented.** A VSIX builds, installs and activates with its proposed APIs granted. - [docs/plans/0001-vscode-chat-session-provider.md](docs/plans/0001-vscode-chat-session-provider.md) — architecture decision, API mapping, and milestones. - [docs/gaps.md](docs/gaps.md) — what the chat UI wanted, what `/api` could not give it, and what was done instead.

## ✨ Key Features

- [docs/plans/0001-vscode-chat-session-provider.md](docs/plans/0001-vscode-chat-session-provider.md) — architecture decision, API mapping, and milestones.
- [docs/gaps.md](docs/gaps.md) — what the chat UI wanted, what `/api` could not give it, and what was done instead.

## 📦 Install

```bash
npm install
npm run build
npm run package        # → deepseek-harness-sessions-<version>.vsix
```

## 🚀 Quick Start

```bash
code --install-extension deepseek-harness-sessions-*.vsix
```

## 📚 Learn more

**Install**

This extension is **not on the Marketplace and cannot be** — an extension that declares `enabledApiProposals` is refused at publish time. Installing the VSIX by hand is the only route, and the proposal opt-in below is not optional: without it the contribution is skipped in silence and nothing appears anywhere. **1. Get the VSIX.** Either download it from [Releases](https://github.com/kalynnka/vsco

**Settings**

The bind host is deliberately not configurable: the dsh web server has no TLS and no auth, so a harness this extension starts is always on loopback, as a child it owns and kills on exit. The port is `deepseekHarness.url`'s, fixed rather than ephemeral — an ephemeral port would hide the harness from the next window, which would then start a second one, which is the exact hazard [gaps §23](docs/gaps

## 🔗 Links

- [GitHub Repository](https://github.com/kalynnka/vscode-deepseek-harness)
- [Full README](https://github.com/kalynnka/vscode-deepseek-harness#readme)
- [Back to the MCP & Integrations list](../integrations.md)
