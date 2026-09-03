---
title: "dsh-subagent-cwd"
description: "DeepSeek Harness subagent delegation enhancement"
keywords: "dsh-subagent-cwd, developer, integration, coding, deepseek harness, dsh"
---
# dsh-subagent-cwd

> ⭐ **3** · ✅ active · integration

| | | | |
|---|---|---|---|
| Type | integration | Category | Developer tools |
| Stars | ⭐ 3 | Status | ✅ active |
| Author | [lynx-gt](https://github.com/lynx-gt) | Updated | 2026-08-15 |

## One-liner

> DeepSeek Harness subagent delegation enhancement

## About

Enhanced subagent delegation tools for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (dsh) **with per-call working-directory control**. Everything in [dsh-subagent-tools](https://github.com/lynx-gt/dsh-subagent-tools) (per-call model / provider / persona / toolFilter overrides, `@preset:` references, `provider/model` composite ids) **plus** a per-call `cwd` parameter — shipped with the two small provider patches that make `cwd` actually work.

## 📦 Install

```bash
powershell -ExecutionPolicy Bypass -File patches\uninstall.ps1   # Windows
# or: ./patches/uninstall.sh                                     # POSIX
dsh plugin --profile web remove dsh-subagent-cwd
```

## 🚀 Quick Start

```bash
Let a subagent work in a directory without the repo's AGENTS.md injected:
  subagent(description="Summarize this file", prompt="...", cwd="D:\\projects\\scratch\\notes")
```

## 📚 Learn more

**re-run the installer (it is idempotent; it also detects vers**

powershell -ExecutionPolicy Bypass -File patches\install.ps1 If the installer reports "anchor not found", the target packages changed shape — check for a new dsh-subagent-cwd release or file an issue.

**Example**

Let a subagent work in a directory without the repo's AGENTS.md injected: subagent(description="Summarize this file", prompt="...", cwd="D:\\projects\\scratch\\notes")

## 🔗 Links

- [GitHub Repository](https://github.com/lynx-gt/dsh-subagent-cwd)
- [Full README](https://github.com/lynx-gt/dsh-subagent-cwd#readme)
- [Back to the MCP & Integrations list](../integrations.md)
