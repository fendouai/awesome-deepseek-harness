---
title: "dsh-plugin-image-tools"
description: "DSH 图片插件：图片选择卡 + 回复内嵌图片 + 盲模型收图"
keywords: "dsh-plugin-image-tools, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-plugin-image-tools

> ⭐ **1** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 1 | Status | ✅ active |
| Author | [Pasumao](https://github.com/Pasumao) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> DSH 图片插件：图片选择卡 + 回复内嵌图片 + 盲模型收图

## About

[**中文**](./README.md) | [English](./README.en.md) **dsh 插件市场里唯一支持「图片选择卡」的插件**：给 DeepSeek Harness Web GUI 增加图片能力， 三个工具覆盖三种场景——模型让你在选项里挑图、在回复正文里展示图、你把图发给盲模型。全部零 token 本地渲染： 图片来源统一支持三种：**本地路径**（相对会话工作区或绝对路径，含 ComfyUI 出图产物）、 **http(s) URL**（服务端拉取后转存）、**base64 data URI**。纯插件实现，不改核心包。

## ✨ Key Features

- **`ask_user_choice`**（图片 / 图文混合选项）：
- **`show_images`**（回复内嵌图片）：
- **`save_received_images`**（盲模型收图 → 文件）：
- 纯文字问题不带图片时，客户端自动放行给原生 UI，互不影响。

## 📦 Install

```bash
# npm（推荐）
dsh plugin --profile web add dsh-plugin-image-tools
# 或 GitHub
dsh plugin --profile web add github:Pasumao/dsh-plugin-image-tools
```

## 🚀 Quick Start

```bash
git clone https://github.com/Pasumao/dsh-plugin-image-tools.git
cd dsh-plugin-image-tools
npm install
# 以 link: 方式挂载进 profile
```

## 🔗 Links

- [GitHub Repository](https://github.com/Pasumao/dsh-plugin-image-tools)
- [Full README](https://github.com/Pasumao/dsh-plugin-image-tools#readme)
- [Back to the Plugins list](../plugins.md)
