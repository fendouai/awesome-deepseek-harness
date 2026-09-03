---
title: "dsh-upload"
description: "Upload button for the DSH web composer: local files land as bytes in the session workspace (.uploads/<sessionId>/), the absolute path is appended to the draft (visible and editable), and the agent reads the file with its own fs tools. Zero dependencies. / DSH Web 的上传按钮：点 📎 选本地文件，字节落盘到会话工作区 .uploads/<会话ID>/，绝对路径追加进输入框（可见可编辑），AI 用自带 fs 工具直接读取。零依赖。"
keywords: "dsh-upload, developer, plugin, files, deepseek harness, dsh"
---
# dsh-upload

> ⭐ **0** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 0 | Status | ✅ active |
| Author | [Ei-Ayw](https://github.com/Ei-Ayw) | Updated | — |
| Subcategory | 📁 Files & import | Capabilities | files |

## One-liner

> Upload button for the DSH web composer: local files land as bytes in the session workspace (.uploads/<sessionId>/), the absolute path is appended to the draft (visible and editable), and the agent reads the file with its own fs tools. Zero dependencies. / DSH Web 的上传按钮：点 📎 选本地文件，字节落盘到会话工作区 .uploads/<会话ID>/，绝对路径追加进输入框（可见可编辑），AI 用自带 fs 工具直接读取。零依赖。

## About

给 DeepSeek Harness Web 加一个**真正的"上传文件"按钮**——回答社区 [#867](https://github.com/deepseek-ai/deepseek-harness/discussions/867)("为什么连个上传文件的按钮都没有？")。 - **点 📎 → 选本地文件 → 字节落盘到会话工作区** `.uploads//` → 绝对路径自动追加进输入框 - 路径**可见、可编辑**：你清楚知道发给 AI 的是什么，发之前随时删改 - AI 用自带的 fs 工具直接读落盘文件；配合 [`dsh-word-docs`](https://github.com/Ei-Ayw/dsh-word-docs) 就是完整文档工作流：**上传 → 处理 → 产出正式 Word** - 纯浏览器原生 API + 一个 POST 路由，无第三方依赖

## ✨ Key Features

- **点 📎 → 选本地文件 → 字节落盘到会话工作区** `.uploads/<sessionId>/` → 绝对路径自动追加进输入框
- 路径**可见、可编辑**：你清楚知道发给 AI 的是什么，发之前随时删改
- AI 用自带的 fs 工具直接读落盘文件；配合 [`dsh-word-docs`](https://github.com/Ei-Ayw/dsh-word-docs) 就是完整文档工作流：**上传 → 处理 → 产出正式 Word**
- 纯浏览器原生 API + 一个 POST 路由，无第三方依赖

## 📦 Install

```bash
dsh plugin --profile web add github:Ei-Ayw/dsh-upload
# 重启 dsh Web → composer 工具行左端出现 📎
```

## 🚀 Quick Start

```bash
- id: dsh-upload
  config:
    maxBytes: 52428800      # 单文件上限，默认 50MB
    subDir: '.uploads'      # 工作区内落盘目录
```

## 📚 Learn more

**使用**

1. 打开一个会话，点输入框左侧的 **📎** 2. 选择本地任意文件（PDF / Word / Excel / 图片 / 压缩包…） 3. 输入框自动追加一行 `📎 /绝对路径/…`，点发送 4. AI 用 fs 工具读取该文件并处理 > 落盘位置：`<工作区>/.uploads/<会话ID>/<原文件名>`。上传的文件属于该会话工作区，随时可以在文件管理器里看到、删除。

## 🔗 Links

- [GitHub Repository](https://github.com/Ei-Ayw/dsh-upload)
- [Full README](https://github.com/Ei-Ayw/dsh-upload#readme)
- [Back to the Plugins list](../plugins.md)
