---
title: "dsh-codex-connect"
description: "ChatGPT OAuth and Codex models for DeepSeek Harness."
keywords: "dsh-codex-connect, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-codex-connect

> ⭐ **34** · ✅ active · plugin · ⬆️ +5 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 34 | Status | ✅ active |
| Author | [franksong2702](https://github.com/franksong2702) | Updated | 2026-08-21 |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> ChatGPT OAuth and Codex models for DeepSeek Harness.

## About

Connect your ChatGPT subscription to DeepSeek Harness with OAuth, optional GPT Image generation, user-controlled defaults, Harness-native approvals, diagnostics, and reliable session recovery. `dsh-codex-connect` adds the `openai-codex` model catalog and a separate ChatGPT OAuth login. Models run through Harness's normal LLM service, so streaming, tool calls, reasoning replay, compaction, filesystem controls, permission gates, and approval prompts remain Harness-owned. It does not turn a ChatGPT subscription into an OpenAI Platform API credential. When an eligible GPT Codex model is selected, the Composer also shows a conversation-scoped Fast Mode toggle and compact server-reported quota bars. Installation is additive. The bundle does not replace the current default model or search route. 

## ✨ Key Features

- id: llm-openai-codex

## 📦 Install

```bash
dsh plugin --profile web add dsh-codex-connect@0.1.0-alpha.4.25
```

## 🚀 Quick Start

```bash
dsh plugin --profile web update dsh-codex-connect
```

## 📚 Learn more

**Quick start (about five minutes)**

This quick start targets DSH `0.1.2-alpha.5` with Codex Connect Alpha 4.25. Check `dsh --version` first. For DSH `0.1.2-alpha.2`, `0.1.1-rc.2`, or `0.1.0-rc.7`, select the matching plugin version in [INSTALL.md](INSTALL.md). This guide uses the `web` profile; replace `web` with the name of the Harness profile you already use. From a DeepSeek Harness source checkout, prefix the commands with `pnpm`

**1. Install the plugin into one profile**

dsh plugin --profile web add dsh-codex-connect@0.1.0-alpha.4.25 Expected result: the package is added to that profile. This does not change the profile's default model or global search route. Use the exact version above to keep the verified DSH and plugin pair reproducible. `alpha` is a moving npm tag, not a compatibility guarantee.

**Usage limits in Plugin configuration**

After sign-in, the Codex Connect settings card can show several server-reported windows. They are separate buckets, not three views of one number: Each bar shows the remaining percentage and its local reset time. OpenAI controls the returned windows, eligibility, and reset values; Codex Connect does not remove a returned window based on the plan name or invent a missing one.

## 🔗 Links

- [GitHub Repository](https://github.com/franksong2702/dsh-codex-connect)
- [Full README](https://github.com/franksong2702/dsh-codex-connect#readme)
- [Back to the Plugins list](../plugins.md)
