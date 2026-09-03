---
title: "dsh-vision-toolkit"
description: "让纯文本模型更好的视觉工具箱：带意图图片问答、长截图 OCR、UI 还原、grounding、像素 diff。"
keywords: "dsh-vision-toolkit, vision, plugin, multimodal, research, deepseek harness, dsh"
---
# dsh-vision-toolkit

> ⭐ **802** · ✅ 活跃 · 插件 · 近期 ⬆️ +20

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 802 | 状态 | ✅ 活跃 |
| 作者 | [Anionex](https://github.com/Anionex) | 更新时间 | 2026-08-20 |
| 子分类 | 👁️ 视觉工具 | 能力 | multimodal, vision, research |

## 一句话介绍

> 让纯文本模型更好的视觉工具箱：带意图图片问答、长截图 OCR、UI 还原、grounding、像素 diff。

## 详细介绍

**A more powerful vision toolkit—give text-only models in DeepSeek Harness eyes: image Q&A, long-screenshot OCR, UI restoration, and GUI visual tasks in one toolkit and Skill.** 🚀 Paste an image and ask directly | Install with one command | Broad use cases [Highlights](#highlights) | [Quick start](#quick-start-three-steps) | [Toolbox](#toolbox) | [Configuration and limits](#configuration-and-limits) | [Troubleshooting](#troubleshooting) | [Community](#development-and-community) 🏆 This project is the first comprehensive vision-tool plugin in the DeepSeek Harness ecosystem: it was initiated before internal beta and built during the beta with reference to [`agent-vision-toolkit`](https://github.com/Anionex/agent-vision-toolkit).

## ✨ 核心特性

- **Paste an image and ask directly.** In DSH Web, pasting an image switches the text-only model to its `(Vision Toolkit)` variant automatically — no manual path 
- **One command to install.** After installation, configure a vision provider in **Settings → Vision Toolkit** and start using the tools.
- **Not just a caption — the content that matters.** The model does not produce a generic description; it extracts evidence around the current task, such as “Wher
- **A battle-tested visual-task methodology.** The bundled Skill tells the agent what to look at for different visual tasks, which tool to choose, how to proceed,

## 📦 安装

```bash
dsh plugin --profile web add @anionex/dsh-vision-toolkit
```

## 🚀 快速开始

```bash
dsh plugin --profile headless add @anionex/dsh-vision-toolkit
```

## 📚 更多信息

**Screenshot to editable page**

<p align="center">   </p> > Prompt example: “(Use vision-skills) Rebuild this image into HTML.” *Left: the reference screenshot. Right: an editable HTML/CSS result. The result can continue into screenshot rendering and pixel comparison instead of ending as an image description.*

**1. Install**

dsh plugin --profile web add @anionex/dsh-vision-toolkit You can install it into a Headless Profile too: dsh plugin --profile headless add @anionex/dsh-vision-toolkit Using DSH Desktop? It bundles its own `dsh` CLI and intentionally does not add it to your system PATH. Open **DSH Terminal** from the tray and run the command there, targeting the Desktop profile: dsh plugin --profile desktop add @an

**Configure a vision model**

Configure the vision provider in **Settings → Vision Toolkit** and store the API key as a DSH Credential. Settings stores the Credential reference and never reads the saved secret back into the browser. **Step-by-step AIHubMix tutorial:** [Get an AIHubMix API key and configure Gemini 3.7 Flash for vision](docs/aihubmix-gemini-vision.md). It includes screenshots for account/API-key setup, the exact

**Configure the Python runtime**

Most users never need to configure the Python runtime: the plugin prefers a system Python 3.11+ and otherwise downloads a pinned standalone Python automatically from the domestic mirror, falling back to GitHub when the mirror is unreachable. For advanced setups — overriding `runtime.python`, using `runtime.mode: external`, verifying the runtime, or allowing additional input directories — see [Pyth

## 🔗 链接

- [GitHub 仓库](https://github.com/Anionex/dsh-vision-toolkit)
- [完整 README](https://github.com/Anionex/dsh-vision-toolkit#readme)
- [返回dsh-vision-toolkit所在分类](../plugins.md)
