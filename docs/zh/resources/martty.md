---
title: "Martty"
description: "面向 DeepSeek Harness 的 Rust/ratatui Agent TUI，支持流式工具调用、子代理、持久会话和可扩展的 Cordis 客户端界面（deepseek-harness-tui 的继任者）。"
keywords: "Martty, terminal, client, ui, multi-agent, deepseek harness, dsh"
---
# Martty

> ⭐ **66** · ✅ 活跃 · 客户端

| | | | |
|---|---|---|---|
| 类型 | 客户端 | 分类 | 终端 |
| 星数 | ⭐ 66 | 状态 | ✅ 活跃 |
| 作者 | [openma-ai](https://github.com/openma-ai) | 更新时间 | — |

## 一句话介绍

> 面向 DeepSeek Harness 的 Rust/ratatui Agent TUI，支持流式工具调用、子代理、持久会话和可扩展的 Cordis 客户端界面（deepseek-harness-tui 的继任者）。

## 详细介绍

全局安装后直接启动： npm install --global martty martty 不想安装到全局，可以直接运行： npx --yes martty Martty 内置 ACP 连接层，默认启动并连接 DSH。已有 DSH 环境时，也可以把 Martty 安装到独立 profile，交给 DSH 管理插件和升级： npm install --global @deepseek-ai/dsh dsh plugin --profile martty add martty@latest dsh --profile martty 只想看界面，可以运行： martty --demo martty --demo-skin

## 📦 安装

```bash
npm install --global martty
martty
```

## 🚀 快速开始

```bash
npx --yes martty
```

## 🔗 链接

- [GitHub 仓库](https://github.com/openma-ai/Martty)
- [完整 README](https://github.com/openma-ai/Martty#readme)
- [返回Martty所在分类](../clients.md)
