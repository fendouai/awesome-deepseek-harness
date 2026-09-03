---
title: "dsh-omi-voice"
description: "Immersive voice reading plugin: in-chat read/pause/resume with Doubao TTS natural voices (BYOK), reads only the final answer, filters code/tables/graphics."
keywords: "dsh-omi-voice, ui, plugin, multimodal, deepseek harness, dsh"
---
# dsh-omi-voice

> ⭐ **34** · ✅ active · plugin · ⬆️ +6 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 34 | Status | ✅ active |
| Author | [PolinniZhong](https://github.com/PolinniZhong) | Updated | 2026-08-19 |

## One-liner

> Immersive voice reading plugin: in-chat read/pause/resume with Doubao TTS natural voices (BYOK), reads only the final answer, filters code/tables/graphics.

## About

1. 安装插件 + 构建并打开 Omi 引擎（见下方「获取豆包 API Key」与「安装」）。 2. 在 Omi 引擎设置页保存一次豆包 API Key。 3. 在 DSH 对话里点 AI 回复旁的 🔊，即可朗读。 flowchart LR A[点 🔊] --> B[插件取回复的最终回答文本] B --> C[POST 127.0.0.1:8765/v1/speak] C --> D[Omi 引擎清洗 + 分段] D --> E[豆包 TTS 流式合成] E --> F[本机扬声器播放]

## 📦 Install

```bash
dsh plugin --profile web add "github:PolinniZhong/dsh-omi-voice#v0.1.3&path:/"
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add dsh-omi-voice
```

## 📚 Learn more

**安装**

dsh plugin --profile web add "github:PolinniZhong/dsh-omi-voice#v0.1.3&path:/" 已发布 npm，也可直接装（更短）： dsh plugin --profile web add dsh-omi-voice 本地开发可直接装目录： dsh plugin --profile web add /path/to/dsh-omi-voice 引擎（Omi DSH）构建见 [engine/README.md](engine/README.md)：`./engine/build/build-service.sh` 后 `ditto` 到 `~/Applications/Omi DSH.app`。

## 🔗 Links

- [GitHub Repository](https://github.com/PolinniZhong/dsh-omi-voice)
- [Full README](https://github.com/PolinniZhong/dsh-omi-voice#readme)
- [Back to the Plugins list](../plugins.md)
