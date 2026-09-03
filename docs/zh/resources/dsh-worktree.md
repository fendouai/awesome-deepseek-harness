---
title: "dsh-worktree"
description: "Codex-style permanent git worktrees for DeepSeek Harness: worktree_create/list/remove agent tools, a /worktree chat command, and durable per-repo manifests."
keywords: "dsh-worktree, vision, plugin, coding, git, multi-agent, deepseek harness, dsh"
---
# dsh-worktree

> ⭐ **7** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 7 | 状态 | ✅ 活跃 |
| 作者 | [FlashingChen](https://github.com/FlashingChen) | 更新时间 | — |
| 子分类 | 👁️ 视觉工具 | 能力 | coding, git, multi-agent |

## 一句话介绍

> Codex-style permanent git worktrees for DeepSeek Harness: worktree_create/list/remove agent tools, a /worktree chat command, and durable per-repo manifests.

## 详细介绍

Codex-style **permanent git worktrees** for DeepSeek Harness — a Cordis plugin that gives a DSH profile the same durable-worktree workflow as `codex worktree create --permanent`. A permanent worktree is a real `git worktree add --detach` checkout that **survives sessions and restarts**. You (or the agent) create it once, and any later session can be opened inside it to keep working where the previous one left off — without ever touching your main working tree.

## ✨ 核心特性

- Worktrees live at `<repo-root>/.dsh-worktrees/<name>` — the same hidden
- Every worktree is recorded in a per-repository manifest,
- Creating a worktree also registers it in `ctx.workspaceRegistry`, so it
- Removing a worktree runs `git worktree remove` (with `--force` when

## 📦 安装

```bash
# 1. make the plugin available to your profile (installs from npm)
dsh plugin --profile web add dsh-worktree

# 2. activate it in the profile's patch layer
#    add to ~/.dsh/profiles/web/cordis.patch.yml:
#
#    - insert:
#        - id: worktree
#          name: 'dsh-worktree'

# 3. restart the profile (e.g. restart the `dsh web` process)
```

## 🚀 快速开始

```bash
git clone https://github.com/FlashingChen/dsh-worktree.git
cd dsh-worktree
npm install            # self-contained deps, pinned to the harness versions
dsh plugin --profile web add "$PWD"
# ... then the patch row and restart as above
```

## 🔗 链接

- [GitHub 仓库](https://github.com/FlashingChen/dsh-worktree)
- [完整 README](https://github.com/FlashingChen/dsh-worktree#readme)
- [返回dsh-worktree所在分类](../plugins.md)
