---
title: "dsh-repo-setup"
description: "Read-only repo bootstrap scanner (repo_setup_scan tool): detects stack/tests/docs/git/db and recommends plugins, MCP servers and hygiene files (claude-code-setup counterpart)."
keywords: "dsh-repo-setup, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-repo-setup

> ⭐ **1** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 1 | Status | ✅ active |
| Author | [gongyijie85](https://github.com/gongyijie85) | Updated | 2026-08-16 |
| Subcategory | 🧪 Code, tests & review | Capabilities | coding |

## One-liner

> Read-only repo bootstrap scanner (repo_setup_scan tool): detects stack/tests/docs/git/db and recommends plugins, MCP servers and hygiene files (claude-code-setup counterpart).

## About

[English](README.en.md) | **简体中文** 仓库体检引导插件 —— Anthropic **claude-code-setup** 的 DeepSeek Harness 版。 注册一个**只读**工具 `repo_setup_scan`:扫描项目目录的语言栈、测试设置、 文档、git、Docker 与数据库线索,然后给出设置建议:该装哪些 DSH 技能插件、 该挂哪些 MCP 服务器、该补哪些卫生文件。**绝不修改任何东西。**

## 📦 Install

```bash
# npm
dsh plugin --profile web add dsh-repo-setup

# GitHub
dsh plugin --profile web add github:gongyijie85/dsh-repo-setup

# 本地开发
dsh plugin --profile web add D:\plugins\dsh-repo-setup
```

## 🚀 Quick Start

```bash
node --check lib/index.js
# 功能冒烟(伪 ctx 注册 + 直接调 scanRepo 逻辑见 scripts/verify-tool.mjs)
node scripts/verify-tool.mjs
```

## 🔗 Links

- [GitHub Repository](https://github.com/gongyijie85/dsh-repo-setup)
- [Full README](https://github.com/gongyijie85/dsh-repo-setup#readme)
- [Back to the Plugins list](../plugins.md)
