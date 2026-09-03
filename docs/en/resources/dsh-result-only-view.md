---
title: "dsh-result-only-view"
description: "Results-only view toggle for the DSH Web GUI: folds thinking/tool-call process rows so conversations show only user messages and final replies; live summary chips for running steps, click-to-expand turn trace with hover-peek, auto/manual fold modes. / 「只看结果」开关：折叠思考与工具调用过程行，只留用户消息与最终回复；实时摘要芯片、回合痕迹行（点击展开/悬停预览）、自动/手动折叠。"
keywords: "dsh-result-only-view, ui, plugin, deepseek harness, dsh"
---
# dsh-result-only-view

> ⭐ **2** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 2 | Status | ✅ active |
| Author | [YEYEYEYESHIFU](https://github.com/YEYEYEYESHIFU) | Updated | — |
| Subcategory | 💡 Generative UI | Capabilities | ui |

## One-liner

> Results-only view toggle for the DSH Web GUI: folds thinking/tool-call process rows so conversations show only user messages and final replies; live summary chips for running steps, click-to-expand turn trace with hover-peek, auto/manual fold modes. / 「只看结果」开关：折叠思考与工具调用过程行，只留用户消息与最终回复；实时摘要芯片、回合痕迹行（点击展开/悬停预览）、自动/手动折叠。

## About

A **Results only** toggle for the DeepSeek Harness Web GUI. Turn it on and thinking, tool-call and context-injection rows fold away — only your messages and the final replies remain. Open any of them again whenever you want the details. - Default on; the state persists in `localStorage`. - **While the agent runs** — one compact chip per running step (tool name + args hint, or the latest thinking line). Click a chip to reveal and expand that step's native row mid-run. With no active step, a single live status line shows the latest one. - **After a turn settles** — a `Processed N steps · Xs ▸` trace appears at the turn tail: click to expand that turn's process rows; click again to fold them back. Moving the mouse across the line does nothing — expansion is strictly click-driven. - **Fold mod

## ✨ Key Features

- Default on; the state persists in `localStorage`.
- **While the agent runs** — one compact chip per running step (tool name + args hint, or the latest thinking line). Click a chip to reveal and expand that step's
- **After a turn settles** — a `Processed N steps · Xs ▸` trace appears at the turn tail: click to expand that turn's process rows; click again to fold them back.
- **Fold modes** — Auto folds settled turns for you; Manual keeps them visible until you fold them from the trace line.
- **Never hidden** — whitelisted interactive cards (`ask_user_question`, `cordis_run`) and composer approval prompts stay visible.
- Settings → General → Results only: show/hide the trace, restore animations under reduced motion, pick the fold mode. zh-CN/en localized.

## 📦 Install

```bash
dsh plugin --profile web add dsh-result-only-view
```

## 📚 Learn more

**Install**

dsh plugin --profile web add dsh-result-only-view Then restart `dsh web`. Uninstall with `dsh plugin --profile web remove dsh-result-only-view` + restart.

**安装**

dsh plugin --profile web add dsh-result-only-view 然后重启 `dsh web`。卸载用 `dsh plugin --profile web remove dsh-result-only-view` 再重启。

## 🔗 Links

- [GitHub Repository](https://github.com/YEYEYEYESHIFU/dsh-result-only-view)
- [Full README](https://github.com/YEYEYEYESHIFU/dsh-result-only-view#readme)
- [Back to the Plugins list](../plugins.md)
