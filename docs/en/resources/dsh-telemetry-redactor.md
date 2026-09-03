---
title: "dsh-telemetry-redactor"
description: "Fail-closed export-copy redaction for DeepSeek Harness session telemetry"
keywords: "dsh-telemetry-redactor, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-telemetry-redactor

> ⭐ **3** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 3 | Status | ✅ active |
| Author | [030611](https://github.com/030611) | Updated | 2026-08-14 |
| Subcategory | 📁 Files & import | Capabilities | coding |

## One-liner

> Fail-closed export-copy redaction for DeepSeek Harness session telemetry

## About

**Redact supported credential patterns from outbound telemetry copies before configured backends receive them—without rewriting canonical session logs.** dsh plugin --profile web add dsh-telemetry-redactor `dsh-telemetry-redactor` is a minimal DeepSeek Harness Profile Bundle that redacts sensitive values from session telemetry before a backend receives them. It mounts on the official `session-telemetry/record` waterfall, calls `next()` so other deployment rules still compose, and returns a new recursively redacted record. The official telemetry coordinator deep-copies canonical session events before this waterfall and contains thrown rules per record. Therefore this plugin changes only the outbound copy: it never rewrites the canonical session log. In this document, **fail-closed means onl

## ✨ Key Features

- Values under high-risk key names such as `authorization`, `cookie`, `credential`, `password`, `secret`, `token`, `apiKey`, `access_token`, `clientSecret`, and `
- Bearer and Basic authorization values embedded in strings.
- Common credential forms including `sk-...`, GitHub tokens, Slack tokens, JWT-like triples, and `token=...` / `api_key: ...` assignments.

## 📦 Install

```bash
dsh plugin --profile web add dsh-telemetry-redactor
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add dsh-telemetry-redactor
dsh --profile web --dump-config
```

## 📚 Learn more

**Install**

Install the public package into the selected DSH profile, then inspect the resolved configuration: dsh plugin --profile web add dsh-telemetry-redactor dsh --profile web --dump-config The dump must contain the inserted `telemetry-redactor` row. The bundle does not add, replace, or enable a telemetry backend; it only protects records handled by whatever backend the deployment already selected.

**Configuration**

The only option is `replacement`, which defaults to `[REDACTED]`. It must contain 1 to 128 characters and must not itself match a supported credential pattern; invalid values fail loudly when the Cordis plugin fiber is awaited. config: replacement: '[TELEMETRY-REDACTED]' The key and pattern rules are fixed security behavior and cannot be disabled through configuration.

## 🔗 Links

- [GitHub Repository](https://github.com/030611/dsh-telemetry-redactor)
- [Full README](https://github.com/030611/dsh-telemetry-redactor#readme)
- [Back to the Plugins list](../plugins.md)
