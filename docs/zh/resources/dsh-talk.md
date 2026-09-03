---
title: "dsh-talk"
description: "Voice-first session loop for DeepSeek Harness: a composer microphone button with browser/local speech-to-text (Web Speech, FunASR, whisper.cpp), a speak tool for text-to-speech replies (browser, edge-tts, piper), event announcements with mute, and speak-to-interrupt."
keywords: "dsh-talk, browser, integration, coding, deepseek harness, dsh"
---
# dsh-talk

> ⭐ **5** · ✅ 活跃 · 集成

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | 浏览器控制 |
| 星数 | ⭐ 5 | 状态 | ✅ 活跃 |
| 作者 | [PerryLink](https://github.com/PerryLink) | 更新时间 | — |

## 一句话介绍

> Voice-first session loop for DeepSeek Harness: a composer microphone button with browser/local speech-to-text (Web Speech, FunASR, whisper.cpp), a speak tool for text-to-speech replies (browser, edge-tts, piper), event announcements with mute, and speak-to-interrupt.

## 详细介绍

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-talk` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **Voice-first session loop for DeepSeek Harness: talk to it, hear it answer.** *Press the mic, speak, and the reply is spoken back — with speak-to-interrupt.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ 核心特性

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-talk` (counts toward the [deepseek1024.com](https://deepseek1024.com

## 📦 安装

```bash
# 1. install the bundle into your profile
dsh plugin --profile web add "github:PerryLink/dsh-talk#main"

# or from npm (published releases)
dsh plugin --profile web add dsh-talk

# 2. restart and verify the row
dsh --profile web --dump-config | grep -A2 'id: talk'
```

## 🚀 快速开始

```bash
> Say "hello" with the speak tool.
```

## 📚 更多信息

**Install & uninstall**

> If pnpm reports `ERR_PNPM_IGNORED_BUILDS` for this package (esbuild's harmless platform-binary validation), add `allowBuilds: { esbuild: true }` to your `pnpm-workspace.yaml` — the `dsh` CLI prints the exact snippet.

**Configuration**

All tunables are Schemastery `Config` fields (changeable from cordis.yml). `cordis.patch.yml` documents each key inline. `stt.silenceFinaliseMs` and `record.vad.silenceMs` are separate mechanisms: the first finalises the Web Speech transcript when continuous recognition hears no speech, the second is the MediaRecorder energy-based detector that ends the recording (and submits it when `record.autoS

## 🔗 链接

- [GitHub 仓库](https://github.com/PerryLink/dsh-talk)
- [完整 README](https://github.com/PerryLink/dsh-talk#readme)
- [返回dsh-talk所在分类](../integrations.md)
