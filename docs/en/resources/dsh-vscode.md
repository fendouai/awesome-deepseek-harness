---
title: "dsh-vscode"
description: "在 VS Code 侧边栏内嵌使用 DeepSeek Harness（DSH）网页界面的插件"
keywords: "dsh-vscode, ide, integration, coding, deepseek harness, dsh"
---
# dsh-vscode

> ⭐ **25** · ✅ active · integration

| | | | |
|---|---|---|---|
| Type | integration | Category | IDE & editors |
| Stars | ⭐ 25 | Status | ✅ active |
| Author | [Fengze233](https://github.com/Fengze233) | Updated | — |

## One-liner

> 在 VS Code 侧边栏内嵌使用 DeepSeek Harness（DSH）网页界面的插件

## About

Bring DeepSeek Harness into the same place you write code. dsh-vscode gives DSH a Claude Code/Codex-style right sidebar that already understands your project, active file, and selected code. Ask DeepSeek to inspect, change, and verify code without switching between your editor, terminal, and a separate chat window. 👋 I built this because I wanted DSH right beside my editor. If that sounds useful to you too, give it a try! I'd love to hear how it fits into your workflow. [Website](https://lixxx1.github.io/dsh-vscode/) · [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=lixxx1.dsh-sidebar)

## ✨ Key Features

- **Autonomous VS Code debugging.** Let DeepSeek launch the current project from `.vscode/launch.json`, manage breakpoints, step through execution, and inspect st
- **Official DSH inside VS Code.** Sessions, streaming responses, tool calls, approvals, and follow-up questions run through the official DSH runtime.
- **Project-aware editor context.** The active file, selected code, and `@file` or `@folder` references travel with your prompt.
- **Session controls where you need them.** Switch Permission and Plan modes, choose Model and Reasoning Effort, or steer an active task.
- **Native review and safe revert.** Review changes in VS Code's Diff Editor, Keep or Revert edits, and stop DSH before it overwrites a file with unsaved changes.
- **Extend DSH from the sidebar.** Discover and manage Tools, Skills, MCP integrations, Memory, and Agent Hooks loaded by DSH.

## 📦 Install

```bash
npm install -g @deepseek-ai/dsh
```

## 🚀 Quick Start

```bash
git clone https://github.com/Lixxx1/dsh-vscode.git
cd dsh-vscode
pnpm install --frozen-lockfile
pnpm run package
```

## 📚 Learn more

**📦 Install**

Install the official DeepSeek Harness CLI: npm install -g @deepseek-ai/dsh Then choose the extension channel that fits you:

## 🔗 Links

- [GitHub Repository](https://github.com/Fengze233/dsh-vscode)
- [Full README](https://github.com/Fengze233/dsh-vscode#readme)
- [Back to the MCP & Integrations list](../integrations.md)
