---
title: "dsh-sidechain"
description: "Side sessions: persistent /side sessions (Codex style) and one-off /btw questions (Claude style) in temporary forks."
keywords: "dsh-sidechain, multi-agent, agent, context, deepseek harness, dsh"
---
# dsh-sidechain

> ⭐ 7 · ✅ active · agent

## One-liner

Side sessions: persistent /side sessions (Codex style) and one-off /btw questions (Claude style) in temporary forks.

## About

DSH 侧会话插件。它通过 fork 当前会话创建独立子会话，让用户在不中断主线程的情况下发起一次性问题或持续对话。 当前版本适配公开版 DSH rc.5（npm `0.0.1-rc.5`，源码提交 `47f94385`）。 侧会话继承主会话已经完成的回合作为参考上下文，但拥有独立的消息记录和执行过程。侧会话的提示、思考、工具调用和回答不会进入主会话的模型上下文。

## Author
**[omdsh-dev](https://github.com/omdsh-dev)**

## Links

- [GitHub Repository](https://github.com/omdsh-dev/dsh-sidechain)
- [Full README](https://github.com/omdsh-dev/dsh-sidechain#readme)
- [Back to the Agents & Multi-Agent list](../agents.md)
