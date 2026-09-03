---
title: "dsh-task-status"
description: "DSH 插件：后台任务状态条（对话页任务进度 + 实时输出 tail）。官方 bundle 插件，dsh plugin --profile web add 安装"
keywords: "dsh-task-status, learning, skill, coding, deepseek harness, dsh"
---
# dsh-task-status

> ⭐ **9** · ✅ 活跃 · 技能

| | | | |
|---|---|---|---|
| 类型 | 技能 | 分类 | 学习 |
| 星数 | ⭐ 9 | 状态 | ✅ 活跃 |
| 作者 | [vlln](https://github.com/vlln) | 更新时间 | — |

## 一句话介绍

> DSH 插件：后台任务状态条（对话页任务进度 + 实时输出 tail）。官方 bundle 插件，dsh plugin --profile web add 安装

## 详细介绍

**UI** (chat-page dock slot): **Routes** (Node half): **Output tail contention semantics** (official 0809 API constraint): `tasks.read` is a consumptive, incremental read (one shared cursor per task). This plugin applies a **mirror patch** to `ctx.tasks.read` — the official read becomes buffered mirror (increments already read by others, not re-consumed) + direct read of the latest (normal consumption); the plugin's own reads go straight to the underlying rawRead. The official tool and the plugin see the same increment sequence (no duplicates, no loss); only the proactively self-read part can no longer be replayed by the official side alone (official semantics is inherently incremental, so model perception is unaffected).

## 📦 安装

```bash
dsh plugin --profile web add "github:vlln/dsh-task-status#main"   # one-line git source (build artifacts committed)
# or npm source: dsh plugin --profile web add @vlln/dsh-task-status@0.3.1
```

## 🚀 快速开始

```bash
⚙ 1 background task running
  ● bash-1  for i in $(seq 1 20)…   started 21:30:15   running
```

## 📚 更多信息

**Installation**

**Recommended: one-line install from a git source** (build artifacts are committed; a git source doesn't trigger a build): dsh plugin --profile web add "github:vlln/dsh-task-status#main" # one-line git source (build artifacts committed)

**Usage**

Run a background task and the status bar appears (e.g. the model-side `bash` tool with `run_in_background: true`): ⚙ 1 background task running ● bash-1 for i in $(seq 1 20)… started 21:30:15 running Click a task row to expand → the output tail scrolls live (a scrollbar appears once it exceeds 10 lines). The status bar disappears automatically when the task finishes.

## 🔗 链接

- [GitHub 仓库](https://github.com/vlln/dsh-task-status)
- [完整 README](https://github.com/vlln/dsh-task-status#readme)
- [返回dsh-task-status所在分类](../skills.md)
