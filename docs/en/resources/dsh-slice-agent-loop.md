---
title: "dsh-slice-agent-loop"
description: "Drop-in agent loop whose context engine is a bounded slice instead of a growing transcript."
keywords: "dsh-slice-agent-loop, multi-agent, agent, context, workflow, deepseek harness, dsh"
---
# dsh-slice-agent-loop

> ⭐ 1 · ✅ active · agent

## One-liner

Drop-in agent loop whose context engine is a bounded slice instead of a growing transcript.

## About

That sounds like common sense, but today's mainstream coding agents replay the entire conversation history back to the model every call: the excess is never trimmed, and what falls short can never be recovered. This plugin brings a slice loop built around that one sentence into the [DeepSeek Harness](https://github.com/dsh2026): **same harness, same model, same tools and persistence — only the agent loop is swapped**, so in every comparison below the loop itself is the only variable. Early beta;

## Author
**[TT-Wang](https://github.com/TT-Wang)**

## Links

- [GitHub Repository](https://github.com/TT-Wang/dsh-slice-agent-loop)
- [Full README](https://github.com/TT-Wang/dsh-slice-agent-loop#readme)
- [Back to the Agents & Multi-Agent list](../agents.md)
