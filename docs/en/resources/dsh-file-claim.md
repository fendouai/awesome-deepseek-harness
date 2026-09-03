---
title: "dsh-file-claim"
description: "File ownership/claim system for parallel agent sessions on the same project: claim/release, heartbeat stale takeover and async 3-way merge."
keywords: "dsh-file-claim, developer, plugin, files, multi-agent, git, deepseek harness, dsh"
---
# dsh-file-claim

> ⭐ **6** · ✅ active · plugin · ⬆️ +2 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 6 | Status | ✅ active |
| Author | [Nwflower](https://github.com/Nwflower) | Updated | 2026-08-16 |
| Subcategory | 📁 Files & import | Capabilities | files, multi-agent, git |

## One-liner

> File ownership/claim system for parallel agent sessions on the same project: claim/release, heartbeat stale takeover and async 3-way merge.

## About

When several DSH sessions run in parallel against one workspace, they have no awareness of each other: two sessions can overwrite the same file, a crashed session leaves stale state behind, and a session that wants to edit a file another session owns can only wait or guess. `dsh-file-claim` turns a proven coordination protocol into native DSH tools, lifecycle events, and a write guard — so parallel agents cooperate instead of clobbering each other. claim_files({ paths: ["README.md"] }) # "I'm editing this" write / edit ... # writes to files claimed by others are denied release_files({ paths: ["README.md"] }) # "done — pending edits auto-merge now"

## ✨ Key Features

- 🔒 **claim / release** — a session declares exclusive ownership of file paths before editing
- ❤️ **heartbeat + stale takeover + orphan self-heal** — heartbeats refresh automatically via agent
- 🧩 **async pending merge area** — instead of blocking, a session writes its edited content plus
- 🛡️ **write guard** — a `tools/pre-execute` guard refuses writes to files actively claimed by
- ⚡ **zero automation burden** — `agent/created` / `agent/status` refresh the heartbeat, and
- 📦 **pure Host plugin, zero dependencies** — no Browser side, no build step, `node:` builtins
- 🧾 **audit trail** — every claim / release / takeover / pending mutation is appended as one JSON

## 📦 Install

```bash
dsh plugin add dsh-file-claim
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add -w link:<repo-path>
```

## 📚 Learn more

**Install**

dsh plugin add dsh-file-claim For development / manual verification against a local checkout: dsh plugin --profile web add -w link:<repo-path> Requires DSH with `node >= 18` and `git` on `PATH` (used only by the 3-way merge).

**Quick Start**

1. **Claim before you write.** Editing files? Call `claim_files` first — it declares exclusive ownership so other sessions leave them alone. 2. **Write freely.** Your own claims never block you; writes to files actively claimed by *another* session are denied with a hint (wait / takeover when stale / pend). 3. **Busy file? Don't wait — pend.** Use `pending_write` to drop your edited content into t

**Usage Examples**

**Two sessions, one workspace.** Session A owns `README.md`; session B wants to edit it too: // Session A claim_files({ paths: ["README.md"], note: "rewriting the docs" }) write ... README.md // allowed: own claim release_files({ paths: ["README.md"] }) // Session B — meanwhile who_claims({ paths: ["README.md"] }) // → claimed by A write ... README.md // → DENIED with a hint pending_write({ path: 

**Configuration**

Passed as plugin config in the bundle (`cordis.patch.yml`): - id: dsh-file-claim name: dsh-file-claim config: staleMs: 3600000 # 1h guardCommit: true # also guard explicit git commits Since 0.2.0, state is stored as **workspace sidecar files** — the lock travels with the protected file (the claude-code-file-locks `.agentlock` idiom, adopted because DSH reserves no in-workspace directory convention

## 🔗 Links

- [GitHub Repository](https://github.com/Nwflower/dsh-file-claim)
- [Full README](https://github.com/Nwflower/dsh-file-claim#readme)
- [Back to the Plugins list](../plugins.md)
