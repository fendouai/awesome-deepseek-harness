---
title: "PicGo DSH Plugin"
description: "PicGo 官方插件：从 DSH 上传图片/文件到图床并获取公网 URL。"
keywords: "PicGo DSH Plugin, mcp, integration, files, deepseek harness, dsh"
---
# PicGo DSH Plugin

> ⭐ **4** · ✅ 活跃 · 集成

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | MCP |
| 星数 | ⭐ 4 | 状态 | ✅ 活跃 |
| 作者 | [PicGo](https://github.com/PicGo) | 更新时间 | 2026-08-17 |

## 一句话介绍

> PicGo 官方插件：从 DSH 上传图片/文件到图床并获取公网 URL。

## 详细介绍

Upload images and files to your image host from [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness), powered by [PicGo](https://picgo.app/). Harness can show your agent a screenshot, but it has no way to turn a local file into a link. So when the agent writes a README, renders a chart, or captures a screenshot, the image stays on disk and `` becomes a dead link the moment you push. This plugin closes that gap. It uploads through **whatever image host you already configured in PicGo** — PicGo Cloud, GitHub, S3, Tencent COS, Qiniu, or any third-party uploader plugin you installed. Nothing to re-configure. If you've never used PicGo, it walks you into PicGo Cloud's free tier. If the **PicGo desktop app** is running, uploads go through it, reusing the image host you set up in i

## 📦 安装

```bash
dsh plugin --profile web add @picgo/dsh-plugin
```

## 🚀 快速开始

```bash
dsh --profile web
```

## 📚 更多信息

**Install**

dsh plugin --profile web add @picgo/dsh-plugin Then boot as usual: dsh --profile web

**Configuration**

Every field has a working default. Override them from your profile's `cordis.patch.yml`: name: '@picgo/dsh-plugin' config: silent: true timeoutMs: 120000 `gui` controls the desktop-app route described in [Upload routes](#upload-routes): A patch replaces a row's **entire** `config` rather than merging keys, so restate every field you want to keep. Within `gui`, unset keys still fall back to the def

## 🔗 链接

- [GitHub 仓库](https://github.com/PicGo/dsh-plugin)
- [完整 README](https://github.com/PicGo/dsh-plugin#readme)
- [返回PicGo DSH Plugin所在分类](../integrations.md)
