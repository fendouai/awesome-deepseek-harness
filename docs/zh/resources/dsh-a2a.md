---
title: "dsh-a2a"
description: "DSH 的 A2A v1.0 双端插件:Client 发现远程 Agent 并映射为工具,Server 对外提供 JSON-RPC/SSE 端点与连接面板 ｜ A2A v1.0 dual-mode DSH plugin: A2A client (skills as tools) + A2A server (JSON-RPC/SSE) with dashboard."
keywords: "dsh-a2a, multi-agent, agent, coding, deepseek harness, dsh"
---
# dsh-a2a

> ⭐ **7** · ✅ 活跃 · 智能体

| | | | |
|---|---|---|---|
| 类型 | 智能体 | 分类 | 多智能体 |
| 星数 | ⭐ 7 | 状态 | ✅ 活跃 |
| 作者 | [ryubyte](https://github.com/ryubyte) | 更新时间 | — |

## 一句话介绍

> DSH 的 A2A v1.0 双端插件:Client 发现远程 Agent 并映射为工具,Server 对外提供 JSON-RPC/SSE 端点与连接面板 ｜ A2A v1.0 dual-mode DSH plugin: A2A client (skills as tools) + A2A server (JSON-RPC/SSE) with dashboard.

## 详细介绍

- id: a2a name: '@dpskh/a2a' config: hub: # optional: run the mesh hub server host: 127.0.0.1 port: 43123 # base bind port maxPort: 43223 # optional: walk up on EADDRINUSE mesh: # optional: mesh client project: main # project to connect to (defaults to main) agentId: main # local agent this presence belongs to name: main # roster name; defaults to the agent id autoConnect: true # connect when the configured agent registers persistConnections: false # remember each session's last connection and rejoin it reconnectMs: 500 # initial reconnect delay (doubles to 10 s) The hub needs a routed storage backend: mount `@deepseek-ai/dsh-storage`, a backend (`storage-json` or `storage-sqlite`), and `@deepseek-ai/dsh-storage-domain` with the backend routed to the `a2a` domain. The entry plugin composes

## ✨ 核心特性

- id: a2a

## 📚 更多信息

**Configuration**

name: '@dpskh/a2a' config: hub: # optional: run the mesh hub server host: 127.0.0.1 port: 43123 # base bind port maxPort: 43223 # optional: walk up on EADDRINUSE mesh: # optional: mesh client project: main # project to connect to (defaults to main) agentId: main # local agent this presence belongs to name: main # roster name; defaults to the agent id autoConnect: true # connect when the configured

## 🔗 链接

- [GitHub 仓库](https://github.com/ryubyte/dsh-a2a)
- [完整 README](https://github.com/ryubyte/dsh-a2a#readme)
- [返回dsh-a2a所在分类](../agents.md)
