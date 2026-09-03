---
title: "dsh-vscode"
description: "在 VS Code 侧边栏内嵌使用 DeepSeek Harness（DSH）网页界面的插件"
keywords: "dsh-vscode, ide, integration, coding, deepseek harness, dsh"
---
# dsh-vscode

> ⭐ **25** · ✅ 活跃 · 集成

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | IDE 与编辑器 |
| 星数 | ⭐ 25 | 状态 | ✅ 活跃 |
| 作者 | [Fengze233](https://github.com/Fengze233) | 更新时间 | — |

## 一句话介绍

> 在 VS Code 侧边栏内嵌使用 DeepSeek Harness（DSH）网页界面的插件

## 详细介绍

Bring DeepSeek Harness into the same place you write code. dsh-vscode gives DSH a Claude Code/Codex-style right sidebar that already understands your project, active file, and selected code. Ask DeepSeek to inspect, change, and verify code without switching between your editor, terminal, and a separate chat window. 👋 I built this because I wanted DSH right beside my editor. If that sounds useful to you too, give it a try! I'd love to hear how it fits into your workflow. [Website](https://lixxx1.github.io/dsh-vscode/) · [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=lixxx1.dsh-sidebar)

## ✨ 核心特性

- **Autonomous VS Code debugging.** Let DeepSeek launch the current project from `.vscode/launch.json`, manage breakpoints, step through execution, and inspect st
- **Official DSH inside VS Code.** Sessions, streaming responses, tool calls, approvals, and follow-up questions run through the official DSH runtime.
- **Project-aware editor context.** The active file, selected code, and `@file` or `@folder` references travel with your prompt.
- **Session controls where you need them.** Switch Permission and Plan modes, choose Model and Reasoning Effort, or steer an active task.
- **Native review and safe revert.** Review changes in VS Code's Diff Editor, Keep or Revert edits, and stop DSH before it overwrites a file with unsaved changes.
- **Extend DSH from the sidebar.** Discover and manage Tools, Skills, MCP integrations, Memory, and Agent Hooks loaded by DSH.

## 📦 安装

```bash
npm install -g @deepseek-ai/dsh
```

## 🚀 快速开始

```bash
git clone https://github.com/Lixxx1/dsh-vscode.git
cd dsh-vscode
pnpm install --frozen-lockfile
pnpm run package
```

## 📚 更多信息

**📦 Install**

Install the official DeepSeek Harness CLI: npm install -g @deepseek-ai/dsh Then choose the extension channel that fits you:

## 🔗 链接

- [GitHub 仓库](https://github.com/Fengze233/dsh-vscode)
- [完整 README](https://github.com/Fengze233/dsh-vscode#readme)
- [返回dsh-vscode所在分类](../integrations.md)
