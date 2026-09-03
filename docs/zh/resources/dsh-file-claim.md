---
title: "dsh-file-claim"
description: "并行 Agent 会话的文件归属/认领系统：认领/释放、心跳过期接管、异步三路合并。"
keywords: "dsh-file-claim, developer, plugin, files, multi-agent, git, deepseek harness, dsh"
---
# dsh-file-claim

> ⭐ **6** · ✅ 活跃 · 插件 · 近期 ⬆️ +2

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 6 | 状态 | ✅ 活跃 |
| 作者 | [Nwflower](https://github.com/Nwflower) | 更新时间 | 2026-08-16 |
| 子分类 | 📁 文件与导入 | 能力 | files, multi-agent, git |

## 一句话介绍

> 并行 Agent 会话的文件归属/认领系统：认领/释放、心跳过期接管、异步三路合并。

## 详细介绍

When several DSH sessions run in parallel against one workspace, they have no awareness of each other: two sessions can overwrite the same file, a crashed session leaves stale state behind, and a session that wants to edit a file another session owns can only wait or guess. `dsh-file-claim` turns a proven coordination protocol into native DSH tools, lifecycle events, and a write guard — so parallel agents cooperate instead of clobbering each other. claim_files({ paths: ["README.md"] }) # "I'm editing this" write / edit ... # writes to files claimed by others are denied release_files({ paths: ["README.md"] }) # "done — pending edits auto-merge now"

## ✨ 核心特性

- 🔒 **claim / release** — a session declares exclusive ownership of file paths before editing
- ❤️ **heartbeat + stale takeover + orphan self-heal** — heartbeats refresh automatically via agent
- 🧩 **async pending merge area** — instead of blocking, a session writes its edited content plus
- 🛡️ **write guard** — a `tools/pre-execute` guard refuses writes to files actively claimed by
- ⚡ **zero automation burden** — `agent/created` / `agent/status` refresh the heartbeat, and
- 📦 **pure Host plugin, zero dependencies** — no Browser side, no build step, `node:` builtins
- 🧾 **audit trail** — every claim / release / takeover / pending mutation is appended as one JSON

## 📦 安装

```bash
dsh plugin add dsh-file-claim
```

## 🚀 快速开始

```bash
dsh plugin --profile web add -w link:<repo-path>
```

## 📚 更多信息

**Install**

dsh plugin add dsh-file-claim For development / manual verification against a local checkout: dsh plugin --profile web add -w link:<repo-path> Requires DSH with `node >= 18` and `git` on `PATH` (used only by the 3-way merge).

**Quick Start**

1. **Claim before you write.** Editing files? Call `claim_files` first — it declares exclusive ownership so other sessions leave them alone. 2. **Write freely.** Your own claims never block you; writes to files actively claimed by *another* session are denied with a hint (wait / takeover when stale / pend). 3. **Busy file? Don't wait — pend.** Use `pending_write` to drop your edited content into t

**Usage Examples**

**Two sessions, one workspace.** Session A owns `README.md`; session B wants to edit it too: // Session A claim_files({ paths: ["README.md"], note: "rewriting the docs" }) write ... README.md // allowed: own claim release_files({ paths: ["README.md"] }) // Session B — meanwhile who_claims({ paths: ["README.md"] }) // → claimed by A write ... README.md // → DENIED with a hint pending_write({ path: 

**Configuration**

Passed as plugin config in the bundle (`cordis.patch.yml`): - id: dsh-file-claim name: dsh-file-claim config: staleMs: 3600000 # 1h guardCommit: true # also guard explicit git commits Since 0.2.0, state is stored as **workspace sidecar files** — the lock travels with the protected file (the claude-code-file-locks `.agentlock` idiom, adopted because DSH reserves no in-workspace directory convention

## 🔗 链接

- [GitHub 仓库](https://github.com/Nwflower/dsh-file-claim)
- [完整 README](https://github.com/Nwflower/dsh-file-claim#readme)
- [返回dsh-file-claim所在分类](../plugins.md)
