---
title: "dsh-result-only-view"
description: "「只看结果」开关：折叠思考与工具调用过程行，对话只留用户消息与最终回复；运行中显示实时摘要芯片，回合后痕迹行可点击展开并支持悬停预览，自动/手动折叠模式。"
keywords: "dsh-result-only-view, ui, plugin, deepseek harness, dsh"
---
# dsh-result-only-view

> ⭐ **2** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 2 | 状态 | ✅ 活跃 |
| 作者 | [YEYEYEYESHIFU](https://github.com/YEYEYEYESHIFU) | 更新时间 | — |
| 子分类 | 💡 生成式界面 | 能力 | ui |

## 一句话介绍

> 「只看结果」开关：折叠思考与工具调用过程行，对话只留用户消息与最终回复；运行中显示实时摘要芯片，回合后痕迹行可点击展开并支持悬停预览，自动/手动折叠模式。

## 详细介绍

A **Results only** toggle for the DeepSeek Harness Web GUI. Turn it on and thinking, tool-call and context-injection rows fold away — only your messages and the final replies remain. Open any of them again whenever you want the details. - Default on; the state persists in `localStorage`. - **While the agent runs** — one compact chip per running step (tool name + args hint, or the latest thinking line). Click a chip to reveal and expand that step's native row mid-run. With no active step, a single live status line shows the latest one. - **After a turn settles** — a `Processed N steps · Xs ▸` trace appears at the turn tail: click to expand that turn's process rows; click again to fold them back. Moving the mouse across the line does nothing — expansion is strictly click-driven. - **Fold mod

## ✨ 核心特性

- Default on; the state persists in `localStorage`.
- **While the agent runs** — one compact chip per running step (tool name + args hint, or the latest thinking line). Click a chip to reveal and expand that step's
- **After a turn settles** — a `Processed N steps · Xs ▸` trace appears at the turn tail: click to expand that turn's process rows; click again to fold them back.
- **Fold modes** — Auto folds settled turns for you; Manual keeps them visible until you fold them from the trace line.
- **Never hidden** — whitelisted interactive cards (`ask_user_question`, `cordis_run`) and composer approval prompts stay visible.
- Settings → General → Results only: show/hide the trace, restore animations under reduced motion, pick the fold mode. zh-CN/en localized.

## 📦 安装

```bash
dsh plugin --profile web add dsh-result-only-view
```

## 📚 更多信息

**Install**

dsh plugin --profile web add dsh-result-only-view Then restart `dsh web`. Uninstall with `dsh plugin --profile web remove dsh-result-only-view` + restart.

**安装**

dsh plugin --profile web add dsh-result-only-view 然后重启 `dsh web`。卸载用 `dsh plugin --profile web remove dsh-result-only-view` 再重启。

## 🔗 链接

- [GitHub 仓库](https://github.com/YEYEYEYESHIFU/dsh-result-only-view)
- [完整 README](https://github.com/YEYEYEYESHIFU/dsh-result-only-view#readme)
- [返回dsh-result-only-view所在分类](../plugins.md)
