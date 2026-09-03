---
title: "dsh-upload"
description: "DSH Web 的上传按钮：点 📎 选本地文件，字节落盘到会话工作区 .uploads/<会话ID>/，绝对路径追加进输入框（可见可编辑），AI 用自带 fs 工具直接读取。零依赖。"
keywords: "dsh-upload, developer, plugin, files, deepseek harness, dsh"
---
# dsh-upload

> ⭐ 0 · ✅ 活跃 · 插件

## 一句话介绍

DSH Web 的上传按钮：点 📎 选本地文件，字节落盘到会话工作区 .uploads/<会话ID>/，绝对路径追加进输入框（可见可编辑），AI 用自带 fs 工具直接读取。零依赖。

## 详细介绍

给 DeepSeek Harness Web 加一个**真正的"上传文件"按钮**——回答社区 [#867](https://github.com/deepseek-ai/deepseek-harness/discussions/867)("为什么连个上传文件的按钮都没有？")。 - **点 📎 → 选本地文件 → 字节落盘到会话工作区** `.uploads/<sessionId>/` → 绝对路径自动追加进输入框 - 路径**可见、可编辑**：你清楚知道发给 AI 的是什么，发之前随时删改 - AI 用自带的 fs 工具直接读落盘文件；配合 [`dsh-word-docs`](https://github.com/Ei-Ayw/dsh-word-docs) 就是完整文档工作流：**上传 → 处理 → 产出正式 Word** - 纯浏览器原生 API + 一个 POST 路由，无第三方依赖

## 作者
**[Ei-Ayw](https://github.com/Ei-Ayw)**

## 链接

- [GitHub 仓库](https://github.com/Ei-Ayw/dsh-upload)
- [完整 README](https://github.com/Ei-Ayw/dsh-upload#readme)
- [返回dsh-upload所在分类](../plugins.md)
