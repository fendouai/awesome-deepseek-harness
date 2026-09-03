---
title: "dsh-file-uploads"
description: "Upload arbitrary local files from the Web composer with pending cards, managed in Settings."
keywords: "dsh-file-uploads, input-editing, plugin, files, ui, deepseek harness, dsh"
---
# dsh-file-uploads

> ⭐ **3** · ✅ active · plugin · ⬆️ +2 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Input & editing |
| Stars | ⭐ 3 | Status | ✅ active |
| Author | [l541402398](https://github.com/l541402398) | Updated | 2026-08-14 |

## One-liner

> Upload arbitrary local files from the Web composer with pending cards, managed in Settings.

## About

Upload arbitrary local files from the DeepSeek Harness Web composer, attach their container paths to prompts, and manage stored uploads from Settings.

## ✨ Key Features

- Adds a **Files** button beside the existing composer controls.
- Accepts multiple arbitrary local files, not only images.
- Shows pending files as image-like cards above the composer.
- Keeps the text editor clean: no visible path or generated description is inserted into the draft.
- Serializes each hidden file reference into a model-readable absolute path only when the message is submitted.
- Clears pending cards after submission and restores them when submission fails.
- Stores every upload in one fixed directory, `$DSH_HOME/uploads` by default.
- Lists uploaded files in **Settings → Uploaded files**, with download and delete actions.

## 📦 Install

```bash
dsh plugin --profile web add "github:l541402398/dsh-file-uploads#v1.0.0"
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add "github:l541402398/dsh-file-uploads#main"
```

## 📚 Learn more

**Install**

Install the tagged GitHub release into the Web profile: dsh plugin --profile web add "github:l541402398/dsh-file-uploads#v1.0.0" Restart the running Web profile after installation, then refresh the browser page. To install the latest development branch instead: dsh plugin --profile web add "github:l541402398/dsh-file-uploads#main" To remove it: dsh plugin --profile web remove dsh-file-uploads

**Settings**

The plugin adds an **Uploaded files** section to Settings. It displays: Files persist until they are deleted manually.

**Configuration**

The plugin works without configuration. These environment variables override its defaults: Example Docker Compose fragment: services: dsh: environment: DSH_UPLOAD_DIR: /data/dsh/uploads DSH_UPLOAD_MAX_BYTES: 104857600 DSH_UPLOAD_TOTAL_MAX_BYTES: 1073741824 volumes: - ./dsh-data:/data/dsh

## 🔗 Links

- [GitHub Repository](https://github.com/l541402398/dsh-file-uploads)
- [Full README](https://github.com/l541402398/dsh-file-uploads#readme)
- [Back to the Plugins list](../plugins.md)
