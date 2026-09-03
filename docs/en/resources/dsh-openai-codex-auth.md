---
title: "dsh-openai-codex-auth"
description: "OpenAI Codex OAuth login and usage card plugin for DeepSeek Harness"
keywords: "dsh-openai-codex-auth, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-openai-codex-auth

> ⭐ **12** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 12 | Status | ✅ active |
| Author | [yoke233](https://github.com/yoke233) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> OpenAI Codex OAuth login and usage card plugin for DeepSeek Harness

## About

将插件安装到 DSH 的 `web` profile： dsh plugin --profile web add github:yoke233/dsh-openai-codex-auth 启动或重启该 profile： dsh --profile web 然后完成首次连接： 1. 打开 DSH Web，进入 **设置 → OpenAI Codex**。 2. 点击 **登录 OpenAI**，在弹出的 OpenAI 官方授权页完成登录。 3. 返回 DSH，在 **设置 → 模型提供方** 中选择 `openai-codex`。

## 📦 Install

```bash
dsh plugin --profile web add github:yoke233/dsh-openai-codex-auth
```

## 🚀 Quick Start

```bash
dsh --profile web
```

## 📚 Learn more

**配置**

插件通常无需额外配置。默认凭据文件为： $DSH_HOME/openai-codex-auth.json 如需改变存储位置，可在 Cordis 配置中设置 `path`： - id: openai-codex-auth name: dsh-openai-codex-auth config: path: /secure/path/openai-codex-auth.json `path` 的优先级高于 `dshHome`。

## 🔗 Links

- [GitHub Repository](https://github.com/yoke233/dsh-openai-codex-auth)
- [Full README](https://github.com/yoke233/dsh-openai-codex-auth#readme)
- [Back to the Plugins list](../plugins.md)
