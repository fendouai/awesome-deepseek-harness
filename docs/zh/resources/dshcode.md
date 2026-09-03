---
title: "dshcode"
description: "Community desktop companion for DeepSeek Harness — one-click Electron app for macOS and Windows"
keywords: "dshcode, desktop, client, coding, deepseek harness, dsh"
---
# dshcode

> ⭐ **126** · ✅ 活跃 · 客户端 · 近期 ⬆️ +92

| | | | |
|---|---|---|---|
| 类型 | 客户端 | 分类 | 桌面端 |
| 星数 | ⭐ 126 | 状态 | ✅ 活跃 |
| 作者 | [whitelonng](https://github.com/whitelonng) | 更新时间 | 2026-08-21 |

## 一句话介绍

> Community desktop companion for DeepSeek Harness — one-click Electron app for macOS and Windows

## 详细介绍

[English](README.zh.md) | 中文 DSHCode 是一款面向 macOS 和 Windows 的免费开源桌面 AI Agent 应用。它将 DeepSeek 官方开源项目 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 的 Web UI 与插件运行时打包成一个可直接安装的 Electron 应用——无需 Node.js、无需终端、无需命令行。

## ✨ 核心特性

- **macOS**：在访达中右键点击应用并选择**打开**，然后在弹窗中确认。或者在终端执行一次 `xattr -cr /Applications/DSHCode.app`。
- **Windows**：在 SmartScreen 弹窗中点击**更多信息**，然后选择**仍要运行**。

## 📦 安装

```bash
git clone https://github.com/whitelonng/dshcode.git
cd dshcode
pnpm install
pnpm run build
pnpm dsh web
```

## 🚀 快速开始

```bash
git clone https://github.com/whitelonng/dshcode.git
cd dshcode
pnpm install
pnpm run desktop:dist
```

## 📚 更多信息

**功能特性**

DSHCode 继承了 DeepSeek Harness 的完整能力，并加上了开箱即用的桌面体验。 **Agent 核心** — 插件化框架，内置 bash、文件系统、网页搜索/抓取、终端、LSP 与子进程工具；支持沙箱隔离与逐操作审批提示。 **交互式 UI** — 内联渲染的 GenUI 卡片：图表、表格、测验、3D 场景、示意图、表单与进度视图。 **Skills 技能** — 可安装的技能目录，为 Agent 提供专项工作流——研究、文档写作、视觉工具等。 **编排能力** — Subagent 并行委派，以及可跨多个 Agent 分阶段并行展开的 Workflow。 **长任务** — 执行前先审查再批准的 Plan 模式、跨轮次持续进行的 Goal 目标、可恢复的会话。 **模型体验** — 通过官方 API 使用 DeepSeek 模型；会话日志完整记录模型所见内容，任何一次

**构建桌面安装包**

git clone https://github.com/whitelonng/dshcode.git cd dshcode pnpm install pnpm run desktop:dist 构建产物写入 `.artifacts/desktop/release/`。名为 `Desktop` 的 GitHub Actions 工作流会构建 macOS Apple Silicon、macOS Intel 和 Windows x64 安装包；`desktop-v*` tag 会把完整构建矩阵及 SHA-256 校验和发布到 GitHub Releases。

## 🔗 链接

- [GitHub 仓库](https://github.com/whitelonng/dshcode)
- [完整 README](https://github.com/whitelonng/dshcode#readme)
- [返回dshcode所在分类](../clients.md)
