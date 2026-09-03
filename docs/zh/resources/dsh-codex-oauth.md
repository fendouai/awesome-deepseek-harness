---
title: "dsh-codex-oauth"
description: "Use your OpenAI subscription with DeepSeek Harness to access GPT models, image generation, and web search."
keywords: "dsh-codex-oauth, search, plugin, coding, multimodal, deepseek harness, dsh"
---
# dsh-codex-oauth

> ⭐ **15** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 搜索与研究 |
| 星数 | ⭐ 15 | 状态 | ✅ 活跃 |
| 作者 | [WNJXYK](https://github.com/WNJXYK) | 更新时间 | — |
| 子分类 | 🌐 网页搜索 | 能力 | coding, multimodal, search |

## 一句话介绍

> Use your OpenAI subscription with DeepSeek Harness to access GPT models, image generation, and web search.

## 详细介绍

- **🚀 Direct subscription access** — GPT models, image generation, and web search share your OpenAI subscription quota. - **🧩 Controlled integration** — the model picker, generated images, and web search integrate into DeepSeek Harness with dedicated controls. - **🔐 Multiple sign-in methods** — supports browser sign-in and headless device-code authorization. - **🌗 UI adaptation** — follows DSH's English/Chinese language and Light, Dark, or System theme.

## ✨ 核心特性

- **🚀 Direct subscription access** — GPT models, image generation, and web search share your OpenAI subscription quota.
- **🧩 Controlled integration** — the model picker, generated images, and web search integrate into DeepSeek Harness with dedicated controls.
- **🔐 Multiple sign-in methods** — supports browser sign-in and headless device-code authorization.
- **🌗 UI adaptation** — follows DSH's English/Chinese language and Light, Dark, or System theme.

## 📦 安装

```bash
dsh plugin --profile web add -w @wnjxyk/dsh-codex-oauth@latest
```

## 🚀 快速开始

```bash
dsh plugin --profile web add -w github:WNJXYK/dsh-codex-oauth
```

## 📚 更多信息

**🗑️ Uninstall**

npm and GitHub installations use the same removal command: dsh plugin --profile web remove -w @wnjxyk/dsh-codex-oauth

**⚙️ Detailed configuration**

No configuration is normally required. Available options are: Example Cordis configuration: - id: dsh-codex-oauth name: "@wnjxyk/dsh-codex-oauth" config: dshHome: /data/dsh path: /secure/codex-oauth.json preferencesPath: /secure/codex-oauth-preferences.json issuer: https://auth.openai.com usageUrl: https://chatgpt.com/backend-api/wham/usage controlPort: 1456 redirectPort: 1455 - id: codex-web-sear

## 🔗 链接

- [GitHub 仓库](https://github.com/WNJXYK/dsh-codex-oauth)
- [完整 README](https://github.com/WNJXYK/dsh-codex-oauth#readme)
- [返回dsh-codex-oauth所在分类](../plugins.md)
