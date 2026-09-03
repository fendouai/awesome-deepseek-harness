---
title: "dsh-everything-oauth"
description: "Import local Codex / Grok / Claude / OpenCode / CC Switch logins into DeepSeek Harness"
keywords: "dsh-everything-oauth, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-everything-oauth

> ⭐ **3** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 3 | 状态 | ✅ 活跃 |
| 作者 | [kam74515-boop](https://github.com/kam74515-boop) | 更新时间 | — |
| 子分类 | 👁️ 视觉工具 | 能力 | coding |

## 一句话介绍

> Import local Codex / Grok / Claude / OpenCode / CC Switch logins into DeepSeek Harness

## 详细介绍

Import local coding-platform logins into [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) without signing in again. Scans the same places [CC Switch](https://github.com/farion1231/cc-switch) cares about: Official routes: `claude-oauth`, `codex-oauth`, `grok-oauth`, `gemini-oauth`, `copilot-oauth`. CC Switch gateways become `everything-*` custom routes (Anthropic-compatible or OpenAI-compatible).

## 📦 安装

```bash
dsh plugin --profile web add github:kam74515-boop/dsh-everything-oauth
dsh web
```

## 🚀 快速开始

```bash
dsh plugin --profile web exec dsh-everything-oauth status
dsh plugin --profile web exec dsh-everything-oauth import live:codex-auth live:grok-auth
```

## 📚 更多信息

**Install**

dsh plugin --profile web add github:kam74515-boop/dsh-everything-oauth dsh web Then **Settings → Everything OAuth**: 1. **Sources** — select local logins / keys 2. **Imported** — enable only the models you want in the picker CLI: dsh plugin --profile web exec dsh-everything-oauth status dsh plugin --profile web exec dsh-everything-oauth import live:codex-auth live:grok-auth Source files are read-o

## 🔗 链接

- [GitHub 仓库](https://github.com/kam74515-boop/dsh-everything-oauth)
- [完整 README](https://github.com/kam74515-boop/dsh-everything-oauth#readme)
- [返回dsh-everything-oauth所在分类](../plugins.md)
