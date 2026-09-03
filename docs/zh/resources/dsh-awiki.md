---
title: "dsh-awiki"
description: "AWiki identity and messaging plugin for DeepSeek Harness"
keywords: "dsh-awiki, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-awiki

> ⭐ **9** · ✅ 活跃 · 插件 · 近期 ⬆️ +2

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 9 | 状态 | ✅ 活跃 |
| 作者 | [AgentConnect](https://github.com/AgentConnect) | 更新时间 | 2026-08-21 |
| 子分类 | 👁️ 视觉工具 | 能力 | coding |

## 一句话介绍

> AWiki identity and messaging plugin for DeepSeek Harness

## 详细介绍

AWiki identity and messaging for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness). The package installs one Host service, its production Rust SDK provider, the model tools, and a Web client with a draggable AWiki Me launcher. [中文说明](./README.zh.md) Identity-entry failures preserve the currently mounted form and local pending identity material. The phone and OTP never enter browser persistence, controller snapshots, or public Remote results. Closed registration, unavailable verification state, and commit conflicts each give a safe next action without exposing remote response details. The Rust SDK exclusively owns the identity, SecretVault, database, cache, and metadata below the configured `stateRoot`. This release performs a clean cutover and does not import the former T

## ✨ 核心特性

- Enter a Handle and phone through one Web UI flow. Before any code is sent, the Host classifies the Handle: a new Handle receives a registration OTP and creates 
- Open the top-left AWiki account menu to sign out locally without deleting the encrypted identity or message database; **Resume local identity** restores the sam
- Reuse that identity across the root Agent and its subagents.
- Direct-message and existing-group conversation lists, unread counts, latest-message previews, and persisted display names. Core SQLite remains the persistent so
- Create a private-discovery, open-join, transport-protected group from the Web UI with a name and 1–50 initial Handle or DID members. The group opens immediately
- Text messages plus one attachment per message, with Enter-to-send, Shift+Enter line breaks, optimistic sending bubbles reconciled by an exact client message ID,
- A draggable circular launcher that defaults to the lower-left sidebar area, adaptive popup placement, dark mode, and remembered active conversation.
- User-triggered AI summaries for up to 50 recent or unread messages, kept only in runtime memory with explicit stale, retry, copy, and source-navigation states.

## 📦 安装

```bash
dsh plugin --profile web add @awiki/dsh-plugin@latest
```

## 🚀 快速开始

```bash
dsh plugin --profile web add @awiki/dsh-model-proxy@latest
```

## 📚 更多信息

**Install**

Install the official public npm package: dsh plugin --profile web add @awiki/dsh-plugin@latest The main package no longer installs the AWiki-hosted model provider. Add the independently versioned Model Proxy package only when that capability is wanted: dsh plugin --profile web add @awiki/dsh-model-proxy@latest The profile installer both adds the package and activates its bundle layer. A plain `npm

**Configuration**

The plugin works against the public `awiki.ai` tenant without environment configuration. Set these variables only when a deployment needs an override: The default state directory is isolated by DSH profile. Desktop uses the Host's `desktopProfiles.current.name`; ordinary `dsh --profile` accepts the name only when the Loader root exactly matches `$DSH_HOME/profiles/<name>`. The plugin does not gues

## 🔗 链接

- [GitHub 仓库](https://github.com/AgentConnect/dsh-awiki)
- [完整 README](https://github.com/AgentConnect/dsh-awiki#readme)
- [返回dsh-awiki所在分类](../plugins.md)
