---
title: "dsh-doctor"
description: "Find what your DeepSeek Harness (dsh) patches silently broke — dead patches, config fields dropped by whole-config replacement, unmaintained plugins. Read-only, zero deps."
keywords: "dsh-doctor, discovery, plugin, coding, deepseek harness, dsh"
---
# dsh-doctor

> ⭐ 1 · ✅ 活跃 · 插件

## 一句话介绍

Find what your DeepSeek Harness (dsh) patches silently broke — dead patches, config fields dropped by whole-config replacement, unmaintained plugins. Read-only, zero deps.

## 详细介绍

Deterministic diagnostics and recovery for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness). DSH Doctor is the safety net for the two ways a Harness usually breaks itself: it **cannot converse** (the Web UI opens but the loop is broken), or it **cannot start** (boot fails after a config, dependency, or plugin change). When the Web UI still opens, the Doctor button calls a loopback-only Host recovery service. When Harness cannot start, the same engine runs as a standalone CLI —

## 作者
**[asdf17128](https://github.com/asdf17128)**

## 链接

- [GitHub 仓库](https://github.com/asdf17128/dsh-doctor)
- [完整 README](https://github.com/asdf17128/dsh-doctor#readme)
- [返回dsh-doctor所在分类](../plugins.md)
