---
title: "deepseek-harness-SupportVisionModel"
description: "基于 deepseek-harness 二次开发：支持单独配置视觉模型读图。"
keywords: "deepseek-harness-SupportVisionModel, vision, plugin, multimodal, deepseek harness, dsh"
---
# deepseek-harness-SupportVisionModel

> ⭐ **8** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 8 | 状态 | ✅ 活跃 |
| 作者 | [TryDing-T](https://github.com/TryDing-T) | 更新时间 | 2026-08-14 |
| 子分类 | 👁️ 视觉工具 | 能力 | multimodal, vision |

## 一句话介绍

> 基于 deepseek-harness 二次开发：支持单独配置视觉模型读图。

## 详细介绍

DeepSeek Harness SupportVisionModel is a community fork of [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness). It keeps the upstream plugin architecture and adds a unified image-routing path for image-capable and text-only main models. This repository is maintained independently at [TryDing-T/deepseek-harness-SupportVisionModel](https://github.com/TryDing-T/deepseek-harness-SupportVisionModel). It is not an official DeepSeek AI distribution.

## ✨ 核心特性

- Model catalog entries can explicitly declare text-and-image input support.
- A dedicated Vision settings page selects the auxiliary provider and model, maximum attempts, per-attempt timeout, and output-token limit.
- Image-capable main models receive the original image attachments.
- Text-only or unknown-capability main models receive a validated description from the configured vision model.
- Missing or exhausted vision routes degrade to explicit attachment references instead of rejecting a successful user or tool action.
- Web uploads, top-level tool image results, ordinary `read_image`, and nested Code Mode `read_image` share the same router.

## 📦 安装

```bash
git clone https://github.com/TryDing-T/deepseek-harness-SupportVisionModel.git
cd deepseek-harness-SupportVisionModel
pnpm install
pnpm run build
pnpm dsh web
```

## 🚀 快速开始

```bash
git fetch upstream
git diff main..upstream/master
```

## 📚 更多信息

**Configure the vision route**

The auxiliary model must explicitly declare both text and image input support. One attempt sends the complete ordered image batch without tools.

**Configure image routing**

1. Open **Settings → Models**, configure the provider, model, and API key, then enable **Supports images** only for a real multimodal endpoint. 2. Open **Settings → Vision**, select that provider and model, and set the attempt, timeout, and output-token limits. 3. Select any main model. Image-capable models receive images directly; text-only models use the configured vision route. API keys belong 

## 🔗 链接

- [GitHub 仓库](https://github.com/TryDing-T/deepseek-harness-SupportVisionModel)
- [完整 README](https://github.com/TryDing-T/deepseek-harness-SupportVisionModel#readme)
- [返回deepseek-harness-SupportVisionModel所在分类](../plugins.md)
