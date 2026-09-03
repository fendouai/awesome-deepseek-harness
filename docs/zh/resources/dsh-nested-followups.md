---
title: "dsh-nested-followups"
description: "Ask a follow-up on any past answer in an isolated branch, keeping your main conversation clean. 针对任意历史回答发起追问，新问题在独立分支中展开，主对话保持干净。A conversation-tree plugin for DeepSeek Harness / DeepSeek Harness 会话树插件。"
keywords: "dsh-nested-followups, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-nested-followups

> ⭐ **13** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 13 | 状态 | ✅ 活跃 |
| 作者 | [sluminositys](https://github.com/sluminositys) | 更新时间 | 2026-08-19 |
| 子分类 | 👁️ 视觉工具 | 能力 | coding |

## 一句话介绍

> Ask a follow-up on any past answer in an isolated branch, keeping your main conversation clean. 针对任意历史回答发起追问，新问题在独立分支中展开，主对话保持干净。A conversation-tree plugin for DeepSeek Harness / DeepSeek Harness 会话树插件。

## 详细介绍

**Branch from any answer. Keep branching at any depth.** A [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) plugin for isolated follow-ups that can keep branching recursively, with no plugin-defined depth limit. Start a side trail from any answer, then turn any answer anywhere in that trail into the next isolated fork point. Repeat for as many levels as the question needs. Every level inherits only its ancestor path, while the main task stays linear and untouched. _Recorded in an unmodified DeepSeek Harness `0.1.1-rc.2` web profile. The UI and sessions are real; the captions and cursor are added in post._ - **Start a side trail anywhere.** The first branch receives exactly the history that existed at the selected answer. - **Keep branching at any depth.** Every answer in

## ✨ 核心特性

- **Start a side trail anywhere.** The first branch receives exactly the history
- **Keep branching at any depth.** Every answer in every side trail can become
- **Keep the main task clean.** Nothing asked or answered in a branch flows back

## 📦 安装

```bash
dsh plugin --profile web add dsh-nested-followups
```

## 🚀 快速开始

```bash
git clone https://github.com/sluminositys/dsh-nested-followups.git
cd dsh-nested-followups
pnpm install
pnpm run check
dsh plugin --profile web add .
```

## 📚 更多信息

**Install**

dsh plugin --profile web add dsh-nested-followups Restart the DeepSeek Harness web profile if it is already running, open a conversation, and select **Tree View**. <details> <summary>Install from source</summary> git clone https://github.com/sluminositys/dsh-nested-followups.git cd dsh-nested-followups pnpm install pnpm run check dsh plugin --profile web add . </details>

**Uninstall**

dsh plugin --profile web remove dsh-nested-followups Uninstalling removes the plugin UI and services. It does not modify the main conversation or delete persisted branch history.

## 🔗 链接

- [GitHub 仓库](https://github.com/sluminositys/dsh-nested-followups)
- [完整 README](https://github.com/sluminositys/dsh-nested-followups#readme)
- [返回dsh-nested-followups所在分类](../plugins.md)
