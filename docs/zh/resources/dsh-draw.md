---
title: "dsh-draw"
description: "统一文生图路由：配置驱动 OpenAI 兼容引擎路由 + 健康感知回退。"
keywords: "dsh-draw, vision, plugin, deepseek harness, dsh"
---
# dsh-draw

> ⭐ **5** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 5 | 状态 | ✅ 活跃 |
| 作者 | [PerryLink](https://github.com/PerryLink) | 更新时间 | — |
| 子分类 | 👁️ 视觉工具 | 能力 | vision |

## 一句话介绍

> 统一文生图路由：配置驱动 OpenAI 兼容引擎路由 + 健康感知回退。

## 详细介绍

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-draw` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **Unified static-image generation routing for DeepSeek Harness.** *One tool, many engines — health-aware fallback, durable results, counted usage.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ 核心特性

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-draw` (counts toward the [deepseek1024.com](https://deepseek1024.com

## 🚀 快速开始

```bash
model                           harness
  │ image_generate {prompt, ...} ──▶ validate ──▶ quota check ──▶ router
  │                                  openai ──(fail)──▶ cogview ──▶ images
  │ ◀── canonical JSON + image blocks (durable attachment refs)
  │                       └── draw/generated session event (quota + audit)
```

## 📚 更多信息

**Install & uninstall**

> If pnpm reports `ERR_PNPM_IGNORED_BUILDS` for this package (esbuild's harmless platform-binary validation), add `allowBuilds: { esbuild: true }` to your `pnpm-workspace.yaml` — the `dsh` CLI prints the exact snippet.

**Configuration**

All tunables are Schemastery `Config` fields (changeable from cordis.yml). An id-targeted override replaces the whole row — restate every key you need. `cordis.patch.yml` documents each key inline. Example override in your profile patch: - id: dsh-draw name: dsh-draw config: defaultEngine: cogview maxImagesPerCall: 2

## 🔗 链接

- [GitHub 仓库](https://github.com/PerryLink/dsh-draw)
- [完整 README](https://github.com/PerryLink/dsh-draw#readme)
- [返回dsh-draw所在分类](../plugins.md)
