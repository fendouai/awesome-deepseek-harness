---
title: "DeepSeek-Harness-Vision-Tools"
description: "视觉代理：任意文本模型 + 任意视觉模型即可让 DSH 看图。"
keywords: "DeepSeek-Harness-Vision-Tools, vision, plugin, multimodal, deepseek harness, dsh"
---
# DeepSeek-Harness-Vision-Tools

> ⭐ **12** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 12 | 状态 | ✅ 活跃 |
| 作者 | [tonyd2wild](https://github.com/tonyd2wild) | 更新时间 | 2026-08-13 |
| 子分类 | 👁️ 视觉工具 | 能力 | multimodal, vision |

## 一句话介绍

> 视觉代理：任意文本模型 + 任意视觉模型即可让 DSH 看图。

## 详细介绍

**Give your [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`) eyes: keep your text model as the brain, and let a local vision model do the *seeing*. Any text model, any vision model, on Mac or Windows/PC.** The model driving `dsh` is usually **text-only** (DeepSeek, dense Qwen, Llama, Mistral). Hand it an image and `dsh` refuses before it sends, naming the model. Declaring `input: [text, image]` to force it through is worse: the endpoint then answers `400 "not a multimodal model"` mid-turn, after the message is already durable, and the session retries forever. So there are **two doors an image can come through, and this repo ships a mechanism for each.** They are complementary, not primary-and-alternative. **Why both.** The tool cannot serve a chat attachment: for

## ✨ 核心特性

- **`parameters` is a property map**, not raw JSON Schema. `{ path: { type:
- **`output` must exist**, with a `schema` and a `render`. `defineTool` reads

## 📦 安装

```bash
npm i -g @deepseek-ai/dsh@0.1.0-rc.6
```

## 🚀 快速开始

```bash
SessionCreateError: session create failed: agent-preset-invalid:
agent-presets: preset "<name>" failed to mount:
failed to apply loader entry tool-vision
```

## 📚 更多信息

**Quick start**

git clone https://github.com/tonyd2wild/DeepSeek-Harness-Vision-Tools cd DeepSeek-Harness-Vision-Tools cp .env.example .env # point the endpoints at YOUR hosts ./setup.sh # brings up a local vision server (+ the proxy with RUN_PROXY=1) **Door 1, the proxy** (chat attachments): python3 shim/vision_shim.py --port 8900 \ --upstream http://127.0.0.1:8000 \ --vision-url http://YOUR_FAST_VISION_HOST:808

**Configuration**

**Proxy** (env, or the matching CLI flag which overrides it): **Tool** (plugin config block or env): Full example: **[.env.example](.env.example)**. ---

## 🔗 链接

- [GitHub 仓库](https://github.com/tonyd2wild/DeepSeek-Harness-Vision-Tools)
- [完整 README](https://github.com/tonyd2wild/DeepSeek-Harness-Vision-Tools#readme)
- [返回DeepSeek-Harness-Vision-Tools所在分类](../plugins.md)
