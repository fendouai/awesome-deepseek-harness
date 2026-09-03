---
title: "dsh-vision-router"
description: "纯文本 Agent 的眼睛：内置免费免密钥视觉链路 + 像素级工具（问答、grounding、裁剪、OCR、SVG 描摹）。"
keywords: "dsh-vision-router, vision, plugin, multimodal, deepseek harness, dsh"
---
# dsh-vision-router

> ⭐ **927** · ✅ 活跃 · 插件 · 近期 ⬆️ +41

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 927 | 状态 | ✅ 活跃 |
| 作者 | [ysr666](https://github.com/ysr666) | 更新时间 | 2026-08-21 |
| 子分类 | 👁️ 视觉工具 | 能力 | multimodal, vision |

## 一句话介绍

> 纯文本 Agent 的眼睛：内置免费免密钥视觉链路 + 像素级工具（问答、grounding、裁剪、OCR、SVG 描摹）。

## 详细介绍

Most DSH vision plugins bridge images to DeepSeek as *text descriptions* — lossy, one-shot, and blind to pixels. This plugin keeps the **Host-canonical image pixels on the vision model's side** and DeepSeek on the reasoning side, and makes looking at an image an **ordinary tool call**: - **One command install.** The package ships its own composition patch (`dsh.bundle.patch`): `dsh plugin add` wires the row, the admission wrapper and the attachment limits automatically — zero manual file edits. Taking over the official DeepSeek route is an optional setting (stealth mode, off by default). - **Free by default.** Vision tools end with a five-model OVHcloud anonymous fallback: no account, no key, 2 requests/minute per IP per model, roughly 10 RPM in theory across independent buckets. User-prov

## ✨ 核心特性

- [Why this exists](#why-this-exists)
- [How it compares](#how-it-compares)
- [Design lineage](#design-lineage)
- [Acknowledgements](#acknowledgements)
- [Quick start](#quick-start)
- [Free vision key channels](#free-vision-key-channels)

## 📦 安装

```bash
npx @deepseek-ai/dsh plugin --profile web add dsh-vision-router
```

## 🚀 快速开始

```bash
cd deepseek-harness
pnpm dsh plugin --profile web add dsh-vision-router
```

## 📚 更多信息

**1. Install the plugin**

For normal npm/npx installs, installation is a single command: npx @deepseek-ai/dsh plugin --profile web add dsh-vision-router > [!WARNING] > If this profile already loads community plugins manually through `cordis.patch.yml`, do **not** mix that legacy setup with `dsh plugin add` / `dsh plugin list`: current DSH CLI behavior can also append bundle-patch dependencies to `dsh.profile.bundles`, caus

**Web settings**

The Web profile registers a first-class **Settings → Vision Router** surface. Its General page keeps model choice and v2 routing authority together; Vision Strategy, Local & Device, Advanced and Diagnostics separate tool behavior, local backends, sensitive/performance controls and troubleshooting. <p align="center">  </p>

**Configuration**

Everything is optional; defaults work out of the box. Prefer **Settings → Vision Router**; profile overrides remain available for advanced deployments:

**Install**

Normal npm/npx install — one command: npx @deepseek-ai/dsh plugin --profile web add dsh-vision-router > [!NOTE] > Profiles that mix legacy manual `cordis.patch.yml` plugin rows with bundle-managed plugins should read the compatibility warning in [Quick start](#1-install-the-plugin) before running DSH plugin commands. From a DeepSeek Harness source checkout: pnpm dsh plugin --profile web add dsh-vi

## 🔗 链接

- [GitHub 仓库](https://github.com/ysr666/dsh-vision-router)
- [完整 README](https://github.com/ysr666/dsh-vision-router#readme)
- [返回dsh-vision-router所在分类](../plugins.md)
