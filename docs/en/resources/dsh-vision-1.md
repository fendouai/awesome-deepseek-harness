---
title: "dsh-vision (william-jin-cmu)"
description: "Vision bridge: view_image tool over any OpenAI-compatible VLM, defaulting to Zhipu's free tier."
keywords: "dsh-vision (william-jin-cmu), vision, plugin, multimodal, deepseek harness, dsh"
---
# dsh-vision (william-jin-cmu)

> ⭐ **36** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 36 | Status | ✅ active |
| Author | [william-jin-cmu](https://github.com/william-jin-cmu) | Updated | 2026-08-13 |
| Subcategory | 👁️ Vision tools | Capabilities | multimodal, vision |

## One-liner

> Vision bridge: view_image tool over any OpenAI-compatible VLM, defaulting to Zhipu's free tier.

## About

给纯文本的 DeepSeek 加上眼睛。Vision for text-only DeepSeek. deepseek-v4 看不了图。本插件注册一个 `view_image` 工具：模型带着问题调用它（OCR、数数、读图表、看 UI 布局……任意视觉问题），插件把图片和问题转发给任意 **OpenAI 兼容的 VLM 端点**，答案以文本返回。装上之后，dsh 的所有入口（web、TUI、远程通道）同时获得视觉。 用户: 看下 ~/Desktop/error.png 是什么报错 模型 → view_image(source="/Users/me/Desktop/error.png", question="这个报错的完整文本是什么？") ← "TypeError: Cannot read properties of undefined (reading 'map') at …" 模型: 这是一个 … 建议 …

## 🚀 Quick Start

```bash
用户: 看下 ~/Desktop/error.png 是什么报错
模型 → view_image(source="/Users/me/Desktop/error.png", question="这个报错的完整文本是什么？")
     ← "TypeError: Cannot read properties of undefined (reading 'map') at …"
模型: 这是一个 … 建议 …
```

## 📚 Learn more

**配置**

dsh-vision: baseURL: https://open.bigmodel.cn/api/paas/v4 apiKey: "" # 留空则读环境变量 model: glm-4.6v-flash maxTokens: 2048 timeoutMs: 60000 maxImageBytes: 10485760

## 🔗 Links

- [GitHub Repository](https://github.com/william-jin-cmu/dsh-vision)
- [Full README](https://github.com/william-jin-cmu/dsh-vision#readme)
- [Back to the Plugins list](../plugins.md)
