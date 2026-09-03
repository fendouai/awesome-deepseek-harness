---
title: "dsh-turn-rewind"
description: "Rewind conversation and workspace state, powered by a persistent change ledger."
keywords: "dsh-turn-rewind, developer, plugin, files, context, deepseek harness, dsh"
---
# dsh-turn-rewind

> ⭐ **94** · ✅ active · plugin · ⬆️ +3 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 94 | Status | ✅ active |
| Author | [Anionex](https://github.com/Anionex) | Updated | 2026-08-16 |
| Subcategory | 📁 Files & import | Capabilities | files, context |

## One-liner

> Rewind conversation and workspace state, powered by a persistent change ledger.

## About

[中文说明](README.zh.md) Message-anchored project-file recovery for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness), with an option to restart from the restored request. **Turn Rewind** is the user-facing feature, repository, and Profile Bundle name. **Change Ledger** is the durable restore engine underneath it: the `ctx.changeLedger` service, on-disk format, and storage path keep that name because they describe the reusable snapshot and recovery layer rather than the Web action alone. Change Ledger gives a DSH session an explicit safety boundary around workspace mutations: create restore point ↓ agent / user / external tools modify the worktree ↓ preview exact path-level drift ↓ review a full or selective restore plan ↓ press the final restore button in the rewind dialog ↓

## ✨ Key Features

- content-addressed restore-point manifests;
- Git worktree, HEAD, branch, and in-progress-operation fences;
- stale-plan detection between review and mutation;
- exact two-step confirmation plus DSH human approval;
- automatic pre-restore rescue points;
- post-restore hash verification;

## 📦 Install

```bash
pnpm install --frozen-lockfile
pnpm run check

dsh plugin --profile web add @anionex/dsh-turn-rewind
dsh plugin --profile headless add @anionex/dsh-turn-rewind

dsh --profile web --dump-config | grep turn-rewind
```

## 🚀 Quick Start

```bash
export const inject = ['changeLedger']

export async function apply(ctx: Context) {
  const point = await ctx.changeLedger.create({
    cwd: '/absolute/git/worktree',
    sessionId: 'session-id',
    label: 'before refactor',
  })
  // point.id is a durable restore-point id.
}
```

## 📚 Learn more

**Install**

Build the checked-out plugin, then add it to each DSH profile that should expose the service: pnpm install --frozen-lockfile pnpm run check dsh plugin --profile web add @anionex/dsh-turn-rewind dsh plugin --profile headless add @anionex/dsh-turn-rewind dsh --profile web --dump-config | grep turn-rewind Restart a running profile after changing its bundle list. The package is a DSH Profile Bundle. `

**Configuration**

Runtime-tunable options are editable in the DSH web settings page under **Plugins → Turn Rewind** (`turn-rewind` settings namespace). Changes apply live to the next capture, restore, or deletion; they persist in the host's `settings.yaml` and override the profile patch values below. `storageDir` is deliberately not editable there: the storage root must not move while the engine holds locks and jou

## 🔗 Links

- [GitHub Repository](https://github.com/Anionex/dsh-turn-rewind)
- [Full README](https://github.com/Anionex/dsh-turn-rewind#readme)
- [Back to the Plugins list](../plugins.md)
