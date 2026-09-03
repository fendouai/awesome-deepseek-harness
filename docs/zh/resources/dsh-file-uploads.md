---
title: "dsh-file-uploads"
description: "从 Web 输入框上传任意本地文件，待传卡片显示，设置页统一管理。"
keywords: "dsh-file-uploads, input-editing, plugin, files, ui, deepseek harness, dsh"
---
# dsh-file-uploads

> ⭐ **3** · ✅ 活跃 · 插件 · 近期 ⬆️ +2

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 输入与编辑 |
| 星数 | ⭐ 3 | 状态 | ✅ 活跃 |
| 作者 | [l541402398](https://github.com/l541402398) | 更新时间 | 2026-08-14 |

## 一句话介绍

> 从 Web 输入框上传任意本地文件，待传卡片显示，设置页统一管理。

## 详细介绍

Upload arbitrary local files from the DeepSeek Harness Web composer, attach their container paths to prompts, and manage stored uploads from Settings.

## ✨ 核心特性

- Adds a **Files** button beside the existing composer controls.
- Accepts multiple arbitrary local files, not only images.
- Shows pending files as image-like cards above the composer.
- Keeps the text editor clean: no visible path or generated description is inserted into the draft.
- Serializes each hidden file reference into a model-readable absolute path only when the message is submitted.
- Clears pending cards after submission and restores them when submission fails.
- Stores every upload in one fixed directory, `$DSH_HOME/uploads` by default.
- Lists uploaded files in **Settings → Uploaded files**, with download and delete actions.

## 📦 安装

```bash
dsh plugin --profile web add "github:l541402398/dsh-file-uploads#v1.0.0"
```

## 🚀 快速开始

```bash
dsh plugin --profile web add "github:l541402398/dsh-file-uploads#main"
```

## 📚 更多信息

**Install**

Install the tagged GitHub release into the Web profile: dsh plugin --profile web add "github:l541402398/dsh-file-uploads#v1.0.0" Restart the running Web profile after installation, then refresh the browser page. To install the latest development branch instead: dsh plugin --profile web add "github:l541402398/dsh-file-uploads#main" To remove it: dsh plugin --profile web remove dsh-file-uploads

**Settings**

The plugin adds an **Uploaded files** section to Settings. It displays: Files persist until they are deleted manually.

**Configuration**

The plugin works without configuration. These environment variables override its defaults: Example Docker Compose fragment: services: dsh: environment: DSH_UPLOAD_DIR: /data/dsh/uploads DSH_UPLOAD_MAX_BYTES: 104857600 DSH_UPLOAD_TOTAL_MAX_BYTES: 1073741824 volumes: - ./dsh-data:/data/dsh

## 🔗 链接

- [GitHub 仓库](https://github.com/l541402398/dsh-file-uploads)
- [完整 README](https://github.com/l541402398/dsh-file-uploads#readme)
- [返回dsh-file-uploads所在分类](../plugins.md)
