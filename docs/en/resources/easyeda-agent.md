---
title: "easyeda-agent"
description: "EasyEDA Pro automation: Go daemon + in-app connector + agent skill + stdio MCP server for typed schematic/PCB actions, workflow gates, and DRC."
keywords: "easyeda-agent, learning, skill, mcp, coding, deepseek harness, dsh"
---
# easyeda-agent

> ⭐ 224 · ✅ active · skill

## One-liner

EasyEDA Pro automation: Go daemon + in-app connector + agent skill + stdio MCP server for typed schematic/PCB actions, workflow gates, and DRC.

## About

上游 `run-api-gateway` 证明了关键入口:代码能跑在 EasyEDA 内、访问官方 `eda` 对象。但它把「裸 JavaScript 执行」当作主工作流——强大,但对 AI agent 太脆弱。 本项目的连接器是真实可用的:daemon **固定监听单端口 `60832`(`0xEDA0`,"EDA" 写进十六进制;0.15.0 起弃用与官方 gateway 冲突的 49620)**(不外溢、被占用时自动接管旧 easyeda daemon)、连接器锁定该端口、校验握手、**自愈重连**、把一套**有类型的动作目录**分发到官方 `eda.*` API。裸 JS 仅作为需二次确认的 `debug.exec_js` 逃生口保留。 - **Skill** 描述专家工作流和护栏; - **Go CLI/daemon** 暴露稳定的 typed actions; - **EasyEDA 连接器插件** 只做到官方 `eda.*` 的桥接; - 产物、截图、DRC 结果、审计日志都是一等输出。

## Author
**[zhoushoujianwork](https://github.com/zhoushoujianwork)**

## Links

- [GitHub Repository](https://github.com/zhoushoujianwork/easyeda-agent)
- [Full README](https://github.com/zhoushoujianwork/easyeda-agent#readme)
- [Back to the Skills list](../skills.md)
