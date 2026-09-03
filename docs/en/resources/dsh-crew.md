---
title: "dsh-crew"
description: "dsh plugin: run work as a small crew of role agents (product manager, researcher, architect, engineer, QA, code reviewer, security reviewer, doc reviewer) that share work through files on disk"
keywords: "dsh-crew, search, plugin, coding, multi-agent, deepseek harness, dsh"
---
# dsh-crew

> ⭐ **7** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 7 | Status | ✅ active |
| Author | [stuarthu](https://github.com/stuarthu) | Updated | — |
| Subcategory | 🌐 Web search | Capabilities | coding, multi-agent, search |

## One-liner

> dsh plugin: run work as a small crew of role agents (product manager, researcher, architect, engineer, QA, code reviewer, security reviewer, doc reviewer) that share work through files on disk

## About

DSH Crew is a plugin for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (DSH) — an open-source agent harness. It makes DSH agents dispatchable from Claude Code, Codex, Antigravity and Grok: the orchestrator keeps its own model, the work runs on a real DSH agent with that harness's tools, sandbox, presets and session history, and the host still shows it as a native subagent with live progress. What runs the work is a DSH agent, not a bare model call. Tiers (`flash` / `pro`) select how much capability that agent gets from the harness's configured roster — DeepSeek V4 Flash and V4 Pro today — so a change of model in DSH needs no change here.

## 📦 Install

```bash
dsh plugin --profile web add @zseven-w/dsh-crew@latest
dsh web
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add link:/path/to/dsh-crew
dsh web
```

## 📚 Learn more

**📦 One-Click Install**

The settings page installs and updates the Claude Code plugin, the Codex role files and the Antigravity / Grok agents, skills and commands for you — marketplace registration, permission allowlist, HUD wiring, absolute paths rendered for this machine — and restores them just as easily. Every settings file is backed up first. </td> </tr> </table>

**Install**

Install into a DSH profile from npm: dsh plugin --profile web add @zseven-w/dsh-crew@latest dsh web Or, for local development straight from the source tree: dsh plugin --profile web add link:/path/to/dsh-crew dsh web The `link:` protocol symlinks the profile dependency to this repository, so rebuilds are visible immediately.

**Configure DeepSeek credentials (standalone only)**

In hub mode — the installation above — workers run inside the DSH instance and use the DeepSeek credentials it is already configured with. Nothing else to set up. Only the standalone fallback needs a key of its own: dispatching from a host with no DSH instance running launches a worker runtime as a separate process. Obtain an API key from [platform.deepseek.com](https://platform.deepseek.com) and 

**Installation**

One-click installation (choose one): Both do the same thing: register local marketplace (the repo itself, via `.claude-plugin/marketplace.json`) + `claude plugin install` + MCP tool permission allowlist + claude-hud worker status segment config (auto-backup settings.json before changes, idempotent). **Restart the session after installation for changes to take effect.**

## 🔗 Links

- [GitHub Repository](https://github.com/stuarthu/dsh-crew)
- [Full README](https://github.com/stuarthu/dsh-crew#readme)
- [Back to the Plugins list](../plugins.md)
