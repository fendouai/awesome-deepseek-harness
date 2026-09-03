---
title: "dsh-reasoning-settings"
description: "让 DeepSeek Harness 的第三方 API 支持低、中、高等推理强度，并可为每次子 Agent 调用选择模型｜Add Low, Medium, High, and other reasoning levels to third-party APIs, with model selection for each subagent call"
keywords: "dsh-reasoning-settings, multi-agent, agent, coding, deepseek harness, dsh"
---
# dsh-reasoning-settings

> ⭐ **6** · ✅ 活跃 · 智能体

| | | | |
|---|---|---|---|
| 类型 | 智能体 | 分类 | 多智能体 |
| 星数 | ⭐ 6 | 状态 | ✅ 活跃 |
| 作者 | [JuneLearn](https://github.com/JuneLearn) | 更新时间 | — |

## 一句话介绍

> 让 DeepSeek Harness 的第三方 API 支持低、中、高等推理强度，并可为每次子 Agent 调用选择模型｜Add Low, Medium, High, and other reasoning levels to third-party APIs, with model selection for each subagent call

## 详细介绍

A [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) Web settings plugin that adds an independent **reasoning effort** (thinking intensity) page for custom `llm-pi-ai` providers. The official UI only exposes effort selection for first-party DeepSeek models; this plugin makes it work for third-party / relay APIs too. [中文说明](./README.zh-CN.md)

## ✨ 核心特性

- Auto-reads the custom providers and models you already added on the official **Models** page.
- Declares a per-model effort level from `off / minimal / low / medium / high / xhigh / max`.
- Customizes the actual wire value sent to the API for each level.
- Sets a provider-wide default effort, restricted to the levels supported by every model in that provider.
- Configures the reasoning wire format for `openai-completions` providers.
- Writes back to `llm-pi-ai.providers.*` through the official `settings.mutate` API — API keys are never touched.
- Fixes in-process subagents inheriting the Agent's create-time official model instead of the parent's live third-party provider/model selection.
- Makes subagents inherit an explicit parent reasoning effort, or fall back to the target provider's configured default effort.

## 📦 安装

```bash
npx --yes -p @deepseek-ai/dsh dsh plugin --profile web add github:JuneLearn/dsh-reasoning-settings
```

## 🚀 快速开始

```bash
npx --yes -p @deepseek-ai/dsh dsh web
```

## 📚 更多信息

**DSH Reasoning Settings**

A [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) Web settings plugin that adds an independent **reasoning effort** (thinking intensity) page for custom `llm-pi-ai` providers. The official UI only exposes effort selection for first-party DeepSeek models; this plugin makes it work for third-party / relay APIs too. [中文说明](./README.zh-CN.md) > **Third-party service recommendation 

**Uninstall**

npx method: npx --yes -p @deepseek-ai/dsh dsh plugin --profile web remove dsh-reasoning-settings pnpm source method: cd D:\deepseek-harness pnpm dsh plugin --profile web remove dsh-reasoning-settings DSH removes both the dependency and its bundle layer. Restart `dsh web`; the **Reasoning effort** settings page is removed.

**Usage**

1. Add your custom provider and models on the official **Models** page first. 2. Open **Settings > Reasoning effort**. 3. Pick the supported levels for each model and set the provider default effort. 4. Click **Save** under that provider. 5. Start a new session and choose the model and reasoning effort in the model picker. The plugin only declares which effort levels Harness may select and send. W

## 🔗 链接

- [GitHub 仓库](https://github.com/JuneLearn/dsh-reasoning-settings)
- [完整 README](https://github.com/JuneLearn/dsh-reasoning-settings#readme)
- [返回dsh-reasoning-settings所在分类](../agents.md)
