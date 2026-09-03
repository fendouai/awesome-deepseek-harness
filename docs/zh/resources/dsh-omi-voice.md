---
title: "dsh-omi-voice"
description: "沉浸式听朗读插件：对话内点读/暂停/继续，豆包 TTS 自然音色（BYOK），只读最终回答并过滤代码/表格/图形。"
keywords: "dsh-omi-voice, ui, plugin, multimodal, deepseek harness, dsh"
---
# dsh-omi-voice

> ⭐ **34** · ✅ 活跃 · 插件 · 近期 ⬆️ +6

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 34 | 状态 | ✅ 活跃 |
| 作者 | [PolinniZhong](https://github.com/PolinniZhong) | 更新时间 | 2026-08-19 |

## 一句话介绍

> 沉浸式听朗读插件：对话内点读/暂停/继续，豆包 TTS 自然音色（BYOK），只读最终回答并过滤代码/表格/图形。

## 详细介绍

1. 安装插件 + 构建并打开 Omi 引擎（见下方「获取豆包 API Key」与「安装」）。 2. 在 Omi 引擎设置页保存一次豆包 API Key。 3. 在 DSH 对话里点 AI 回复旁的 🔊，即可朗读。 flowchart LR A[点 🔊] --> B[插件取回复的最终回答文本] B --> C[POST 127.0.0.1:8765/v1/speak] C --> D[Omi 引擎清洗 + 分段] D --> E[豆包 TTS 流式合成] E --> F[本机扬声器播放]

## 📦 安装

```bash
dsh plugin --profile web add "github:PolinniZhong/dsh-omi-voice#v0.1.3&path:/"
```

## 🚀 快速开始

```bash
dsh plugin --profile web add dsh-omi-voice
```

## 📚 更多信息

**安装**

dsh plugin --profile web add "github:PolinniZhong/dsh-omi-voice#v0.1.3&path:/" 已发布 npm，也可直接装（更短）： dsh plugin --profile web add dsh-omi-voice 本地开发可直接装目录： dsh plugin --profile web add /path/to/dsh-omi-voice 引擎（Omi DSH）构建见 [engine/README.md](engine/README.md)：`./engine/build/build-service.sh` 后 `ditto` 到 `~/Applications/Omi DSH.app`。

## 🔗 链接

- [GitHub 仓库](https://github.com/PolinniZhong/dsh-omi-voice)
- [完整 README](https://github.com/PolinniZhong/dsh-omi-voice#readme)
- [返回dsh-omi-voice所在分类](../plugins.md)
