---
title: "dsh-review-loop"
description: "Incremental diff reviewer: checkpoint-based review queue with a Web UI panel and /review command."
keywords: "dsh-review-loop, developer, plugin, coding, git, ui, deepseek harness, dsh"
---
# dsh-review-loop

> ⭐ **2** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 2 | Status | ✅ active |
| Author | [wuxiangru915](https://github.com/wuxiangru915) | Updated | 2026-08-21 |
| Subcategory | 🛡️ Security & ops | Capabilities | coding, git, ui |

## One-liner

> Incremental diff reviewer: checkpoint-based review queue with a Web UI panel and /review command.

## About

Incremental diff reviewer for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness). [中文](README.zh.md) · [MIT License](LICENSE) `dsh-review-loop` turns code review of agent work into an incremental, closed-loop process: after you approve a batch of changes, a checkpoint is recorded and the next review shows only the changes made afterward — never a re-review of what you already saw. Review feedback is injected back to the agent through the harness's normal message channel, without interrupting its work.

## ✨ Key Features

- **Incremental review (since-review)**: approving snapshots the working tree into a checkpoint; the next review diffs `checkpoint -> current`, so reviewed files 
- **Two entry points**: a Web UI review panel docked above the conversation composer (2s polling), and a `/review` command for keyboard-first use. The same core l
- **Feedback closed loop**: approvals may carry a comment, delivered to the agent as a user message via `agent.inject()`.
- **No tool-call parsing**: any on-disk change — by the agent, by you, or by another process — is reflected; the plugin reads git, not the agent loop.
- **Checkpoint persistence**: `$DSH_HOME/review-loop/<workspace-hash>.json`, written atomically, never polluting the workspace's own git status.
- **Zero core modifications**: a pure bundle plugin (`dsh.bundle` patch layer); the agent-loop skeleton is untouched.

## 📦 Install

```bash
# one line, from a git source
dsh plugin --profile web add github:wuxiangru915/dsh-review-loop

# restart the web server, then hard-refresh the page
```

## 🚀 Quick Start

```bash
command: /review ------> renderState() ----+
                                           +--> src/review.ts (pure, shared)
web UI:  GET /state ----> collectState() --+
         POST /approve --> approve() + agent.inject()
```

## 📚 Learn more

**Architecture**

src/ ├── review.ts Pure core (collectState / approve / renderState) — shared by command and HTTP paths ├── git.ts git helpers (status / diff / hash-object; zero-dependency spawnSync) ├── checkpoint.ts checkpoint persistence ($DSH_HOME/review-loop/<ws-hash>.json, atomic write) ├── http.ts Web routes: GET /plugins/dsh-review-loop/state · POST /plugins/dsh-review-loop/approve └── client/ └── review-p

## 🔗 Links

- [GitHub Repository](https://github.com/wuxiangru915/dsh-review-loop)
- [Full README](https://github.com/wuxiangru915/dsh-review-loop#readme)
- [Back to the Plugins list](../plugins.md)
