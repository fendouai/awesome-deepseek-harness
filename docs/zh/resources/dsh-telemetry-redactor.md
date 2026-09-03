---
title: "dsh-telemetry-redactor"
description: "Fail-closed export-copy redaction for DeepSeek Harness session telemetry"
keywords: "dsh-telemetry-redactor, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-telemetry-redactor

> ⭐ **3** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 3 | 状态 | ✅ 活跃 |
| 作者 | [030611](https://github.com/030611) | 更新时间 | 2026-08-14 |
| 子分类 | 📁 文件与导入 | 能力 | coding |

## 一句话介绍

> Fail-closed export-copy redaction for DeepSeek Harness session telemetry

## 详细介绍

**Redact supported credential patterns from outbound telemetry copies before configured backends receive them—without rewriting canonical session logs.** dsh plugin --profile web add dsh-telemetry-redactor `dsh-telemetry-redactor` is a minimal DeepSeek Harness Profile Bundle that redacts sensitive values from session telemetry before a backend receives them. It mounts on the official `session-telemetry/record` waterfall, calls `next()` so other deployment rules still compose, and returns a new recursively redacted record. The official telemetry coordinator deep-copies canonical session events before this waterfall and contains thrown rules per record. Therefore this plugin changes only the outbound copy: it never rewrites the canonical session log. In this document, **fail-closed means onl

## ✨ 核心特性

- Values under high-risk key names such as `authorization`, `cookie`, `credential`, `password`, `secret`, `token`, `apiKey`, `access_token`, `clientSecret`, and `
- Bearer and Basic authorization values embedded in strings.
- Common credential forms including `sk-...`, GitHub tokens, Slack tokens, JWT-like triples, and `token=...` / `api_key: ...` assignments.

## 📦 安装

```bash
dsh plugin --profile web add dsh-telemetry-redactor
```

## 🚀 快速开始

```bash
dsh plugin --profile web add dsh-telemetry-redactor
dsh --profile web --dump-config
```

## 📚 更多信息

**Install**

Install the public package into the selected DSH profile, then inspect the resolved configuration: dsh plugin --profile web add dsh-telemetry-redactor dsh --profile web --dump-config The dump must contain the inserted `telemetry-redactor` row. The bundle does not add, replace, or enable a telemetry backend; it only protects records handled by whatever backend the deployment already selected.

**Configuration**

The only option is `replacement`, which defaults to `[REDACTED]`. It must contain 1 to 128 characters and must not itself match a supported credential pattern; invalid values fail loudly when the Cordis plugin fiber is awaited. config: replacement: '[TELEMETRY-REDACTED]' The key and pattern rules are fixed security behavior and cannot be disabled through configuration.

## 🔗 链接

- [GitHub 仓库](https://github.com/030611/dsh-telemetry-redactor)
- [完整 README](https://github.com/030611/dsh-telemetry-redactor#readme)
- [返回dsh-telemetry-redactor所在分类](../plugins.md)
