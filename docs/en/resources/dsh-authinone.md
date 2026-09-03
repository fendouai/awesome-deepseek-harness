---
title: "dsh-authinone"
description: "Self-contained DeepSeek Harness (DSH) plugin for Provider/Auth login, model switching, image fallback, token/cost analytics, and same-port Web restart. Useful? A star helps."
keywords: "dsh-authinone, search, plugin, coding, multimodal, deepseek harness, dsh"
---
# dsh-authinone

> ⭐ **105** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 105 | Status | ✅ active |
| Author | [Stormycry-cryp](https://github.com/Stormycry-cryp) | Updated | — |
| Subcategory | 🌐 Web search | Capabilities | coding, multimodal |

## One-liner

> Self-contained DeepSeek Harness (DSH) plugin for Provider/Auth login, model switching, image fallback, token/cost analytics, and same-port Web restart. Useful? A star helps.

## About

dsh-AuthInOne is a DeepSeek Harness plugin for Provider login, API and custom OpenAI-compatible Provider setup, model switching, optional vision fallback for text-only models, token usage analytics, and cost tracking inside DSH's native **Models** and **Usage** settings. OpenAI Codex uses browser OAuth with state, S256 PKCE, and a loopback callback. Kimi Code opens the Provider's complete authorization link backed by an RFC 8628 device flow; the link carries the short code, so the user normally only signs in and confirms. xAI Grok, Anthropic, GitHub Copilot, Command Code, Cursor, Google Antigravity, and Kiro are explicitly marked **Experimental compatibility**. Installed-Host validation reached each Provider's authorization boundary and stopped before user consent; mock/fixture tests cover

## ✨ Key Features

- It is not an official DeepSeek, OpenAI, or model-provider product and does not imply endorsement.
- It does not claim every compatibility login is a stable or Provider-endorsed integration. Seven entries are explicitly Experimental, and Qwen account OAuth is d
- It does not replace Models business behavior, the attachment pipeline, session log, or model selector; on exact DSH `47f9438` it replaces the two Settings owner
- It does not infer that a model supports or lacks vision when its adapter publishes no modality metadata.
- It does not extend image understanding to audio, video, PDF, or image generation.
- It does not fabricate missing Token buckets, prices, currency conversion, tool ownership, or a successful login.

## 📦 Install

```bash
pnpm install --frozen-lockfile
pnpm typecheck
pnpm test
DSH_SOURCE_ROOT=/path/to/deepseek-harness pnpm verify:boundaries
pnpm build
pnpm pack --dry-run
```

## 🚀 Quick Start

```bash
pnpm dlx github:Stormycry-cryp/dsh-AuthInOne#v0.2.0-alpha.4 install --profile web
```

## 📚 Learn more

**30-second install, upgrade, and remove**

Install or upgrade the immutable tag with the package-owned bootstrap: pnpm dlx github:Stormycry-cryp/dsh-AuthInOne#v0.2.0-alpha.4 install --profile web The bootstrap discovers the single listener at `http://127.0.0.1:3080/`, verifies that it is a standard DSH Host, checks the exact supported DSH owner artifacts, invokes the official DSH plugin add command, and schedules a detached same-port repla

**Usage filters and accounting**

The built-in `deepseek-usd-2026-08-14` catalog contains only DeepSeek-V4-Flash and DeepSeek-V4-Pro USD rows verified from the [official DeepSeek pricing page](https://api-docs.deepseek.com/quick_start/pricing) on 2026-08-14. Every row carries a source URL, verification/update date, effective date, currency, and explicit token-bucket rates. Missing prices remain unknown or partial, never a forged z

## 🔗 Links

- [GitHub Repository](https://github.com/Stormycry-cryp/dsh-AuthInOne)
- [Full README](https://github.com/Stormycry-cryp/dsh-AuthInOne#readme)
- [Back to the Plugins list](../plugins.md)
