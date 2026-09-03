---
title: "dsh-review-loop"
description: "增量代码审查：基于检查点的审查队列 + Web UI 面板 + /review 命令。"
keywords: "dsh-review-loop, developer, plugin, coding, git, ui, deepseek harness, dsh"
---
# dsh-review-loop

> ⭐ **2** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 2 | 状态 | ✅ 活跃 |
| 作者 | [wuxiangru915](https://github.com/wuxiangru915) | 更新时间 | 2026-08-21 |
| 子分类 | 🛡️ 安全与运维 | 能力 | coding, git, ui |

## 一句话介绍

> 增量代码审查：基于检查点的审查队列 + Web UI 面板 + /review 命令。

## 详细介绍

Incremental diff reviewer for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness). [中文](README.zh.md) · [MIT License](LICENSE) `dsh-review-loop` turns code review of agent work into an incremental, closed-loop process: after you approve a batch of changes, a checkpoint is recorded and the next review shows only the changes made afterward — never a re-review of what you already saw. Review feedback is injected back to the agent through the harness's normal message channel, without interrupting its work.

## ✨ 核心特性

- **Incremental review (since-review)**: approving snapshots the working tree into a checkpoint; the next review diffs `checkpoint -> current`, so reviewed files 
- **Two entry points**: a Web UI review panel docked above the conversation composer (2s polling), and a `/review` command for keyboard-first use. The same core l
- **Feedback closed loop**: approvals may carry a comment, delivered to the agent as a user message via `agent.inject()`.
- **No tool-call parsing**: any on-disk change — by the agent, by you, or by another process — is reflected; the plugin reads git, not the agent loop.
- **Checkpoint persistence**: `$DSH_HOME/review-loop/<workspace-hash>.json`, written atomically, never polluting the workspace's own git status.
- **Zero core modifications**: a pure bundle plugin (`dsh.bundle` patch layer); the agent-loop skeleton is untouched.

## 📦 安装

```bash
# one line, from a git source
dsh plugin --profile web add github:wuxiangru915/dsh-review-loop

# restart the web server, then hard-refresh the page
```

## 🚀 快速开始

```bash
command: /review ------> renderState() ----+
                                           +--> src/review.ts (pure, shared)
web UI:  GET /state ----> collectState() --+
         POST /approve --> approve() + agent.inject()
```

## 📚 更多信息

**Architecture**

src/ ├── review.ts Pure core (collectState / approve / renderState) — shared by command and HTTP paths ├── git.ts git helpers (status / diff / hash-object; zero-dependency spawnSync) ├── checkpoint.ts checkpoint persistence ($DSH_HOME/review-loop/<ws-hash>.json, atomic write) ├── http.ts Web routes: GET /plugins/dsh-review-loop/state · POST /plugins/dsh-review-loop/approve └── client/ └── review-p

## 🔗 链接

- [GitHub 仓库](https://github.com/wuxiangru915/dsh-review-loop)
- [完整 README](https://github.com/wuxiangru915/dsh-review-loop#readme)
- [返回dsh-review-loop所在分类](../plugins.md)
