---
title: "dsh-usage-dashboard"
description: "DeepSeek 额度与用量仪表盘 — DSH (DeepSeek Harness) 动态 Cordis 插件"
keywords: "dsh-usage-dashboard, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-usage-dashboard

> ⭐ **8** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 8 | Status | ✅ active |
| Author | [Cassius0924](https://github.com/Cassius0924) | Updated | 2026-08-19 |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> DeepSeek 额度与用量仪表盘 — DSH (DeepSeek Harness) 动态 Cordis 插件

## About

在 [DSH](https://github.com/deepseek-ai)（DeepSeek Harness）的 Web GUI 里，随时看得见 DeepSeek 的钱花在哪： **余额还能撑几天、今天花了多少、哪个模型最贵、缓存替你省了多少，以及 2026-08-17 峰谷定价之后账单会变成什么样。** 装上之后 GUI 里多两样东西：右下角一个可拖动的**悬浮额度窗**，顶部栏多一个**「额度」tab**。 界面支持中文与 English，直接跟随 DSH 全局的「Settings → Language」设置；切换无需刷新，选择由 DSH 持久化。 ---

## ✨ Key Features

- 余额 + **今日消耗**，一眼就够。
- 可拖动，松手自动吸附四角；边界避开侧边栏、右侧详情面板、会话顶栏和输入框——**不会挡住发送按钮**。
- 可收起成一行；**显示/隐藏、所在角落、收起状态都会记住**，刷新页面后原样回来。
- 余额跌破预警线时，状态点和余额数字一起转成警示色。
- 60 秒自动刷新余额。今日消耗读共享缓存，点 ↻ 同时刷新两者。
- 插件加载时就把余额和用量预取到缓存里，所以打开「额度」tab 通常是秒开，

## 📦 Install

```bash
# 从 npm 安装
dsh plugin --profile web add @cassius0924/dsh-usage-dashboard

# 或从 GitHub（git 依赖会跑 prepare 脚本现场构建）
dsh plugin --profile web add github:Cassius0924/dsh-usage-dashboard

# 或本地 checkout
dsh plugin --profile web add ./path/to/dsh-usage-dashboard
```

## 🚀 Quick Start

```bash
pnpm install
pnpm test           # Node 内置测试运行器：计价、缓存、信任围栏与用量聚合
pnpm run build      # esbuild 出 lib/index.js（host）+ lib/client.js（client），再 tsc 出类型
pnpm run typecheck
```

## 📚 Learn more

**dsh-usage-dashboard**

在 [DSH](https://github.com/deepseek-ai)（DeepSeek Harness）的 Web GUI 里，随时看得见 DeepSeek 的钱花在哪： **余额还能撑几天、今天花了多少、哪个模型最贵、缓存替你省了多少，以及 2026-08-17 峰谷定价之后账单会变成什么样。** 装上之后 GUI 里多两样东西：右下角一个可拖动的**悬浮额度窗**，顶部栏多一个**「额度」tab**。 界面支持中文与 English，直接跟随 DSH 全局的「Settings → Language」设置；切换无需刷新，选择由 DSH 持久化。 ---

## 🔗 Links

- [GitHub Repository](https://github.com/Cassius0924/dsh-usage-dashboard)
- [Full README](https://github.com/Cassius0924/dsh-usage-dashboard#readme)
- [Back to the Plugins list](../plugins.md)
