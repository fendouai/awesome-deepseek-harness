---
title: "dsh-bell-notify"
description: "Configurable, unobtrusive Web Audio lifecycle notifications for DeepSeek Harness (dsh): 10 events, custom sounds, offline playback."
keywords: "dsh-bell-notify, search, plugin, coding, deepseek harness, dsh"
---
# dsh-bell-notify

> ⭐ **4** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 4 | Status | ✅ active |
| Author | [Laplace-bit](https://github.com/Laplace-bit) | Updated | — |
| Subcategory | 🌐 Web search | Capabilities | coding |

## One-liner

> Configurable, unobtrusive Web Audio lifecycle notifications for DeepSeek Harness (dsh): 10 events, custom sounds, offline playback.

## About

[中文](./README.md) · [English](./README.en.md) **dsh-bell-notify** 是 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)（`dsh`）的社区插件。它把关键 Agent 生命周期事件变成可配置的声音提示，让你在不盯着页面时仍能掌握进度。 所有铃声均由 Web Audio 实时合成，不携带音频资源。配置集中在 **设置 → 插件 → 插件配置 → 铃声通知**：不再提供工作区悬浮面板或右下角状态点，避免占用会话界面。

## 📦 Install

```bash
pnpm dsh plugin --profile bell add dsh-bell-notify
```

## 🚀 Quick Start

```bash
dsh plugin --profile bell add dsh-bell-notify
```

## 📚 Learn more

**安装**

从 DeepSeek Harness 源码仓库里： pnpm dsh plugin --profile bell add dsh-bell-notify 如果 `PATH` 上已经有 `dsh`： dsh plugin --profile bell add dsh-bell-notify > npm 包带预构建产物，无需 pnpm ≥10 的构建脚本授权，直接可装。 启动： pnpm dsh --profile bell 打开页面后**先点一下页面任意位置**（浏览器的音频自动播放策略，点一次即可解锁声音），然后在 **设置 → 插件 → 插件配置 → 铃声通知** 中按需要调整事件。 卸载： pnpm dsh plugin --profile bell remove dsh-bell-notify

**配置**

常规运行参数仍可在 profile 的 `cordis.patch.yml` 中调整（Cordis 加载时会校验并补默认值）： maxQueue: 8 # 等待队列容量 maxConcurrent: 3 # 同时播放的声音数（1 = 串行，值越大越能重叠） defaultCooldown: 1000 # 规则默认节流窗口（毫秒） 在 **设置 → 插件 → 插件配置 → 铃声通知** 中： 旧版的右下角状态点和浮层设置已移除；现有配置都在插件配置卡中完成。

## 🔗 Links

- [GitHub Repository](https://github.com/Laplace-bit/dsh-bell-notify)
- [Full README](https://github.com/Laplace-bit/dsh-bell-notify#readme)
- [Back to the Plugins list](../plugins.md)
