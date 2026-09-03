---
title: "deepseek-harness-SupportVisionModel"
description: "Secondary development of deepseek-harness supporting a separately configured vision model for reading images."
keywords: "deepseek-harness-SupportVisionModel, vision, plugin, multimodal, deepseek harness, dsh"
---
# deepseek-harness-SupportVisionModel

> ⭐ **8** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 8 | Status | ✅ active |
| Author | [TryDing-T](https://github.com/TryDing-T) | Updated | 2026-08-14 |
| Subcategory | 👁️ Vision tools | Capabilities | multimodal, vision |

## One-liner

> Secondary development of deepseek-harness supporting a separately configured vision model for reading images.

## About

DeepSeek Harness SupportVisionModel is a community fork of [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness). It keeps the upstream plugin architecture and adds a unified image-routing path for image-capable and text-only main models. This repository is maintained independently at [TryDing-T/deepseek-harness-SupportVisionModel](https://github.com/TryDing-T/deepseek-harness-SupportVisionModel). It is not an official DeepSeek AI distribution.

## ✨ Key Features

- Model catalog entries can explicitly declare text-and-image input support.
- A dedicated Vision settings page selects the auxiliary provider and model, maximum attempts, per-attempt timeout, and output-token limit.
- Image-capable main models receive the original image attachments.
- Text-only or unknown-capability main models receive a validated description from the configured vision model.
- Missing or exhausted vision routes degrade to explicit attachment references instead of rejecting a successful user or tool action.
- Web uploads, top-level tool image results, ordinary `read_image`, and nested Code Mode `read_image` share the same router.

## 📦 Install

```bash
git clone https://github.com/TryDing-T/deepseek-harness-SupportVisionModel.git
cd deepseek-harness-SupportVisionModel
pnpm install
pnpm run build
pnpm dsh web
```

## 🚀 Quick Start

```bash
git fetch upstream
git diff main..upstream/master
```

## 📚 Learn more

**Configure the vision route**

The auxiliary model must explicitly declare both text and image input support. One attempt sends the complete ordered image batch without tools.

**Configure image routing**

1. Open **Settings → Models**, configure the provider, model, and API key, then enable **Supports images** only for a real multimodal endpoint. 2. Open **Settings → Vision**, select that provider and model, and set the attempt, timeout, and output-token limits. 3. Select any main model. Image-capable models receive images directly; text-only models use the configured vision route. API keys belong 

## 🔗 Links

- [GitHub Repository](https://github.com/TryDing-T/deepseek-harness-SupportVisionModel)
- [Full README](https://github.com/TryDing-T/deepseek-harness-SupportVisionModel#readme)
- [Back to the Plugins list](../plugins.md)
