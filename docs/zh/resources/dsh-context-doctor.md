---
title: "dsh-context-doctor"
description: "上下文注入审计插件：统计 AGENTS.md 指令链/技能目录/工具 schema 的 token 成本，检测重复与冲突。"
keywords: "dsh-context-doctor, memory, plugin, context, observability, deepseek harness, dsh"
---
# dsh-context-doctor

> ⭐ 7 · ✅ 活跃 · 插件

## 一句话介绍

上下文注入审计插件：统计 AGENTS.md 指令链/技能目录/工具 schema 的 token 成本，检测重复与冲突。

## 详细介绍

DSH 会话里，模型每个请求都自动携带一批注入物：层层叠加的 `AGENTS.md` 指令链、一百多个技能的目录摘要、几十个工具 schema、MCP 工具面。它们悄悄消耗输入 token，且经常出现跨文件重复段落、同名技能互相遮蔽、工具面膨胀——但平时没人量化，问题到上下文告警时才暴露。

## 作者
**[Zhenyu98](https://github.com/Zhenyu98)**

## 链接

- [GitHub 仓库](https://github.com/Zhenyu98/dsh-context-doctor)
- [完整 README](https://github.com/Zhenyu98/dsh-context-doctor#readme)
- [返回dsh-context-doctor所在分类](../plugins.md)
