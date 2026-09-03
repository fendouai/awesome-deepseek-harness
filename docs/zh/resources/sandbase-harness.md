---
title: "sandbase-harness"
description: "开源 CMA 兼容的任意模型 Agent 运行时：MCP 工具、沙箱会话、审计与回放。"
keywords: "sandbase-harness, harness, related, mcp, security, deepseek harness, dsh"
---
# sandbase-harness

> ⭐ **628** · ✅ 活跃 · 相关

| | | | |
|---|---|---|---|
| 类型 | 相关 | 分类 | Harness |
| 星数 | ⭐ 628 | 状态 | ✅ 活跃 |
| 作者 | [sandbaseai](https://github.com/sandbaseai) | 更新时间 | 2026-08-20 |

## 一句话介绍

> 开源 CMA 兼容的任意模型 Agent 运行时：MCP 工具、沙箱会话、审计与回放。

## 详细介绍

[English](./README.md) | [中文](./README.zh-CN.md) AI-readable project metadata: [llms.txt](./llms.txt) · [installation guide](./llms-install.md) A local-first runtime for AI agents. Sessions, sandboxed tools, memory, credentials, audit trails, and a built-in Console — all running on your machine or in your own infrastructure. git clone --branch v0.3.8 --depth 1 https://github.com/sandbaseai/sandbase-harness.git cd sandbase-harness npm ci npm run build mkdir ../my-agents && cd ../my-agents node ../sandbase-harness/dist/index.js init node ../sandbase-harness/dist/index.js start

## ✨ 核心特性

- Claude Managed Agents-style `/v1` API and local Console
- SQLite-backed agents, sessions, environments, credential vaults, memory
- local file/skill bytes stored in the workspace state directory
- Resumable Server-Sent Events for session replay and debugging
- One active model provider boundary configured through Settings V2
- Sandbox backends: local process, Docker (per-session containers), Kubernetes
- Settings V2: one workspace model vendor, loop engine, storage, memory,
- MCP toolsets, permission policies, built-in tools, and skill packages

## 📦 安装

```bash
git clone --branch v0.3.8 --depth 1 https://github.com/sandbaseai/sandbase-harness.git
cd sandbase-harness
npm ci
npm run build
mkdir ../my-agents && cd ../my-agents
node ../sandbase-harness/dist/index.js init
node ../sandbase-harness/dist/index.js start
# open http://127.0.0.1:3000/dashboard
```

## 🚀 快速开始

```bash
node dist/index.js start --host 0.0.0.0
```

## 📚 更多信息

**Quick Start**

git clone --branch v0.3.8 --depth 1 https://github.com/sandbaseai/sandbase-harness.git cd sandbase-harness npm ci npm run build mkdir ../my-agents && cd ../my-agents node ../sandbase-harness/dist/index.js init node ../sandbase-harness/dist/index.js start Open `http://127.0.0.1:3000/dashboard`, go to **Settings > Models**, paste your API key, and you're running. The unscoped `managed-agents` name o

**Configuration**

`.managed-agents/config.yaml`: model: provider: openai api_key: ${OPENAI_API_KEY} storage: metadata: { provider: sqlite, options: {} } artifacts: { provider: local, options: { base_path: files } } Agents pick concrete model IDs (`gpt-4o`, `claude-sonnet-4-20250514`, `openai/gpt-5.5`). The workspace config only says how to reach the model service. For DeepSeek V4 Pro/Flash configuration, including 

**API Examples**

Create an agent: curl -X POST http://127.0.0.1:3000/v1/agents \ -H "Content-Type: application/json" \ -d '{ "name": "Incident commander", "model": "gpt-4o", "system": "You are an on-call incident commander.", "tools": [{ "type": "agent_toolset_20260401" }] }' Create an environment (local sandbox): curl -X POST http://127.0.0.1:3000/v1/environments \ -H "Content-Type: application/json" \ -d '{ "nam

## 🔗 链接

- [GitHub 仓库](https://github.com/sandbaseai/sandbase-harness)
- [完整 README](https://github.com/sandbaseai/sandbase-harness#readme)
- [返回sandbase-harness所在分类](../related.md)
