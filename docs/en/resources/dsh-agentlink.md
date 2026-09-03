---
title: "dsh-agentlink"
description: "Caller-side bridge from Codex and other agent frameworks to DeepSeek Harness, with observable sessions, follow-up, cancellation, and human-gated approvals."
keywords: "dsh-agentlink, ide, integration, coding, multi-agent, deepseek harness, dsh"
---
# dsh-agentlink

> ⭐ **6** · ✅ active · integration · ⬆️ +3 recently

| | | | |
|---|---|---|---|
| Type | integration | Category | IDE & editors |
| Stars | ⭐ 6 | Status | ✅ active |
| Author | [hootandy321](https://github.com/hootandy321) | Updated | 2026-08-20 |

## One-liner

> Caller-side bridge from Codex and other agent frameworks to DeepSeek Harness, with observable sessions, follow-up, cancellation, and human-gated approvals.

## About

dsh-Agentlink is a plugin that lets you use DeepSeek Harness (DSH) from the AI work tool you already use. Your primary agent can delegate implementation, research, debugging, and long-log work to DSH, then observe, continue, or cancel those sessions without leaving its normal workflow. Codex and Claude Code are supported, ZCode integration is in progress, and OpenCode, Workbuddy, and other popular AI coding and agent tools are planned.

## 📦 Install

```bash
git clone https://github.com/hootandy321/dsh-Agentlink.git
   cd dsh-Agentlink
   npm install
```

## 🚀 Quick Start

```bash
npm run setup
   npm run doctor
```

## 📚 Learn more

**Installation**

Prepare the environment first: you need **Node.js 22+**, a supported caller (**Codex or Claude Code**), and a working **DSH CLI**. Configure your preferred model in DSH once; dsh-Agentlink uses that live route automatically.

**Install with your AI agent**

Send the following repository URL and prompt to Codex or another coding agent: Install dsh-Agentlink from https://github.com/hootandy321/dsh-Agentlink. Check Node.js 22+, the DSH CLI, and my DSH Web Host first. Clone it into a location I approve, run npm install and npm test. For Codex, run npm run setup -- --yes. For Claude Code, run npm run setup:claude -- --yes --project /absolute/path/to/my/pr

**Manual installation**

1. Check the environment. DSH CLI `0.1.0-rc.6` and `0.1.0-rc.7` are the current tested targets. ```bash node --version dsh --version ``` 2. Start the official DSH Web Host in its own terminal. ```bash dsh web ``` 3. Clone the repository and install its dependencies. ```bash git clone https://github.com/hootandy321/dsh-Agentlink.git cd dsh-Agentlink npm install ``` 4. Configure your caller. For Cod

**Roadmap**

These are planned directions, not implemented capabilities or release commitments. 1. **More caller entrypoints** — complete ZCode support, then add OpenCode, Workbuddy, Claude Desktop MCP, and other callers through the shared Integration Pack architecture. 2. **Agent invocation and information transport** — improve prompt organization, context packaging, output digests, and compression while keep

## 🔗 Links

- [GitHub Repository](https://github.com/hootandy321/dsh-Agentlink)
- [Full README](https://github.com/hootandy321/dsh-Agentlink#readme)
- [Back to the MCP & Integrations list](../integrations.md)
