---
title: "dsh-chatgpt-bridge"
description: "MCP bridge that lets ChatGPT web create, view, continue, and control DeepSeek Harness (DSH) agent sessions."
keywords: "dsh-chatgpt-bridge, mcp, integration, coding, multi-agent, deepseek harness, dsh"
---
# dsh-chatgpt-bridge

> ⭐ **14** · ✅ active · integration

| | | | |
|---|---|---|---|
| Type | integration | Category | MCP |
| Stars | ⭐ 14 | Status | ✅ active |
| Author | [jiezeng2004-design](https://github.com/jiezeng2004-design) | Updated | — |

## One-liner

> MCP bridge that lets ChatGPT web create, view, continue, and control DeepSeek Harness (DSH) agent sessions.

## About

`dsh-chatgpt-bridge` connects **ChatGPT Web → secure MCP tunnel → DeepSeek Harness (DSH)**. ChatGPT becomes the control surface; DSH keeps the agent loop, tools, skills, subagents, workflows, sandbox, approvals and workspace security model. **The bridge connects the two sides. It does not replace DSH, modify DSH core, or route DSH model traffic through ChatGPT.** Current package: **v0.5.1**, targeting DeepSeek Harness **0.1.1-rc.2**. After a successful connection, ChatGPT should see **tool count = 23**.

## ✨ Key Features

- create and inspect native DSH sessions;
- send follow-up instructions without copying context between apps;
- start, inspect, update and wait on Goals;
- approve DSH actions through the bridge when your DSH policy requires it;
- list registered workspaces and inspect runtime health;
- keep using DSH's own sandbox, approval and workspace boundaries;
- manage the supported tunnel runtime from the DSH Web settings UI.

## 📦 Install

```bash
dsh plugin --profile web add dsh-chatgpt-bridge
```

## 🚀 Quick Start

```bash
dsh web
```

## 📚 Learn more

**1. Install the plugin**

dsh plugin --profile web add dsh-chatgpt-bridge `npm install dsh-chatgpt-bridge` alone is not enough: the plugin must be added to a DSH profile bundle.

## 🔗 Links

- [GitHub Repository](https://github.com/jiezeng2004-design/dsh-chatgpt-bridge)
- [Full README](https://github.com/jiezeng2004-design/dsh-chatgpt-bridge#readme)
- [Back to the MCP & Integrations list](../integrations.md)
