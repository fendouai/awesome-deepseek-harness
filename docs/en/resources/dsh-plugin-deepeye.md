---
title: "dsh-plugin-deepeye"
description: "DeepEye vision plugin for DeepSeek Harness (DSH): image description, OCR, VQA, UI layout, and clipboard analysis."
keywords: "dsh-plugin-deepeye, vision, plugin, coding, multimodal, ui, deepseek harness, dsh"
---
# dsh-plugin-deepeye

> ⭐ **4** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 4 | Status | ✅ active |
| Author | [Favio8](https://github.com/Favio8) | Updated | 2026-08-17 |
| Subcategory | 👁️ Vision tools | Capabilities | coding, multimodal, ui |

## One-liner

> DeepEye vision plugin for DeepSeek Harness (DSH): image description, OCR, VQA, UI layout, and clipboard analysis.

## About

为 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 提供视觉能力的原生 Cordis 插件。 让纯文本模型获得"眼睛"：图片描述、OCR 文字提取、视觉问答、UI 布局分析、剪贴板截图分析，以及**粘贴图片自动翻译**（在纯文本模型会话里直接粘贴图片也能发）。

## ✨ Key Features

- **原生集成** — 直接注册到 `ctx.tools`，无 MCP 中间层开销
- **多后端** — 支持 OpenAI (GPT-4o)、Google Gemini、自定义 OpenAI-compatible 端点
- **智能预处理** — 自动缩放过大图片、转换 JPEG 以节省 token
- **结果缓存** — LRU 缓存减少重复 API 调用（含 TTL，键覆盖后端/模型，切换后端不会误命中）
- **友好错误处理** — 鉴权失败/限流/超时给出可执行的修复建议，不再回显原始 API 报错
- **非阻塞剪贴板读取** — `vision_clipboard` 异步读取系统剪贴板（不卡事件循环、可取消），且能区分「剪贴板是文本」「没有内容」并给出引导
- **System Prompt** — 自动注入提示段落，让模型知道何时使用视觉能力
- **粘贴图片兼容** — 纯文本模型（如 DeepSeek）会话中直接粘贴图片，自动翻译成文字后交给模型（见下文 pasteCompat）

## 📦 Install

```bash
# 发布后（npm 安装）
dsh plugin --profile web add dsh-plugin-deepeye

# 本地开发时（从插件源码目录的上一级执行）
dsh plugin --profile web add ./dsh-plugin-deepeye
```

## 🚀 Quick Start

```bash
dsh --profile web --dump-config   # 确认出现 dsh-plugin-deepeye 层
dsh web                           # web 是 --profile web 的别名
```

## 📚 Learn more

**使用 OpenAI**

name: 'dsh-plugin-deepeye' config: provider: openai # apiKey: !!js process.env.OPENAI_API_KEY # 可省略，自动回退 model: gpt-4o # 可选，默认 gpt-4o # baseUrl: '' # 可选，代理或 Azure 端点

**使用 Gemini**

name: 'dsh-plugin-deepeye' config: provider: gemini model: gemini-2.0-flash # 可选，默认 gemini-2.0-flash

**使用智谱 GLM-4V（免费）**

智谱的 `glm-4v-flash` 是免费视觉模型，走 OpenAI-compatible 端点，对应 `provider: custom`。 把 [`examples/zhipu-glm4v.cordis.patch.yml`](examples/zhipu-glm4v.cordis.patch.yml) 的内容合并到 profile 的用户 patch 层（`%USERPROFILE%\.dsh\profiles\web\cordis.patch.yml`，Linux/macOS 为 `~/.dsh/profiles/web/cordis.patch.yml`）： config: provider: custom baseUrl: https://open.bigmodel.cn/api/paas/v4 model: glm-4v-flash maxTokens: 1024 API 

**使用自定义端点**

适用于 vLLM、Ollama、LM Studio 等 OpenAI-compatible 服务： name: 'dsh-plugin-deepeye' config: provider: custom baseUrl: http://localhost:8080/v1 # 必填：端点地址 model: qwen-vl-plus # 必填：模型名 # apiKey: !!js process.env.DEEPEYE_API_KEY # 可省略

## 🔗 Links

- [GitHub Repository](https://github.com/Favio8/dsh-plugin-deepeye)
- [Full README](https://github.com/Favio8/dsh-plugin-deepeye#readme)
- [Back to the Plugins list](../plugins.md)
