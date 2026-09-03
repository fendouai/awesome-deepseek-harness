---
title: "dsh-chatgpt-bridge"
description: "MCP bridge that lets ChatGPT web create, view, continue, and control DeepSeek Harness (DSH) agent sessions."
keywords: "dsh-chatgpt-bridge, mcp, integration, coding, multi-agent, deepseek harness, dsh"
---
# dsh-chatgpt-bridge

> ⭐ **14** · ✅ 活跃 · 集成

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | MCP |
| 星数 | ⭐ 14 | 状态 | ✅ 活跃 |
| 作者 | [jiezeng2004-design](https://github.com/jiezeng2004-design) | 更新时间 | — |

## 一句话介绍

> MCP bridge that lets ChatGPT web create, view, continue, and control DeepSeek Harness (DSH) agent sessions.

## 详细介绍

`dsh-chatgpt-bridge` connects **ChatGPT Web → secure MCP tunnel → DeepSeek Harness (DSH)**. ChatGPT becomes the control surface; DSH keeps the agent loop, tools, skills, subagents, workflows, sandbox, approvals and workspace security model. **The bridge connects the two sides. It does not replace DSH, modify DSH core, or route DSH model traffic through ChatGPT.** Current package: **v0.5.1**, targeting DeepSeek Harness **0.1.1-rc.2**. After a successful connection, ChatGPT should see **tool count = 23**.

## ✨ 核心特性

- create and inspect native DSH sessions;
- send follow-up instructions without copying context between apps;
- start, inspect, update and wait on Goals;
- approve DSH actions through the bridge when your DSH policy requires it;
- list registered workspaces and inspect runtime health;
- keep using DSH's own sandbox, approval and workspace boundaries;
- manage the supported tunnel runtime from the DSH Web settings UI.

## 📦 安装

```bash
dsh plugin --profile web add dsh-chatgpt-bridge
```

## 🚀 快速开始

```bash
dsh web
```

## 📚 更多信息

**1. Install the plugin**

dsh plugin --profile web add dsh-chatgpt-bridge `npm install dsh-chatgpt-bridge` alone is not enough: the plugin must be added to a DSH profile bundle.

## 🔗 链接

- [GitHub 仓库](https://github.com/jiezeng2004-design/dsh-chatgpt-bridge)
- [完整 README](https://github.com/jiezeng2004-design/dsh-chatgpt-bridge#readme)
- [返回dsh-chatgpt-bridge所在分类](../integrations.md)
