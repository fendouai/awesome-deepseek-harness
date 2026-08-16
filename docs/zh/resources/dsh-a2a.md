---
title: "dsh-a2a"
description: "面向 Harness 的 Agent2Agent 网状网络。"
keywords: "dsh-a2a, multi-agent, agent, deepseek harness, dsh"
---
# dsh-a2a

> ⭐ 4 · ✅ 活跃 · 智能体

## 一句话介绍

面向 Harness 的 Agent2Agent 网状网络。

## 详细介绍

- id: a2a name: '@dpskh/a2a' config: hub: # optional: run the mesh hub server host: 127.0.0.1 port: 43123 # base bind port maxPort: 43223 # optional: walk up on EADDRINUSE mesh: # optional: mesh client project: main # project to connect to (defaults to main) agentId: main # local agent this presence belongs to name: main # roster name; defaults to the agent id autoConnect: true # connect when the configured agent registers persistConnections: false # remember each session's last connection and r

## 作者
**[dpskh](https://github.com/dpskh)**

## 链接

- [GitHub 仓库](https://github.com/dpskh/dsh-a2a)
- [完整 README](https://github.com/dpskh/dsh-a2a#readme)
- [返回dsh-a2a所在分类](../agents.md)
