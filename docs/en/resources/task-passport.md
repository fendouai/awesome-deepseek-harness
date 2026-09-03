---
title: "Task Passport"
description: "Open task handoff protocol for DeepSeek Harness, WorkBuddy, Claude Code and Codex: verified state, not chat logs."
keywords: "Task Passport, multi-agent, agent, workflow, deepseek harness, dsh"
---
# Task Passport

> ⭐ **9** · ✅ active · agent · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | agent | Category | Multi-agent |
| Stars | ⭐ 9 | Status | ✅ active |
| Author | [dongsheng123132](https://github.com/dongsheng123132) | Updated | 2026-08-15 |

## One-liner

> Open task handoff protocol for DeepSeek Harness, WorkBuddy, Claude Code and Codex: verified state, not chat logs.

## About

让一个任务带着“当前世界状态”在 DeepSeek Harness、Claude Code、Codex 等 AI Harness 之间接力，不搬运聊天记录。 一个项目可以有多个任务护照；一个任务护照可以经历多个 Harness 和多个会话。

## ✨ Key Features

- 每个任务一个稳定短号，例如 `TP-7K4M-9D2Q`。
- `list`：只列身份与摘要，不误装载别的任务。
- `open`：读取目标、当前状态、验证过的事实、决策理由和下一步。
- `checkpoint`：工作完成后写回；带状态版本，过期写入直接冲突，不静默覆盖。
- `pack` / `land`：把任务装进一个文件发给别人、发给另一台机器，或者收下别人发来的。
- `conformance`：判定一个文件是不是合规的 TaskPack（退出码 0 / 2）。

## 📦 Install

```bash
dsh plugin --profile web add task-passport@0.3.0
dsh --profile web --dump-config
dsh web
```

## 🚀 Quick Start

```bash
- id: task-passport
  name: task-passport
  config:
    ukingExecutable: 'C:/path/to/U-King.exe'
    # 或者不依赖 U-King：storeDirectory: 'D:/task-passports'
    allowCheckpoint: true
```

## 📚 Learn more

**在 DeepSeek Harness 中安装**

从 GitHub 安装（纯 JavaScript，仓库已包含运行产物，不需要 `prepare` 构建权限）： dsh plugin --profile web add task-passport@0.3.0 dsh --profile web --dump-config dsh web `dsh web` 在当前 rc.5 固定组合 `web` profile；需要浏览器界面时，插件也应安装到这个 profile。自定义 profile 可用于 TUI，但不能作为 `web` 子命令的父级 profile。 如果 U-King 不在 PATH，在该 profile 的 `cordis.patch.yml` 覆盖插件配置： name: task-passport config: ukingExecutable: 'C:/path/to/U-King.exe' # 或者不依赖 U-King：

## 🔗 Links

- [GitHub Repository](https://github.com/dongsheng123132/task-passport)
- [Full README](https://github.com/dongsheng123132/task-passport#readme)
- [Back to the Agents & Multi-Agent list](../agents.md)
