---
title: "dsh-ffmpeg"
description: "DeepSeek Harness 视频处理插件：ffmpeg_probe/cut/concat/encode/subtitle/extract/gif 七工具，走官方 subprocess 服务、argv 数组无 shell 注入、零运行时依赖；纯 Node 全平台。· Video processing tools for DeepSeek Harness agents."
keywords: "dsh-ffmpeg, vision, plugin, coding, multi-agent, deepseek harness, dsh"
---
# dsh-ffmpeg

> ⭐ **4** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 4 | 状态 | ✅ 活跃 |
| 作者 | [STARDUSTLC666](https://github.com/STARDUSTLC666) | 更新时间 | 2026-08-18 |
| 子分类 | 👁️ 视觉工具 | 能力 | coding, multi-agent |

## 一句话介绍

> DeepSeek Harness 视频处理插件：ffmpeg_probe/cut/concat/encode/subtitle/extract/gif 七工具，走官方 subprocess 服务、argv 数组无 shell 注入、零运行时依赖；纯 Node 全平台。· Video processing tools for DeepSeek Harness agents.

## 详细介绍

DSH（DeepSeek Harness）视频处理工具插件：十个工具：探测、剪辑、拼接、转码、字幕、提取、GIF、抽帧、调整（变速/音量/静音/旋转）与自检，全部由 ffmpeg/ffprobe 完成。

## 📦 安装

```bash
dsh plugin --profile web add dsh-ffmpeg
```

## 🚀 快速开始

```bash
dsh plugin --profile web remove dsh-ffmpeg
```

## 📚 更多信息

**安装**

dsh plugin --profile web add dsh-ffmpeg 需要本机已安装 ffmpeg（`ffmpeg -version` 能出结果即可）；不在 PATH 上时可用 `ffmpegPath`/`ffprobePath` 显式指定，或设置环境变量 `DSH_FFMPEG_PATH` / `DSH_FFPROBE_PATH`。

**配置**

在你自己的 profile 的 `cordis.patch.yml` 里覆盖本插件行（缺省时全部用默认值）： name: 'dsh-ffmpeg' config: # ffmpegPath: C:\tools\ffmpeg\bin\ffmpeg.exe # 非 PATH 时显式指定（也可用 DSH_FFMPEG_PATH） # ffprobePath: C:\tools\ffmpeg\bin\ffprobe.exe # 也可用 DSH_FFPROBE_PATH timeoutMs: 300000 # 单次操作超时（默认 5 分钟，10 秒 - 2 小时） # overwrite: true # 允许覆盖同名输出（默认自动加 _1/_2 序号）

**示例**

ffmpeg_probe { input: E:\videos\raw.mp4 } ffmpeg_cut { input: E:\videos\raw.mp4, start: 10, end: 30 } ffmpeg_encode { input: E:\videos\raw.mp4, preset: bilibili-1080p } ffmpeg_subtitle { input: E:\videos\raw.mp4, subtitle: E:\videos\subs.srt } ffmpeg_gif { input: E:\videos\raw.mp4, duration: 3, width: 480 }

## 🔗 链接

- [GitHub 仓库](https://github.com/STARDUSTLC666/dsh-ffmpeg)
- [完整 README](https://github.com/STARDUSTLC666/dsh-ffmpeg#readme)
- [返回dsh-ffmpeg所在分类](../plugins.md)
