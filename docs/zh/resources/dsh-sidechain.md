---
title: "dsh-sidechain"
description: "侧会话：/side 持续性侧会话（Codex 风格）与 /btw 一次性侧问（Claude 风格），临时 fork 中运行。"
keywords: "dsh-sidechain, multi-agent, agent, context, deepseek harness, dsh"
---
# dsh-sidechain

> ⭐ 7 · ✅ 活跃 · 智能体

## 一句话介绍

侧会话：/side 持续性侧会话（Codex 风格）与 /btw 一次性侧问（Claude 风格），临时 fork 中运行。

## 详细介绍

DSH 侧会话插件。它通过 fork 当前会话创建独立子会话，让用户在不中断主线程的情况下发起一次性问题或持续对话。 当前版本适配公开版 DSH rc.5（npm `0.0.1-rc.5`，源码提交 `47f94385`）。 侧会话继承主会话已经完成的回合作为参考上下文，但拥有独立的消息记录和执行过程。侧会话的提示、思考、工具调用和回答不会进入主会话的模型上下文。

## 作者
**[omdsh-dev](https://github.com/omdsh-dev)**

## 链接

- [GitHub 仓库](https://github.com/omdsh-dev/dsh-sidechain)
- [完整 README](https://github.com/omdsh-dev/dsh-sidechain#readme)
- [返回dsh-sidechain所在分类](../agents.md)
