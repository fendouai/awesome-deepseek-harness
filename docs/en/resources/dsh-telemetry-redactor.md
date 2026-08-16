---
title: "dsh-telemetry-redactor"
description: "Fail-closed export-copy redaction for DeepSeek Harness session telemetry"
keywords: "dsh-telemetry-redactor, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-telemetry-redactor

> ⭐ 3 · ✅ active · plugin

## One-liner

Fail-closed export-copy redaction for DeepSeek Harness session telemetry

## About

**Redact supported credential patterns from outbound telemetry copies before configured backends receive them—without rewriting canonical session logs.** dsh plugin --profile web add dsh-telemetry-redactor `dsh-telemetry-redactor` is a minimal DeepSeek Harness Profile Bundle that redacts sensitive values from session telemetry before a backend receives them. It mounts on the official `session-telemetry/record` waterfall, calls `next()` so other deployment rules still compose, and returns a new r

## Author
**[030611](https://github.com/030611)**

## Links

- [GitHub Repository](https://github.com/030611/dsh-telemetry-redactor)
- [Full README](https://github.com/030611/dsh-telemetry-redactor#readme)
- [Back to the Plugins list](../plugins.md)
