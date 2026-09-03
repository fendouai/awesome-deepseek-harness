---
title: "dsh-pr-checks"
description: "DSH plugin (host + web client): status and progress of GitHub Actions checks of the open PRs, grouped by workspace/project, in the sidebar footer."
keywords: "dsh-pr-checks, ui, plugin, git, deepseek harness, dsh"
---
# dsh-pr-checks

> ⭐ **0** · 🧪 experimental · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 0 | Status | 🧪 experimental |
| Author | [pauloapoloni](https://github.com/pauloapoloni) | Updated | — |
| Subcategory | 🖥️ Sidebars & panels | Capabilities | ui, git |

## One-liner

> DSH plugin (host + web client): status and progress of GitHub Actions checks of the open PRs, grouped by workspace/project, in the sidebar footer.

## About

[DSH](https://github.com/deepseek-ai/deepseek-harness) plugin (host + web client) that shows, in the sidebar footer, the **status and progress of the checks** (GitHub Actions) of the open PRs, grouped by **Workspace → Project → PR**. - Progress bar per PR (`done/total`), colored dots per check (tooltip with the name) and a "PR checks" header. - Only PRs with checks **still running** (`IN_PROGRESS`/`QUEUED`/`PENDING`) are shown: when they finish, the PR drops out of the list — and with nothing running, the whole widget **hides** (it comes back when a check starts running again). - Hidden when the sidebar is collapsed. - **Durable**: complete profile plugin, no patch to the DSH runtime files — survives DSH updates.

## ✨ Key Features

- Progress bar per PR (`done/total`), colored dots per check (tooltip with the name) and a "PR checks" header.
- Only PRs with checks **still running** (`IN_PROGRESS`/`QUEUED`/`PENDING`) are shown: when they finish, the PR drops out of the list — and with nothing running, 
- Hidden when the sidebar is collapsed.
- **Durable**: complete profile plugin, no patch to the DSH runtime files — survives DSH updates.

## 📦 Install

```bash
dsh plugin --profile <name> add dsh-pr-checks
# or directly from the git repository:
# dsh plugin --profile <name> add github:pauloapoloni/dsh-pr-checks
```

## 🚀 Quick Start

```bash
cd ~/.dsh/profiles/web
npm install github:pauloapoloni/dsh-pr-checks
```

## 📚 Learn more

**Installation**

The package is a DSH **bundle** (manifest `dsh.bundle`): it ships its own `cordis.patch.yml` layer, so installing it also registers the plugin row. Published on npm as `dsh-pr-checks`. To install it in a profile: dsh plugin --profile <name> add dsh-pr-checks

## 🔗 Links

- [GitHub Repository](https://github.com/pauloapoloni/dsh-pr-checks)
- [Full README](https://github.com/pauloapoloni/dsh-pr-checks#readme)
- [Back to the Plugins list](../plugins.md)
