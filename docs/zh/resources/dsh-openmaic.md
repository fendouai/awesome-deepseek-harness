---
title: "dsh-openmaic"
description: "OpenMAIC for DeepSeek Harness: classrooms, slides, interactive widgets, and Socratic teaching"
keywords: "dsh-openmaic, vision, plugin, coding, multimodal, deepseek harness, dsh"
---
# dsh-openmaic

> ⭐ **28** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 28 | 状态 | ✅ 活跃 |
| 作者 | [THU-MAIC](https://github.com/THU-MAIC) | 更新时间 | — |
| 子分类 | 👁️ 视觉工具 | 能力 | coding, multimodal |

## 一句话介绍

> OpenMAIC for DeepSeek Harness: classrooms, slides, interactive widgets, and Socratic teaching

## 详细介绍

把 OpenMAIC 带进 DeepSeek Harness。Bring OpenMAIC into DeepSeek Harness. `dsh-openmaic` is a DeepSeek Harness plugin that registers four tools and a Socratic teaching skill: - `openmaic_generate`: tell your agent "make me a lesson about X", and the plugin submits the requirement to [open.maic.chat](https://open.maic.chat/), waits for the async generation job, and returns a playable classroom link. - `openmaic_slide`: the agent writes one OpenMAIC slide (PPTist-style Slide JSON) and the plugin renders it with OpenMAIC's official renderer (text, shapes, images, tables, charts, formulas, code). - `openmaic_widget`: the agent writes an OpenMAIC-style interactive widget (simulation, game, or code) per the bundled contract; the code streams as it writes, then renders inline as a sandboxed card. - `o

## ✨ 核心特性

- `openmaic_generate`: tell your agent "make me a lesson about X", and the plugin submits the requirement to [open.maic.chat](https://open.maic.chat/), waits for 
- `openmaic_slide`: the agent writes one OpenMAIC slide (PPTist-style Slide JSON) and the plugin renders it with OpenMAIC's official renderer (text, shapes, image
- `openmaic_widget`: the agent writes an OpenMAIC-style interactive widget (simulation, game, or code) per the bundled contract; the code streams as it writes, th
- `openmaic_render`: the agent writes an inline HTML teaching fragment (concept card, quiz, walkthrough) and the plugin renders it as a sandboxed card right in th
- `openmaic-teach` skill: turns a session into a Socratic OpenMAIC lesson, teaching by guided questioning and pulling in slides, widgets, and cards as aids.

## 📦 安装

```bash
dsh plugin --profile web add git+https://github.com/THU-MAIC/dsh-openmaic.git
```

## 🚀 快速开始

```bash
dsh-openmaic:
  baseUrl: https://open.maic.chat
  accessCode: ""     # invite code; not enforced online yet, leave empty
  pollIntervalMs: 5000
  maxWaitMs: 600000
```

## 📚 更多信息

**Install**

dsh plugin --profile web add git+https://github.com/THU-MAIC/dsh-openmaic.git Then restart `dsh web` and refresh. The plugin ships its compiled `lib/`, so a git install needs no build step.

**Config**

dsh-openmaic: baseUrl: https://open.maic.chat accessCode: "" # invite code; not enforced online yet, leave empty pollIntervalMs: 5000 maxWaitMs: 600000

## 🔗 链接

- [GitHub 仓库](https://github.com/THU-MAIC/dsh-openmaic)
- [完整 README](https://github.com/THU-MAIC/dsh-openmaic#readme)
- [返回dsh-openmaic所在分类](../plugins.md)
