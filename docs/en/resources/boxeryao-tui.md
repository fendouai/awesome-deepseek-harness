---
title: "deepseek-harness-tui (boxeryao)"
description: "Lightweight fast terminal plugin connected directly to the DSH runtime."
keywords: "deepseek-harness-tui (boxeryao), terminal, client, deepseek harness, dsh"
---
# deepseek-harness-tui (boxeryao)

> ⭐ **10** · ✅ active · client · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | client | Category | Terminal |
| Stars | ⭐ 10 | Status | ✅ active |
| Author | [boxeryao](https://github.com/boxeryao) | Updated | 2026-08-16 |

## One-liner

> Lightweight fast terminal plugin connected directly to the DSH runtime.

## About

[English](README.en.md) | 中文 [DeepSeek Harness（DSH）](https://github.com/deepseek-ai/deepseek-harness) 的极简终端 UI 插件。它保留完整的 Agent 与工具能力，但默认把执行过程收进后台，让终端专注于你的输入和模型的最终回答。 界面、npm 包与 GitHub 仓库统一命名为 **DSH Mini TUI** / [`dsh-mini-tui`](https://github.com/boxeryao/dsh-mini-tui)：`Mini` 指更少的界面噪声，而不是更少的 Harness 能力。中文也可以昵称为 **“单身汉 Mini TUI”**，取自 DSH 的谐音。

## ✨ Key Features

- **轻量** — 专注于终端展示层，不携带 Web 应用运行时。
- **快捷** — 多行输入响应迅速，键盘控制直接，工具活动默认不打断对话流。
- **深海视觉** — 启动仪表盘、状态标签、路径引用和思考状态使用统一的低反差深海色系。
- **原生衔接 DSH** — 直接使用 DSH 的 scoped 工具、审批、Agent 生命周期和持久化 Session 日志。

## 📦 Install

```bash
dsh plugin --profile tui add dsh-mini-tui@latest
dsh --profile tui
```

## 🚀 Quick Start

```bash
& "$HOME\.dsh\profiles\tui\node_modules\dsh-mini-tui\scripts\install-dsh-tui-context-menu.cmd"
```

## 📚 Learn more

**快速安装**

从 npm 将最新版 DSH Mini TUI 安装到 DSH 的 `tui` profile： dsh plugin --profile tui add dsh-mini-tui@latest dsh --profile tui > 注意：npm 上的 `deepseek-harness-tui` 属于另一个项目。本项目的正确包名是 `dsh-mini-tui`。

## 🔗 Links

- [GitHub Repository](https://github.com/boxeryao/deepseek-harness-tui)
- [Full README](https://github.com/boxeryao/deepseek-harness-tui#readme)
- [Back to the Clients (Desktop & TUI) list](../clients.md)
