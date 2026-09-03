---
title: "dsh-think-translate"
description: "DSH Web 界面显示层翻译：思考链、任务卡片与回答正文翻译为 8 种目标语言；本地 Ollama 为主力（面板内下载），Google/Bing 兜底。"
keywords: "dsh-think-translate, ui, plugin, deepseek harness, dsh"
---
# dsh-think-translate

> ⭐ **3** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 3 | 状态 | ✅ 活跃 |
| 作者 | [UncleK](https://github.com/UncleK) | 更新时间 | — |
| 子分类 | 🖥️ 侧边栏与面板 | 能力 | ui |

## 一句话介绍

> DSH Web 界面显示层翻译：思考链、任务卡片与回答正文翻译为 8 种目标语言；本地 Ollama 为主力（面板内下载），Google/Bing 兜底。

## 详细介绍

**Languages:** [English](README.md) · [中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) --- Translate the **reasoning / thinking chain (chain-of-thought), task cards and answers** of the [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) Web UI into one of **8 target languages** — in real time, on the display layer only. The originals stay untouched in the transcript, and the translated text **never enters the model context**.

## ✨ 核心特性

- **🕵️ Read any thinking chain** — reasoning, chain-of-thought, task cards and answers translated in real time, streamed batch by batch
- **🌍 8 languages, one consistent UI** — 中文 / English / 日本語 / 한국어 / Español / Français / Deutsch / Русский; the settings panel, thinking rows and task cards all f
- **🔒 Private & offline-first** — local Ollama (qwen2.5:7b / 14b or custom) is the default provider: free, unlimited, nothing leaves your machine. First local-mod
- **🧠 Zero context cost** — pure display layer: the model still sees the original text, and translated text never consumes the context window
- **☁️ Google / Bing fallback** — automatic switch when the local model is unavailable (google goes through a Node CONNECT tunnel using the system proxy, bypassin
- **🛡️ Code-safe** — file paths, commands, URLs, regexes and pure-code lines are never translated

## 🚀 快速开始

```bash
browser → POST /_xlate/translate (same-origin, no CORS)
  → host provider chain (fail-open):
      openai-compatible (local Ollama, Node fetch to loopback)
      → google gtx (Node https + CONNECT tunnel through system proxy)
      → bing (curl form)
  → browser-direct fallback
```

## 📚 更多信息

**🚀 Usage**

1. Open **Settings → Think Translation** 2. Pick the **target language** (e.g. 日本語) — the settings panel, thinking rows and task cards all switch to it 3. Pick the **preferred provider**: - **Local model (Ollama)** — on first selection a download prompt appears (qwen2.5:7b / 14b or custom); it auto-enables when finished. The "+" button next to the model picker downloads more models anytime - **goo

## 🔗 链接

- [GitHub 仓库](https://github.com/UncleK/dsh-think-translate)
- [完整 README](https://github.com/UncleK/dsh-think-translate#readme)
- [返回dsh-think-translate所在分类](../plugins.md)
