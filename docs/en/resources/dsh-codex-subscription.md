---
title: "dsh-codex-subscription"
description: "ChatGPT/Codex subscription provider for DeepSeek Harness with OAuth, models, quota, search, and image tools—no API key or Codex CLI."
keywords: "dsh-codex-subscription, vision, plugin, coding, multimodal, search, deepseek harness, dsh"
---
# dsh-codex-subscription

> ⭐ **26** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 26 | Status | ✅ active |
| Author | [WSL043](https://github.com/WSL043) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding, multimodal, search |

## One-liner

> ChatGPT/Codex subscription provider for DeepSeek Harness with OAuth, models, quota, search, and image tools—no API key or Codex CLI.

## About

**简体中文** · [English](https://github.com/WSL043/dsh-codex-subscription/blob/main/README.en.md) **把 ChatGPT / Codex 订阅直接接入 DeepSeek Harness** 在 DeepSeek Harness 中直接登录 ChatGPT 并使用 Codex 订阅。无需 OpenAI API Key，也不依赖 Codex CLI； 模型、搜索、额度和图片生成都留在 DSH 里。 [三步开始](#三步开始) · [安装](#安装) · [参与贡献](CONTRIBUTING.md) · [更新与卸载](#更新与卸载)

## ✨ Key Features

- ChatGPT OAuth 登录，凭据保留在本机；可手动添加、切换和移除多个账号，不会自动轮换或合并额度；
- Codex 模型和 Beta 图片生成与编辑直接出现在 DSH 会话中；
- 搜索来源是全局设置，可在 DSH 默认搜索与 Codex 订阅搜索之间切换；它对所有模型和会话生效，不会随当前模型自动切换；
- 设置页显示服务端返回的额度、重置时间和更新时间；
- 普通 Codex、Codex-Spark、Credits 等独立额度分开显示；
- 显示重置卡数量与最早到期时间，也允许在额度未完全用尽时主动尝试，并经过分层确认且不会自动重试；
- 输入框可用百分比、进度条或可选的 Beta 续航预测显示当前 Codex 模型的剩余额度（默认关闭）；
- 输入框可为支持的 Codex 模型切换标准或高速模式；

## 📦 Install

```bash
dsh plugin --profile web add dsh-codex-subscription
```

## 🚀 Quick Start

```bash
dsh plugin --profile headless add dsh-codex-subscription
dsh --profile headless "只回复：ok"
```

## 📚 Learn more

**安全使用额度重置**

ChatGPT 返回可用重置卡时，设置页会用紧凑的一行显示数量和服务端提供的最早到期时间。即使额度尚未到 100%， 也可以主动尝试使用，适合重置卡即将过期的情况；是否需要重置仍由 ChatGPT 判断，服务端可能返回“当前无需重置”且不扣次数。 最终操作需要勾选知情确认并等待 5 秒。取消不会消耗，快速连续点击只允许一次请求，网络结果不确定时也不会自动重试。

## 🔗 Links

- [GitHub Repository](https://github.com/WSL043/dsh-codex-subscription)
- [Full README](https://github.com/WSL043/dsh-codex-subscription#readme)
- [Back to the Plugins list](../plugins.md)
