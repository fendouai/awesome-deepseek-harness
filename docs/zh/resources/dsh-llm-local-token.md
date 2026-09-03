---
title: "dsh-llm-local-token"
description: "复用本机 Codex CLI 与 Claude Code OAuth 凭据的 DSH 模型提供方路由，无需另配 API Key。"
keywords: "dsh-llm-local-token, developer, plugin, security, observability, deepseek harness, dsh"
---
# dsh-llm-local-token

> ⭐ **0** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 0 | 状态 | ✅ 活跃 |
| 作者 | [tianxia--](https://github.com/tianxia--) | 更新时间 | 2026-08-17 |
| 子分类 | 💰 费用与统计 | 能力 | security, observability |

## 一句话介绍

> 复用本机 Codex CLI 与 Claude Code OAuth 凭据的 DSH 模型提供方路由，无需另配 API Key。

## 详细介绍

A [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) plugin that serves LLM calls with the OAuth tokens your **local CLIs already hold** — no separate API key, no extra login. If you are signed in to the Codex CLI or to Claude Code, those subscriptions become usable model routes inside DSH. Both routes appear in the model picker as soon as the plugin loads. A route whose credential is missing is skipped instead of failing the boot. The usage badge additionally reports a **GLM Coding Plan** subscription, which DSH already serves through pi-ai's own `zai-coding-cn` route — the plugin adds the quota, not a second route, so the model picker gains no duplicate. See [Subscription usage badge](#subscription-usage-badge). Both subscriptions as routes in the model picker Subscripti

## 📦 安装

```bash
dsh plugin --profile web add dsh-llm-local-token

# or straight from git
dsh plugin --profile web add https://github.com/tianxia--/dsh-llm-local-token.git
```

## 🚀 快速开始

```bash
- insert:
    - id: llm-local-token
      name: dsh-llm-local-token
```

## 📚 更多信息

**~/.dsh/settings.yaml**

agent-default-model: provider: openai-codex model: gpt-5.6-terra reasoningEffort: medium

**Subscription usage badge**

Codex and Claude state their quota in response headers, so reading it off a real request costs nothing. A route you never call has nothing to report, though — so the plugin also refreshes on a schedule, with one deliberately tiny request per provider (16 input tokens for Codex, 9 for Anthropic) that carries no prompt, skills, tools or history and is never stored. A badge appears in the composer ba

**`Provider is not configured: openai-codex`**

Means the pi-ai provider refused an API-key override. This plugin already attaches an api-key auth method to the OAuth-only Codex provider; seeing this error again implies a pi-ai version whose `resolveProviderAuth` changed — open an issue with your `@earendil-works/pi-ai` version.

## 🔗 链接

- [GitHub 仓库](https://github.com/tianxia--/dsh-llm-local-token)
- [完整 README](https://github.com/tianxia--/dsh-llm-local-token#readme)
- [返回dsh-llm-local-token所在分类](../plugins.md)
