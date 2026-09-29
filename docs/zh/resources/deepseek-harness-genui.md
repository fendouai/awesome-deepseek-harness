---
title: "deepseek-harness-genui"
description: "为 DeepSeek Harness 当前任务生成 React 交互界面，保存用户选择供下一轮 Agent 继续处理"
keywords: "deepseek-harness-genui, ui, plugin, deepseek harness, dsh"
---
# deepseek-harness-genui

> ⭐ **114** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 114 | 状态 | ✅ 活跃 |
| 作者 | [pengyue-polaron](https://github.com/pengyue-polaron) | 更新时间 | — |
| 子分类 | 💡 生成式界面 | 能力 | ui |

## 一句话介绍

> 为 DeepSeek Harness 当前任务生成 React 交互界面，保存用户选择供下一轮 Agent 继续处理

## 详细介绍

DeepSeek Harness GenUI lets an Agent build a focused interface when a task is awkward in text. The Coding Agent writes ordinary React + TypeScript—not a component-tree DSL—and the interface can save user selections for the next Agent turn. The result is a task-specific app that can explain a difficult relationship, collect connected choices, or continue a tool-backed workflow without asking the user to repeat their input. Related research: [*EvoGenUI-Bench: Evaluating LLMs as Multi-Turn Generative UI Assistants*](https://arxiv.org/abs/2608.29387).

## 📦 安装

```bash
dsh plugin --profile web add dsh-plugin-genui --allow-build=esbuild
dsh --profile web
```

## 🚀 快速开始

```bash
Plan a Saturday route with a museum, a riverside garden, and dinner. Build an
interface where I can change the times and make the garden optional.
```

## 📚 更多信息

**Install**

Requires Node.js `^22.19.0 || ^24.0.0` and a supported DeepSeek Harness Web profile. dsh plugin --profile web add dsh-plugin-genui --allow-build=esbuild dsh --profile web v0.14 supports Inline, Canvas, fullscreen, and localhost on the tested Harness versions listed in the [release notes](docs/release-notes-v0.14.0.md). TUI/headless profiles are not supported. `--allow-build=esbuild` enables the lo

## 🔗 链接

- [GitHub 仓库](https://github.com/pengyue-polaron/deepseek-harness-genui)
- [完整 README](https://github.com/pengyue-polaron/deepseek-harness-genui#readme)
- [返回deepseek-harness-genui所在分类](../plugins.md)
