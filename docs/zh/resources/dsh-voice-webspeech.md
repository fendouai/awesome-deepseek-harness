---
title: "dsh-voice-webspeech"
description: "Browser Web Speech API voice input for DSH: zero server, zero keys, zero model downloads (Edge=Azure, Chrome=Google speech)."
keywords: "dsh-voice-webspeech, input-editing, plugin, coding, deepseek harness, dsh"
---
# dsh-voice-webspeech

> ⭐ **1** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 输入与编辑 |
| 星数 | ⭐ 1 | 状态 | ✅ 活跃 |
| 作者 | [anweat](https://github.com/anweat) | 更新时间 | 2026-08-14 |

## 一句话介绍

> Browser Web Speech API voice input for DSH: zero server, zero keys, zero model downloads (Edge=Azure, Chrome=Google speech).

## 详细介绍

DSH Web GUI 的**浏览器语音输入**插件：默认零服务端、零 API Key、零模型下载、零 Python， 也可在设置中按需下载本地模型用于离线识别。 按住输入框旁的麦克风按钮说话，松手即把语音转成文字——转写完全由**浏览器内置语音识别** （Web Speech API）完成：

## ✨ 核心特性

- **按住说话 / 松手转文字**：按住麦克风按钮开始聆听，松手停止；期间连续短句自动累积。
- **实时反馈**：聆听时按钮上方悬浮显示"正在聆听… + 实时识别文字"（可关闭）。
- **两种落字方式**（设置里切换）：
- **多语言**：中文普通话/粤语/繁体、英/日/韩/法/德/西/俄等（BCP-47）。
- **隐私**：音频直接交给浏览器语音服务，不经过任何 DSH 服务端、不落盘。

## 📦 安装

```bash
pnpm dsh plugin --profile web add github:anweat/dsh-voice-webspeech
```

## 🚀 快速开始

```bash
cd D:/codeproject/dsh-voice-webspeech
pnpm dsh plugin --profile web add .
```

## 📚 更多信息

**安装**

插件为 out-of-tree client bundle（`dsh.client` + `dsh.bundle.patch`）。 仓库已提交构建产物 `lib/`，git 安装无需再 build。

**方式 A：从 GitHub 安装（推荐）**

pnpm dsh plugin --profile web add github:anweat/dsh-voice-webspeech > 若 pnpm ≥10 提示需要 allowBuilds（因 `prepare`），把打印的包键写进 profile 的 > `pnpm-workspace.yaml` 后重跑；本仓库已提交 `lib/`，通常不会触发。建议固定到提交： > `github:anweat/dsh-voice-webspeech#<sha>`。

**方式 C：打包 tgz 安装**

cd D:/codeproject/dsh-voice-webspeech pnpm run build pnpm pack # 产出 dsh-voice-webspeech-0.1.0.tgz pnpm dsh plugin --profile web add ./dsh-voice-webspeech-0.1.0.tgz **激活**：重启 `dsh web`（`pnpm dsh web`）。插件的 `dsh.bundle.patch` 会把它自动挂进 插件树，客户端 bundle 由 `dsh.client` 声明 + `exports["./client"]` 自动加载。 不要手工把本插件插进 profile 的 `cordis.patch.yml`，否则同一 loader id 会重复。

## 🔗 链接

- [GitHub 仓库](https://github.com/anweat/dsh-voice-webspeech)
- [完整 README](https://github.com/anweat/dsh-voice-webspeech#readme)
- [返回dsh-voice-webspeech所在分类](../plugins.md)
