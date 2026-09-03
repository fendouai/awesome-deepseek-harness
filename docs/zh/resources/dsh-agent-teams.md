---
title: "dsh-agent-teams"
description: "面向团队的 DSH 多 Agent 扩展。"
keywords: "dsh-agent-teams, multi-agent, agent, workflow, deepseek harness, dsh"
---
# dsh-agent-teams

> ⭐ **746** · ✅ 活跃 · 智能体 · 近期 ⬆️ +75

| | | | |
|---|---|---|---|
| 类型 | 智能体 | 分类 | 多智能体 |
| 星数 | ⭐ 746 | 状态 | ✅ 活跃 |
| 作者 | [NanmiCoder](https://github.com/NanmiCoder) | 更新时间 | 2026-08-21 |

## 一句话介绍

> 面向团队的 DSH 多 Agent 扩展。

## 详细介绍

`dsh-agent-teams` turns the current DeepSeek Harness session into a captain that can assemble durable sub-agents, split a goal into dependency-aware tasks, and coordinate work through direct messages. Ask in natural language. The plugin provides the team protocol, eleven coordination tools, persistent state, an automatic shared-task scheduler, and a live Web UI—without requiring a separate workflow engine.

## 📦 安装

```bash
npm install --global @deepseek-ai/dsh@0.1.2-alpha.2
dsh --version
dsh plugin --profile web add @nanmicoder/dsh-agent-teams@latest
```

## 🚀 快速开始

```bash
dsh plugin --profile web add @nanmicoder/dsh-agent-teams@0.1.14
```

## 📚 更多信息

**Install**

> [!IMPORTANT] > **Plugin 0.1.15 (`@latest`) requires DeepSeek Harness 0.1.2-alpha.2.** Updating this plugin does not update Harness. This release has no adapter for the old RC host APIs. Check the version of the instance you actually launch with `dsh --version` before installing. **The default plugin release follows the current supported Harness developer preview: `latest=0.1.15`, for Harness Alp

**Configuration**

Defaults work without extra setup. A trusted profile can override member behavior: config: stateDir: .agent-teams memberProvider: spawn memberModel: deepseek-v4 memberMaxDepth: 1 maxMembers: 8 `memberProvider` is the sub-agent runtime backend (`spawn` / `fork`), not an LLM provider. Cross-LLM-provider routing uses the optional `provider` + `model` fields of `agent_teams_add_member`; `memberModel` 

## 🔗 链接

- [GitHub 仓库](https://github.com/NanmiCoder/dsh-agent-teams)
- [完整 README](https://github.com/NanmiCoder/dsh-agent-teams#readme)
- [返回dsh-agent-teams所在分类](../agents.md)
