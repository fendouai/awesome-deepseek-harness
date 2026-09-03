---
title: "dsh-chat-imagine"
description: "在 DSH 聊天窗口自动调用生图工具（API 渠道，或本机 CLI：已支持mmx / codex / agy）并展示图片，也支持利用对应 CLI 识别图片。"
keywords: "dsh-chat-imagine, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-chat-imagine

> ⭐ **11** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 11 | Status | ✅ active |
| Author | [corrinehu](https://github.com/corrinehu) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> 在 DSH 聊天窗口自动调用生图工具（API 渠道，或本机 CLI：已支持mmx / codex / agy）并展示图片，也支持利用对应 CLI 识别图片。

## About

[English](./README.en.md) | 中文 实现了在 [DeepSeek Harness（DSH）](https://github.com/deepseek-ai/deepseek-harness) 的聊天窗口中自动调用生图工具（API 渠道，或本机 CLI：已支持mmx / codex / agy）并展示图片，也支持利用对应 CLI 识别图片。

## ✨ Key Features

- 使用 DSH 中已配置的 OpenAI 兼容接口，从中查找可用的生图模型。
- 内置渠道（如 OpenRouter）在 DSH 设置里未填写 base URL 时，插件会自动使用 DSH 内置的默认地址，与聊天路由的行为一致。

## 📦 Install

```bash
# npm（推荐，自带预构建产物）
dsh plugin --profile web add dsh-chat-imagine

# 或从 GitHub 源码安装
dsh plugin --profile web add github:corrinehu/dsh-chat-imagine
```

## 🚀 Quick Start

```bash
帮我生成一个 Q 版蓝鲸 Logo
```

## 📚 Learn more

**使用**

安装启用插件后，在新对话里直接说你想画什么，例如： 帮我生成一个 Q 版蓝鲸 Logo 插件会检索可用的渠道和模型，并询问默认生图的渠道： 设置后，不必重复选择。之后，直接在聊天里描述你想要的图片： 生成一张 16:9 的雪山日出 生成结果会直接显示在聊天中。 也可使用其他生图渠道： 在对话中直接说明即可，例如： 用 agy 生成一张手绘彩铅风格说明大模型后训练的宽屏图片

## 🔗 Links

- [GitHub Repository](https://github.com/corrinehu/dsh-chat-imagine)
- [Full README](https://github.com/corrinehu/dsh-chat-imagine#readme)
- [Back to the Plugins list](../plugins.md)
