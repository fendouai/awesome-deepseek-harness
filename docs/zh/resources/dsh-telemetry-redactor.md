---
title: "dsh-telemetry-redactor"
description: "Fail-closed export-copy redaction for DeepSeek Harness session telemetry"
keywords: "dsh-telemetry-redactor, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-telemetry-redactor

> ⭐ 3 · ✅ 活跃 · 插件

## 一句话介绍

Fail-closed export-copy redaction for DeepSeek Harness session telemetry

## 详细介绍

**Redact supported credential patterns from outbound telemetry copies before configured backends receive them—without rewriting canonical session logs.** dsh plugin --profile web add dsh-telemetry-redactor `dsh-telemetry-redactor` is a minimal DeepSeek Harness Profile Bundle that redacts sensitive values from session telemetry before a backend receives them. It mounts on the official `session-telemetry/record` waterfall, calls `next()` so other deployment rules still compose, and returns a new r

## 作者
**[030611](https://github.com/030611)**

## 链接

- [GitHub 仓库](https://github.com/030611/dsh-telemetry-redactor)
- [完整 README](https://github.com/030611/dsh-telemetry-redactor#readme)
- [返回dsh-telemetry-redactor所在分类](../plugins.md)
