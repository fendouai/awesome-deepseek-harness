---
title: "dsh-voice-input-plugin"
description: "Composer mic for DeepSeek Harness Web: tap-to-monitor live transcription and hold-to-talk, with host Edge TTS reply reading that streams while the model generates, echo-pause during reading, and tap-to-stop."
keywords: "dsh-voice-input-plugin, search, plugin, coding, deepseek harness, dsh"
---
# dsh-voice-input-plugin

> ⭐ **6** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 6 | Status | ✅ active |
| Author | [Zhangbo-cn](https://github.com/Zhangbo-cn) | Updated | — |
| Subcategory | 🌐 Web search | Capabilities | coding |

## One-liner

> Composer mic for DeepSeek Harness Web: tap-to-monitor live transcription and hold-to-talk, with host Edge TTS reply reading that streams while the model generates, echo-pause during reading, and tap-to-stop.

## About

Composer **voice control** for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness): a minimal linear mic button in the composer tool row that turns your speech into text — with a **tap-to-monitor** mode (continuous, live 逐字 streaming, send-anytime) and a **hold-to-talk** voice-chat mode (release to send, reply read aloud). Zero API key: recognition runs in the browser via the Web Speech API; reply reading uses the host's Edge TTS (`/api/tts`) with a browser `speechSynthesis` fallback. `dsh-plugin` · TypeScript · React

## ✨ Key Features

- **Tap to monitor**: click the mic, speak — text streams into the draft live (逐字输入), the mic keeps listening even in silence, and you can send or keep adding spe
- **Auto-send on silence** *(optional)*: with `autoSendOnSilenceMs` configured, tap-to-monitor becomes hands-free — once you stop talking for the configured windo
- **Hold to talk**: press-and-hold to record a voice-chat message, release to send it; the assistant's reply is read aloud — host Edge neural TTS (`/api/tts`) fir
- **Continuous across silences**: each recognition segment auto-restarts so monitoring never drops.
- **Respects the composer**: speech appends to the draft (base preserved); a send clears the draft cleanly without re-filling old text; monitoring continues after
- **DeepSeek-blue listening state**: the icon pulses in DeepSeek brand blue while listening; borderless linear icon, no clutter.
- **Configurable**: recognition language (default `zh-CN`) and interim results.

## 📦 Install

```bash
dsh plugin add @zhangbo-cn/dsh-client-ui-voice-input
```

## 🚀 Quick Start

```bash
- id: ui-voice-input
  name: '@zhangbo-cn/dsh-client-ui-voice-input'
```

## 📚 Learn more

**Install**

The package is a `dsh.bundle` installable, published on npm as [`@zhangbo-cn/dsh-client-ui-voice-input`](https://www.npmjs.com/package/@zhangbo-cn/dsh-client-ui-voice-input). One command: dsh plugin add @zhangbo-cn/dsh-client-ui-voice-input > **0.1.1+ required.** `0.1.0` registered the browser bundle under the wrong ModuleLoader id (`@deepseek-ai/...`), so Harness failed with `loaded without regis

**Configuration**

name: '@zhangbo-cn/dsh-client-ui-voice-input' config: language: 'zh-CN' # Web Speech recognition language tag interimResults: true # stream live interim transcript into the draft autoSendOnSilenceMs: 0 # auto-submit after this many ms of silence following committed speech (0 = off)

## 🔗 Links

- [GitHub Repository](https://github.com/Zhangbo-cn/dsh-voice-input-plugin)
- [Full README](https://github.com/Zhangbo-cn/dsh-voice-input-plugin#readme)
- [Back to the Plugins list](../plugins.md)
