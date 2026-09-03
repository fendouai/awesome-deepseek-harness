---
title: "dsh-vision"
description: "Near-native image understanding for DeepSeek Harness"
keywords: "dsh-vision, vision, plugin, coding, multimodal, deepseek harness, dsh"
---
# dsh-vision

> ⭐ **88** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 88 | 状态 | ✅ 活跃 |
| 作者 | [oil-oil](https://github.com/oil-oil) | 更新时间 | — |
| 子分类 | 👁️ 视觉工具 | 能力 | coding, multimodal |

## 一句话介绍

> Near-native image understanding for DeepSeek Harness

## 详细介绍

The plugin does not replace the main model selected in Harness. Multiple image attachments are analyzed together, so comparisons and combined evidence work naturally. The user's task is forwarded unchanged instead of being wrapped in a fixed report template.

## 📦 安装

```bash
npx @deepseek-ai/dsh plugin --profile web add github:oil-oil/dsh-vision
```

## 🚀 快速开始

```bash
llm-deepseek:
  visionBackend: zenmux
  visionBackendModel: qwen/qwen3.7-plus
  visionBackendBaseURL: https://zenmux.ai/api/v1
  maxImages: 8
```

## 📚 更多信息

**Install**

Use the plugin manager built into DeepSeek Harness: npx @deepseek-ai/dsh plugin --profile web add github:oil-oil/dsh-vision Restart Harness, then paste or drag images into the composer as usual. The plugin replaces the official `deepseek-official` adapter while preserving its model catalog, settings, and credentials. It also adds a **Vision Recognition** card to **Settings → Plugins → Plugin confi

**Configure Vision Recognition**

Open **Settings → Plugins → Plugin configuration → Vision Recognition**. Select ZenMux, Alibaba Cloud Model Studio, TokenDance, or OpenRouter, then enter its API key. The same card lets you change the model ID, API endpoint, and image limit. The API key is stored through Harness's official credential service. It is write-only in the browser: the plugin can report whether a key exists, but never re

**Advanced file configuration**

Most setups should use the UI. The equivalent non-secret fields live in the existing `llm-deepseek` section of `$DSH_HOME/settings.yaml`: llm-deepseek: visionBackend: zenmux visionBackendModel: qwen/qwen3.7-plus visionBackendBaseURL: https://zenmux.ai/api/v1 maxImages: 8 Do not put API keys in this file. Save them in the Vision Recognition card or provide the matching environment variable. Changes

## 🔗 链接

- [GitHub 仓库](https://github.com/oil-oil/dsh-vision)
- [完整 README](https://github.com/oil-oil/dsh-vision#readme)
- [返回dsh-vision所在分类](../plugins.md)
