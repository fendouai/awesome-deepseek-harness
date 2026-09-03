---
title: "dsh-pi-tui"
description: "A third-party TUI mode for DeepSeek Harness (dsh), built on a vendored fork of pi-tui"
keywords: "dsh-pi-tui, terminal, client, coding, ui, deepseek harness, dsh"
---
# dsh-pi-tui

> ⭐ **16** · ✅ active · client

| | | | |
|---|---|---|---|
| Type | client | Category | Terminal |
| Stars | ⭐ 16 | Status | ✅ active |
| Author | [XMoon](https://github.com/XMoon) | Updated | — |

## One-liner

> A third-party TUI mode for DeepSeek Harness (dsh), built on a vendored fork of pi-tui

## About

[pi 的 TUI](https://github.com/earendil-works/pi/tree/main/packages/tui)（`@earendil-works/pi-tui`）驱动的 DeepSeek Harness 终端前端：界面是 pi 的观感（品牌蓝 prompt、流式 Markdown、thinking 折叠、工具调用卡片、微分渲染防闪烁），内核（模型路由、工具、会话持久化、slash 命令、审批）全部由 dsh 官方机制提供。

## ✨ Key Features

- 流式渲染：`assistant/chunk` 增量 → Markdown、thinking 折叠标签
- 工具调用卡片：运行/成功/失败三态 + 参数与结果预览；Ctrl+O 展开完整输出；write/edit 结果带**彩色 diff 高亮**（官方 meta.diffs）
- `read_image` 结果在 kitty/iTerm2 终端内联渲染图片（Ctrl+O 展开）
- slash 命令：`/compact` `/goal` `/plan` `/feedback` 等全部来自官方 `ctx.commands` 注册表（自动补全 + 动态发现）
- 权限审批弹窗（`approval/request`）与 `ask_user_question` 交互表单（选项/多选/自由文本；plan-review 特化弹窗）
- 会话管理：创建、恢复、fork、子代理树、选择器（官方持久化后端；resume 选择器显示官方自动标题）
- 转录搜索：`Ctrl+F` 在 transcript 内搜索并跳转（输入即定位 + 高亮，↑/↓ 循环）；`/retry` 一键重发失败 turn；`/copy` 复制 assistant/工具结果/错误/id/resume 命令（OSC 52 三路剪贴板）
- 长会话折叠：消息超过阈值自动折叠旧消息（`/expand-all` 展开）

## 📦 Install

```bash
dsh plugin --profile pi-tui add dsh-pi-tui   # 自动初始化 profile 并挂为 bundle
dsh --profile pi-tui                          # 新会话
dsh --profile pi-tui --resume <session-id>    # 恢复指定会话
dsh --profile pi-tui --resume                 # 从持久化会话列表中选择
dsh --profile pi-tui --preset <id>            # 选择 agent preset（standard/minimal/code）
dsh --profile pi-tui --preset                 # 从 preset 列表中选择
```

## 🚀 Quick Start

```bash
npm install && npm run build && npm test
# 本地联调：profile 里是 link: 软链，重新 build 后直接重启即可
```

## 📚 Learn more

**安装**

前置：官方 [`dsh`](https://github.com/deepseek-ai/deepseek-harness) CLI（`npm i -g @deepseek-ai/dsh`）与 `pnpm`。 dsh plugin --profile pi-tui add dsh-pi-tui # 自动初始化 profile 并挂为 bundle dsh --profile pi-tui # 新会话 dsh --profile pi-tui --resume <session-id> # 恢复指定会话 dsh --profile pi-tui --resume # 从持久化会话列表中选择 dsh --profile pi-tui --preset <id> # 选择 agent preset（standard/minimal/code） dsh --profile pi-tui --pre

## 🔗 Links

- [GitHub Repository](https://github.com/XMoon/dsh-pi-tui)
- [Full README](https://github.com/XMoon/dsh-pi-tui#readme)
- [Back to the Clients (Desktop & TUI) list](../clients.md)
