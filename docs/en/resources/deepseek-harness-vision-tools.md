---
title: "DeepSeek-Harness-Vision-Tools"
description: "Vision proxy for chat: give DSH eyes with any text model plus any vision model."
keywords: "DeepSeek-Harness-Vision-Tools, vision, plugin, multimodal, deepseek harness, dsh"
---
# DeepSeek-Harness-Vision-Tools

> ⭐ **12** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 12 | Status | ✅ active |
| Author | [tonyd2wild](https://github.com/tonyd2wild) | Updated | 2026-08-13 |
| Subcategory | 👁️ Vision tools | Capabilities | multimodal, vision |

## One-liner

> Vision proxy for chat: give DSH eyes with any text model plus any vision model.

## About

**Give your [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`) eyes: keep your text model as the brain, and let a local vision model do the *seeing*. Any text model, any vision model, on Mac or Windows/PC.** The model driving `dsh` is usually **text-only** (DeepSeek, dense Qwen, Llama, Mistral). Hand it an image and `dsh` refuses before it sends, naming the model. Declaring `input: [text, image]` to force it through is worse: the endpoint then answers `400 "not a multimodal model"` mid-turn, after the message is already durable, and the session retries forever. So there are **two doors an image can come through, and this repo ships a mechanism for each.** They are complementary, not primary-and-alternative. **Why both.** The tool cannot serve a chat attachment: for

## ✨ Key Features

- **`parameters` is a property map**, not raw JSON Schema. `{ path: { type:
- **`output` must exist**, with a `schema` and a `render`. `defineTool` reads

## 📦 Install

```bash
npm i -g @deepseek-ai/dsh@0.1.0-rc.6
```

## 🚀 Quick Start

```bash
SessionCreateError: session create failed: agent-preset-invalid:
agent-presets: preset "<name>" failed to mount:
failed to apply loader entry tool-vision
```

## 📚 Learn more

**Quick start**

git clone https://github.com/tonyd2wild/DeepSeek-Harness-Vision-Tools cd DeepSeek-Harness-Vision-Tools cp .env.example .env # point the endpoints at YOUR hosts ./setup.sh # brings up a local vision server (+ the proxy with RUN_PROXY=1) **Door 1, the proxy** (chat attachments): python3 shim/vision_shim.py --port 8900 \ --upstream http://127.0.0.1:8000 \ --vision-url http://YOUR_FAST_VISION_HOST:808

**Configuration**

**Proxy** (env, or the matching CLI flag which overrides it): **Tool** (plugin config block or env): Full example: **[.env.example](.env.example)**. ---

## 🔗 Links

- [GitHub Repository](https://github.com/tonyd2wild/DeepSeek-Harness-Vision-Tools)
- [Full README](https://github.com/tonyd2wild/DeepSeek-Harness-Vision-Tools#readme)
- [Back to the Plugins list](../plugins.md)
