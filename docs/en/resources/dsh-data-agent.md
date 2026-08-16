---
title: "dsh-data-agent"
description: "Session-scoped database connections with a dedicated data agent: let the model connect to databases and write SQL."
keywords: "dsh-data-agent, research, agent, coding, deepseek harness, dsh"
---
# dsh-data-agent

> ⭐ 25 · ✅ active · agent

## One-liner

Session-scoped database connections with a dedicated data agent: let the model connect to databases and write SQL.

## About

[English](README.en.md) | **中文** 用AI写过SQL的同学都有这种体验，AI现在写代码能力已经很强了，但SQL逻辑老写不对。**原因是AI并没有与数据库操作形成Agent Loop**，它只能根据静态指令生成SQL，却无法感知执行结果、无法根据报错或返回数据动态调优。 这个插件就是来填这个坑的。它复用DeepSeek Harness强大的Agent主循环能力，让AI连上数据库并获得实时反馈，同时删掉所有跟数据无关的上下文和工具，让AI专注于SQL生成和业务数据分析。 我利用DeepSeek Harness的Agent预设功能，定义了专用的Data Agent预设。仅保留read、edit、write三个DSH自带的 tools，并自定义sqlcmd tool替代bash tool。 懂行的朋友一眼就能看出，这是借鉴了Pi Agent的设计，只使用最基本的工具。 用起来也很简单：在对话界面配好数据库连接，授权AI访问权限，然后就可以向AI提问，让AI帮你查询、更新、分析。

## Author
**[omdsh-dev](https://github.com/omdsh-dev)**

## Links

- [GitHub Repository](https://github.com/omdsh-dev/dsh-data-agent)
- [Full README](https://github.com/omdsh-dev/dsh-data-agent#readme)
- [Back to the Agents & Multi-Agent list](../agents.md)
