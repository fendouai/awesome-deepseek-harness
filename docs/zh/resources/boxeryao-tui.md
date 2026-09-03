---
title: "deepseek-harness-tui (boxeryao)"
description: "轻量快速终端插件，直连 DSH 运行时。"
keywords: "deepseek-harness-tui (boxeryao), terminal, client, deepseek harness, dsh"
---
# deepseek-harness-tui (boxeryao)

> ⭐ **10** · ✅ 活跃 · 客户端 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 客户端 | 分类 | 终端 |
| 星数 | ⭐ 10 | 状态 | ✅ 活跃 |
| 作者 | [boxeryao](https://github.com/boxeryao) | 更新时间 | 2026-08-16 |

## 一句话介绍

> 轻量快速终端插件，直连 DSH 运行时。

## 详细介绍

[English](README.en.md) | 中文 [DeepSeek Harness（DSH）](https://github.com/deepseek-ai/deepseek-harness) 的极简终端 UI 插件。它保留完整的 Agent 与工具能力，但默认把执行过程收进后台，让终端专注于你的输入和模型的最终回答。 界面、npm 包与 GitHub 仓库统一命名为 **DSH Mini TUI** / [`dsh-mini-tui`](https://github.com/boxeryao/dsh-mini-tui)：`Mini` 指更少的界面噪声，而不是更少的 Harness 能力。中文也可以昵称为 **“单身汉 Mini TUI”**，取自 DSH 的谐音。

## ✨ 核心特性

- **轻量** — 专注于终端展示层，不携带 Web 应用运行时。
- **快捷** — 多行输入响应迅速，键盘控制直接，工具活动默认不打断对话流。
- **深海视觉** — 启动仪表盘、状态标签、路径引用和思考状态使用统一的低反差深海色系。
- **原生衔接 DSH** — 直接使用 DSH 的 scoped 工具、审批、Agent 生命周期和持久化 Session 日志。

## 📦 安装

```bash
dsh plugin --profile tui add dsh-mini-tui@latest
dsh --profile tui
```

## 🚀 快速开始

```bash
& "$HOME\.dsh\profiles\tui\node_modules\dsh-mini-tui\scripts\install-dsh-tui-context-menu.cmd"
```

## 📚 更多信息

**快速安装**

从 npm 将最新版 DSH Mini TUI 安装到 DSH 的 `tui` profile： dsh plugin --profile tui add dsh-mini-tui@latest dsh --profile tui > 注意：npm 上的 `deepseek-harness-tui` 属于另一个项目。本项目的正确包名是 `dsh-mini-tui`。

## 🔗 链接

- [GitHub 仓库](https://github.com/boxeryao/deepseek-harness-tui)
- [完整 README](https://github.com/boxeryao/deepseek-harness-tui#readme)
- [返回deepseek-harness-tui (boxeryao)所在分类](../clients.md)
