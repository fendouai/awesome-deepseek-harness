---
title: "dsh-agent-teams"
description: "Multi-agent team-oriented extensions for DSH."
keywords: "dsh-agent-teams, multi-agent, agent, workflow, deepseek harness, dsh"
---
# dsh-agent-teams

> ⭐ **746** · ✅ active · agent · ⬆️ +75 recently

| | | | |
|---|---|---|---|
| Type | agent | Category | Multi-agent |
| Stars | ⭐ 746 | Status | ✅ active |
| Author | [NanmiCoder](https://github.com/NanmiCoder) | Updated | 2026-08-21 |

## One-liner

> Multi-agent team-oriented extensions for DSH.

## About

`dsh-agent-teams` turns the current DeepSeek Harness session into a captain that can assemble durable sub-agents, split a goal into dependency-aware tasks, and coordinate work through direct messages. Ask in natural language. The plugin provides the team protocol, eleven coordination tools, persistent state, an automatic shared-task scheduler, and a live Web UI—without requiring a separate workflow engine.

## 📦 Install

```bash
npm install --global @deepseek-ai/dsh@0.1.2-alpha.2
dsh --version
dsh plugin --profile web add @nanmicoder/dsh-agent-teams@latest
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add @nanmicoder/dsh-agent-teams@0.1.14
```

## 📚 Learn more

**Install**

> [!IMPORTANT] > **Plugin 0.1.15 (`@latest`) requires DeepSeek Harness 0.1.2-alpha.2.** Updating this plugin does not update Harness. This release has no adapter for the old RC host APIs. Check the version of the instance you actually launch with `dsh --version` before installing. **The default plugin release follows the current supported Harness developer preview: `latest=0.1.15`, for Harness Alp

**Configuration**

Defaults work without extra setup. A trusted profile can override member behavior: config: stateDir: .agent-teams memberProvider: spawn memberModel: deepseek-v4 memberMaxDepth: 1 maxMembers: 8 `memberProvider` is the sub-agent runtime backend (`spawn` / `fork`), not an LLM provider. Cross-LLM-provider routing uses the optional `provider` + `model` fields of `agent_teams_add_member`; `memberModel` 

## 🔗 Links

- [GitHub Repository](https://github.com/NanmiCoder/dsh-agent-teams)
- [Full README](https://github.com/NanmiCoder/dsh-agent-teams#readme)
- [Back to the Agents & Multi-Agent list](../agents.md)
