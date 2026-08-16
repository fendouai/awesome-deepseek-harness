---
title: "dsh-llm-fallbacks"
description: "Role-based LLM retry and fallback strategy plugin."
keywords: "dsh-llm-fallbacks, multi-agent, agent, context, automation, deepseek harness, dsh"
---
# dsh-llm-fallbacks

> ⭐ 4 · ✅ active · agent

## One-liner

Role-based LLM retry and fallback strategy plugin.

## About

[English](README.md) | [中文](README.zh-CN.md) Automatic provider/model fallback chains for dsh (DeepSeek Harness): when an agent's LLM requests keep failing — retries exhausted, auth errors, quota exceeded, rate limiting (429) — the plugin switches provider/model along the fallback chain for the current role, and the current step/turn continues on the target model: tasks are not interrupted by model problems. Install with a single command (see [Install](#install)): dsh plugin --profile web add ds

## Author
**[omdsh-dev](https://github.com/omdsh-dev)**

## Links

- [GitHub Repository](https://github.com/omdsh-dev/dsh-llm-fallbacks)
- [Full README](https://github.com/omdsh-dev/dsh-llm-fallbacks#readme)
- [Back to the Agents & Multi-Agent list](../agents.md)
