---
title: "dsh-worktree"
description: "Codex-style permanent git worktrees for DeepSeek Harness: worktree_create/list/remove agent tools, a /worktree chat command, and durable per-repo manifests."
keywords: "dsh-worktree, vision, plugin, coding, git, multi-agent, deepseek harness, dsh"
---
# dsh-worktree

> ⭐ **7** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 7 | Status | ✅ active |
| Author | [FlashingChen](https://github.com/FlashingChen) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding, git, multi-agent |

## One-liner

> Codex-style permanent git worktrees for DeepSeek Harness: worktree_create/list/remove agent tools, a /worktree chat command, and durable per-repo manifests.

## About

Codex-style **permanent git worktrees** for DeepSeek Harness — a Cordis plugin that gives a DSH profile the same durable-worktree workflow as `codex worktree create --permanent`. A permanent worktree is a real `git worktree add --detach` checkout that **survives sessions and restarts**. You (or the agent) create it once, and any later session can be opened inside it to keep working where the previous one left off — without ever touching your main working tree.

## ✨ Key Features

- Worktrees live at `<repo-root>/.dsh-worktrees/<name>` — the same hidden
- Every worktree is recorded in a per-repository manifest,
- Creating a worktree also registers it in `ctx.workspaceRegistry`, so it
- Removing a worktree runs `git worktree remove` (with `--force` when

## 📦 Install

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

## 🚀 Quick Start

```bash
git clone https://github.com/FlashingChen/dsh-worktree.git
cd dsh-worktree
npm install            # self-contained deps, pinned to the harness versions
dsh plugin --profile web add "$PWD"
# ... then the patch row and restart as above
```

## 🔗 Links

- [GitHub Repository](https://github.com/FlashingChen/dsh-worktree)
- [Full README](https://github.com/FlashingChen/dsh-worktree#readme)
- [Back to the Plugins list](../plugins.md)
