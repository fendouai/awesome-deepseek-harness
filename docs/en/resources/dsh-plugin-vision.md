---
title: "dsh-plugin-vision"
description: "一个可以让没有视觉的大模型拥有视觉能力的插件（当然，是通过外挂视觉模型实现的）"
keywords: "dsh-plugin-vision, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-plugin-vision

> ⭐ **1** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 1 | Status | ✅ active |
| Author | [MoneShadow](https://github.com/MoneShadow) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> 一个可以让没有视觉的大模型拥有视觉能力的插件（当然，是通过外挂视觉模型实现的）

## About

- [简介 Introduction](#简介-introduction) - [功能特性 Features](#功能特性-features) - [安装 Installation](#安装-installation) - [API Key 配置 API Key Configuration](#api-key-配置-api-key-configuration) - [使用方法 Usage](#使用方法-usage) - [工具参考 Tool Reference](#工具参考-tool-reference) - [插件配置项 Plugin Configuration](#插件配置项-plugin-configuration) - [安全说明 Security](#安全说明-security) - [成本说明 Cost](#成本说明-cost) - [浏览器端图片粘贴（可选）Browser Paste & Drop (Optional)](#浏览器端图片粘贴可选browser-paste--drop-optional) - [开发构建 Development](#开发构建-development) - [兼容性 Compatibility](#兼容性-compatibility) - [已知限制 Limitations](#已知限制-limitations) - [常见问题 FAQ](#常见问题-faq) - [许可证 License](#许可证-license) ---

## ✨ Key Features

- [简介 Introduction](#简介-introduction)
- [功能特性 Features](#功能特性-features)
- [安装 Installation](#安装-installation)
- [API Key 配置 API Key Configuration](#api-key-配置-api-key-configuration)
- [使用方法 Usage](#使用方法-usage)
- [工具参考 Tool Reference](#工具参考-tool-reference)

## 📦 Install

```bash
npm i -D dsh-plugin-vision
dsh web --patch node_modules/dsh-plugin-vision/cordis.patch.yml
```

## 🚀 Quick Start

```bash
- insert:
    - id: dsh-plugin-vision
      name: 'dsh-plugin-vision'
```

## 📚 Learn more

**方式二：合并进 profile（持久安装）**

将以下内容合并进你的 profile `cordis.patch.yml`： - id: dsh-plugin-vision name: 'dsh-plugin-vision' 如需自定义配置，可附加 `config`（字段见 [插件配置项](#插件配置项-plugin-configuration)）： - id: dsh-plugin-vision name: 'dsh-plugin-vision' config: provider: auto # auto | gemini | glm glmModel: glm-4.6v-flash

**使用方法 Usage**

在对话中自然描述需求即可，模型会自动调用视觉工具： 帮我看看这张图 D:\work\screenshot.png 这张订单截图里商品是什么？多少钱？ 用 GLM 分析 code/my/logo.png，描述一下配色 显式指定提供商 / 模型： 用 gemini-3.6-flash 看 baojia/data/purchased_items/xxx.jpg，做 OCR

**常见问题 FAQ**

**Q：为什么不把图片直接作为附件发送？** A：DeepSeek 等文本模型不支持图片输入，DSH 的输入框会拦截图片附件。本插件采用「保存图片 → 路径入消息 → 工具读图」的桥接方案，是文本模型下最接近原生视觉模型体验的实现。 **Q：两个提供商都配了，会重复扣费吗？** A：不会。`auto` 模式按顺序尝试（记住上次成功者），仅在失败时切换；不会并行请求两个提供商。 **Q：Key 存在哪里？安全吗？** A：存于 `~/.dsh/.credentials.yaml`（权限 0600）或环境变量。仓库、会话日志均不落盘 Key。

## 🔗 Links

- [GitHub Repository](https://github.com/MoneShadow/dsh-plugin-vision)
- [Full README](https://github.com/MoneShadow/dsh-plugin-vision#readme)
- [Back to the Plugins list](../plugins.md)
