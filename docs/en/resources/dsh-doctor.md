---
title: "dsh-doctor"
description: "Find what your DeepSeek Harness (dsh) patches silently broke — dead patches, config fields dropped by whole-config replacement, unmaintained plugins. Read-only, zero deps."
keywords: "dsh-doctor, discovery, plugin, coding, deepseek harness, dsh"
---
# dsh-doctor

> ⭐ 1 · ✅ active · plugin

## One-liner

Find what your DeepSeek Harness (dsh) patches silently broke — dead patches, config fields dropped by whole-config replacement, unmaintained plugins. Read-only, zero deps.

## About

Deterministic diagnostics and recovery for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness). DSH Doctor is the safety net for the two ways a Harness usually breaks itself: it **cannot converse** (the Web UI opens but the loop is broken), or it **cannot start** (boot fails after a config, dependency, or plugin change). When the Web UI still opens, the Doctor button calls a loopback-only Host recovery service. When Harness cannot start, the same engine runs as a standalone CLI —

## Author
**[asdf17128](https://github.com/asdf17128)**

## Links

- [GitHub Repository](https://github.com/asdf17128/dsh-doctor)
- [Full README](https://github.com/asdf17128/dsh-doctor#readme)
- [Back to the Plugins list](../plugins.md)
