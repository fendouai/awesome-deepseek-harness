---
title: "dsh-turn-rewind"
description: "对话与代码状态回退插件，基于持久化变更账本。"
keywords: "dsh-turn-rewind, developer, plugin, files, context, deepseek harness, dsh"
---
# dsh-turn-rewind

> ⭐ **94** · ✅ 活跃 · 插件 · 近期 ⬆️ +3

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 94 | 状态 | ✅ 活跃 |
| 作者 | [Anionex](https://github.com/Anionex) | 更新时间 | 2026-08-16 |
| 子分类 | 📁 文件与导入 | 能力 | files, context |

## 一句话介绍

> 对话与代码状态回退插件，基于持久化变更账本。

## 详细介绍

[中文说明](README.zh.md) Message-anchored project-file recovery for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness), with an option to restart from the restored request. **Turn Rewind** is the user-facing feature, repository, and Profile Bundle name. **Change Ledger** is the durable restore engine underneath it: the `ctx.changeLedger` service, on-disk format, and storage path keep that name because they describe the reusable snapshot and recovery layer rather than the Web action alone. Change Ledger gives a DSH session an explicit safety boundary around workspace mutations: create restore point ↓ agent / user / external tools modify the worktree ↓ preview exact path-level drift ↓ review a full or selective restore plan ↓ press the final restore button in the rewind dialog ↓

## ✨ 核心特性

- content-addressed restore-point manifests;
- Git worktree, HEAD, branch, and in-progress-operation fences;
- stale-plan detection between review and mutation;
- exact two-step confirmation plus DSH human approval;
- automatic pre-restore rescue points;
- post-restore hash verification;

## 📦 安装

```bash
pnpm install --frozen-lockfile
pnpm run check

dsh plugin --profile web add @anionex/dsh-turn-rewind
dsh plugin --profile headless add @anionex/dsh-turn-rewind

dsh --profile web --dump-config | grep turn-rewind
```

## 🚀 快速开始

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

## 📚 更多信息

**Install**

Build the checked-out plugin, then add it to each DSH profile that should expose the service: pnpm install --frozen-lockfile pnpm run check dsh plugin --profile web add @anionex/dsh-turn-rewind dsh plugin --profile headless add @anionex/dsh-turn-rewind dsh --profile web --dump-config | grep turn-rewind Restart a running profile after changing its bundle list. The package is a DSH Profile Bundle. `

**Configuration**

Runtime-tunable options are editable in the DSH web settings page under **Plugins → Turn Rewind** (`turn-rewind` settings namespace). Changes apply live to the next capture, restore, or deletion; they persist in the host's `settings.yaml` and override the profile patch values below. `storageDir` is deliberately not editable there: the storage root must not move while the engine holds locks and jou

## 🔗 链接

- [GitHub 仓库](https://github.com/Anionex/dsh-turn-rewind)
- [完整 README](https://github.com/Anionex/dsh-turn-rewind#readme)
- [返回dsh-turn-rewind所在分类](../plugins.md)
