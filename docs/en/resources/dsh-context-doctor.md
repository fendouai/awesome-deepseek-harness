---
title: "dsh-context-doctor"
description: "Audits what actually enters every model request: token cost of AGENTS.md chains, skill catalogs and tool schemas, with duplicate/conflict detection."
keywords: "dsh-context-doctor, memory, plugin, context, observability, deepseek harness, dsh"
---
# dsh-context-doctor

> ⭐ 7 · ✅ active · plugin

## One-liner

Audits what actually enters every model request: token cost of AGENTS.md chains, skill catalogs and tool schemas, with duplicate/conflict detection.

## About

DSH 会话里，模型每个请求都自动携带一批注入物：层层叠加的 `AGENTS.md` 指令链、一百多个技能的目录摘要、几十个工具 schema、MCP 工具面。它们悄悄消耗输入 token，且经常出现跨文件重复段落、同名技能互相遮蔽、工具面膨胀——但平时没人量化，问题到上下文告警时才暴露。

## Author
**[Zhenyu98](https://github.com/Zhenyu98)**

## Links

- [GitHub Repository](https://github.com/Zhenyu98/dsh-context-doctor)
- [Full README](https://github.com/Zhenyu98/dsh-context-doctor#readme)
- [Back to the Plugins list](../plugins.md)
