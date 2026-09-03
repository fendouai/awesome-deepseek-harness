---
title: "PicGo DSH Plugin"
description: "Official PicGo plugin: upload images/files to your image host from DSH and get public URLs."
keywords: "PicGo DSH Plugin, mcp, integration, files, deepseek harness, dsh"
---
# PicGo DSH Plugin

> ⭐ **4** · ✅ active · integration

| | | | |
|---|---|---|---|
| Type | integration | Category | MCP |
| Stars | ⭐ 4 | Status | ✅ active |
| Author | [PicGo](https://github.com/PicGo) | Updated | 2026-08-17 |

## One-liner

> Official PicGo plugin: upload images/files to your image host from DSH and get public URLs.

## About

Upload images and files to your image host from [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness), powered by [PicGo](https://picgo.app/). Harness can show your agent a screenshot, but it has no way to turn a local file into a link. So when the agent writes a README, renders a chart, or captures a screenshot, the image stays on disk and `` becomes a dead link the moment you push. This plugin closes that gap. It uploads through **whatever image host you already configured in PicGo** — PicGo Cloud, GitHub, S3, Tencent COS, Qiniu, or any third-party uploader plugin you installed. Nothing to re-configure. If you've never used PicGo, it walks you into PicGo Cloud's free tier. If the **PicGo desktop app** is running, uploads go through it, reusing the image host you set up in i

## 📦 Install

```bash
dsh plugin --profile web add @picgo/dsh-plugin
```

## 🚀 Quick Start

```bash
dsh --profile web
```

## 📚 Learn more

**Install**

dsh plugin --profile web add @picgo/dsh-plugin Then boot as usual: dsh --profile web

**Configuration**

Every field has a working default. Override them from your profile's `cordis.patch.yml`: name: '@picgo/dsh-plugin' config: silent: true timeoutMs: 120000 `gui` controls the desktop-app route described in [Upload routes](#upload-routes): A patch replaces a row's **entire** `config` rather than merging keys, so restate every field you want to keep. Within `gui`, unset keys still fall back to the def

## 🔗 Links

- [GitHub Repository](https://github.com/PicGo/dsh-plugin)
- [Full README](https://github.com/PicGo/dsh-plugin#readme)
- [Back to the MCP & Integrations list](../integrations.md)
