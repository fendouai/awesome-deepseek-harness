---
title: "dsh-git-branch-switcher"
description: "Session-header git branch pill: shows the workspace branch and switches it from the Web UI."
keywords: "dsh-git-branch-switcher, developer, plugin, git, ui, deepseek harness, dsh"
---
# dsh-git-branch-switcher

> ⭐ **0** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 0 | Status | ✅ active |
| Author | [mixin-ai](https://github.com/mixin-ai) | Updated | 2026-08-14 |
| Subcategory | 🧪 Code, tests & review | Capabilities | git, ui |

## One-liner

> Session-header git branch pill: shows the workspace branch and switches it from the Web UI.

## About

A DeepSeek Harness (DSH) Web plugin: a Git branch pill in the session header that shows the current branch of the session's workspace and lets you switch branches straight from the UI.

## ✨ Key Features

- Shows the current git branch in the top-right session header (only for git-managed workspaces)
- Click the pill to open the branch panel: local branches, current one highlighted with ✓
- Click any branch to `git checkout` it; the pill updates immediately
- Detached HEAD support: shows the short commit hash with an explanation
- Auto-refresh every 30s (picks up terminal-side switches) plus a manual refresh button
- Checkout failures (e.g. conflicting local changes) surface git's own error message
- Theme-aware: all colors use the shell's `--dsw-*` tokens, light/dark ready
- Sandbox-aware: git runs under the same sandbox policy as the session's shell

## 📦 Install

```bash
dsh plugin --profile web add "github:mixin-ai/dsh-git-branch-switcher#main"
```

## 🚀 Quick Start

```bash
dsh --profile web
```

## 📚 Learn more

**Install**

dsh plugin --profile web add "github:mixin-ai/dsh-git-branch-switcher#main" Then restart your Web profile: dsh --profile web The plugin is now listed under Settings → Plugins and the branch pill appears in the session header. Alternative (source checkout): git clone https://github.com/mixin-ai/dsh-git-branch-switcher dsh web --patch ./dsh-git-branch-switcher/cordis.patch.yml

**Usage**

1. Open a session whose workspace is a git repository. 2. The branch pill appears at the top-right of the conversation header. 3. Click it → branch list → click a branch to switch. 4. The ↻ button re-reads the branch list.

**安装**

dsh plugin --profile web add "github:mixin-ai/dsh-git-branch-switcher#main" 然后重启 Web profile： dsh --profile web 插件会出现在「设置 → 插件」中，分支胶囊显示在会话头部。 源码方式（patch 覆盖层）： git clone https://github.com/mixin-ai/dsh-git-branch-switcher dsh web --patch ./dsh-git-branch-switcher/cordis.patch.yml

**使用**

1. 打开一个工作区为 git 仓库的会话。 2. 会话头部右上角出现分支胶囊。 3. 点击胶囊 → 分支列表 → 点击分支即可切换。 4. ↻ 按钮重新读取分支列表。

## 🔗 Links

- [GitHub Repository](https://github.com/mixin-ai/dsh-git-branch-switcher)
- [Full README](https://github.com/mixin-ai/dsh-git-branch-switcher#readme)
- [Back to the Plugins list](../plugins.md)
