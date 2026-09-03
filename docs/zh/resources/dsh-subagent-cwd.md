---
title: "dsh-subagent-cwd"
description: "DeepSeek Harness subagent delegation enhancement"
keywords: "dsh-subagent-cwd, developer, integration, coding, deepseek harness, dsh"
---
# dsh-subagent-cwd

> ⭐ **3** · ✅ 活跃 · 集成

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | 开发者工具 |
| 星数 | ⭐ 3 | 状态 | ✅ 活跃 |
| 作者 | [lynx-gt](https://github.com/lynx-gt) | 更新时间 | 2026-08-15 |

## 一句话介绍

> DeepSeek Harness subagent delegation enhancement

## 详细介绍

Enhanced subagent delegation tools for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (dsh) **with per-call working-directory control**. Everything in [dsh-subagent-tools](https://github.com/lynx-gt/dsh-subagent-tools) (per-call model / provider / persona / toolFilter overrides, `@preset:` references, `provider/model` composite ids) **plus** a per-call `cwd` parameter — shipped with the two small provider patches that make `cwd` actually work.

## 📦 安装

```bash
powershell -ExecutionPolicy Bypass -File patches\uninstall.ps1   # Windows
# or: ./patches/uninstall.sh                                     # POSIX
dsh plugin --profile web remove dsh-subagent-cwd
```

## 🚀 快速开始

```bash
Let a subagent work in a directory without the repo's AGENTS.md injected:
  subagent(description="Summarize this file", prompt="...", cwd="D:\\projects\\scratch\\notes")
```

## 📚 更多信息

**re-run the installer (it is idempotent; it also detects vers**

powershell -ExecutionPolicy Bypass -File patches\install.ps1 If the installer reports "anchor not found", the target packages changed shape — check for a new dsh-subagent-cwd release or file an issue.

**Example**

Let a subagent work in a directory without the repo's AGENTS.md injected: subagent(description="Summarize this file", prompt="...", cwd="D:\\projects\\scratch\\notes")

## 🔗 链接

- [GitHub 仓库](https://github.com/lynx-gt/dsh-subagent-cwd)
- [完整 README](https://github.com/lynx-gt/dsh-subagent-cwd#readme)
- [返回dsh-subagent-cwd所在分类](../integrations.md)
