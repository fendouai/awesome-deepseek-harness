---
title: "dsh-plugin-choice-refresh"
description: "DSH 选择增强插件：「重新生成选项」/「更多选项」按钮。Choice refresh (regenerate / more options) for DeepSeek Harness (dsh)."
keywords: "dsh-plugin-choice-refresh, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-plugin-choice-refresh

> ⭐ **2** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 2 | Status | ✅ active |
| Author | [Pasumao](https://github.com/Pasumao) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> DSH 选择增强插件：「重新生成选项」/「更多选项」按钮。Choice refresh (regenerate / more options) for DeepSeek Harness (dsh).

## About

[**中文**](./README.md) | [English](./README.en.md) **dsh 插件市场里唯一的选择增强插件**：给 `ask_user_question` / `ask_user_choice` 的选择卡加上两个按钮—— 选项都不满意？一键让模型换一批完全不同的。选项太少？一键让模型补充。 纯前端交互实现，**不注册新工具、不改核心包**；对原生文字选项和 [dsh-plugin-image-tools](https://github.com/Pasumao/dsh-plugin-image-tools) 的 图片选项卡都生效（图片卡由本插件直接渲染，复用其图片路由）。

## ✨ Key Features

- 🔄 **重新生成选项**：`ask_user_question` / `ask_user_choice` 给出的选项都不满意时，
- ➕ **更多选项**：选项太少不够选时，一键让模型在保留原选项的基础上补充新选项（总数 6~10 个）；
- 纯前端交互实现，**不注册新工具、不改核心包**；
- 对原生文字选项卡与 `dsh-plugin-image-tools` 图片选项卡同时生效；
- 与 `plan-review` 计划审阅卡兼容，不影响原生流程。

## 📦 Install

```bash
# npm（推荐）
dsh plugin --profile web add dsh-plugin-choice-refresh
# 或 GitHub
dsh plugin --profile web add github:Pasumao/dsh-plugin-choice-refresh
```

## 🚀 Quick Start

```bash
git clone https://github.com/Pasumao/dsh-plugin-choice-refresh.git
cd dsh-plugin-choice-refresh
npm install        # 或 pnpm install
# 以 link: 方式挂载进 profile，详见 设计说明.md
```

## 📚 Learn more

**以 link: 方式挂载进 profile，详见 设计说明.md**

装完刷新浏览器即生效（profile 已有 dsh-client-hmr 时会自动热更新，无需重启）。 本地开发可改用 `link:` 方式挂载，详见 `设计说明.md`。

**使用**

模型（或按 novel-* 技能等）照常调用 `ask_user_question` / `ask_user_choice` 提问时，选择卡底部会多出「重新生成选项」和「更多选项」两个按钮： `【系统 · 选项刷新】` 用户消息，模型立即换一组选项重新提问； > 注入消息保持简短（一两行），作为用户消息留在会话里供模型理解指令； > 界面会原样显示这条消息。 > 说明：刷新/补充由模型理解指令后重新调用提问工具完成，属于「软」增强—— > 模型偶尔可能调整问题本身。若对结果仍不满意，可再点一次或直接打字说明。

## 🔗 Links

- [GitHub Repository](https://github.com/Pasumao/dsh-plugin-choice-refresh)
- [Full README](https://github.com/Pasumao/dsh-plugin-choice-refresh#readme)
- [Back to the Plugins list](../plugins.md)
