---
title: "dsh-talk"
description: "Voice-first session loop for DeepSeek Harness: a composer microphone button with browser/local speech-to-text (Web Speech, FunASR, whisper.cpp), a speak tool for text-to-speech replies (browser, edge-tts, piper), event announcements with mute, and speak-to-interrupt."
keywords: "dsh-talk, browser, integration, coding, deepseek harness, dsh"
---
# dsh-talk

> ⭐ **5** · ✅ active · integration

| | | | |
|---|---|---|---|
| Type | integration | Category | Browser control |
| Stars | ⭐ 5 | Status | ✅ active |
| Author | [PerryLink](https://github.com/PerryLink) | Updated | — |

## One-liner

> Voice-first session loop for DeepSeek Harness: a composer microphone button with browser/local speech-to-text (Web Speech, FunASR, whisper.cpp), a speak tool for text-to-speech replies (browser, edge-tts, piper), event announcements with mute, and speak-to-interrupt.

## About

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-talk` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **Voice-first session loop for DeepSeek Harness: talk to it, hear it answer.** *Press the mic, speak, and the reply is spoken back — with speak-to-interrupt.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ Key Features

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-talk` (counts toward the [deepseek1024.com](https://deepseek1024.com

## 📦 Install

```bash
# 1. install the bundle into your profile
dsh plugin --profile web add "github:PerryLink/dsh-talk#main"

# or from npm (published releases)
dsh plugin --profile web add dsh-talk

# 2. restart and verify the row
dsh --profile web --dump-config | grep -A2 'id: talk'
```

## 🚀 Quick Start

```bash
> Say "hello" with the speak tool.
```

## 📚 Learn more

**Install & uninstall**

> If pnpm reports `ERR_PNPM_IGNORED_BUILDS` for this package (esbuild's harmless platform-binary validation), add `allowBuilds: { esbuild: true }` to your `pnpm-workspace.yaml` — the `dsh` CLI prints the exact snippet.

**Configuration**

All tunables are Schemastery `Config` fields (changeable from cordis.yml). `cordis.patch.yml` documents each key inline. `stt.silenceFinaliseMs` and `record.vad.silenceMs` are separate mechanisms: the first finalises the Web Speech transcript when continuous recognition hears no speech, the second is the MediaRecorder energy-based detector that ends the recording (and submits it when `record.autoS

## 🔗 Links

- [GitHub Repository](https://github.com/PerryLink/dsh-talk)
- [Full README](https://github.com/PerryLink/dsh-talk#readme)
- [Back to the MCP & Integrations list](../integrations.md)
