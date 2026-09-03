---
title: "dsh-crew"
description: "dsh plugin: run work as a small crew of role agents (product manager, researcher, architect, engineer, QA, code reviewer, security reviewer, doc reviewer) that share work through files on disk"
keywords: "dsh-crew, search, plugin, coding, multi-agent, deepseek harness, dsh"
---
# dsh-crew

> ⭐ **7** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 搜索与研究 |
| 星数 | ⭐ 7 | 状态 | ✅ 活跃 |
| 作者 | [stuarthu](https://github.com/stuarthu) | 更新时间 | — |
| 子分类 | 🌐 网页搜索 | 能力 | coding, multi-agent, search |

## 一句话介绍

> dsh plugin: run work as a small crew of role agents (product manager, researcher, architect, engineer, QA, code reviewer, security reviewer, doc reviewer) that share work through files on disk

## 详细介绍

DSH Crew is a plugin for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (DSH) — an open-source agent harness. It makes DSH agents dispatchable from Claude Code, Codex, Antigravity and Grok: the orchestrator keeps its own model, the work runs on a real DSH agent with that harness's tools, sandbox, presets and session history, and the host still shows it as a native subagent with live progress. What runs the work is a DSH agent, not a bare model call. Tiers (`flash` / `pro`) select how much capability that agent gets from the harness's configured roster — DeepSeek V4 Flash and V4 Pro today — so a change of model in DSH needs no change here.

## 📦 安装

```bash
dsh plugin --profile web add @zseven-w/dsh-crew@latest
dsh web
```

## 🚀 快速开始

```bash
dsh plugin --profile web add link:/path/to/dsh-crew
dsh web
```

## 📚 更多信息

**📦 One-Click Install**

The settings page installs and updates the Claude Code plugin, the Codex role files and the Antigravity / Grok agents, skills and commands for you — marketplace registration, permission allowlist, HUD wiring, absolute paths rendered for this machine — and restores them just as easily. Every settings file is backed up first. </td> </tr> </table>

**Install**

Install into a DSH profile from npm: dsh plugin --profile web add @zseven-w/dsh-crew@latest dsh web Or, for local development straight from the source tree: dsh plugin --profile web add link:/path/to/dsh-crew dsh web The `link:` protocol symlinks the profile dependency to this repository, so rebuilds are visible immediately.

**Configure DeepSeek credentials (standalone only)**

In hub mode — the installation above — workers run inside the DSH instance and use the DeepSeek credentials it is already configured with. Nothing else to set up. Only the standalone fallback needs a key of its own: dispatching from a host with no DSH instance running launches a worker runtime as a separate process. Obtain an API key from [platform.deepseek.com](https://platform.deepseek.com) and 

**Installation**

One-click installation (choose one): Both do the same thing: register local marketplace (the repo itself, via `.claude-plugin/marketplace.json`) + `claude plugin install` + MCP tool permission allowlist + claude-hud worker status segment config (auto-backup settings.json before changes, idempotent). **Restart the session after installation for changes to take effect.**

## 🔗 链接

- [GitHub 仓库](https://github.com/stuarthu/dsh-crew)
- [完整 README](https://github.com/stuarthu/dsh-crew#readme)
- [返回dsh-crew所在分类](../plugins.md)
