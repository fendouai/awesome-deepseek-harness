---
title: "dsh-agentlink"
description: "Caller-side bridge from Codex and other agent frameworks to DeepSeek Harness, with observable sessions, follow-up, cancellation, and human-gated approvals."
keywords: "dsh-agentlink, ide, integration, coding, multi-agent, deepseek harness, dsh"
---
# dsh-agentlink

> ⭐ **6** · ✅ 活跃 · 集成 · 近期 ⬆️ +3

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | IDE 与编辑器 |
| 星数 | ⭐ 6 | 状态 | ✅ 活跃 |
| 作者 | [hootandy321](https://github.com/hootandy321) | 更新时间 | 2026-08-20 |

## 一句话介绍

> Caller-side bridge from Codex and other agent frameworks to DeepSeek Harness, with observable sessions, follow-up, cancellation, and human-gated approvals.

## 详细介绍

dsh-Agentlink is a plugin that lets you use DeepSeek Harness (DSH) from the AI work tool you already use. Your primary agent can delegate implementation, research, debugging, and long-log work to DSH, then observe, continue, or cancel those sessions without leaving its normal workflow. Codex and Claude Code are supported, ZCode integration is in progress, and OpenCode, Workbuddy, and other popular AI coding and agent tools are planned.

## 📦 安装

```bash
git clone https://github.com/hootandy321/dsh-Agentlink.git
   cd dsh-Agentlink
   npm install
```

## 🚀 快速开始

```bash
npm run setup
   npm run doctor
```

## 📚 更多信息

**Installation**

Prepare the environment first: you need **Node.js 22+**, a supported caller (**Codex or Claude Code**), and a working **DSH CLI**. Configure your preferred model in DSH once; dsh-Agentlink uses that live route automatically.

**Install with your AI agent**

Send the following repository URL and prompt to Codex or another coding agent: Install dsh-Agentlink from https://github.com/hootandy321/dsh-Agentlink. Check Node.js 22+, the DSH CLI, and my DSH Web Host first. Clone it into a location I approve, run npm install and npm test. For Codex, run npm run setup -- --yes. For Claude Code, run npm run setup:claude -- --yes --project /absolute/path/to/my/pr

**Manual installation**

1. Check the environment. DSH CLI `0.1.0-rc.6` and `0.1.0-rc.7` are the current tested targets. ```bash node --version dsh --version ``` 2. Start the official DSH Web Host in its own terminal. ```bash dsh web ``` 3. Clone the repository and install its dependencies. ```bash git clone https://github.com/hootandy321/dsh-Agentlink.git cd dsh-Agentlink npm install ``` 4. Configure your caller. For Cod

**Roadmap**

These are planned directions, not implemented capabilities or release commitments. 1. **More caller entrypoints** — complete ZCode support, then add OpenCode, Workbuddy, Claude Desktop MCP, and other callers through the shared Integration Pack architecture. 2. **Agent invocation and information transport** — improve prompt organization, context packaging, output digests, and compression while keep

## 🔗 链接

- [GitHub 仓库](https://github.com/hootandy321/dsh-Agentlink)
- [完整 README](https://github.com/hootandy321/dsh-Agentlink#readme)
- [返回dsh-agentlink所在分类](../integrations.md)
