---
title: "dsh-think-translate"
description: "Display-layer UI translation for DSH Web: thinking chain, task cards and answer text in 8 target languages; local Ollama primary with in-panel model download, Google/Bing fallback."
keywords: "dsh-think-translate, ui, plugin, deepseek harness, dsh"
---
# dsh-think-translate

> ⭐ **3** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 3 | Status | ✅ active |
| Author | [UncleK](https://github.com/UncleK) | Updated | — |
| Subcategory | 🖥️ Sidebars & panels | Capabilities | ui |

## One-liner

> Display-layer UI translation for DSH Web: thinking chain, task cards and answer text in 8 target languages; local Ollama primary with in-panel model download, Google/Bing fallback.

## About

**Languages:** [English](README.md) · [中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) --- Translate the **reasoning / thinking chain (chain-of-thought), task cards and answers** of the [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) Web UI into one of **8 target languages** — in real time, on the display layer only. The originals stay untouched in the transcript, and the translated text **never enters the model context**.

## ✨ Key Features

- **🕵️ Read any thinking chain** — reasoning, chain-of-thought, task cards and answers translated in real time, streamed batch by batch
- **🌍 8 languages, one consistent UI** — 中文 / English / 日本語 / 한국어 / Español / Français / Deutsch / Русский; the settings panel, thinking rows and task cards all f
- **🔒 Private & offline-first** — local Ollama (qwen2.5:7b / 14b or custom) is the default provider: free, unlimited, nothing leaves your machine. First local-mod
- **🧠 Zero context cost** — pure display layer: the model still sees the original text, and translated text never consumes the context window
- **☁️ Google / Bing fallback** — automatic switch when the local model is unavailable (google goes through a Node CONNECT tunnel using the system proxy, bypassin
- **🛡️ Code-safe** — file paths, commands, URLs, regexes and pure-code lines are never translated

## 🚀 Quick Start

```bash
browser → POST /_xlate/translate (same-origin, no CORS)
  → host provider chain (fail-open):
      openai-compatible (local Ollama, Node fetch to loopback)
      → google gtx (Node https + CONNECT tunnel through system proxy)
      → bing (curl form)
  → browser-direct fallback
```

## 📚 Learn more

**🚀 Usage**

1. Open **Settings → Think Translation** 2. Pick the **target language** (e.g. 日本語) — the settings panel, thinking rows and task cards all switch to it 3. Pick the **preferred provider**: - **Local model (Ollama)** — on first selection a download prompt appears (qwen2.5:7b / 14b or custom); it auto-enables when finished. The "+" button next to the model picker downloads more models anytime - **goo

## 🔗 Links

- [GitHub Repository](https://github.com/UncleK/dsh-think-translate)
- [Full README](https://github.com/UncleK/dsh-think-translate#readme)
- [Back to the Plugins list](../plugins.md)
