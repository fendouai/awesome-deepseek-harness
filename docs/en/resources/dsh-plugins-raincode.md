---
title: "dsh-plugins-raincode"
description: "dsh plugin: DeepSeek Harness 的模型层 = raincode(模型池/缓存/重试) + /skills 浏览"
keywords: "dsh-plugins-raincode, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-plugins-raincode

> ⭐ 3 · ✅ active · plugin

## One-liner

dsh plugin: DeepSeek Harness 的模型层 = raincode(模型池/缓存/重试) + /skills 浏览

## About

Make **raincode** the model layer of **DeepSeek Harness (dsh)**: a cheap model pool with StablePrefix prompt caching, retries, and failover, driven by a local OpenAI-compatible gateway. Inside dsh you can pick any model from your raincode pool and browse the raincode skill library with `/skills`. The plugin is the "mouth" — it translates dsh's `GenerateOptions` to the OpenAI wire format and streams chunks back — while the raincode gateway (Rust) is the "brain" that owns profile selection, cachin

## Author
**[rainforest888](https://github.com/rainforest888)**

## Links

- [GitHub Repository](https://github.com/rainforest888/dsh-plugins-raincode)
- [Full README](https://github.com/rainforest888/dsh-plugins-raincode#readme)
- [Back to the Plugins list](../plugins.md)
