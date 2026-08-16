---
title: "dsh-file-mount"
description: "增量文件挂载 + 行区间去重：相同文件内容不再重复发送给模型。"
keywords: "dsh-file-mount, memory, plugin, context, files, deepseek harness, dsh"
---
# dsh-file-mount

> ⭐ 3 · ✅ 活跃 · 插件

## 一句话介绍

增量文件挂载 + 行区间去重：相同文件内容不再重复发送给模型。

## 详细介绍

DeepSeek Harness 插件：**文件增量挂载 + 重复读取去重**。记录每个文件哪些行范围已经进入模型上下文，重复读取只补缺失部分，文件在磁盘上变化时自动失效重挂，并提供一个「挂载文件」标签页实时展示账本。 移植自 [piwpi](https://github.com/earendil-works/pi-mono) 的 context-mount 机制。

## 作者
**[acefun29](https://github.com/acefun29)**

## 链接

- [GitHub 仓库](https://github.com/acefun29/dsh-file-mount)
- [完整 README](https://github.com/acefun29/dsh-file-mount#readme)
- [返回dsh-file-mount所在分类](../plugins.md)
