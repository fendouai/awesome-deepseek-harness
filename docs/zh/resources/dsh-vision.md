---
title: "dsh-vision (william-jin-cmu)"
description: "视觉桥接：view_image 工具桥接任意 OpenAI 兼容 VLM，默认智谱免费档。"
keywords: "dsh-vision (william-jin-cmu), vision, plugin, multimodal, deepseek harness, dsh"
---
# dsh-vision (william-jin-cmu)

> ⭐ 23 · ✅ 活跃 · 插件

## 一句话介绍

视觉桥接：view_image 工具桥接任意 OpenAI 兼容 VLM，默认智谱免费档。

## 详细介绍

给纯文本的 DeepSeek 加上眼睛。Vision for text-only DeepSeek. deepseek-v4 看不了图。本插件注册一个 `view_image` 工具：模型带着问题调用它（OCR、数数、读图表、看 UI 布局……任意视觉问题），插件把图片和问题转发给任意 **OpenAI 兼容的 VLM 端点**，答案以文本返回。装上之后，dsh 的所有入口（web、TUI、远程通道）同时获得视觉。 用户: 看下 ~/Desktop/error.png 是什么报错 模型 → view_image(source="/Users/me/Desktop/error.png", question="这个报错的完整文本是什么？") ← "TypeError: Cannot read properties of undefined (reading 'map') at …" 模型: 这是一个 … 建议 …

## 作者
**[william-jin-cmu](https://github.com/william-jin-cmu)**

## 链接

- [GitHub 仓库](https://github.com/william-jin-cmu/dsh-vision)
- [完整 README](https://github.com/william-jin-cmu/dsh-vision#readme)
- [返回dsh-vision (william-jin-cmu)所在分类](../plugins.md)
