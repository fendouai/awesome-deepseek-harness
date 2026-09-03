---
title: "notes (zhaoolee)"
description: "Open-source Smartisan Notes clone: Docker private deployment, skill invocation, dsh plugin support and one-click WeChat-format export."
keywords: "notes (zhaoolee), registry, awesome-list, ui, files, deepseek harness, dsh"
---
# notes (zhaoolee)

> ⭐ **149** · ✅ active · awesome-list · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | awesome-list | Category | Registries |
| Stars | ⭐ 149 | Status | ✅ active |
| Author | [zhaoolee](https://github.com/zhaoolee) | Updated | 2026-08-18 |

## One-liner

> Open-source Smartisan Notes clone: Docker private deployment, skill invocation, dsh plugin support and one-click WeChat-format export.

## About

- 一个锤子便签风格的导出器，预览与图片导出支持**暖白纸感**、**深夜便签**、**iPhone 备忘录深浅模式**和 **Bear 极简排版**。 - 可用来分享与openclaw的对话记录。 - 完美复刻锤子便签网页版和PC版，支持多便签，分类存储。 - 支持Docker一键私有化部署 - 纯WEB应用，无需安装任何App，打开即用 - 支持PC端和手机版，多端数据同步，支持公网部署 - 支持图片插入。 - 支持一键粘贴到公众号助手。 - 支持直接导出便签为图片，或复制为markdown格式进行分享。 - 自带浏览器持久化，关闭页面也不会丢失数据。 - 开源免费，可私有化部署。 - 工匠精神沁入AI，可以通过AI Skill直接调用工具，生成便签。 - 支持自定义底部标识（点击即可编辑） - API原生封装支持Hermes Agent，OpenClaw直接通过skill驱动管理便签 - 支持 DeepSeek Harness（DSH），让智能体将对话导出为锤子便签。 - 支持接入DeepSeek润色书写内容，语法标点检查，重点加粗，复杂概念通俗化释义。 - 支持一键下载包含图片的Markdown资源包 - 支持下载为html离线查看

## ✨ Key Features

- 一个锤子便签风格的导出器，预览与图片导出支持**暖白纸感**、**深夜便签**、**iPhone 备忘录深浅模式**和 **Bear 极简排版**。
- 可用来分享与openclaw的对话记录。
- 完美复刻锤子便签网页版和PC版，支持多便签，分类存储。
- 支持Docker一键私有化部署
- 纯WEB应用，无需安装任何App，打开即用
- 支持PC端和手机版，多端数据同步，支持公网部署

## 📦 Install

```bash
dsh plugin --profile web add @zhaoolee/dsh-notes
```

## 🚀 Quick Start

```bash
从clawhub安装 notes-export-api这个 skill,
联网获取最近一周 AI 相关的新闻，将新闻转化为 markdown 生成便签图片，把便签图片绝对路径返回给我，把图片往“下载”文件夹复制一份
```

## 📚 Learn more

**使用 Docker Hub 镜像部署**

单镜像同时包含 Web 前端和后端服务，便签管理、图片导入和 PNG 导出均可在本地 运行。公众号复制和 AI 等可选功能需另行配置相应服务。 需要登录、多端同步或 Skill 工作区管理时，先复制 `.env.example`，并配置 `SUPERADMIN`、`SUPERADMINPASSWORD` 和高熵 `SESSION_SECRET`： cp .env.example .env mkdir -p ./storage/images ./storage/data docker run -d \ --restart unless-stopped \ --name notes \ -p 127.0.0.1:18080:3001 \ --env-file .env \ -v "$(pwd)/storage/images:/app/storage/images" \ -v "$(pwd)/s

## 🔗 Links

- [GitHub Repository](https://github.com/zhaoolee/notes)
- [Full README](https://github.com/zhaoolee/notes#readme)
- [Back to the Awesome Lists & Registries list](../awesome-lists.md)
