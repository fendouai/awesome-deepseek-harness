---
title: "dsh-file-mount"
description: "Incremental file mounting with line-range deduplication: identical file contents are never re-sent to the model."
keywords: "dsh-file-mount, memory, plugin, context, files, deepseek harness, dsh"
---
# dsh-file-mount

> ⭐ 3 · ✅ active · plugin

## One-liner

Incremental file mounting with line-range deduplication: identical file contents are never re-sent to the model.

## About

DeepSeek Harness 插件：**文件增量挂载 + 重复读取去重**。记录每个文件哪些行范围已经进入模型上下文，重复读取只补缺失部分，文件在磁盘上变化时自动失效重挂，并提供一个「挂载文件」标签页实时展示账本。 移植自 [piwpi](https://github.com/earendil-works/pi-mono) 的 context-mount 机制。

## Author
**[acefun29](https://github.com/acefun29)**

## Links

- [GitHub Repository](https://github.com/acefun29/dsh-file-mount)
- [Full README](https://github.com/acefun29/dsh-file-mount#readme)
- [Back to the Plugins list](../plugins.md)
