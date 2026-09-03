---
title: "dsh-openmaic"
description: "OpenMAIC for DeepSeek Harness: classrooms, slides, interactive widgets, and Socratic teaching"
keywords: "dsh-openmaic, vision, plugin, coding, multimodal, deepseek harness, dsh"
---
# dsh-openmaic

> ⭐ **28** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 28 | Status | ✅ active |
| Author | [THU-MAIC](https://github.com/THU-MAIC) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding, multimodal |

## One-liner

> OpenMAIC for DeepSeek Harness: classrooms, slides, interactive widgets, and Socratic teaching

## About

把 OpenMAIC 带进 DeepSeek Harness。Bring OpenMAIC into DeepSeek Harness. `dsh-openmaic` is a DeepSeek Harness plugin that registers four tools and a Socratic teaching skill: - `openmaic_generate`: tell your agent "make me a lesson about X", and the plugin submits the requirement to [open.maic.chat](https://open.maic.chat/), waits for the async generation job, and returns a playable classroom link. - `openmaic_slide`: the agent writes one OpenMAIC slide (PPTist-style Slide JSON) and the plugin renders it with OpenMAIC's official renderer (text, shapes, images, tables, charts, formulas, code). - `openmaic_widget`: the agent writes an OpenMAIC-style interactive widget (simulation, game, or code) per the bundled contract; the code streams as it writes, then renders inline as a sandboxed card. - `o

## ✨ Key Features

- `openmaic_generate`: tell your agent "make me a lesson about X", and the plugin submits the requirement to [open.maic.chat](https://open.maic.chat/), waits for 
- `openmaic_slide`: the agent writes one OpenMAIC slide (PPTist-style Slide JSON) and the plugin renders it with OpenMAIC's official renderer (text, shapes, image
- `openmaic_widget`: the agent writes an OpenMAIC-style interactive widget (simulation, game, or code) per the bundled contract; the code streams as it writes, th
- `openmaic_render`: the agent writes an inline HTML teaching fragment (concept card, quiz, walkthrough) and the plugin renders it as a sandboxed card right in th
- `openmaic-teach` skill: turns a session into a Socratic OpenMAIC lesson, teaching by guided questioning and pulling in slides, widgets, and cards as aids.

## 📦 Install

```bash
dsh plugin --profile web add git+https://github.com/THU-MAIC/dsh-openmaic.git
```

## 🚀 Quick Start

```bash
dsh-openmaic:
  baseUrl: https://open.maic.chat
  accessCode: ""     # invite code; not enforced online yet, leave empty
  pollIntervalMs: 5000
  maxWaitMs: 600000
```

## 📚 Learn more

**Install**

dsh plugin --profile web add git+https://github.com/THU-MAIC/dsh-openmaic.git Then restart `dsh web` and refresh. The plugin ships its compiled `lib/`, so a git install needs no build step.

**Config**

dsh-openmaic: baseUrl: https://open.maic.chat accessCode: "" # invite code; not enforced online yet, leave empty pollIntervalMs: 5000 maxWaitMs: 600000

## 🔗 Links

- [GitHub Repository](https://github.com/THU-MAIC/dsh-openmaic)
- [Full README](https://github.com/THU-MAIC/dsh-openmaic#readme)
- [Back to the Plugins list](../plugins.md)
