---
title: "dsh-plugin-image-tools"
description: "DSH 图片插件：图片选择卡 + 回复内嵌图片 + 盲模型收图"
keywords: "dsh-plugin-image-tools, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-plugin-image-tools

> ⭐ **1** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 1 | 状态 | ✅ 活跃 |
| 作者 | [Pasumao](https://github.com/Pasumao) | 更新时间 | — |
| 子分类 | 👁️ 视觉工具 | 能力 | coding |

## 一句话介绍

> DSH 图片插件：图片选择卡 + 回复内嵌图片 + 盲模型收图

## 详细介绍

[**中文**](./README.md) | [English](./README.en.md) **dsh 插件市场里唯一支持「图片选择卡」的插件**：给 DeepSeek Harness Web GUI 增加图片能力， 三个工具覆盖三种场景——模型让你在选项里挑图、在回复正文里展示图、你把图发给盲模型。全部零 token 本地渲染： 图片来源统一支持三种：**本地路径**（相对会话工作区或绝对路径，含 ComfyUI 出图产物）、 **http(s) URL**（服务端拉取后转存）、**base64 data URI**。纯插件实现，不改核心包。

## ✨ 核心特性

- **`ask_user_choice`**（图片 / 图文混合选项）：
- **`show_images`**（回复内嵌图片）：
- **`save_received_images`**（盲模型收图 → 文件）：
- 纯文字问题不带图片时，客户端自动放行给原生 UI，互不影响。

## 📦 安装

```bash
# npm（推荐）
dsh plugin --profile web add dsh-plugin-image-tools
# 或 GitHub
dsh plugin --profile web add github:Pasumao/dsh-plugin-image-tools
```

## 🚀 快速开始

```bash
git clone https://github.com/Pasumao/dsh-plugin-image-tools.git
cd dsh-plugin-image-tools
npm install
# 以 link: 方式挂载进 profile
```

## 🔗 链接

- [GitHub 仓库](https://github.com/Pasumao/dsh-plugin-image-tools)
- [完整 README](https://github.com/Pasumao/dsh-plugin-image-tools#readme)
- [返回dsh-plugin-image-tools所在分类](../plugins.md)
