---
title: "dsh-plugins-raincode"
description: "dsh plugin: DeepSeek Harness 的模型层 = raincode(模型池/缓存/重试) + /skills 浏览"
keywords: "dsh-plugins-raincode, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-plugins-raincode

> ⭐ 3 · ✅ 活跃 · 插件

## 一句话介绍

dsh plugin: DeepSeek Harness 的模型层 = raincode(模型池/缓存/重试) + /skills 浏览

## 详细介绍

Make **raincode** the model layer of **DeepSeek Harness (dsh)**: a cheap model pool with StablePrefix prompt caching, retries, and failover, driven by a local OpenAI-compatible gateway. Inside dsh you can pick any model from your raincode pool and browse the raincode skill library with `/skills`. The plugin is the "mouth" — it translates dsh's `GenerateOptions` to the OpenAI wire format and streams chunks back — while the raincode gateway (Rust) is the "brain" that owns profile selection, cachin

## 作者
**[rainforest888](https://github.com/rainforest888)**

## 链接

- [GitHub 仓库](https://github.com/rainforest888/dsh-plugins-raincode)
- [完整 README](https://github.com/rainforest888/dsh-plugins-raincode#readme)
- [返回dsh-plugins-raincode所在分类](../plugins.md)
