---
title: "dsh-message-edit"
description: "Branch-based message editing, reroll, retry and version timeline."
keywords: "dsh-message-edit, developer, plugin, ui, context, deepseek harness, dsh"
---
# dsh-message-edit

> ⭐ **35** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 35 | Status | ✅ active |
| Author | [Moeblack](https://github.com/Moeblack) | Updated | 2026-08-16 |
| Subcategory | 🧪 Code, tests & review | Capabilities | ui, context |

## One-liner

> Branch-based message editing, reroll, retry and version timeline.

## About

`dsh-message-edit`（[npm](https://www.npmjs.com/package/dsh-message-edit) · [GitHub](https://github.com/Moeblack/dsh-message-edit)）为 DeepSeek Harness 补充基于事件溯源的「消息编辑与重生成」能力。插件不改写历史事件，也不修改 DSH 引擎内部；每次编辑、重生成或重试都会从目标回合之前创建一个新会话版本，原会话始终保留并可随时切回。 dsh plugin --profile web add dsh-message-edit

## ✨ Key Features

- **编辑消息**：可编辑已落定的用户文本、`assistant.reasoning` 思考块与 `assistant.response` 回复文本。
- **重生成**：从最后一条已落定助手回复所属回合之前分支，使用原用户输入重新生成。
- **重试任意回合**：在 Timeline 中选择任意历史回合重新执行。
- **级联策略**：
- **版本切换**：会话标题栏的 `←` 撤销当前原子效果，`→` 重施加最新直接子效果；Timeline 展示完整已知分支树、操作时间、编辑前后内容与当前版本。
- **Timeline 标签页**：注册到 `conversation.view`，`order: 15`，位于 Trajectory（10）与 Prompt Studio（20）之间。

## 📦 Install

```bash
dsh plugin --profile web add dsh-message-edit
```

## 🚀 Quick Start

```bash
npm install
npm run build
```

## 📚 Learn more

**安装**

dsh plugin --profile web add dsh-message-edit 或本地开发： dsh plugin --profile web add -w link:/path/to/dsh-message-edit `dsh plugin` 是 pnpm 转发器：`add` 后会自动识别 `dsh.bundle` 声明并把插件收编进 profile 的 `dsh.profile.bundles`，重启 dsh 即生效。本地开发建议用 `link:`（符号链接），改动源码重构建后重启即更新。

## 🔗 Links

- [GitHub Repository](https://github.com/Moeblack/dsh-message-edit)
- [Full README](https://github.com/Moeblack/dsh-message-edit#readme)
- [Back to the Plugins list](../plugins.md)
